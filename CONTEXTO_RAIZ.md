# CONTEXTO — GS 2026.2 CitizenTech · Projeto RAIZ

> Documento de continuidade do projeto. Pode ser compartilhado com outras IAs no início de uma conversa.
> Atualizado em 11/11/2026. Complementa o contexto geral e o progresso de Python enviados anteriormente.

## 0. Como a IA deve ajudar

O briefing da FIAP define a IA como copiloto: pode apoiar o aprendizado e revisar, mas não desenvolver o trabalho pelo grupo. O aluno escreve o código e precisa conseguir explicar cada linha.

Fluxo esperado para ajudar João (apelido Linguine): explicar o conceito, mostrar um exemplo simples, propor um exercício, deixar o aluno tentar e depois revisar o raciocínio e o código. Usar respostas curtas, claras e em português do Brasil. Registrar os prompts reais e a análise crítica no `prompts.md` da entrega.

As regras variam por disciplina: Front-end Design proíbe IA; Web Development pede `AI.md` se houver uso de IA; UX pede explicação do uso; Python permite copiloto com documentação em `prompts.md`. Confirmar o briefing de cada disciplina antes de ajudar a produzir entregas.

## 1. Global Solution

- FIAP, Engenharia de Software, 1º ano. Tema: CitizenTech, tecnologia construída a partir de necessidades reais.
- Uma CitizenTech integra as sete disciplinas e a equipe tem até cinco integrantes.
- Prazo informado: 19/11/2026 às 23h55; apenas um integrante envia cada disciplina.
- Links e arquivos devem estar públicos e funcionando para a correção, quando aplicável.
- O projeto deve partir de um problema próximo da equipe, com uma pessoa real que conviva com ele: observar, escutar, definir, rabiscar, construir e contar.
- Não usar dados pessoais reais; usar dados simulados ou públicos e citar a origem.
- Todo integrante deve conseguir explicar o projeto.

A ficha da CitizenTech deve incluir: nome, cidade e bairro, cidadão beneficiado, problema em uma frase, como funciona, o que cada parte faz, link do repositório, indicador de impacto e ODS conectados.

## 2. Projeto RAIZ — proposta e validação

**Proposta:** um sensor no canteiro mede umidade do solo e temperatura, indica localmente se há necessidade de irrigar e uma aplicação de apoio estima o tempo até o solo atingir o limite crítico.

**Público considerado:** pequeno produtor de hortaliças folhosas que abastece feiras de São Paulo, possivelmente no cinturão verde da RMSP.

**Problema ainda não validado:** hipótese de que o produtor irriga mais do que o necessário por receio de perder a lavoura. A entrevista com um produtor é indispensável antes de fechar a frase do problema e calibrar a proposta.

**Indicador em estudo:** litros de água economizados por ciclo, estimados com base em irrigações evitadas. Sempre identificar como estimativa e declarar as premissas.

**ODS considerados:** 2, 13, 9 e 10. Confirmar a pertinência na proposta final.

### Parâmetros provisórios do modelo

```text
U(t) = U0 * e^(-k(T) * t)
k(T) = 0,0096 + 0,0011 * (T - 22)       válido para 15 <= T <= 40 °C
Limite crítico provisório = 40 %
t = ln(U0 / 40) / k(T)                   aplicável somente se U0 > 40
```

U representa umidade percentual, t horas desde a última rega e T temperatura média do dia. Valores de referência do modelo: 80% e 34 °C dão aproximadamente 30 horas; 80% e 22 °C dão aproximadamente 72 horas. São resultados matemáticos do modelo, ainda não uma calibração agronômica local.

Estados definidos para manter consistência entre disciplinas:

- `SOLO OK`: U > 60%; LED verde, exibe leitura e fica em silêncio.
- `ATENÇÃO`: 40 < U <= 60%; LED amarelo e estimativa de horas restantes.
- `IRRIGAR AGORA`: U <= 40%; LED vermelho e alerta sonoro intermitente.
- `SENSOR FALHOU`: leitura abaixo de 0% ou acima de 100%; LED magenta, aviso e nenhuma recomendação.

A histerese de 3 pontos foi mencionada, mas a regra detalhada de entrada e saída de estado ainda precisa ser definida em equipe.

## 3. Entregas da Global Solution

1. **Matemática:** modelo e gráfico dos cenários, análise de domínio, imagem, decrescimento e limitações.
2. **UX:** escopo, requisitos, histórias com critérios de aceite e priorização.
3. **Edge Computing:** circuito standalone no Wokwi, múltiplos estados, leitura inválida, suavização e demonstração.
4. **Python:** aplicação CLI de decisão, com menu, validação, listas, repetição e documentação do uso de IA.
5. **Front-end Design:** landing page com cinco seções e os requisitos visuais definidos no briefing; IA proibida conforme contexto fornecido.
6. **Web Development:** JavaScript puro na mesma página, slideshow, formulário validado, manipulação do DOM, responsividade, organização GitHub e `AI.md` se houver uso de IA.
7. **Pitch:** vídeo de até três minutos cobrindo as nove etapas definidas no briefing.

