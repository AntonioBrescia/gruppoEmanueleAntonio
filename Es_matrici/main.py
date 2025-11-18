# ====================================
# ============ CLASSE PADRE ==========
# ====================================

class GestoreMatrice:
    def __init__(self, matrice): # # Costruttore: salva la matrice dentro all'oggetto
        self.matrice = matrice

    def stampa_matrice(self): # Stampa ogni riga della matrice
        for riga in self.matrice:
            print(riga)
        print()  
        
    def valida_matrice(self): # Controlla che tutte le righe abbiano la stessa lunghezza
        if len(self.matrice) == 0: # matrice vuota -> valida
            return True
        
        lunghezza = len(self.matrice[0]) # lunghezza della prima riga
        
        for riga in self.matrice: # controllo ogni riga
            if len(riga) != lunghezza: # se una riga è diversa -> non valida
                return False
            
        return True # tutte le righe sono uguali -> valida

# ====================================
# =========== CLASSE FIGLIO =========
# ====================================

class ElaboratoreMatematco(GestoreMatrice): # La classe eredita TUTTO da GestoreMatrice

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