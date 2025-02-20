import random

letters = [
["capable", "zdolny"], ["caution", ["ostrożność", "pouczenie"]], ["rough", ["szorstki", "przybliżony", "trudny"]], ["lethal", "śmiertelny"], ["severed", "odcięty"], ["remained", "pozostał"], ["safe", "bezpieczny"], ["unharmed", "nieuszkodzony"], ["harmed", "zraniony"], ["consuming her instead", "zamiast tego ją pochłonął"], ["rumors", "plotki"], ["occured", "wystąpił"], ["landing page", "strona docelowa"], ["interrupt", "przerywać"], ["conjecture", "przypuszczenie"],
["havoc", "spustoszenie"], ["fog", "mgła"], ["protruding", "wystające"], ["exhibit", "wystawa"], ["barely", "ledwie"], ["incentive", "zachęta"], ["haunted", "nawiedzany"], ["narrow", "węższy"], ["wider", "szerzej"], ["dodge", "unik"], ["leech", "pijawka"], ["fluttering", "trzepotliwy"], ["exceed", "przekroczyć"], ["chamber", "izba"], ["apart", "oprócz"], ["stealth", "podstępny"], ["scorched", "przypalony"], ["embedding", "osadzanie"],
["retrieve", "odzyskać"], ["lectern", "mównica"], ["desert", "pustynia"], ["merit", "zasługa"], ["squirming", "wiercić się"], ["underrated", "niedoceniany"], ["conjuring", "wyczarowywanie"], ["appearance", "wygląd"], ["draught", "przeciągi"], ["wellspring", "źródło"], ["medieval", "średniowieczny"], ["explicit", "wyraźny"], ["leather", "skóra"], ["quarry", "kamieniołom"], ["vows", "śluby"], ["stood", "stał"], ["composure", "opanowanie"],
["excessive", "nadmierny"], ["always have an out", "zawsze mam wyjście"], ["broker", "pośrednik"], ["allies", "sojusznicy"], ["lichess", "szachy"], ["reap", "zbierać"], ["reaper", "żniwiarz"], ["periodically", "cykliczne"], ["pedestals", "postumenty"], ["disable", "wyłącz"], ["enable", "włącz"], ["inference", "wnioskowanie"], ["up to date", "na bieżąco"], ["furry", "puszysty"], ["dart", "strzałka"], ["canva", "płótno"], ["map", "skartografować"],
["manufacture", "produkcja"], ["concludes", "kończy"], ["acquire", "nabyć"], ["loosely", "luźno"], ["resources", "zasoby"], ["left over by", "pozostałe po"], ["basics", "podstawy"], ["plunder", "splądrować"], ["sail", "żeglować"], ["the seas", "po morzach"], ["covenant", "przymierze"], ["fateful", "fatalny"], ["lean on", "oprzeć się"], ["worth", "opłaca się"], ["twilight", "zmierzch"], ["based on", "wzoruje się"], ["debris", "gruz"], ["floating", "ruchomy"],
["exceeding", "nadzwyczajny"], ["extraordinary", "nadzwyczajny"], ["immune", "odporny"], ["anointed", "namaszczony"], ["stalling", "opóźnianie"], ["might", "potęga"], ["belly", "brzuch"], ["tummy", "brzuch"], ["descent", ["upadek", "pochodzenie"]], ["denied", "zaprzeczony"], ["sassiest", "najbezczelniejszy"], ["briefly", "pokrótce"], ["roads", "drogi"], ["get in touch with", "zorientować się w czymś"], ["tales", "opowieści"], ["tomb", "grób"],
["magnificent", "wspaniały"], ["swamp", "bagno"], ["marsh", "bagno"], ["manor", "dwór"], ["sunbeam", "promień słońca"], ["arch", "łuk"], ["heritage", "dziedzictwo"], ["mug", "kubek"], ["replenished", "uzupełniony"], ["grants", "dotacje"], ["evenly", "równomiernie"], ["disperses", "rozprasza się"], ["bonds", "pęta"], ["traces", "ślady"], ["decay", "rozkładające się"], ["elden", "starszy"], ["divine", "boski"], ["looming", "zbliżający się"],
["hideout", "kryjówka"], ["insufficient", "niewystarczający"], ["slate", "łupek"], ["shale", "łupek"], ["alignment", "wyrównanie"], ["exercise", "ćwiczenia"], ["sank", "zatopić"], ["decoy", "wabik"], ["hull", "kadłub"], ["forge", ["kuć", "rozpoczynać"]], ["radiance", "blask"], ["all of a suddan", "nagle"], ["deploy", "wdrożyć"], ["simultaneously", "jednocześnie"], ["requirement", "wymóg"], ["clever", "bystry"], ["mog", "odjeżdżać"], ["spare you", "oszczędzę cię"],
["naive", "naiwny"], ["undisputed", "bezsprzeczny"], ["sight off", "widok z dala"], ["chance", ["szansa", "przypadek"]], ["relive", "przeżyć na nowo"], ["relevance", "znaczenie"], ["wholesome", "zdrowy"], ["cruise", "rejs"], ["exile", "wygnanie"], ["tide", "pływ"], ["major", "główny"], ["minor", "drugorzędny"], ["doomsday", "dzień sądu ostatecznego"], ["revered", "czczony"], ["gismo", "gadżet"], ["although", "aczkolwiek"], ["extrude", "wyciskać"],
["assets", "aktywa"], ["starve", "głodować"], ["curve", "krzywa"], ["curvature", "krzywizna"], ["gather", "zbierać"], ["solely", "wyłącznie"], ["overdrive", "zajeździć"], ["ray tracing", "śledzenie promieni"], ["spooky", "upiorny"], ["fulfillment", "spełnienie"], ["dents", "wgniecenia"], ["upon", "od"], ["encountered", "spotykany"], ["foreign", "obcy"], ["credits", "zasługi"], ["curtain", "zasłaniać"], ["hint", "wskazówka"], ["tarnish", "zmatowienie"],
["mindscape", "krajobraz umysłu"], ["retention", "zatrzymanie"], ["acquisition", "nabytek"], ["discoverability", "odkrywalność"], ["the vast", "ogromny"], ["funfair", "wesołe miasteczko"], ["overhead", "nad głową"], ["buckle up", "wziąć się do roboty"], ["lit up", "naćpany"], ["demystify", ["demistyfikować", "objaśniać"]], ["hands-on", "praktyczny"], ["wrap it up", ["zawiń to", "zakończyć"]], ["pipeline", "rurociąg"], ["coverage", "zasięg"],
["cover", "relacjonować"], ["intimate", "intymne"], ["smithing", "kucie"], ["smith", "kowal"], ["match", "pasować"], ["traces", "ślady"], ["cashing", "spieniężanie"], ["mimic", "imitować"], ["trailer park", "park przyczep kempingowych"], ["conducting", "przeprowadzanie"]]

