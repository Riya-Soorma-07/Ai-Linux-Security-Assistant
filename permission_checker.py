def check_permission(permission):

    if len(permission) != 10:
        return {
            "owner": "Invalid",
            "group": "Invalid",
            "others": "Invalid",
            "risk": "Unknown",
            "recommendation": "Enter a valid permission like -rwxr-xr--"
        }

    owner = permission[1:4]
    group = permission[4:7]
    others = permission[7:10]

    risk = "Low"
    recommendation = "Permissions look safe."

    if owner == "rwx" and group == "rwx" and others == "rwx":
        risk = "Critical"
        recommendation = "Never use chmod 777. Everyone gets full access."

    elif others == "rwx":
        risk = "High"
        recommendation = "Others should not have full permissions."

    elif "w" in others:
        risk = "Medium"
        recommendation = "Avoid giving write permission to others."

    return {
        "owner": owner,
        "group": group,
        "others": others,
        "risk": risk,
        "recommendation": recommendation
    }