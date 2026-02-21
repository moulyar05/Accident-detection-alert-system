incident_logged=False

def log_incident(timestamp):
    global incident_logged
    if incident_logged:
        return
    incident_logged = True
    with open("incidents.csv", "a") as file:
        row_message=f"Fall detcted at {timestamp}"
        file.write(row_message + "\n")
    print("Incident logged")