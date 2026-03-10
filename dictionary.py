class Dictionary:
    def __init__(self):
        self.diz=[]

    def loadDictionary(self,path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    self.diz.append(line.strip().lower())
                self.diz.sort()
        except FileNotFoundError:
            print(f"Errore: File {path} non trovato.")

    def printAll(self):
        if not self.diz:
            print("Il dizionario è vuoto.")
            return

        print(f"Contenuto del dizionario ({len(self.diz)} parole):")
        for word in sorted(self.diz):
            print(word)


    @property
    def dict(self):
        return self.diz