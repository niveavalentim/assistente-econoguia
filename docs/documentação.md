# Documentação do Agente

## Nome

EconoguIA

## Objetivo

O EconoguIA é um assistente virtual educacional criado para auxiliar estudantes e interessados em economia na compreensão de conceitos econômicos fundamentais.

A ideia surgiu da dificuldade comum de entender termos econômicos presentes em notícias e análises de mercado — palavras como "Selic", "IPCA" ou "balança comercial" aparecem com frequência, mas raramente são explicadas de forma simples.

## Público-Alvo

- Estudantes de Economia e Administração
- Estudantes do Ensino Médio
- Universitários de qualquer área
- Pessoas interessadas em educação financeira
- Quem quer entender as notícias econômicas do dia a dia

## Como Funciona

O usuário digita uma pergunta em linguagem natural. O agente analisa o texto e busca na base de conhecimento o conceito mais relevante.

A busca funciona em duas etapas:

1. **Correspondência exata** — verifica se a pergunta é exatamente um conceito cadastrado
2. **Correspondência parcial** — verifica se algum conceito está contido dentro da pergunta

Se nenhum conceito for encontrado, o agente informa ao usuário sem inventar uma resposta.

## Comandos Disponíveis

| Comando    | O que faz                                       |
|------------|-------------------------------------------------|
| `ajuda`    | Exibe os comandos disponíveis                   |
| `listar`   | Mostra todos os conceitos cadastrados na base   |
| `sair`     | Encerra o EconoguIA                             |
| pergunta   | Qualquer outro texto é interpretado como pergunta |

## Comportamento Esperado

O assistente deve:

- Responder perguntas relacionadas à economia
- Utilizar apenas informações presentes na base de conhecimento
- Utilizar linguagem simples e objetiva
- Evitar respostas inventadas
- Informar quando não possuir informação suficiente para responder

## Limitações

- O assistente não consulta informações em tempo real
- As respostas dependem exclusivamente dos conceitos cadastrados na base de conhecimento
- A busca é baseada em palavras-chave; perguntas muito elaboradas podem não encontrar o conceito correto
- Perguntas sobre assuntos não cadastrados retornam uma mensagem informando que a informação não foi encontrada

## Possíveis Melhorias Futuras

- Integração com uma LLM para respostas mais naturais e contextuais
- Interface gráfica (GUI) ou interface web
- Base de conhecimento expandida com exemplos práticos e dados reais
- Suporte a sinônimos (ex: "juro" encontrar "juros")
- Histórico de perguntas feitas na sessão
- 
