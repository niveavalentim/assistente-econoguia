# EconoguIA - Assistente Virtual de Economia com Inteligência Artificial

## Sobre o Projeto

O EconoguIA é um assistente virtual desenvolvido como parte do desafio "Construa seu Assistente Virtual com Inteligência Artificial" da DIO.

O projeto foi criado com o objetivo de auxiliar estudantes, profissionais e pessoas interessadas em economia a compreender conceitos econômicos de forma simples, objetiva e confiável.

O assistente utiliza uma base de conhecimento própria para responder perguntas relacionadas à economia, evitando respostas inventadas e informando ao usuário quando não possui informações suficientes para responder determinada questão.

---

## Problema

A economia está presente no cotidiano das pessoas, mas muitos conceitos importantes podem ser difíceis de compreender, especialmente para quem está iniciando os estudos na área.

Termos como inflação, PIB, taxa Selic, desemprego e elasticidade aparecem frequentemente em notícias, análises econômicas e conteúdos acadêmicos, mas nem sempre são apresentados de forma clara e acessível.

---

## Solução

O EconoguIA foi desenvolvido para atuar como um guia de aprendizagem em economia.

Por meio de uma base de conhecimento estruturada, o assistente é capaz de:

- Identificar conceitos econômicos presentes na pergunta do usuário;
- Buscar informações em sua base de conhecimento;
- Retornar respostas objetivas e compreensíveis;
- Informar quando não possui conhecimento suficiente para responder;
- Apoiar estudantes e interessados no aprendizado de economia.

---

## Objetivos

- Facilitar o aprendizado de conceitos econômicos.
- Demonstrar a utilização de Inteligência Artificial em aplicações educacionais.
- Aplicar conceitos de organização de conhecimento.
- Desenvolver uma solução simples, funcional e escalável.

---

## Público-Alvo

O EconoguIA foi pensado para atender:

- Estudantes de Economia;
- Estudantes do Ensino Médio;
- Universitários;
- Pessoas interessadas em educação financeira;
- Usuários que desejam aprender conceitos econômicos básicos.

---

## Funcionalidades

- Consulta de conceitos econômicos.
- Respostas baseadas em uma base de conhecimento própria.
- Tratamento de perguntas desconhecidas.
- Respostas simples e objetivas.
- Estrutura facilmente expansível para novos temas.

---

## Base de Conhecimento

A base de conhecimento contém conceitos econômicos fundamentais, incluindo:

- Inflação
- IPCA
- Taxa Selic
- PIB
- Desemprego
- Oferta e Demanda
- Elasticidade
- Concorrência Perfeita
- Monopólio
- Oligopólio
- Adam Smith
- John Maynard Keynes
- Thomas Malthus

Novos conceitos podem ser adicionados facilmente ao arquivo de conhecimento do projeto.

---

## Estrutura do Projeto

```text
econoguia/
│
├── README.md
│
├── data/
│   └── base_conhecimento.json
│
├── docs/
│   ├── documentacao.md
│   ├── metricas.md
│   └── pitch.md
│
└── src/
    └── app.py
```

---

## Tecnologias Utilizadas

- Python 3
- JSON
- Git
- GitHub

---

## Funcionamento do Assistente

O EconoguIA utiliza uma lógica simples baseada em busca por palavras-chave.

Quando o usuário realiza uma pergunta:

1. O sistema recebe a entrada do usuário.
2. A pergunta é convertida para letras minúsculas.
3. O assistente procura termos relacionados na base de conhecimento.
4. Caso encontre uma correspondência, retorna a resposta cadastrada.
5. Caso não encontre, informa que não possui a informação solicitada.

---

## Prompt do Assistente

O assistente segue as seguintes instruções:

> Você é o EconoguIA.
>
> Sua função é auxiliar usuários na compreensão de conceitos econômicos.
>
> Responda apenas utilizando informações presentes na base de conhecimento.
>
> Utilize linguagem simples e objetiva.
>
> Não invente informações.
>
> Caso não encontre uma resposta adequada, informe:
>
> "Desculpe, não encontrei essa informação na minha base de conhecimento."

---

## Como Executar

### Clonar o Repositório

```bash
git clone https://github.com/SEU-USUARIO/econoguia.git
```

### Acessar a Pasta do Projeto

```bash
cd econoguia
```

### Executar o Programa

```bash
python src/app.py
```

---

## Exemplos de Uso

### Exemplo 1

Entrada:

```text
O que é inflação?
```

Saída:

```text
Inflação é o aumento generalizado dos preços de bens e serviços.
```

---

### Exemplo 2

Entrada:

```text
Explique o PIB.
```

Saída:

```text
PIB significa Produto Interno Bruto e representa a soma dos bens e serviços produzidos em um país.
```

---

### Exemplo 3

Entrada:

```text
O que é a taxa Selic?
```

Saída:

```text
A taxa Selic é a taxa básica de juros da economia brasileira.
```

---

### Exemplo 4

Entrada:

```text
Quem foi Milton Friedman?
```

Saída:

```text
Desculpe, não encontrei essa informação na minha base de conhecimento.
```

---

## Avaliação e Métricas

Foram realizados testes para verificar o comportamento do assistente diante de perguntas conhecidas e desconhecidas.

| Cenário | Resultado Esperado |
|----------|------------------|
| Conceito presente na base | Resposta correta |
| Conceito ausente na base | Mensagem de não encontrado |
| Pergunta com texto adicional | Identificação correta do conceito |

### Resultados

- Perguntas avaliadas: 10
- Respostas corretas: 8
- Precisão estimada: 80%

---

## Diferenciais do Projeto

- Aplicação voltada para educação econômica.
- Estrutura simples e fácil de compreender.
- Fácil manutenção e expansão.
- Possibilidade de integração futura com APIs econômicas.
- Base para evolução para agentes de IA mais avançados.

---

## Melhorias Futuras

- Inclusão de mais conceitos econômicos.
- Integração com dados do IBGE.
- Integração com dados do Banco Central.
- Consulta de indicadores econômicos em tempo real.
- Interface web para interação com usuários.
- Utilização de modelos de linguagem para interpretação avançada das perguntas.
- Dashboard com indicadores econômicos.

---

## Conclusão

O EconoguIA demonstra como uma solução simples baseada em Inteligência Artificial e organização de conhecimento pode auxiliar no processo de aprendizagem de economia.

Além de atender aos requisitos do desafio proposto pela DIO, o projeto serve como base para futuras evoluções envolvendo agentes inteligentes, integração com fontes externas de dados e aplicações educacionais mais completas.

---

## Autora

Nívea Valentim

Graduanda em Ciências Econômicas

Projeto desenvolvido para o desafio "Construa seu Assistente Virtual com Inteligência Artificial" da Digital Innovation One (DIO).

---

## Licença

Este projeto possui finalidade exclusivamente educacional e foi desenvolvido para fins de estudo e aprendizado.
