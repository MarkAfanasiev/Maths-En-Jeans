def calculer_differences(sequence):
    nouvelle_sequence = []
    for i in range(len(sequence) - 1):
        diff = abs(sequence[i] - sequence[i+1])
        nouvelle_sequence.append(diff)
    return nouvelle_sequence

def formater_ligne(sequence):
    return " ".join(map(str, sequence))

def lancer_conjecture():
    print("Entrez votre suite de base (séparée par des espaces).")
    print("Exemple: 1 2 3 4 5 6")
    
    entree = input("\nVotre suite : ")
    
    try:
        suite_actuelle = [int(x) for x in entree.split()]
    except ValueError:
        print("Mettez les nombres correctement")
        return
    
    iteration = 0
    premiers_elements = []

    while len(suite_actuelle) > 0:
        ligne_str = formater_ligne(suite_actuelle)
        padding = " " * iteration
        print(f"{padding}{ligne_str}")
        premiers_elements.append(suite_actuelle[0])
        suite_actuelle = calculer_differences(suite_actuelle)
        iteration += 1

if __name__ == "__main__":
    lancer_conjecture()
