import streamlit as st
from command_parser import analyze_command
from permission_checker import check_permission
from security_score import calculate_score
from hardening import get_hardening_tips
from password_checker import check_password
from log_analyzer import analyze_logs
from chatbot import ask_ai
from about import get_about

# Page Configuration
st.set_page_config(
    page_title="AI Linux Security Assistant",
    page_icon="🐧",
    layout="wide"
)

# Title


st.title("🐧 AI Linux Security Assistant")

st.caption("AI Powered Linux Security Analysis Platform")
st.write("Welcome to the AI Linux Security Assistant Project.")

# Sidebar
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "Home",
        "Analyze Command",
        "Permission Checker",
        "Password Checker",
        "Log Analyzer",
        "AI Chatbot",
        "About Project"
    ]
)
# ---------------- HOME ----------------

if option == "Home":

    st.header("🏠 Dashboard")

    st.markdown("""
    ## 🐧 AI Linux Security Assistant
    ### AI Powered Linux Security Analysis Platform

    Welcome! This application helps analyze Linux commands, permissions,
    passwords, logs, and provides AI-powered security guidance.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Modules", "7")

    with col2:
        st.metric("AI Status", "🟢 Active")

    with col3:
        st.metric("Security", "High")

    st.markdown("---")

    st.subheader("🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🔍 Linux Command Analyzer")
        st.success("🔒 Permission Checker")
        st.success("🔑 Password Strength Checker")
        st.success("📄 Linux Log Analyzer")

    with col2:
        st.success("🤖 AI Security Chatbot")
        st.success("🛡 Security Score")
        st.success("💡 Linux Hardening Tips")

    st.markdown("---")

    st.info("💡 Tip: Use the left sidebar to explore all the project modules.")

    

# ---------------- ANALYZE COMMAND ----------------

elif option == "Analyze Command":

    st.header("Linux Command Analyzer")

    command = st.text_input("Enter Linux Command")

    if st.button("Analyze"):

        result = analyze_command(command)

        st.subheader("Purpose")
        st.write(result["purpose"])

        st.subheader("Risk Level")
        st.write(result["risk"])

        st.subheader("Recommendation")
        st.success(result["recommendation"])
        st.subheader("Linux Hardening Tips")

        tips = get_hardening_tips(result["risk"])

        for tip in tips:
            st.write(tip)
        score = calculate_score(result["risk"])

        st.subheader("Security Score")

        st.progress(score)

        st.metric("Overall Security Score", f"{score}/100")

# ---------------- PERMISSION CHECKER ----------------

# ---------------- PERMISSION CHECKER ----------------

elif option == "Permission Checker":

    st.header("🔒 Linux Permission Checker")

    permission = st.text_input(
        "Enter Linux Permission",
        placeholder="-rwxr-xr--"
    )

    if st.button("Check Permission"):

        result = check_permission(permission)

        st.subheader("Owner")
        st.write(result["owner"])

        st.subheader("Group")
        st.write(result["group"])

        st.subheader("Others")
        st.write(result["others"])

        st.subheader("Risk Level")
        st.write(result["risk"])

        st.subheader("Recommendation")
        st.success(result["recommendation"])
        # ---------------- PASSWORD CHECKER ----------------

elif option == "Password Checker":

    st.header("🔑 Password Strength Checker")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Check Password"):

        strength = check_password(password)

        st.subheader("Password Strength")
        st.success(strength)


    elif option == "Log Analyzer":

        st.header("📄 Linux Log Analyzer")

        uploaded_file = st.file_uploader(
            "Upload Linux Log File",
            type=["txt", "log"]
    )

        if uploaded_file is not None:

            log_data = uploaded_file.read().decode("utf-8")

            findings = analyze_logs(log_data)

            st.subheader("Analysis Result")

            for item in findings:
                st.write(item)

            # ---------------- LOG ANALYZER ----------------

elif option == "Log Analyzer":

    st.header("📄 Linux Log Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Linux Log File",
        type=["log", "txt"]
    )

    if uploaded_file is not None:

        log_data = uploaded_file.read().decode("utf-8")

        findings = analyze_logs(log_data)

        st.subheader("Analysis Result")

        for item in findings:
            st.write(item)




elif option == "AI Chatbot":

    st.header("🤖 AI Linux Security Chatbot")

    question = st.text_area("Ask a Linux Security Question")

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            answer = ask_ai(question)

            st.subheader("AI Response")

            st.write(answer)


elif option == "About Project":

    st.header("About Project")

    st.markdown(get_about())

    st.markdown("---")
    st.caption("AI Linux Security Assistant | Developed using Python + Streamlit + Gemini AI")