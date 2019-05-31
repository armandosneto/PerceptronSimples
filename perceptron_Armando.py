import numpy as np
import matplotlib.pyplot as plt
from random import *

def plotar(w1,w2,bias,title):
    xvals = np.arange(-1, 3, 0.01)     
    newyvals = (((xvals * w2) * - 1) - bias) / w1
    plt.plot(xvals, newyvals, 'r-')    
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis([-1,2,-1,2])
    plt.plot([0,1,0],[0,0,1], 'b^')
    plt.plot([1],[1], 'go')
    plt.xticks([0,1])
    plt.yticks([0,1])
    plt.show()

def perceptron(max_it, E, alpha, X, d):
    w = [random(),random()]
    b = random()
    t = 1
    while t < max_it and E > 0:
        e = []
        for i in range(len(X)):
            y = f(somador(w, X[i])+b)
            e.append(d[i]-y)
            corretorPesos(w,X[i],alpha,e[i])
            b = b + alpha * e[i]
            E = contaErros(e);
        t = t+1
        print(E)
        print(w)
    return w,b

def somador(w,X):
    U=0;
    for j in range(len(w)):
        U = U + (w[j] * X[j])
    return U
def corretorPesos(w,X,alpha,e):
    for j in range(len(w)):
        w[j] = w[j] + alpha * e * X[j]

def contaErros(e):
    E=0
    for k in range(len(e)):
        if e[k] != 0:
            E = E + 1
    return E
def f(U):
    if(U>0):
        return 1
    else:
        return -1

def main():
    X = [[1,1],[1,0],[0,1],[0,0]]
    d = [1,-1,-1,-1]

    
    # Implemente a função Percepton que deve retornar o vetor de pesos e o bias, respectivamente.
    max_it = 100
    E = 0.00001
    alpha = 0.1
    w, bias = perceptron(max_it, E, alpha, X, d)
    plotar(w[0],w[1],bias,"Porta lógica AND com Perceptron")

if __name__ == '__main__':
    main()