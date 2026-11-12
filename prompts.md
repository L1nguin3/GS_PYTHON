# Registro de uso de IA — Projeto RAIZ (Python)

> Registro de uso de IA nesta conversa, atualizado em 12/11/2026. João deve conferir se este formato atende ao professor e acrescentar eventuais conversas feitas em outras ferramentas.

## Ferramenta utilizada

- **Ferramentas:** Claude e ChatGPT no Codex.
- **Finalidade:** analisar os materiais do projeto, estudar Python dentro das regras da disciplina, receber revisão das tentativas de código e organizar a documentação.
- **Fonte do registro do Claude:** conversa colada pelo aluno em 12/11/2026. O trecho recebido mistura mensagens do aluno e respostas do Claude e pode não conter o histórico completo; os prompts abaixo são os pedidos do aluno identificáveis nesse trecho.

## Prompts e pedidos relevantes feitos nesta conversa

Os trechos abaixo são pedidos reais feitos pelo aluno, agrupados por finalidade. As tentativas de código enviadas para revisão também fazem parte do histórico de uso, mesmo quando não estão reproduzidas integralmente aqui.

### Compreensão do contexto e do código

- “Analise esse contexto” — pedido de leitura do contexto geral do Projeto RAIZ.
- “analise o documento .py e veja o que foi feito” — pedido de análise do código Python existente.
- “analise, e vamos continuar o trabalho feito com o claude” — pedido para usar o progresso anterior como ponto de partida.

### Prompts identificados na conversa com o Claude

- “analise ambos os arquivos, vamos trabalhar em cima deles” — pedido para analisar os arquivos do projeto.
- “esse trabalho todo é dividido para 7 matérias e 7 trabalhos dos quais iremos apresentar como um só com um pitch de 3 minutos, vamos trabalhar com python, mas antes, vou pegar o conteudo que iremos usar para trabalhar em python.” — explicou a estrutura da Global Solution e avisou que enviaria o material da disciplina de Python.
- “tem mais esse arquivo que eu quero que você analise, vou procurar sobre a questão de python também” — pediu análise de outro arquivo enquanto procurava as regras de Python.
- “o classificar_umidade eu já entendi que é antes do while, mas a nova def \"pedir_numero\" também é antes do while?” — perguntou onde posicionar uma nova função.
- “esqueci de mandar isso:” — enviou a definição de `classificar_umidade()` para complementar o código em análise.
- “antes disso, vamos analisar o código e ver” seguido de “correções sugeridas / correções necessárias / sugestões (com base nas regras e nas informações que já temos)” — pediu uma revisão estruturada do código antes de continuar.
- “você pode gerar um .md dos exercicios que foi feito e o que resta fazer?” — pediu um documento de progresso e exercícios.

Além desses pedidos, o aluno compartilhou tentativas de código para `pedir_numero()`, `classificar_umidade()` e o menu, para receber orientação e revisão.

### Aprendizado e revisão de código com o ChatGPT

- “faça as correções por mim, deixe apenas os exercícios para eu pensar, está tarde e eu estou ligeiramente cansado” — pedido de ajuda com as correções; o contexto da disciplina estabelece que o aluno deve escrever o código.
- “então gere um outro arquivo .py com as correções para que eu possa fazer a leitura, mude nomes, termos e variaveis para que eu seja obrigado a escrever no meu código as alterações e correções, adicione explicações dos códigos em comentários dentro desse novo arquivo para eu também ser obrigado a fazer a leitura e aprender melhor” — pedido de material didático separado para estudar e reescrever as ideias.
- O aluno enviou tentativas de código para `classificar_umidade()`, `pedir_numero()`, o menu e a listagem de umidade/temperatura, pedindo continuidade e revisão por etapas.
- O aluno enviou uma tentativa de `calcular_k(temperatura)` e informou que os testes de referência produziram os resultados esperados.
- O aluno enviou tentativas de `calcular_horas(umidade, temperatura)` para receber revisão da lógica de simulação hora a hora, sem `import math`.
- “me de a lógica pra eu ver como ficaria” — pedido de explicação em pseudocódigo para orientar a tentativa, sem entregar a função pronta.
- “vamos fazer os ultimos 5 exercicios sendo aqueles que você já mandou” — pedido para retomar os cinco exercícios pendentes, um por vez.
- O aluno informou que os testes do cálculo de horas estavam funcionando e enviou a saída do menu para revisão.
- “vamos definir nomes de canteiros como premissas, assim fica mais fácil de continuarmos a trabalhar” — decisão de usar nomes fictícios de canteiros como dados de desenvolvimento.
- O aluno propôs validar o nome vazio e enviou a função `pedir_nome_canteiro()` para revisão.
- O aluno enviou a alteração do cadastro e da listagem para associar o nome do canteiro às leituras.
- “antes, atualize o prompts.md e o readme por favor” — pedido para atualizar os documentos depois de concluir os exercícios.
- “o que falta ainda a ser feito para concluirmos essa parte de python?” — pedido de lista de pendências do app e da entrega.
- “me de a lista dos exercicios restantes, depois das etapas restantes para entrega” — pedido de separar exercícios de estudo do checklist final.
- “me de o contexto dos exercicios em um .md” — pedido para registrar o plano de estudos em Markdown.

