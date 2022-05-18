#!/usr/bin/env python
# coding: utf-8

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# 
# - Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# ### Passo a Passo de um Projeto de Ciência de Dados
# 
# - Passo 1: Entendimento do Desafio
# - Passo 2: Entendimento da Área/Empresa
# - Passo 3: Extração/Obtenção de Dados
# - Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# - Passo 5: Análise Exploratória
# - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# - Passo 7: Interpretação de Resultados

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# - TV, Jornal e Rádio estão em milhares de reais
# - Vendas estão em milhões

# #### Importar a Base de dados

# In[ ]:


get_ipython().system('pip install matplotlib ')
get_ipython().system('pip install seaborn ')
get_ipython().system('pip install scikit-learn ')


# In[19]:


import pandas as pd
tabela = pd.read_csv("advertising.csv")
display (tabela)


# #### Análise Exploratória
# - Vamos tentar visualizar como as informações de cada item estão distribuídas
# - Vamos ver a correlação entre cada um dos itens

# In[22]:


import seaborn as sns 
import matplotlib.pyplot as plt

#cria gráfico
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)

#mostra o gráfico

plt.show()
#COMO AS VENDAS ESTÃO SE COMPORTANDO DE ACORDO COM OS INVESTIMENTOS


# #### Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# 
# - Separando em dados de treino e dados de teste

# In[24]:


y=tabela['Vendas']
x=tabela[['TV','Radio', 'Jornal']]

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)


# #### Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# 
# - Regressão Linear
# - RandomForest (Árvore de Decisão)

# In[25]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#criar os modelos
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#treinar os modelos
modelo_regressaolinear.fit (x_treino, y_treino)
modelo_arvoredecisao.fit (x_treino, y_treino)


# #### Teste da AI e Avaliação do Melhor Modelo
# 
# - Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

# In[29]:


previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao =  modelo_arvoredecisao.predict(x_teste)

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))


# #### Visualização Gráfica das Previsões

# In[ ]:


#árvore de decisão é o melhor modelo, vamos usar ele para fazer as previsões


# #### Como fazer uma nova previsão?

# In[31]:


#importar a tabela com as novas previsões que você quer prever
nova_tabela = pd.read_csv('novos.csv')
display(nova_tabela)
#usar o modelo_arvoredecisao e fazer um predict com ele
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

