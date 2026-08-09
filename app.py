import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from context import TWIN_SYSTEM_PROMPT
from styles import CSS, EXAMPLES, JS
from tools import handle_tool_calls, tools


load_dotenv(override=True)

MODEL_NAME = "openai/gpt-4.1-nano"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

openrouter = OpenAI(
    base_url=OPENROUTER_BASE_URL,
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]

    response = openrouter.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    while response.choices[0].finish_reason == "tool_calls":
        assistant_message = response.choices[0].message
        results = handle_tool_calls(assistant_message.tool_calls)

        messages.append(assistant_message)
        messages.extend(results)

        response = openrouter.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
        )

    return response.choices[0].message.content


if __name__ == "__main__":
    with gr.Blocks(elem_id="twin-app") as demo:
        gr.Markdown("# Digital Twin", elem_id="twin-title")

        gr.Markdown(
            "I'm A Digital Assistant. What would you like to know about my career?",
            elem_id="career-intro",
        )

        gr.ChatInterface(
            fn=chat,
            chatbot=gr.Chatbot(
                show_label=False,
                height=500,
            ),
            examples=EXAMPLES,
        )

    demo.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )