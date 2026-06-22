# 📊 EconoguIA

> Assistente virtual educacional para aprender conceitos de economia de forma simples e objetiva.

Projeto desenvolvido como desafio final do bootcamp de IA da [DIO](https://www.dio.me/). Foi meu primeiro projeto com Python e IA aplicada — criado para tornar a economia mais acessível para quem está começando.

---

## O que é?

O **EconoguIA** é um chatbot de linha de comando que responde perguntas sobre conceitos econômicos. Ele consulta uma base de conhecimento local e retorna explicações simples e diretas — sem inventar respostas.

**Exemplos do que você pode perguntar:**
- *"O que é inflação?"*
- *"Explique o PIB"*
- *"Quem foi Adam Smith?"*
- *"O que é Taxa Selic?"*

---

##  Funcionalidades

-  Respostas para **30+ conceitos econômicos**
-  Comando `listar` para ver todos os conceitos disponíveis
-  Busca por correspondência exata e parcial
-  Informa quando não encontra a resposta (sem inventar)
-  Tratamento de interrupção do teclado (Ctrl+C)

---

##  Estrutura do Projeto

```
econoguia/
├── data/
│   └── base_conhecimento.json   # Base com conceitos econômicos
├── docs/
│   ├── documentacao.md          # Documentação do agente
│   ├── prompts.md               # Prompt principal
│   ├── metricas.md              # Avaliação e métricas de teste
│   └── pitch.md                 # Pitch do projeto
├── src/
│   └── app.py                   # Código principal
└── README.md
```

---

##  Como rodar

**Pré-requisito:** Python 3.10 ou superior

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/econoguia.git
cd econoguia

# Execute o projeto
python src/app.py
```

---

##  Demonstração

```
==================================================
         📊  EconoguIA — Seu guia de economia
==================================================
  Base de conhecimento: 30 conceitos disponíveis
  Digite 'ajuda' para ver os comandos disponíveis.
==================================================

💬 Você: o que é inflação?

📖 EconoguIA:
   Inflação é o aumento generalizado dos preços de bens e serviços ao
   longo do tempo, reduzindo o poder de compra da moeda. No Brasil, a
   inflação é medida principalmente pelo IPCA.

💬 Você: quem foi keynes?

📖 EconoguIA:
   John Maynard Keynes (1883–1946) foi um economista britânico que defendeu
   a intervenção do Estado na economia para estimular o crescimento e reduzir
   o desemprego...
```

---

##  Testes

Foram realizados 5 testes cobrindo conceitos cadastrados e perguntas fora da base:

| # | Pergunta | Resultado |
|---|----------|-----------|
| 1 | O que é inflação? | ✅ Resposta correta |
| 2 | Explique o PIB | ✅ Resposta correta |
| 3 | O que é a Taxa Selic? | ✅ Resposta correta |
| 4 | Quem foi Milton Friedman? | ✅ Informado que não encontrou |
| 5 | O que é desemprego? | ✅ Resposta correta |

**Taxa de sucesso: 100% (5/5)**

---

##  Tecnologias

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-base%20de%20dados-black?style=flat&logo=json)
![Git](https://img.shields.io/badge/Git-controle%20de%20versão-F05032?style=flat&logo=git&logoColor=white)

---

##  Conceitos na Base de Conhecimento

`inflação` · `IPCA` · `IGP-M` · `Selic` · `Copom` · `PIB` · `desemprego` · `PNAD` · `oferta` · `demanda` · `elasticidade` · `concorrência perfeita` · `monopólio` · `oligopólio` · `Adam Smith` · `Keynes` · `Malthus` · `Friedman` · `juros` · `dívida pública` · `Tesouro Direto` · `câmbio` · `balança comercial` · `recessão` · `política fiscal` · `política monetária` · `Banco Central` · `microeconomia` · `macroeconomia` · `custo de oportunidade`

---

##  Autor

Desenvolvido como projeto de conclusão do bootcamp de IA da DIO.

> *"A economia está em todo lugar. Entendê-la é uma vantagem."*

---

##  Licença

Este projeto está sob a licença MIT.
