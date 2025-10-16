import os
from agents import RunConfig,AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)
model_provider=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
    
)
config=RunConfig(
    model=model_provider,
    model_provider=client,
    tracing_disabled=False

)