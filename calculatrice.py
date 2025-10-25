"""
Calculatrice Simple
Une calculatrice en ligne de commande pour les opérations de base
"""

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustrait b de a"""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres"""
    return a * b

def diviser(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def afficher_menu():
    """Affiche le menu des opérations"""
    print("\n=== Calculatrice Simple ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    print("=" * 27)

def main():
    """Fonction principale de la calculatrice"""
    while True:
        afficher_menu()

        choix = input("\nChoisissez une opération (1-5): ")

        if choix == "5":
            print("Au revoir!")
            break

        if choix not in ["1", "2", "3", "4"]:
            print("Choix invalide. Veuillez réessayer.")
            continue

        try:
            a = float(input("Premier nombre: "))
            b = float(input("Deuxième nombre: "))

            if choix == "1":
                resultat = additionner(a, b)
                print(f"\nRésultat: {a} + {b} = {resultat}")
            elif choix == "2":
                resultat = soustraire(a, b)
                print(f"\nRésultat: {a} - {b} = {resultat}")
            elif choix == "3":
                resultat = multiplier(a, b)
                print(f"\nRésultat: {a} × {b} = {resultat}")
            elif choix == "4":
                resultat = diviser(a, b)
                print(f"\nRésultat: {a} ÷ {b} = {resultat}")

        except ValueError as e:
            print(f"\nErreur: {e}")
        except Exception as e:
            print(f"\nUne erreur s'est produite: {e}")

if __name__ == "__main__":
    main()
