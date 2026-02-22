# Logs fall incidents to CSV file
# Only logs once per session using incident_logged flag

incident_logged=False

def log_incident(timestamp):
    global incident_logged
    if incident_logged:
        return
    incident_logged = True
    with open("incidents.csv", "a") as file:
        # Write fall details with timestamp
        row_message=f"Fall detected at {timestamp}"
        file.write(row_message + "\n")
    print("Incident logged")