def analyze_logs(log_text):

    findings = []

    if "Failed password" in log_text:
        findings.append("❌ Failed Login Attempt Detected")

    if "Accepted password" in log_text:
        findings.append("✅ Successful Login")

    if "sudo" in log_text:
        findings.append("⚠ Sudo Command Used")

    if "error" in log_text.lower():
        findings.append("🚨 Error Found")

    if "root" in log_text.lower():
        findings.append("🔒 Root Account Activity")

    if len(findings) == 0:
        findings.append("✅ No suspicious activity detected.")

    return findings