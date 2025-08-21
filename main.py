from openai import OpenAI

# Cliente apontando para LiteLLM local
client = OpenAI(
    base_url="http://127.0.0.1:4000/v1",
    api_key="not-needed"
)

# Define a personalidade do modelo
system_message = input("Defina a personalidade do modelo (ex: assistente útil, professor de física): ")

# Lista de mensagens começando com o system
messages = [{"role": "system", "content": system_message}]

print("\nDigite 'sair' para encerrar a conversa.\n")

while True:
    # Entrada do usuário
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Encerrando conversa.")
        break

    # Adiciona a mensagem do usuário
    messages.append({"role": "user", "content": user_input})

    # Chamada para o modelo
    resp = client.chat.completions.create(
        model="ollama/llama3.2:3b",
        messages=messages
    )

    # Resposta do modelo
    reply = resp.choices[0].message.content
    print("Modelo:", reply)

    # Adiciona a resposta do modelo à lista para contexto
    messages.append({"role": "assistant", "content": reply})
