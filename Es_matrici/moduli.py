# ====================================
# =========== CLASSE FIGLIO =========
# ============ ANZELLOTTI ===========
# ====================================

import main

class ElaboratoreMatematco(main.GestoreMatrice): # La classe eredita TUTTO da GestoreMatrice

    def trasponi(self): # Metodo che crea la matrice trasposta
        righe = len(self.matrice)
        colonne = len(self.matrice[0])

        nuova_matrice = [] # sarà la matrice trasposta
        
        for c in range(colonne): # ciclo per ogni colonna della vecchia matrice
            nuova_riga = [] # diventerà una riga della trasposta
            
            for r in range(righe): # prendo l'elemento [r][c] da ogni riga r
                nuova_riga.append(self.matrice[r][c])
                
            nuova_matrice.append(nuova_riga) # aggiungo la riga costruita

        return nuova_matrice

    def moltiplica_per_scalare(self, k): # Metodo che moltiplica la matrice per uno scalare k
        nuova_matrice = []
        
        for riga in self.matrice: # per ogni riga
            nuova_riga = []
            
            for elem in riga: # moltiplico ogni elemento della riga
                nuova_riga.append(elem * k)
                
            nuova_matrice.append(nuova_riga) # aggiungo la riga modificata
            
        return nuova_matrice