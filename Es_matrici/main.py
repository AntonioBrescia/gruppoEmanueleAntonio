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