def analyze_command(command):

    commands = {

        "ls": {
            "purpose": "Lists files and folders.",
            "risk": "Low",
            "recommendation": "Safe command."
        },

        "pwd": {
            "purpose": "Shows current working directory.",
            "risk": "Low",
            "recommendation": "Safe command."
        },

        "cd": {
            "purpose": "Changes current directory.",
            "risk": "Low",
            "recommendation": "Be careful while accessing sensitive folders."
        },

        "chmod": {
            "purpose": "Changes file permissions.",
            "risk": "Medium",
            "recommendation": "Avoid using chmod 777."
        },

        "sudo": {
            "purpose": "Runs command as administrator.",
            "risk": "High",
            "recommendation": "Use only when necessary."
        },

        "rm": {
            "purpose": "Deletes files.",
            "risk": "Critical",
            "recommendation": "Deleting files is irreversible."
        }

    }

    first_word = command.split()[0]

    if first_word in commands:
        return commands[first_word]

    return {
        "purpose": "Unknown Command",
        "risk": "Unknown",
        "recommendation": "Command not found."
    }