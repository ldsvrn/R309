#!/usr/bin/python3

"""
Pour cette fonction de l'enfer, les return sont éxécutés que lorsque res = 0,
car on apelle plus la fonction divEntier() avant le return à chaque fois. On
"remonte" les return.

Pour divEntier(6, 2):
x y
6 2 # premier appel
4 2 # deuxième appel
2 2 # troisème appel
0 2 # quatrième appel, 0 est renvoyé, divEntier() n'est plus rappelé, on peut
remonter la pile

0 # return du quatrième appel
0 + 1 = 1 # return du troisème appel
1 + 1 = 2 # return du deuxième appel 
2 + 1 = 3 # return du premier appel, ce qu'on récupère dans notre programme
"""


def divEntier(x: int, y: int) -> int:
    try:
        if y <= 0: # bon j'ai pas mis pour x sinon la fonction ne fonctionne plus 
            raise ValueError("Entrez des nombres supérieurs à 0!")
        elif y == 0:
            raise ValueError("y doit être positif!")

        if x < y:
            res = 0
        else:
            x = x - y
            res = divEntier(x, y) + 1
    except TypeError:
        raise TypeError("Entrez un int!")
    except RecursionError: # normalement vu que y doit positif c'est x qui est trop grand
        raise RecursionError("Fonction éxécutée trop de fois, x trop grand.")
    else:
        return res


if __name__ == "__main__":
    for x, y in [(1000, -1), (999999, 2), (10, 0), (500, 2)]:
        print(x, y)
        try:
            print(divEntier(x, y))
        except Exception as err:
            print(err)
