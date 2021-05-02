# Tarefa relacionada com o EP1: Escolha do conjunto de dados

**Objetivo**
Entender o funcionamento do algoritmo KNN.

**Conjunto de dados escolhido**
Credit Card Fraud Detection (Disponível no [kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud))

**Conteúdo**
O conjunto de dados contém 284.807 transações que ocorreram em dois dias de setembro de 2013, realizadas por pessoas na Europa. O conjunto é altamente desbalanceado, com apenas 0.172% de transações fraudulentas. 

**Atributos**
Possui 28 atributos numéricos contínuos, derivados das variáveis originais por meio de análise de componentes principais, um atributo numérico que indica a ordem em que as transações ocorreram no tempo e outro atributo numérico com o valor original da transação, totalizando 30 atributos.

<details><summary><strong>Atributos detalhados</strong></summary>
It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. 
</details>
<hr>

**Tarefas**

- [ ] Copiar o algoritmo KNN em R descrito nas vídeo aulas, incluir comentários e executar no conjunto de dados escolhido para o EP1 ou para um outro conjunto de dados do repositório "UCI Machine Learning Repository" que tenha como tarefa "classificação" e que o tipo de atributos seja inteiro ou real.
- [ ] Escolher e implementar uma outra métrica de distância.  
- [ ] Adicionar um novo parâmetro ao algoritmo para poder escolher entre a distância euclidiana e a outra distância implementada.
- [ ] O código deve ser bem documentado (em DETALHES) de forma que seja simples identificar passagens do código que são importantes para a verificação do entendimento do grupo sobre a lógica que implementa o algoritmo KNN.
- [ ] Demonstração da execução do algoritmo com algumas instâncias de teste. Ecoar e explicar as saídas intermediárias, fazer testes com diferentes valores de k, diferentes distâncias e mostrar os plots.



