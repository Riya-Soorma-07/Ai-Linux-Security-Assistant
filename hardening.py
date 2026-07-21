def get_hardening_tips(risk):

    if risk == "Critical":

        return [

            "❌ Never use chmod 777.",

            "🔒 Use chmod 750 or chmod 755.",

            "🛡 Enable UFW Firewall.",

            "🔑 Use SSH Key Authentication.",

            "🚫 Disable Root Login.",

            "📦 Enable Automatic Updates."

        ]

    elif risk == "High":

        return [

            "Restrict file permissions.",

            "Enable Firewall.",

            "Review user access."

        ]

    elif risk == "Medium":

        return [

            "Review permissions.",

            "Keep software updated."

        ]

    else:

        return [

            "System looks secure.",

            "Continue regular updates."

        ]