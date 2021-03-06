"""O exercício proposto foi baseado no seguinte código:
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IfWD22pKXdrIKFSGt-B04qbk6nqS_rug

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

archive = 'german_credit_data.csv'
n_neighbors=40 #defino a vizinhança

#lendo nosso database
df = pd.read_csv(archive, sep = ';')

#separamos os dados ('Age','Credidt Amount') da resposta ('Risk')
X = df.drop('Risk', axis=1)
y = df.Risk

#pré processamento de dados - normatização
scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X)

#montando o treinamento e o teste com os dados obtidos
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.434, random_state=42)

# treinando o classificador
knn = KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(X_train, y_train)
print(accuracy_score(y_test, knn.predict(X_test)))

X_new = [[18, 1000]]
X_new = scaler.transform(X_new)
knn.predict(X_new)