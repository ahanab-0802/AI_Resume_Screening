import json
import os
from typing import Dict, List, Optional

from groq import Groq


def generate_llm_resume_suggestions(
    matched_skills: List[str],
    missing_skills: List[str],
) -> List[Dict]:
    """Generate personalized resume suggestions using Groq."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return []

    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    prompt = f"""
You are an AI resume improvement assistant.

The resume-JD matching system has already calculated these results:

Matched skills:
{json.dumps(matched_skills, ensure_ascii=False)}

Missing / not demonstrated skills:
{json.dumps(missing_skills, ensure_ascii=False)}

Generate up to 3 concise, actionable resume suggestions.

Your suggestions must:
1. Be based ONLY on the supplied skills.
2. Never claim that the candidate has a skill that is listed as missing.
3. Suggest a resume section, bullet-point improvement, or rewording opportunity.
4. If a missing skill is important, suggest where the candidate could mention
   it ONLY if they genuinely have that experience.
5. Do not change or recalculate any score.
6. Do not mention ATS score, semantic score, or matching calculations.
7. Do not give generic advice unrelated to the supplied skills.

Return ONLY valid JSON in this exact format:
[
  {{
    "title": "Short suggestion title",
    "suggestion": "Actionable suggestion",
    "type": "llm_resume_suggestion"
  }}
]
"""

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a resume improvement assistant. "
                        "Return only valid JSON."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
            max_tokens=500,
        )

        generated_text = (
            response.choices[0].message.content or ""
        ).strip()

        if not generated_text:
            print("⚠️ Groq returned empty recommendation content")
            return []

        if generated_text.startswith("```"):
            generated_text = generated_text.replace(
                "```json", "", 1
            )
            generated_text = generated_text.replace(
                "```", ""
            ).strip()

        parsed = json.loads(generated_text)

        if not isinstance(parsed, list):
            return []

        suggestions = []

        for item in parsed[:3]:
            if not isinstance(item, dict):
                continue

            title = str(item.get("title", "")).strip()
            suggestion = str(item.get("suggestion", "")).strip()

            if title and suggestion:
                suggestions.append({
                    "icon": "🤖",
                    "title": title,
                    "suggestion": suggestion,
                    "type": "llm_resume_suggestion",
                })

        print(
            f"✅ Groq recommendation call succeeded: "
            f"{len(suggestions)} suggestions"
        )

        return suggestions

    except Exception as e:
        print(f"❌ Groq recommendation call failed: {e}")
        return []
