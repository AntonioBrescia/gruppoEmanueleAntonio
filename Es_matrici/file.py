# ====================================
# ================ MAIN ==============
# ====================================

import moduli as mod

righe = int(input("Quante righe ha la matrice? "))
colonne = int(input("Quante colonne ha la matrice? "))

matrice = []

# Inserisco gli elementi riga per riga
while True:
    matrice.clear() # Svuoto la matrice ad ogni tentativo
    
    for r in range(righe): 
        while True:  # Ciclo finché la riga non è valida
            riga_input = input(f"\nInserisci i {colonne} valori della riga {r+1}, separati da spazi: ")
            riga = [int(x) for x in riga_input.split()]
            
            if len(riga) != colonne:
                print(f"\nErrore: devi inserire esattamente {colonne} numeri.")
            else:
                break  # riga valida
    
        matrice.append(riga)

    mat = mod.ElaboratoreMatematco(matrice) # Creo l'oggetto
    if mat.valida_matrice() == True: # vedo se è valida
        print("\nMatrice salvata con successo.")
        break
    else:
        print("\nMatrice non valida. Riprova.")
        continue

# MENU
while True:
    print("\nScegli un'operazione:")
    print("(1) Visualizza matrice")
    print("(2) Trasponi matrice")
    print("(3) Moltiplica per scalare")
    print("(0) Esci")

    scelta = input("\nScelta (0-3): ")

    match scelta:
        case "1":
            print("\nMatrice originale:")
            mat.stampa_matrice()

        case "2":
            trasposta = mat.trasponi()
            print("\nMatrice trasposta:")
            for riga in trasposta:
                print(riga)

        case "3":
            k = int(input("\nInserisci scalare: "))
            moltiplicata = mat.moltiplica_per_scalare(k)
            print(f"Matrice moltiplicata per {k}:")
            for riga in moltiplicata:
                print(riga)

        case "0":
            print("\nUscita.")
            break

        case _:
            print("\nScelta non valida. Riprova.")