import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()
    txtIn = input("Scelta: ")

    if not txtIn.isdigit():
        print("Inserire un numero valido.")
        continue

    scelta = int(txtIn)
    lingue = {1: "italian", 2: "english", 3: "spanish"}

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


