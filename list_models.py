from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Jx80UlOzF6CYgIpD0czVTxcaVCXFM0M-0k39DJcPEG6w")

try:
    models = client.models.list()

    print("Available models:\n")

    for model in models:
        print(model.name)

except Exception as e:
    print(e)