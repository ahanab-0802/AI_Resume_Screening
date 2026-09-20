from typing import Any, Dict

import streamlit as st

from frontend.components.score_display import display_overall_score, display_score_breakdown
from frontend.components.jd_comparison import display_jd_comparison


def display_jd_recommendations(analysis: Dict[str, Any]) -> None:
    """Display evidence-based JD recommendations."""
    recommendations = analysis.get("jd_recommendations", [])

    if not recommendations:
        return

    st.markdown("---")
    st.markdown("### 💡 Recommendations")

    for rec in recommendations:
        title = rec.get("title", "")
        suggestion = rec.get("suggestion", "")

        if title and suggestion:
            st.markdown(f"**{title}**")
            st.markdown(f"→ {suggestion}")
        elif suggestion:
            st.markdown(f"→ {suggestion}")


def display_results_dashboard(analysis: Dict[str, Any]) -> None:
    """Render the concise analysis results without changing backend scoring."""
    display_overall_score(analysis)
    st.markdown("---")

    display_score_breakdown(analysis)

    jd_comparison = analysis.get("jd_comparison") or analysis.get("jd_match_analysis")

    if jd_comparison:
        st.markdown("---")
        display_jd_comparison(jd_comparison)

        display_jd_recommendations(analysis)