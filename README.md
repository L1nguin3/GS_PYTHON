# Projeto RAIZ — acompanhamento da versão Python

ESSE ARQUIVO MD NÃO É O README FINAL, APENAS UTILIZO ELE PARA INFORMAR OS INTEGRANTES DE EQUIPE O QUE ESTÁ SENDO FEITO ATÉ AGORA. README FINAL SERA FEITO APÓS A CONCLUSÃO DESTE PROJETO.

## Sobre o projeto

O RAIZ é uma proposta de apoio a pequenos produtores de hortaliças. A ideia é acompanhar a umidade do solo e a temperatura para indicar o estado atual do canteiro e, nas próximas etapas, estimar quando pode ser necessário irrigar.

Este repositório registra o desenvolvimento da parte em Python da Global Solution 2026.2. O código está sendo construído aos poucos pelo aluno, com foco em entender e conseguir explicar cada trecho.

## O que já funciona em `raiz.py`

- Mantém leituras de umidade e temperaturas em duas listas relacionadas pela posição.
- Classifica a umidade nos estados `SENSOR FALHOU`, `IRRIGAR AGORA`, `ATENÇÃO` e `SOLO OK`.
- Repete a solicitação de números enquanto estiverem fora da faixa informada.
- Apresenta um menu para cadastrar leituras, listar registros e sair.
- Lista umidade, temperatura e classificação de cada registro.
- Confere se as listas têm o mesmo tamanho e informa quando não há registros.
- Calcula o coeficiente `k` da curva a partir da temperatura.

## Como executar

Com Python 3.10 ou mais recente, abra um terminal nesta pasta e execute:

```text
python raiz.py
```

O programa usa `match/case`, disponível a partir do Python 3.10.

## Estado atual e próximo passo

O menu e o cadastro básico estão em andamento. A função `calcular_k(temperatura)` já foi escrita e os valores de referência conferidos: `0.0096` a 22 °C e `0.0228` a 34 °C.

No arquivo atual, essa função aparece depois do laço principal do menu. Como o menu só termina quando a pessoa escolhe sair, o fluxo normal não chega à definição enquanto o menu está aberto. Antes de conectar o cálculo a uma opção do menu, será preciso posicionar a função antes do laço.

Próxima etapa de estudo: calcular o tempo estimado até a umidade chegar ao limite crítico de 40%, respeitando o caso em que a umidade já está em 40% ou menos.

## Limites e cuidados

- A umidade aceita valores de -100 a 200 para permitir simular falhas do sensor; valores fora de 0 a 100 são classificados como `SENSOR FALHOU`.
- A temperatura aceita valores de 15 a 40 °C, que é o intervalo definido para a fórmula atual.
- Letras digitadas onde se espera um número ainda podem causar erro. O uso de `try/except` ou outra forma de validação precisa ser confirmado com o professor.
- Os parâmetros da curva e a hipótese do problema ainda dependem da entrevista com o produtor e podem mudar após essa validação.
- Qualquer valor de água poupada deve ser apresentado como estimativa, com suas premissas explicadas.

## Uso de IA

As regras da disciplina determinam que a IA seja usada como copiloto para explicar conceitos, propor exercícios e revisar o código. O aluno escreve e precisa compreender cada linha. Os prompts reais e a análise crítica do uso de IA devem ser registrados no arquivo de entrega `prompts.md`, conforme a orientação do professor.

## Arquivos

- `raiz.py` — protótipo atual do menu e das leituras.
- `testes_codigo.py` — rascunho comentado usado para conferir a função de cálculo de `k`.
- `CONTEXTO_RAIZ.md` — estado do projeto preparado para retomar o trabalho com outras IAs.