start = input("POL - UK ? : ")

count = 0

if start.lower() == "pol":
    # Główna pętla programu
    while True:
        # Losowanie słowa
        x = random.randint(0, len(letters) - 1)  # Losowanie słowa z listy
        word_pair = letters[x]  # Wylosowana para słów

        # Sprawdzanie, czy angielskie słowo ma jedno czy więcej tłumaczeń
        if isinstance(word_pair[1], list):
            correct_translation = random.choice(word_pair[1])  # Wybór jednego z tłumaczeń, jeśli jest ich więcej
        else:
            correct_translation = word_pair[1]

        # Pytanie użytkownika
        print(f"\nCo to znaczy: {word_pair[0]} (wpisz 'exit', aby zakończyć)")

        # Pętla do zgadywania
        while True:
            user_input = input("Twoja odpowiedź: ")

            # Sprawdzenie, czy użytkownik chce zakończyć program
            if user_input.lower() == "exit":
                print("Zakończono program.")
                exit()  # Zakończenie działania programu

            # Sprawdzenie poprawności odpowiedzi
            if user_input.lower() == correct_translation.lower():
                print(f"Dobrze! {word_pair[0]} to {correct_translation}.")
                break  # Wyjście z pętli i losowanie nowego słowa
            else:
                print("Źle. Spróbuj jeszcze raz.")
elif start.lower() == "uk":
    # Główna pętla programu
    while True:
        # Losowanie słowa
        x = random.randint(0, len(letters) - 1)  # Losowanie słowa z listy
        word_pair = letters[x]  # Wylosowana para słów

        # Sprawdzanie, czy angielskie słowo ma jedno czy więcej tłumaczeń
        if isinstance(word_pair[1], list):
            pol_word = random.choice(word_pair[1])  # Wybór jednego z tłumaczeń, jeśli jest ich więcej
        else:
            pol_word = word_pair[1]

        # Pytanie użytkownika
        print(f"\nCo to znaczy: {pol_word} (wpisz 'exit', aby zakończyć)")

        # Pętla do zgadywania
        while True:
            user_input = input("Twoja odpowiedź: ")

            # Sprawdzenie, czy użytkownik chce zakończyć program
            if user_input.lower() == "exit":
                print("Zakończono program.")
                exit()  # Zakończenie działania programu

            # Sprawdzenie poprawności odpowiedzi
            if user_input.lower() == word_pair[0]:
                count += 1
                print(f"Dobrze! {pol_word} to {word_pair[0]}. Słowo nr. {count}")
                break  # Wyjście z pętli i losowanie nowego słowa
            else:
                print("Źle. Spróbuj jeszcze raz.")