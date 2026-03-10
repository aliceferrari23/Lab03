import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multi_dic=md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        cleaned_text=replaceChars(txtIn)
        words = cleaned_text.split()

        print("-" * 30)

        # 1. Metodo: "Using contains" (L'operatore 'in' di Python)
        start = time.time()
        # Supponiamo che searchWord usi l'operatore 'in' internamente
        res_contains = self._multi_dic.searchWord(words, language)
        end = time.time()
        self._print_results("Using contains", res_contains, end - start)

        print("-" * 30)

        # 2. Metodo: "Using Linear search"
        start = time.time()
        res_linear = self._multi_dic.searchWordLinear(words, language)
        end = time.time()
        self._print_results("Using Linear search", res_linear, end - start)

        print("-" * 30)

        # 3. Metodo: "Using Dichotomic search"
        start = time.time()
        res_dicho = self._multi_dic.searchWordDichotomic(words, language)
        end = time.time()
        self._print_results("Using Dichotomic search", res_dicho, end - start)

    def _print_results(self, title, results, elapsed):
        print(title)
        for rw in results:
            if not rw.corretta:
                print(str(rw))  # Stampa solo le parole errate
        print(f"Time elapsed {elapsed}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"

    for c in chars:
        text = text.replace(c, "")
    return text