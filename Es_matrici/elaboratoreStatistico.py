# elaboratoreStatistico.py
from main import GestoreMatrice  # Importa la classe base

class ElaboratoreStatistico(GestoreMatrice):
    def trova_massimo(self):
        # Restituisce il valore massimo presente nell'intera matrice
        if not self.matrice or not self.matrice[0]:
            return None
        massimo = self.matrice[0][0]
        for riga in self.matrice:
            for valore in riga:
                if valore > massimo:
                    massimo = valore
        return massimo

    def media_riga(self, indice_riga):
        # Calcola la media dei valori di una riga specifica
        riga = self.matrice[indice_riga]
        if len(riga) == 0:
            return 0
        else:
            return sum(riga) / len(riga)


# =========================
# MENU INTERATTIVO
# =========================
if __name__ == "__main__":
    # Creazione matrice da input utente
    righe = int(input("Quante righe ha la matrice? "))
    colonne = int(input("Quante colonne ha la matrice? "))

    matrice = []
    for r in range(righe):
        while True:
            riga_input = input(f"Inserisci {colonne} numeri separati da spazi per la riga {r+1}: ")
            riga = [int(x) for x in riga_input.split()]
            if len(riga) != colonne:
                print(f"Errore: devi inserire esattamente {colonne} numeri.")
            else:
                matrice.append(riga)
                break

    elaboratore = ElaboratoreStatistico(matrice)
    print("\nMatrice salvata con successo!\n")

    # Menu principale
    while True:
        print("\nScegli un'operazione:")
        print("1 - Visualizza matrice")
        print("2 - Trova massimo")
        print("3 - Calcola media di una riga")
        print("0 - Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            print("\nMatrice:")
            elaboratore.stampa_matrice()
        elif scelta == "2":
            massimo = elaboratore.trova_massimo()
            print(f"\nValore massimo: {massimo}")
        elif scelta == "3":
            indice = int(input("Inserisci indice della riga (0-based): "))
            if 0 <= indice < righe:
                media = elaboratore.media_riga(indice)
                print(f"Media riga {indice}: {media}")
            else:
                print("Indice non valido!")
        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")
