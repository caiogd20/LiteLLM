from openai import OpenAI
import os

# tenta carregar system_message de arquivo
system_message = "Você é um assistente útil."  # fallback padrão
if os.path.exists("system_message.txt"):
    with open("system_message.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:
            system_message = content
            print(f"[OK] system_message carregado: \"{system_message}\"")
        else:
            print("[AVISO] O arquivo system_message.txt está vazio. Usando padrão: \"Você é um assistente útil.\"")
else:
    print("[AVISO] O arquivo system_message.txt não foi encontrado. Usando padrão: \"Você é um assistente útil.\"")

client = OpenAI(
    base_url="http://127.0.0.1:4000/v1",
    api_key="not-needed"
)

messages = [
    {"role": "system", "content": system_message}
]

MAX_HISTORY = 10  # número máximo de mensagens no histórico

print("\nDigite 'sair' para encerrar a conversa.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        break

    messages.append({"role": "user", "content": user_input})

    resp = client.chat.completions.create(
        model="ollama/llama3.2:3b",
        messages=messages
    )

    reply = resp.choices[0].message.content
    print(f"Modelo: {reply}\n")

    messages.append({"role": "assistant", "content": reply})

    if len(messages) > MAX_HISTORY + 1:
        messages = [messages[0]] + messages[-MAX_HISTORY:]
