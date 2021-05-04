# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# 
# | Nome        | nUSP           | 
# | ------------- |:-------------:|
# | Pedro Raul Taborga da Costa | 4537076 |
# | Flavio de Figueiroa Teixeira Silva | 11270722|
# 
# 
# ## Tarefas

# %%
import pandas as pd

df_or = pd.DataFrame({
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y":  [0,1,1,1]
})
df_and = pd.DataFrame({
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y":  [0,0,0,1]

})


# %%
import random as r

def random_weight(k: int, min_v: int = -5, max_v: int = 5, n_decimal: int = 8):
    if 0 in (k,min_v,max_v,n_decimal):
        raise ValueError("Valores devem ser maiores que 0")
    w_list = [0]
    r_min = min_v*(10**n_decimal)
    r_max = max_v*(10**n_decimal)
    while 0 in w_list:
        w_list = list(map(lambda x : x/(10**n_decimal),r.choices(range(r_min,r_max),k=k)))
    return w_list

def fnet(net):
    return 1 if net >= 0.5 else 0

def perceptron_train(data: pd.DataFrame, eta: int = 0.1, threshold: float = 1e-2):
    n_cols = len(data.columns.to_list())
    last_col = data.columns.to_list()[-1]
    classes_values = data[last_col]

    X = data.iloc[:,:-1]
    Y = classes_values

    weights = random_weight(n_cols)
    weights = [-0.1795974,0.196303,-0.1550512 ] #Tirar
    sqerror = 2*threshold

    while(sqerror > threshold):
        sqerror = 0
        for i, row in X.iterrows():
            theta = pd.Series({"theta":1})
            row = row.append(theta)

            net = (row * weights).sum() #esse sum talvez
            y_output = fnet(net)
            y_input = Y.iloc[i]
            
            error = y_input - y_output
            print(row.shape)            
            sqerror += error**2


            dE2 = 2*error*(-net)
            weights = weights - eta * dE2
        print("Squared error: ",sqerror)
        sqerror = sqerror/(X.shape[0])
        print("Squared dividido: ", sqerror)
    return weights

    # print(Y)
print(perceptron_train(df_and))



# %%



