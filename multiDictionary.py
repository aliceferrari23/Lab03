import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionari = {
            "italian": d.Dictionary(),
            "english": d.Dictionary(),
            "spanish": d.Dictionary()
        }
        self.dizionari["italian"].loadDictionary("resources/Italian.txt")
        self.dizionari["english"].loadDictionary("resources/English.txt")
        self.dizionari["spanish"].loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language in self.dizionari:
            print(f"\n--- Contenuto Dizionario: {language.upper()} ---")
            target_dict = self.dizionari[language].dict

            if not target_dict:
                print("Il dizionario selezionato è vuoto.")
            else:
                for word in sorted(target_dict):
                    print(word)
        else:
            print(f"Errore: La lingua '{language}' non è gestita.")

    def searchWord(self, words, language):
        rich_words = []
        dizionario = self.dizionari[language].dict
        for w in words:
            rw_obj = rw.RichWord(w)
            rw_obj.corretta = w.lower() in dizionario
            rich_words.append(rw_obj)
        return rich_words

    def searchWordLinear(self, words, language):
        rich_words = []
        dizionario_lista = self.dizionari[language].dict

        for w in words:
            rw_obj = rw.RichWord(w)
            trovata = False
            # Ricerca Lineare: scorro tutta la lista
            for item in dizionario_lista:
                if item == w.lower():
                    trovata = True
                    break
            rw_obj.corretta = trovata
            rich_words.append(rw_obj)
        return rich_words

    def searchWordDichotomic(self, words, language):
        rich_words = []
        dizionario_lista = self.dizionari[language].dict

        for w in words:
            rw_obj = rw.RichWord(w)
            target = w.lower()
            trovata = False

            low = 0
            high = len(dizionario_lista) - 1

            while low <= high:
                mid = (low + high) // 2
                if dizionario_lista[mid] == target:
                    trovata = True
                    break
                elif dizionario_lista[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            rw_obj.corretta = trovata
            rich_words.append(rw_obj)
        return rich_words


