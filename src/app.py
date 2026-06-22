import json

with open("../data/base_conhecimento.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

print("=== EconoguIA ===")
print("Digite 'sair' para encerrar.")

while True:
    pergunta = input("\nPergunta: ").lower()

    if pergunta == "sair":
        print("Encerrando o EconoguIA...")
        break

    resposta = None

    for conceito in base:
        if conceito in pergunta:
            resposta = base[conceito]
            break

    if resposta:
        print("\nResposta:")
        print(resposta)
    else:
        print("\nDesculpe, não encontrei essa informação na minha base de conhecimento.")
