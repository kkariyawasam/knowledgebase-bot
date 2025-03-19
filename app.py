import os
import glob
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI


MODEL = "gpt-4o-mini" 

# Load environment variables in a file called .env
load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
openai = OpenAI()

context = {}

# Load employee files
employees = glob.glob("knowledge-base/employees/*")
for employee in employees:
    name = os.path.splitext(os.path.basename(employee))[0]
    with open(employee, "r", encoding="utf-8") as f:
        doc = f.read()
    context[name] = doc

# Load product files
products = glob.glob("knowledge-base/products/*")
for product in products:
    name = os.path.splitext(os.path.basename(product))[0]
    with open(product, "r", encoding="utf-8") as f:
        doc = f.read()
    context[name] = doc

# Load contract files
contracts = glob.glob("knowledge-base/contracts/*")
for contract in contracts:
    name = os.path.splitext(os.path.basename(contract))[0]
    with open(contract, "r", encoding="utf-8") as f:
        doc = f.read()
    context[name] = doc
    
contracts = glob.glob("knowledge-base/company/*")
for contract in contracts:
    name = os.path.splitext(os.path.basename(contract))[0]
    with open(contract, "r", encoding="utf-8") as f:
        doc = f.read()
    context[name] = doc

system_message = "You are an expert in answering accurate questions about Insurellm, the Insurance Tech company. Give brief, accurate answers. If you don't know the answer, say so. Do not make anything up if you haven't been provided with relevant context."

def get_relevant_context(message):
    relevant_context = []
    for context_title, context_details in context.items():
        if context_title.lower() in message.lower():
            relevant_context.append(context_details)
    return relevant_context          

def add_context(message):
    relevant_context = get_relevant_context(message)
    if relevant_context:
        message += "\n\nThe following additional context might be relevant in answering this question:\n\n"
        for relevant in relevant_context:
            message += relevant + "\n\n"
    return message

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history
    message = add_context(message)
    messages.append({"role": "user", "content": message})

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

def load_css():
    with open('style.css', 'r') as file:
        css_content = file.read()
    return css_content
        

# Launch Gradio interface
if __name__ == "__main__":
    view = gr.ChatInterface(chat, css=load_css(), type="messages").launch()