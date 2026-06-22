import json
import os

# ─── Carrega a base de conhecimento ───────────────────────────────────────────

CAMINHO_BASE = os.path.join(os.path.dirname(__file__), "../data/base_conhecimento.json")

with open(CAMINHO_BASE, "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

# ─── Interface ────────────────────────────────────────────────────────────────

def exibir_cabecalho():
    print("\n" + "=" * 50)
    print("         📊  EconoguIA — Seu guia de economia")
    print("=" * 50)
    print(f"  Base de conhecimento: {len(base)} conceitos disponíveis")
    print("  Digite 'ajuda' para ver os comandos disponíveis.")
    print("=" * 50)

def exibir_ajuda():
    print("\n📋 Comandos disponíveis:")
    print("  listar     → mostra todos os conceitos disponíveis")
    print("  sair       → encerra o EconoguIA")
    print("  <pergunta> → pergunte qualquer coisa sobre economia\n")

def listar_conceitos():
    print(f"\n📚 Conceitos disponíveis ({len(base)} no total):\n")
    conceitos = sorted(base.keys())
    for i, conceito in enumerate(conceitos, 1):
        print(f"  {i:2}. {conceito.title()}")
    print()

def buscar_resposta(pergunta: str) -> str | None:
    """
    Busca na base de conhecimento pelo conceito mais relevante.
    Prioriza correspondências exatas antes de buscas parciais.
    """
    pergunta_lower = pergunta.lower()

    # 1ª tentativa: correspondência exata
    if pergunta_lower in base:
        return base[pergunta_lower]

    # 2ª tentativa: o conceito está contido na pergunta
    for conceito in base:
        if conceito in pergunta_lower:
            return base[conceito]

    return None

# ─── Loop principal ───────────────────────────────────────────────────────────

def main():
    exibir_cabecalho()

    while True:
        try:
            pergunta = input("\n💬 Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nEncerrado pelo usuário. Até logo!")
            break

        if not pergunta:
            continue

        comando = pergunta.lower()

        if comando == "sair":
            print("\n✅ Encerrando o EconoguIA. Bons estudos!")
            break

        elif comando == "ajuda":
            exibir_ajuda()

        elif comando == "listar":
            listar_conceitos()

        else:
            resposta = buscar_resposta(pergunta)

            if resposta:
                print(f"\n📖 EconoguIA:\n   {resposta}")
            else:
                print("\n🤔 EconoguIA:")
                print("   Desculpe, não encontrei essa informação na minha base de conhecimento.")
                print("   Tente 'listar' para ver os conceitos disponíveis.")


if __name__ == "__main__":
    main()
