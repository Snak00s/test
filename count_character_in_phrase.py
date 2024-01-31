import numpy as np
import matplotlib.pyplot as plt

def user_text(texte) :
    note = open(texte, "r")
    return f(note), note.close()
def f(phrase):
    M = []
    C = []
    for line in phrase:
        for x in line:
            if x not in M:
                M.append(x)
                C.append(1)
            else:
                index = M.index(x)
                C[index] += 1
    pairs = list(zip(M, C))
    pairs.sort()
    M, C = zip(*pairs)
    P = [M,C]
    plt.bar(P[0],P[1])
    return plt.show()


user_input = input("Entrez votre document texte (.txt) : ")
print(user_text(user_input))