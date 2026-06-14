def generate_report(incident, category, analysis, action):
    return f"""
=== INCIDENT REPORT ===

Incident:
{incident}

Category:
{category}

Analysis:
{analysis}

Action Taken:
{action}
"""