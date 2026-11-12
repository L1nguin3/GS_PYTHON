# Projeto RAIZ — acompanhamento da versão Python

> Este arquivo ainda não é o README final da entrega. Ele serve para manter a equipe informada sobre o que já foi feito na parte de Python. O README final será preparado depois que o projeto estiver concluído.

## Sobre o projeto

O RAIZ é uma proposta de apoio a pequenos produtores de hortaliças. A ideia é acompanhar a umidade do solo e a temperatura para mostrar o estado do canteiro e estimar quantas horas faltam para atingir o limite de irrigação definido no modelo.

Este repositório registra o desenvolvimento da parte em Python da Global Solution 2026.2. O código está sendo construído aos poucos pelo aluno, com foco em entender e conseguir explicar cada trecho.

## O que já funciona em `raiz.py`

- Mantém nomes de canteiros, leituras de umidade e temperaturas em três listas relacionadas pela posição.
- Classifica a umidade nos estados `SENSOR FALHOU`, `IRRIGAR AGORA`, `ATENÇÃO` e `SOLO OK`.
- Repete a solicitação do nome enquanto estiver vazio e valida números dentro das faixas definidas.
- Apresenta um menu para cadastrar, listar, calcular horas até irrigar e sair.
- Lista canteiro, umidade, temperatura e classificação de cada registro.
- Confere se as três listas têm o mesmo número de registros e informa quando não há registros.
- Calcula `k(T)` e estima o tempo até 40% atualizando a umidade hora a hora, sem `import math`.

## Como executar

Com Python 3.10 ou mais recente, abra um terminal nesta pasta e execute:

```text
python raiz.py
```

O programa usa `match/case`, disponível a partir do Python 3.10.

## Estado atual

O menu, o cadastro com nome de canteiro, a listagem e o cálculo de horas estão integrados em `raiz.py`. Os nomes iniciais `Canteiro A`, `Canteiro B` e `Canteiro C` são dados fictícios usados para desenvolvimento.

O cálculo usa a curva hora a hora, por isso os resultados são horas inteiras. O aluno informou que testou os cenários e que o fluxo do menu está funcionando. Nos dados exibidos durante o teste, 80% a 30 °C resultou em 38 horas; 55% a 28 °C, 20 horas; e leituras de 38% resultaram em 0 horas.

Os exercícios de cálculo, integração ao menu, identificação por canteiro, validação básica e fluxo completo foram concluídos pelo aluno. A validação de texto não numérico ainda depende de orientação do professor.

## Limites e cuidados

- A umidade aceita valores de -100 a 200 para permitir simular falhas do sensor; valores fora de 0 a 100 são classificados como `SENSOR FALHOU`.
- A temperatura aceita valores de 15 a 40 °C, que é o intervalo definido para a fórmula atual.
- Letras digitadas onde se espera um número ainda podem causar erro. O uso de `try/except` ou outra forma de validação precisa ser confirmado com o professor.
- Nome vazio é recusado; um nome composto apenas por espaços ainda pode ser aceito. O uso de `.strip()` precisa ser confirmado com o professor.
- A estimativa hora a hora arredonda para a primeira hora inteira em que o modelo atinge 40%; por isso pode diferir do cálculo contínuo.
- Os parâmetros da curva e a hipótese do problema ainda dependem da entrevista com o produtor e podem mudar após essa validação.
- Qualquer valor de água poupada deve ser apresentado como estimativa, com suas premissas explicadas.

## Uso de IA

As regras da disciplina determinam que a IA seja usada como copiloto para explicar conceitos, propor exercícios e revisar o código. O aluno escreve e precisa compreender cada linha. Os prompts reais e a análise crítica do uso de IA devem ser registrados no arquivo de entrega `prompts.md`, conforme a orientação do professor.

## Arquivos

- `raiz.py` — protótipo atual do menu e das leituras.
- `testes_codigo.py` — rascunho comentado usado para conferir a função de cálculo de `k`.
- `CONTEXTO_RAIZ.md` — estado do projeto preparado para retomar o trabalho com outras IAs.
- `prompts.md` — registro do uso de IA, ainda a conferir com as exigências do professor.
