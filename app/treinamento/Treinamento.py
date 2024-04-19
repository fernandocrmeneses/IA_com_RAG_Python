from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

class Treinamento:
    def __init__(self) -> None:
        pass
    
    def efetue_treino_teste(self, x, y, tamanho_test = 0.2, numero_rando_state = 7):
        x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size = tamanho_test, stratify = y, random_state = numero_rando_state)
        self.escalona_dados(x_teste, x_train)
        
    def escalona_dados(self, x_test, x_train):
        scaler = StandardScaler()
        scaler.fit_transform(x_train)
        x_train_escalonado = scaler.transform(x_train)
        x_test_escalonado = scaler.transform(x_test)
    
    def classificacao_com_KNN(self, x_test_escalonado, x_train_escalonado, y_train):
        error = []
        for i in range(1,10):
            knn = KNeighborsClassifier(n_neighbors = i)
            knn.fit(x_train_escalonado, y_train)
            predict_i = knn.predict(x_test_escalonado)
            error.append(np.mean(predict_i != y_train))
    
    def classificacao_com_SVM():
        pass
            