from modules.classifier import classify_incident
from modules.rca import analyze_incident
from modules.decision import decide_action
from modules.reporter import generate_report

def run_incident(incident):
    print("🔍 Classifying incident...")
    category = classify_incident(incident)

    print("🧠 Running analysis...")
    analysis = analyze_incident(incident)

    print("⚙️ Deciding action...")
    action = decide_action()

    print("✅ Generating report...")
    report = generate_report(incident, category, analysis, action)

    return report