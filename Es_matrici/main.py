# main
# classe padre 
class GestoreMatrice:
    def __init__(self, matrice):

        self.matrice = matrice

    def stampa_matrice(self):
        for riga in self.matrice:
            print(riga)
        print()  
        
    def valida_matrice(self):
        if len(self.matrice) == 0:
            return True
        lunghezza = len(self.matrice[0])
        for riga in self.matrice:
            if len(riga) != lunghezza:
                return False
        return True
    
# ==========================
# TEST GESTORE MATRICE
# ==========================
if __name__ == "__main__":
    print("=== TEST GESTORE MATRICE ===")
    matrice_test = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    gestore = GestoreMatrice(matrice_test)

    print("Stampa matrice:")
    gestore.stampa_matrice()

    print("Matrice valida?", gestore.valida_matrice())



