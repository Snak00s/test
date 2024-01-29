import numpy as np
import matplotlib.pyplot as plt

def f(phrase) :
    M=[]
    C=[]
    for i in phrase :
        c=0
        for j in phrase :
            if j==i :
                c=c+1
        if i not in M :     #On verifie si la lettre est deja presente pour éviter les doublons.
            M=M+[i]
            C=C+[c]
    pairs = list(zip(M, C)) #On regroupe les deux listes en une seule pour que le tri se fasse sur les deux listes en même temps.
    pairs.sort()            #On trie les deux listes en même temps.
    M, C = zip(*pairs)      #On les dezippe pour les remettre dans les listes d'origine.
    P=[M,C]
    plt.bar(P[0],P[1])
    return plt.show()
user_input = input("Entrez une phrase : ")
print(f(user_input))