from workflows.incident_flow import run_incident

if __name__ == "__main__":
    incident = "High CPU usage on nginx server"

    report = run_incident(incident)

    print(report)
