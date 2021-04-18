# Tarefa relacionada com o EP1: Escolha do conjunto de dados

**Objetivo**
Conhecer as características de algum conjunto de dados  disponível para classificação.

**Conjunto de dados escolhido**
Credit Card Fraud Detection (Disponível no [kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud))

**Conteúdo**
O conjunto de dados contém 284.807 transações que ocorreram em dois dias de setembro de 2013, realizadas por pessoas na Europa. O conjunto é altamente desbalanceado, com apenas 0.172% de transações fraudulentas. 

**Atributos**
Possui 28 atributos numéricos contínuos, derivados das variáveis originais por meio de análise de componentes principais, um atributo numérico que indica a ordem em que as transações ocorreram no tempo e outro atributo numérico com o valor original da transação, totalizando 30 atributos.

**Atributos detalhados** 
<details><summary>Clique aqui</summary>
It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. 
</details>
<hr>

**Tarefas**

- [ ] Fazer a leitura do conjunto de dados  escolhido usando  bibliotecas prontas ou funções das linguagens de programação Python ou R, por exemplo a biblioteca Pandas do Python.
- [ ] Verificar se existem dados faltantes no conjunto de dados escolhido, caso sim, pesquise como lidar com eles.
- [ ] Se o conjunto de dados escolhido é desbalanceado, aplique alguma técnica de rebalanceamento existente nas bibliotecas do Python ou R.
- [ ] Aplicar alguma técnica de normalização nos dados.
- [ ] Fazer uma análise exploratória do conjunto de dados escolhido (calcular médias, medianas, variâncias, min, max)


