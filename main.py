import json
import random
import os

ARQUIVO = "memoria_bot.json"

# -----------------------------
# carregar memória
# -----------------------------
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as f:
        dados = json.load(f)
        chatbot = dados.get("chatbot", {})
        nivel = dados.get("nivel", 1)
        interacoes = dados.get("interacoes", 0)
else:
    chatbot = {
        "oi": ["opa", "fala aí", "eae 😎"],
        "banana": ["banana detectada 🍌"]
    }
    nivel = 1
    interacoes = 0


# -----------------------------
# salvar memória
# -----------------------------
def salvar():
    with open(ARQUIVO, "w") as f:
        json.dump({
            "chatbot": chatbot,
            "nivel": nivel,
            "interacoes": interacoes
        }, f)


print("Bot: online. digite 'sair' para sair.")

# -----------------------------
# loop principal
# -----------------------------
while True:
    msg = input("Você: ").lower()

    if msg == "sair":
        print("Bot: desligando...")
        salvar()
        break

    # comando: resetar memória
    if msg == "esquecer tudo":
        chatbot = {}
        nivel = 1
        interacoes = 0
        salvar()
        print("Bot: apaguei tudo da minha memória 🧠💥")
        continue

    interacoes += 1

    # sistema de nível
    nivel = 1 + interacoes // 5

    # resposta se já sabe
    if msg in chatbot:
        resposta = random.choice(chatbot[msg])
        print(f"Bot (lvl {nivel}):", resposta)

    else:
        print(f"Bot (lvl {nivel}): não sei isso... me ensina?")
        resp = input("Ensine o bot: ")

        chatbot[msg] = [resp]
        print("Bot: aprendido. guardado na memória 🧠")

    salvar()