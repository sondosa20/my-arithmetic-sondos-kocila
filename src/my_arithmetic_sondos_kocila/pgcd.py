def gcd(a, b):
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de deux entiers a et b.
    Utilise l'algorithme d'Euclide.
    """

    # Convertir les nombres en valeurs absolues pour gérer les négatifs
    a, b = abs(a), abs(b)
    
    while b:
        a, b = b, a % b
    return a

