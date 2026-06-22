# Avaliação e Métricas

## Metodologia

Foram realizados testes manuais com perguntas variadas, incluindo:

- Conceitos presentes na base (esperado: resposta correta)
- Perguntas em linguagem natural, não apenas o termo exato (esperado: resposta correta)
- Conceitos ausentes da base (esperado: mensagem de não encontrado)
- Entradas inválidas como texto vazio e interrupção pelo teclado (esperado: comportamento estável)

---

## Casos de Teste

### Teste 1 — Conceito direto

**Pergunta:** O que é inflação?
**Resultado:** Resposta encontrada corretamente.
**Status:** ✅ Aprovado

---

### Teste 2 — Pergunta em linguagem natural

**Pergunta:** Pode me explicar o PIB?
**Resultado:** Conceito "pib" identificado dentro da frase; resposta encontrada corretamente.
**Status:** ✅ Aprovado

---

### Teste 3 — Sigla e termo técnico

**Pergunta:** O que é a Taxa Selic?
**Resultado:** Conceito "selic" identificado; resposta encontrada corretamente.
**Status:** ✅ Aprovado

---

### Teste 4 — Conceito ausente da base

**Pergunta:** Quem foi Milton Friedman?
**Resultado:** Conceito não encontrado; mensagem de aviso exibida corretamente.
**Observação:** Após este teste, "friedman" foi adicionado à base de conhecimento.
**Status:** ✅ Aprovado

---

### Teste 5 — Conceito presente com variação na pergunta

**Pergunta:** O que é desemprego?
**Resultado:** Resposta encontrada corretamente.
**Status:** ✅ Aprovado

---

### Teste 6 — Entrada vazia

**Pergunta:** *(enter sem digitar nada)*
**Resultado:** O sistema ignorou a entrada e aguardou nova pergunta sem travar.
**Status:** ✅ Aprovado

---

### Teste 7 — Interrupção pelo teclado

**Ação:** Usuário pressionou Ctrl+C durante a execução.
**Resultado:** O programa exibiu mensagem de encerramento e finalizou corretamente, sem gerar erro.
**Status:** ✅ Aprovado

---

## Resultados

| Métrica           | Valor |
|-------------------|-------|
| Total de testes   | 7     |
| Testes aprovados  | 7     |
| Taxa de sucesso   | 100%  |
| Conceitos na base | 30    |

## Conclusão

O EconoguIA apresentou comportamento consistente em todos os cenários testados. O agente encontra corretamente conceitos expressos em linguagem natural e trata adequadamente tanto entradas vazias quanto conceitos fora de sua base de conhecimento.

O principal ponto de atenção identificado foi a sensibilidade a variações de escrita: perguntas com erros de digitação ou sinônimos podem não retornar resultado. Isso é uma limitação conhecida do modelo de busca por palavras-chave e está listada como melhoria futura.
