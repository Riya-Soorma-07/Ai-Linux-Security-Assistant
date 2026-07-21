from google import genai

# Paste your Gemini API key here
client = genai.Client(api_key="AQ.Ab8RN6Jx80UlOzF6CYgIpD0czVTxcaVCXFM0M-0k39DJcPEG6w")

def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"