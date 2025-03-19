# Insurellm Chatbot

## Overview

This project is a chatbot designed to answer questions about Insurellm, an Insurance Tech company. It utilizes OpenAI's GPT-4o-mini model to generate responses based on predefined context data stored in a knowledge base.

## Features

- Uses **GPT-4o-mini** for low-cost AI responses.
- Loads context dynamically from **employees, products, contracts, and company** files.
- Provides accurate and relevant answers based on the available context.
- Implements **Gradio** for an interactive chat interface.

## UI Preview
<img width="767" alt="image" src="https://github.com/user-attachments/assets/6011af5a-6def-4f90-811a-40a072416942" />


## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **pip**

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-repo/knowledgebase-bot.git
   cd knowledgebase-bot
   ```

2. **Set up API Key:**

   - Create a `.env` file in the root directory.
   - Add the following line, replacing `your-api-key` with your OpenAI API key:
     ```sh
     OPENAI_API_KEY=your-api-key
     ```

3. **Ensure knowledge base directories exist:**

   - `knowledge-base/employees/`
   - `knowledge-base/products/`
   - `knowledge-base/contracts/`
   - `knowledge-base/company/`

4. **Run the chatbot:**
   ```sh
   python app.py
   ```

## Project Structure

```
insurellm-chatbot/
│── knowledge-base/
│   ├── employees/
│   ├── products/
│   ├── contracts/
│   ├── company/
│── style.css
│── app.py
│── .env (not included in repo, must be created manually)
```

## Usage

- Run the chatbot and interact via the Gradio UI.
- Ask questions related to Insurellm, and the chatbot will fetch relevant context before responding.
- If no relevant context is found, the chatbot will indicate that it doesn't have an answer.

## Troubleshooting

- **Missing API Key Error:** Ensure `.env` contains `OPENAI_API_KEY`.
- **No Context Available:** Verify that the `knowledge-base/` folder contains relevant files.
- **Gradio Interface Not Loading:** Check that `style.css` exists and is correctly formatted.
