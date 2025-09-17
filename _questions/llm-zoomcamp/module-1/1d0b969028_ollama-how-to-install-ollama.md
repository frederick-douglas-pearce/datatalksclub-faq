---
id: 1d0b969028
question: 'Ollama: How to install Ollama?'
sort_order: 330
---

First, install Ollama:

Go to [https://ollama.com/download](https://ollama.com/download)

Choose your operating system:

macOS: Download the .pkg and install

Windows: Download the .msi and install

Linux: Run this in terminal:

curl -fsSL [ollama.com](https://ollama.com/install.sh) | sh

Open a terminal and type:

ollama run llama3

This will:

Download the LLaMA 3 model (~4GB)

Start the model locally

Open a chat-like interface where you can type questions

To test the Ollama local server, execute the following command:curl [http://localhost:11434](http://localhost:11434)

You should receive something like:

{"models": [...]}

Then, install the Python client:

pip install ollamaHere, you have a minimal python example:import ollama

response = ollama.chat(

model='llama3',

messages=[{"role": "user", "content": your_prompt}]

)

print(response['message']['content'])

Added by Alexander Daniel Rios

