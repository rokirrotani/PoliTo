#INIZIO PROGETTO LAB 2

#1° Importare le librerie:
import numpy
import matplotlib
import matplotlib.pyplot as plt

# 2° Definizione della funzione "mcol": -> Converte un Array numpy in
# un vettore colonna

def mcol(v) :
    return v.reshape((v.size,1))

# 3° Definizione della funzione Load: 
# Carica il dataset da un file CSV e lo converte in una matrice di dati
# e un array di etichette (labels)
# DList : una lista temporanea per raccogliere gli attributi di ogni campione
# labelsList: Una lista per le etichette dei camopioni
# hLabels: Un dizionario per mappare i nomi delle specie di Iris ai valori interi
# Legge il file per linea, estrae gli attributi e le etichette e le aggiunge
# alle loro liste.
# - Gestisce le eccezzioni per evitare errori durante il parsing dei dati
# - Restituisce la matrice dei dati "D" e l'array delle etichette "L"

def load(fname) :
    DList = []
    labelsList = []
    hLabels = {
        "Iris-setosa" : 0,
        "Iris-versicolor" : 1,
        "Iris-virginica" : 2,
    }
    
    with open(fname) as f:
        for line in f:
            try:
                attrs = line.split(',')[0:-1]
                attrs = mcol(numpy.array([float(i) for i in attrs]))
                name = line.split(',')[-1].strip()
                label = hLabels[name]
                DList.append(attrs)
                labelsList.append(label)
            except:
                pass

    return numpy.hstack(DList), numpy.array(labelsList, dtype=numpy.int32)


    
    #Definizione della funzione "Load2" ( non usata nel main:)
    # una definizione alternativa per caricare il dataset IRIS utilizzando la 
    # libreria di : sklearn
    
def load2():

    # The dataset is already available in the sklearn library (pay attention that the library represents samples as row vectors, not column vectors - we need to transpose the data matrix)
    import sklearn.datasets
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']
 
    
# Definizione della funzione plot_hist
# Genera e salva istogrammi della distribuzione di ogni attributo per ciascuna delle tre
# specie di IRIS
# Poi separa i dati per etichetta e genera un istogramma per ciascuna classe

def plot_hist(D, L):

    D0 = D[:, L==0]
    D1 = D[:, L==1]
    D2 = D[:, L==2]

    hFea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
        }

    for dIdx in range(4):
        plt.figure()
        plt.xlabel(hFea[dIdx])
        plt.hist(D0[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Setosa')
        plt.hist(D1[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Versicolor')
        plt.hist(D2[dIdx, :], bins = 10, density = True, alpha = 0.4, label = 'Virginica')
        
        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        plt.savefig('hist_%d.pdf' % dIdx)
    plt.show()
    
# Definizione del plot_scatter:
# produce e salva scatter plot per ogni possibile coppia di attributi, mostrando
# la distribuzione e la relazione tra di essi per ciascuna classe di IRIS.

def plot_scatter(D, L):
    
    D0 = D[:, L==0]
    D1 = D[:, L==1]
    D2 = D[:, L==2]

    hFea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
        }

    for dIdx1 in range(4):
        for dIdx2 in range(4):
            if dIdx1 == dIdx2:
                continue
            plt.figure()
            plt.xlabel(hFea[dIdx1])
            plt.ylabel(hFea[dIdx2])
            plt.scatter(D0[dIdx1, :], D0[dIdx2, :], label = 'Setosa')
            plt.scatter(D1[dIdx1, :], D1[dIdx2, :], label = 'Versicolor')
            plt.scatter(D2[dIdx1, :], D2[dIdx2, :], label = 'Virginica')
        
            plt.legend()
            plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
            plt.savefig('scatter_%d_%d.pdf' % (dIdx1, dIdx2))
        plt.show()


# ESECUZIONE DEL MAIN
# Se lo script è eseguito come programma principale (non importato come modulo),
# eseguirà il blocco di codice all'interno.
# Imposta la dimensione predefinita del font per i grafici.
# Carica i dati e le etichette usando la funzione load.
# (Commentato) Chiama le funzioni plot_hist e plot_scatter per visualizzare i dati.
# Calcola la media, la covarianza, la varianza e la deviazione standard dei dati sia 
# complessivamente che per ciascuna classe di Iris.
# Stampa i risultati statistici per un'analisi generale e per classe.

if __name__ == '__main__':

    # Change default font size - comment to use default values
    plt.rc('font', size=16)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)

    D, L = load('iris.csv')
    #plot_hist(D, L)
    #plot_scatter(D, L)

    mu = D.mean(1).reshape((D.shape[0], 1))
    print('Mean:')
    print(mu)
    print()

    DC = D - mu
    
    C = ((D - mu) @ (D - mu).T) / float(D.shape[1])
    print('Covariance:')
    print(C)
    print()

    var = D.var(1)
    std = D.std(1)
    print('Variance:', var)
    print('Std. dev.:', std)
    print()
    
    for cls in [0,1,2]:
        print('Class', cls)
        DCls = D[:, L==cls]
        mu = DCls.mean(1).reshape(DCls.shape[0], 1)
        print('Mean:')
        print(mu)
        C = ((DCls - mu) @ (DCls - mu).T) / float(DCls.shape[1])
        print('Covariance:')
        print(C)
        var = DCls.var(1)
        std = DCls.std(1)
        print('Variance:', var)
        print('Std. dev.:', std)
        print()