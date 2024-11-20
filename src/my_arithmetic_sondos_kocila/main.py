
from src.my_arithmetic_sondos_kocila.pgcd import gcd

if __name__ == "__main__":
    # Demander les deux entiers à l'utilisateur
    a = int(input("Entrez le premier entier : "))
    b = int(input("Entrez le deuxième entier : "))
    
    # Calculer le PGCD
    result = gcd(a, b)
    
    # Afficher le résultat
    print(f"Le PGCD de {a} et {b} est : {result}")