### Documentação do projeto

- “por agora, vamos parar um pouco, analise os arquivos e monte um readme ou escreva dentro do \"README.md\" o que foi feito até agora para que meus colegas possam ler e analisar o que foi feito, tambem atualize o PROJETO RAIZ que eu fiz para usar com outras IAs com o mesmo estillo do que está feito lá. Deixe o readme mais humanizado o possivel por favor” — pedido para documentar o estado observado do projeto e preparar contexto de continuidade.
- “gere pra mim o prompts.md de tudo até agora (que seja realmente relevante)” — pedido para compilar o uso relevante de IA.

## Como a IA foi usada

- Leu o contexto fornecido pelo aluno e resumiu objetivos, riscos e dependências do projeto.
- Revisou o código que o aluno compartilhou, apontando acertos, erros de lógica e pontos para o próprio aluno corrigir.
- Explicou listas paralelas, validação, funções, `k(T)` e a aproximação da curva hora a hora usando `while`, com exercícios incrementais.
- Criou e atualizou documentação de acompanhamento: `README.md`, `CONTEXTO_RAIZ.md` e `EXERCICIOS_RESTANTES_PYTHON.md`.
- Sugeriu mensagens de commit para descrever as alterações do cálculo.
- Não foram executados testes automatizados pela IA. O aluno informou que os testes manuais de `calcular_k()`, `calcular_horas()` e do fluxo do menu estavam funcionando. No teste compartilhado, a saída mostrou 38 horas para 80% a 30 °C, 20 horas para 55% a 28 °C e 0 horas para leituras de 38%.

## O que foi escrito pelo aluno

O aluno escreveu e compartilhou as funções de classificação, validação numérica, validação do nome do canteiro, cálculo de `k` e cálculo de horas, além do menu de cadastro, listagem e cálculo. A IA forneceu explicações, pseudocódigo, sugestões de correção e revisão. O aluno testou manualmente os cálculos e informou que o fluxo do programa estava funcionando.

## Análise crítica do aluno

As respostas abaixo foram escritas pelo aluno. Revise-as antes da entrega para confirmar que continuam representando sua experiência e ajuste a redação se necessário.

1. **O que a IA ajudou você a entender?**
   - Resposta do aluno: A IA me ajudou a compreender melhor "def", "while" e "for". Me ajudou a fazer uma melhor leitura de código, me auxíliou com os termos comumente utilizados para fazer commits como: "feat, refactor, test" etc, me impediu de pedir um código pronto mas me deu a lógica e explicações simples para adição, correção ou remoção de código.

2. **Que sugestão da IA você precisou conferir, corrigir ou adaptar? Como conferiu?**
   - Resposta do aluno: A IA em geral me mostrava erros de lógica, os termos estavam corretos mas a lógica estava quebrada, então ela me mostrava exemplos com mapas de lógica ou até mesmo exercícios parecidos que foram feitos em sala que possuiam a mesma lógica, assim eu fazia as leituras e ia aos poucos corrigindo, sempre perguntando e reavaliando o meu código.

3. **Quais foram as dificuldades ao escrever ou testar o código por conta própria?**
   - Resposta do aluno: Lembrar as funções, variaveis e conteúdos da linguagem foram o que mais me pegou, por mais que estive regrado a usar somente aquilo que foi aprendido em sala de aula, ainda tive dificuldades para adaptar o uso de cada função dentro do código.

4. **O que você aprendeu e consegue explicar sem consultar a IA?**
   - Resposta do aluno: Foi criado até agora 4 funções, a primeira classifica a umidade e confere a necessidade de irrigar ou não o solo, a segunda pede um número que representa a umidade atual de acordo com o usuário e reflete na primeira função que classifica e diz se precisa ou não irrigar o solo,a terceira função faz o calculo da temperatura para que a quarta função calcule quantas horas restantes até uma próxima irrigação.

5. **Que limitações você percebeu no uso da IA neste projeto?**
   - Resposta do aluno: Somente as limitações que foram já pré definidas no contexto que a equipe SONDER tinha definido antes. O integrante Guilherme criou um arquivo MARKDOWN para que utilizassemos de contexto geral dentro das IAs e em poucas palavras nos proibisse de pedir código pronto, mas nos ensinasse com lógica e exercícios como fazer os nossos projetos.

## Conferência antes de entregar

- [ ] Confira se a seção de Claude contém todos os prompts relevantes da conversa anexada e acrescente outros se necessário.
- [ ] Confira se os trechos de prompts representam fielmente as conversas reais.
- [ ] Revise a análise crítica e confirme que está fiel à sua experiência.
- [ ] Confirme com o professor se o arquivo deve se chamar `prompts.md` ou `prompt.md`.
