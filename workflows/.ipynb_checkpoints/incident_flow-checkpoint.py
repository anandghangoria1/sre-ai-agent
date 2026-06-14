from modules.classifier import classify_incident
from modules.rca import analyze_incident
from modules.decision import decide_action
from modules.reporter import generate_report
from tools.metrics import get_cpu, get_memory, get_disk


def run_incident(incident):
    print("Classifying incident...")
    category = classify_incident(incident)

    print("Running analysis...")
    analysis = analyze_incident(incident)

    print("Deciding action...")
    action = decide_action(category)

    # Get system metrics
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()

    print("\nSystem Status:")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")
    print(f"Disk: {disk}%")

    print("\n" + action)

    # ✅ Skip approval if no action required
    if "No action required" in action:
        final_action = action.replace("Suggested Action: ", "")
    else:
        user_input = input("\nApprove this action? (yes/no): ")

        if user_input.lower() == "yes":
            final_action = f"Executed: {action}"
        else:
            final_action = "Action rejected by user"

    print("Generating report...")

    report = generate_report(
        incident,
        category,
        analysis,
        final_action
    )

    return report