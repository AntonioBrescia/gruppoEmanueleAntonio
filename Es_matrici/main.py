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