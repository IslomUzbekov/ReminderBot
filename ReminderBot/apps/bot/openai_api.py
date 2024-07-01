
import openai


class OpenAIAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def parse_reminder(self, message: str) -> str:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Parse the following message to extract reminder details: {message}",
            max_tokens=100
        )
        return response.choices[0].text.strip()

openai_api = OpenAIAPI(api_key='YOUR_OPENAI_API_KEY')
