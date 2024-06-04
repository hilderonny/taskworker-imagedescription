# pip install ollama
import ollama

# llama3
stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Warum ist der Himmel blau?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

# llava-llama3
# https://ollama.com/library/llava:13b