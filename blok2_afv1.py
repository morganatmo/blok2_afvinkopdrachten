# Naam: Morgan Atmodimedjo
# Datum: 211118
# Versie: ?

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.


def main():
    """Deze functie roept alle andere functies aan.
    input: alpaca_test.fa
    output: roept de rest van de functies aan.
    """
    try:
        bestand = "alpaca_test.fa"
        headers, seqs = lees_inhoud(bestand)

        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
    except FileNotFoundError:
        print("The file is not found. The file is either mistyped or doesn't exist")
    except KeyboardInterrupt:
        print("The keys:(Ctrl + c or delete) were clicked and interrupted the process.")
    except :
        print("There has been an unexpected error")


def lees_inhoud(bestands_naam):
    """Een functie die het volledige bestand inleest en deze scheid op headers en sequenties.
    Het resultaat zijn twee lijsten.
    input: alpaca_test.fa
    output: twee lijsten= headers en sequenties
    """
    try:
        bestand = open(bestands_naam)
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
        return headers, seqs


    except ImportError:
        print("Het bestand kan niet gevonden worden. "
              "Zet een geldig fasta bestand in dezelfde map als waar u het programma vanuit draait "
              "en probeer het dan opnieuw.")


def is_dna(seq):
    """Een functie die controleert of alle nucleotiden werkelijk in DNA voorkomen.
    Deze functie retourneert een boolean die indiceert of alle letters bestaan uit ATGC.
    input: seqs (van vorige defintie.)
    output: of het dna is of niet (true of false)
    """
    try:
        dna = False
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a + t + c + g
        if total == len(seq):
            dna = True
        return dna
    except ValueError:
        print("OOPS, the outcome of 'def is_dna' was not a valid boolean.")


def knipt(alpaca_seq):
    """Een functie die een restrictie enzym accepteert en een sequentie.
    Controleert of dit restrictie-enzym de sequentie knipt en geeft relevante output.
    Je mag hier zelf kiezen voor prints, of juist een return.
    input: enzymen.txt
    output: welke enzym knipt in de sequenties
    """
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except IOError:
        print("The file is not found. The file is either mistyped or doesn't exist")


main()
