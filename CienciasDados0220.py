import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
import numpy as np

#Comandos
#1 - variavel = dataframe[['atributo_1','atributo_2']]

#2 - X_train, X_test, y_train, y_test = train_test_split(base_de_variaveis_independentes(X),base_de_variavel_dependente(y), test_size=tamanho_da_base_de_teste(De 0 a 1), random_state=42)

#3 - classificador.score(base_de_teste)

#4 -
#def nome_da_função(parâmetros):
#   código da função. Aqui, a função vai receber como parâmetro uma linha do dataframe, vai comparar os atributos, que no caso são o valor predito e o valor real,
#   e vai retornar se eles são iguais. Os nomes dos campos serão os definidos lá embaixo, no dataframe criado com os valores preditos e os reais.
#   Para retornar o valor, use o comando return.
#Para chamar a função, use o comando apply.
#Exemplo:
#df['acerto'] = df.apply(nome_da_função, axis = 1)
#Assim, para cada linha de df, ele vai chamar a função nome_da_função e colocar o retorno no atributo acerto. criado especificamente para isso.
#Portanto, serão enviados para nome_da_função cada valor predito e cada valor real. Se forem iguais,
#o código que você criou vai retornar 1 (ou True, ou o que quer que você queira) para o atributo acerto para aquela linha.
#No final, você vai ter um dataframe como o seguinte:
#Predito Real Acerto
#   0      0    1 (True)
#   1      0    0 (False)
#   1      1    1 (True)
#Então, você deve contar quantos verdadeiros existem e mostrar a porcentagem.
#Comando extra para baixar os dados:
X, y = datasets.load_iris(return_X_y=True, as_frame=True)

#1 - Defina as variáveis independentes usando apenas as informações das pétalas - Comando 1
X, y = datasets.load_iris(return_X_y=True, as_frame=True)
datasets_petalas = X[["petal length (cm)", "petal width (cm)"]]
display (X)

#2 - Defina a base de treino como 70% dos exemplos - Comando 2.
X_train, X_test, y_train, y_test = train_test_split(datasets_petalas,y, test_size=0.3, random_state=42)

display (X_train)

#3 - Mostre a acurácia do modelo a partir da base de teste usando o sklearn. Comando 3

#4 - Mostre a acurácia do modelo a partir da base de teste manualmente. Para isso, crie uma função. Comando 4.
#5 - Defina as variáveis independentes usando apenas as informações das sépalas. Comando 1
#6 - Defina a base de treino como 70% dos exemplos. Comando 2.
#7 - Mostre a acurácia do modelo a partir da base de teste usando o sklearn. Comando 3.
#8 - Mostre a acurácia do modelo a partir da base de teste manualmente.  Para isso, crie uma função. Comando 4.
#9 - Compare os dois modelos criados. Qual apresentou melhor acurácia?
