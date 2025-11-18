# elaboratoreStatistico.py
from main import GestoreMatrice  # Importa la classe base

class ElaboratoreStatistico(GestoreMatrice):
    def trova_massimo(self):
        # Restituisce il valore massimo presente nell'intera matrice
        if not self.matrice or not self.matrice[0]:
            return None  # matrice vuota
        
        massimo = self.matrice[0][0]  # prendo il primo elemento come riferimento
        for riga in self.matrice:
            for valore in riga:
                if valore > massimo:
                    massimo = valore
        return massimo

    def media_riga(self, indice_riga):
        # Calcola la media aritmetica dei valori di una riga specifica
        riga = self.matrice[indice_riga]
        if len(riga) == 0:
            return 0
        else:
            return sum(riga) / len(riga)


# Test della sottoclasse
if __name__ == "__main__":
    matrice_test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    elaboratore = ElaboratoreStatistico(matrice_test)
    print("Matrice:")
    elaboratore.stampa_matrice()
    print("Massimo:", elaboratore.trova_massimo())
    print("Media riga 0:", elaboratore.media_riga(0))
    print("Media riga 1:", elaboratore.media_riga(1))
    print("Media riga 2:", elaboratore.media_riga(2))
