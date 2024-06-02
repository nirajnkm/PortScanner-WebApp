import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os


def generate_chat_response(port):
    genai.configure(api_key=os.getenv("API_KEY"))
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(f"These are the open ports found {port}. First, list the open ports detected. Then, provide a structured, comprehensive response detailing their potential security risks and best practices for mitigation. Prioritize clarity and conciseness, incorporating real-world examples to illustrate concepts effectively.")
    return convo.last.text

if __name__ == "__main__":
    response = generate_chat_response(open_port)
    print(response)
