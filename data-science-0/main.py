#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[9]:


import pandas as pd
import numpy as np


# In[10]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[11]:


black_friday.head()


# In[12]:


black_friday.tail()


# In[13]:


black_friday.shape


# In[14]:


black_friday[(black_friday.Gender == "F") &(black_friday.Age == "26-35")].shape[0]


# In[15]:


black_friday.dtypes.nunique()


# In[16]:


black_friday.dtypes


# # Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[17]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[18]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return black_friday[(black_friday.Gender == "F") &(black_friday.Age == "26-35")].shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[19]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[20]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()


# # Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[21]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return float((len(black_friday.index) - len(black_friday.dropna().index))/ len(black_friday.index))


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[22]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[23]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday.Product_Category_3.value_counts().idxmax()


# In[70]:


black_friday['Product_Category_3'].value_counts().idxmax()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[74]:


def q8():
    df=black_friday
    normalized_df=(df["Purchase"]-df["Purchase"].min())/(df["Purchase"].max()-df["Purchase"].min())
    return float(normalized_df.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[61]:


def q9():
    # Retorne aqui o resultado da questão 9.
    black_friday["Purchase_N"]=(black_friday["Purchase"]-black_friday["Purchase"].mean())/black_friday["Purchase"].std() 
    totalpadronizado = black_friday[black_friday["Purchase_N"] >= -1]
    return len(totalpadronizado[totalpadronizado["Purchase_N"] <= 1])


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[43]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return len(black_friday[(black_friday["Product_Category_2"].notna() & black_friday["Product_Category_2"].isna()) | (black_friday["Product_Category_2"].isna() & black_friday["Product_Category_2"].notna())])==0 


# In[67]:


len(black_friday[(black_friday["Product_Category_2"].notna() & black_friday["Product_Category_2"].isna()) | (black_friday["Product_Category_2"].isna() & black_friday["Product_Category_2"].notna())])==0 


# In[ ]:




