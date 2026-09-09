priority_code = 0
is_outage = False
region = "WEST"

if (priority_code > 0):
    print("Priority Review")
elif (is_outage and region == "EAST"):
    print("Emergency Dispatch")
elif (is_outage or region == "REMOTE"):
    print("Escalate")
else:
    print("Routine")

    