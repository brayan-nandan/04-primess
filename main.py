
"""
Module principal pour l'affichage des nombres premiers inférieurs à 100.
Contient la fonction isprime pour tester la primalité.
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Teste si le nombre p est premier.
    Retourne True si p est premier, False sinon.
    """
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for d in range(3, int(sqrt(p)) + 1, 2):
        if p % d == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Affiche les nombres premiers inférieurs à 100.
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