Manter a mesma frase do problema, limites e valores de k(T), identidade visual e explicação do impacto em todas as entregas.

## 4. Python — escopo, regras e progresso real

### Rubrica e restrições

O professor pede menu, validação, entrada e saída adequadas, `if/elif/else`, `match/case`, `while`, `for`, variáveis, listas, boas práticas e boa experiência. A entrega indicada é um ZIP contendo o programa `.py`, `prompts.md` e `readme.md`; confirmar com o professor se o nome singular/plural de `prompt(s).md` está correto.

Usar somente conteúdo visto ou autorizado em aula. Conforme o relato do aluno, já foram estudados `input`, `int`, `float`, `print`, f-strings, operadores, condicionais, `while`, listas, `for`, `match/case` e funções básicas com `return`. Ainda é preciso confirmar com o professor o uso de `import math`, `try/except`, `.replace()`, `.isdigit()`, `range` e outras ferramentas.

### O que já foi praticado

- Listas: índices, `len()` e `append()`.
- Percorrer uma lista com `for`, usar condição dentro do laço e contar itens.
- Menu com `while`, `match/case` e saída com `break`.
- Funções com parâmetro e `return`.
- Validação numérica por faixa com um laço `while True`.
- Percorrer duas listas relacionadas usando contador e o mesmo índice.
- Testar os valores da função `calcular_k()` com as referências da curva.

### Estado observado em `raiz.py` em 11/11/2026

- Listas iniciais: umidades `[80, 55, 38]` e temperaturas `[30, 28, 22]`.
- `classificar_umidade()` devolve os quatro estados oficiais e confere falha do sensor primeiro.
- `pedir_numero()` pede um valor repetidamente até ele estar dentro da faixa recebida. Entrada de letras ainda pode gerar erro.
- Menu textual para cadastrar, listar e sair. As opções são validadas antes de converter para inteiro.
- Cadastro aceita umidade entre -100 e 200 para simular sensor com defeito e temperatura entre 15 e 40 °C.
- A listagem verifica se as listas têm comprimentos iguais, avisa se não houver registros e exibe umidade, temperatura e classificação.
- A função `calcular_k(temperatura)` foi escrita com a fórmula definida. O aluno informou que os testes para 22 °C e 34 °C deram os resultados esperados.
- **Ponto de organização a corrigir antes de usar a função no menu:** `calcular_k()` está atualmente depois do laço principal do menu. Colocá-la antes do menu quando chegar a hora de chamá-la durante a execução.
- `testes_codigo.py` contém apenas chamadas comentadas para conferir `calcular_k`; não é a suíte automatizada do projeto.
- O README foi criado para comunicar o progresso atual à equipe.

### O que ainda não está implementado

- Cadastro e seleção por nome de canteiro.
- Cálculo das horas até o limite crítico, incluindo o caso U <= 40.
- Histórico mais completo e relatório de água poupada com premissas validadas.
- Regra operacional da histerese.
- Tratamento de entradas não numéricas, sujeito à orientação do professor.
- Cabeçalho final com nomes e RMs da equipe, `prompts.md`, ZIP de entrega e validação do `readme.md` definitivo da ficha.

### Próximo passo didático

Continuar com uma função que estime horas até U = 40%. Primeiro discutir o domínio da fórmula: se U <= 40, já é hora de irrigar; se U > 40, aplicar o modelo e considerar a permissão do professor sobre logaritmos/imports. O aluno deve escrever a função. Depois, testar com os dois cenários de referência e comparar os resultados arredondados.

## 5. Próximas decisões e pendências

1. Realizar entrevista com produtor e validar a frase do problema.
2. Confirmar se as localidades propostas atendem ao requisito de proximidade da equipe.
3. Perguntar ao professor de Python sobre nome de `prompts.md`, `import math`, validação de texto e conteúdos ainda não confirmados.
4. Definir com o professor de Edge como simular o sensor de umidade no Wokwi.
5. Definir a histerese e manter os mesmos limites nos protótipos.
6. Completar a ficha da CitizenTech com o papel de cada parte e o link do repositório.
7. Definir a equipe, a divisão de tarefas e o ecossistema de parceiros.
8. Conferir fontes originais antes de citar dados de economia de água ou precedentes técnicos.

## 6. Como retomar com outra IA

Peça à IA para primeiro ler este documento e o `raiz.py`. Ela deve atualizar o estado com base nos arquivos, explicar um conceito de cada vez, propor um exercício pequeno e revisar a tentativa do aluno. Não deve produzir a implementação final do grupo. Toda ajuda usada na entrega de Python deve ser registrada pelo aluno no arquivo `prompts.md`, com análise crítica escrita por ele.
