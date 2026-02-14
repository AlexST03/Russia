from fastapi import FastAPI, Request
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/")
async def alice_webhook(request: Request):
    data = await request.json()
    user_text = data["request"]["original_utterance"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_text}]
    )

    answer = response.choices[0].message.content

    return {
        "version": data["version"],
        "response": {
            "text": answer,
            "end_session": False
        }
    }