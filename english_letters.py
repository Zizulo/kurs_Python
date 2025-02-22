import random

letters = [["branches", "gałęzie"], ["whether", "czy"], ["substitute", "zastąpić"], ["semicolon", "średnik"], ["colon", "dwukropek"], ["slash", ["ukośnik", "nacięcie"]], ["combine", "połączyć"], ["compare", "porównać"], ["scope", "zakres"], ["ternary", "trójskładnikowy"], ["advantage", "korzyść"], ["evaluation", "ocena"], ["currency", "waluta"],
["tie", ["krawat", "remis"]], ["reuse", "ponowne użycie"], ["execute", "wykonać"], ["tabs", "zakładki"], ["tab", "rachunek"], ["comma", "przecinek"], ["associated", "powiązany"], ["template", "szablon"], ["insert", "wstawić"], ["overwrite", "nadpisać"], ["square brackets", "nawiasy kwadratowe"], ["curly brackets", "nawiasy klamrowe"], ["nested", "zagnieżdżony"],
["provide", "dostarczać"], ["built-in", "wbudowany"], ["store", "przechowywać"], ["permanently", "na stałe"], ["temporary", "tymczasowy"], ["dash", "myślnik"], ["assign", "przypisać"], ["reassign", "ponownie przypisać"], ["truthy", "prawdziwy"], ["falsely", "fałszywy"], ["inherit", "dziedziczyć"], ["linked", "połączony"], ["injected", "wstrzyknięty"],
["otherwise", "w przeciwnym razie"], ["coercion", "przymus"], ["further", "dalej"], ["overcome", "pokonać"], ["several", "kilka"], ["range", "rozpiętość"], ["as well", "również"], ["typing", "pisanie"], ["void", "pusty"], ["so far", "dotychczas"], ["due", "należny"], ["equal", "równa się"], ["consecutive", "kolejny"], ["instantly", "natychmiast"],
["pattern", "wzór"], ["above", "powyżej"], ["justify", "uzasadnić"], ["adjustment", "modyfikacja"], ["stretch", "rozciągać się"], ["remainder", "reszta"], ["walkthrough", "solucja"], ["hoisting", "podnoszenie"], ["immediately", "bezpośrednio"], ["bash", "grzmotnąć"], ["bashful", "wstydliwy"], ["struggle", "walka"], ["breed", "wychowany"], ["raise", ["wychować", "wznosić"]],
["involve", "zaangażowany"], ["conquering", "zdobywanie"], ["constrains", "ograniczenia"], ["pressure", "ciśnienie"], ["dispose", "rozmieszczać"], ["reprocessing", "utylizacja"], ["income", "dochód"], ["bodily fluids", "płyny ustrojowe"], ["internal", "wewnętrzny"], ["render", "czynić"], ["capacity", "pojemność"], ["distinct", "odrębny"], ["diverse", "różnorodny"], ["vine", "pnącze"],
["environment", "środowisko"], ["blow up", "wysadzić"], ["shallow", "płytki"], ["sparse", "rzadki"], ["wave", "fala"], ["flow", "przepływ"], ["humiliating", "poniżający"], ["delay", "opóźnienie"], ["stall", "zgaśnięcie silnika"], ["immediate", "natychmiast"], ["multiply", "pomnożyć"], ["closure", "zamknięcie"], ["enclosed", "załączenie"], ["ensure", "zapewnić"], ["thoroughly", "dokładnie"], ["examine", "zbadać"],
["contribute", "przyczyniać się"], ["attend", "brać udział"], ["suspended", "zawieszony"], ["recharge", "doładować"], ["track", "śledzić"], ["underscore", "podkreślnik"], ["exclamation mark", "wykrzyknik"], ["mention", "wzmianka"], ["undo", "cofnąć"], ["directly", "bezpośrednio"], ["inner", "wewnętrzny"], ["intermediate", "pośredni"], ["template string", "ciąg szablonowy"], ["decimal", "dziesiętny"],
["commit", "popełnić"], ["commit on", "zobowiązać się"], ["relate", "odnieść się"], ["attach", "dołączyć"], ["syntax", "składnia"], ["particular", "konkretny"], ["inspect", "sprawdzać"], ["facility", "obiekt"], ["resolution", "rezolucja"], ["breaker room", "pokój wyłącznika"], ["rather", "raczej"], ["beside it", "poza tym"], ["along", "wzdłuż"], ["summary", "streszczenie"],
["utils", "użytkowe"], ["senses", "zmysły"], ["sensitive", "wrażliwe"], ["so you can", "więc możesz"], ["assembled", "zmontowane"], ["pollution", "zanieczyszczenie"], ["external", "zewnętrzny"], ["actions", "czyny"], ["the one", "ten"], ["shift", "zmiana"], ["whistleblower", "informator"], ["wardrobe", "szafa"], ["spyglass", "luneta"], ["drawer", "szuflada"], ["stand out", "wyróżniać się"],
["coil", ["cewka", "zwój"]], ["wedding", "ślub"], ["wire", "drut"], ["mess", "bałagan"], ["messed", ["zepsute", "namieszać"]], ["device", "urządzenie"], ["feel free", "nie krępuj się"], ["firmware", "oprogramowanie"], ["according", "według"], ["healthy habits", "zdrowe nawyki"], ["strict", "wymagający"], ["check out", "wymeldować się"], ["either", "też nie"], ["accompany", "odprowadzić"],
["pull", "ciągnąć"], ["got under his skin", "zalazło mu za skórę"], ["reluctantly", "niechętnie"], ["subtract", "odejmować"], ["by", "za"], ["refuse", "odmawiać"], ["blanket", "koc"], ["literally", "dosłownie"], ["remains", "szczątki"], ["remain", "pozostaje"], ["commonly", "powszechnie"], ["regretted", "żałowałem"], ["thanks for reaching out", "dziękuję za kontakt"], ["regarding", "w sprawie"], ["certain", "pewien"],
["valuable", "wartościowe"], ["hence", "stąd"], ["exact", "dokładny"], ["approach", "podejście"], ["deprecated", "przestarzałe"], ["catcher", "łapacz"], ["capture", "schwytać"], ["subfield", "podpole"], ["hilarious", "zabawne"], ["jealous", "zazdrosny"], ["boarding pass", "karta pokładowa"], ["cord", "przewód"], ["neat", "czystą"], ["lot", "działka"], ["plot", "działka"], ["obtained", "uzyskany"], ["below", "poniżej"],
["wont mind", "nie mieć nic przeciwko"], ["catch on", "zrozumieć"], ["twin primes", "liczby pierwsze"], ["disadvantages", "niedogodności"], ["to stage", "wystawiać"], ["aborts", "przerywa"], ["tricky", "zdradliwy"], ["suite", ["komplet", "apartament"]], ["execution policy", "polityka wykonania"], ["release", ["uwolnienie", "wersje"]], ["recently", "ostatnio"], ["though", "chociaż"], ["expect", "oczekiwać"], ["approved", "zatwierdzony"],
["spreadsheet", "arkusz"], ["meant to be", "jest przeznaczony"], ["on the other hand", "z drugiej strony"], ["supposedly", "rzekomo"], ["exhausted", "wyczerpany"], ["motion", "ruch"], ["bear with me", "proszę o chwile cierpliwości"], ["bug", "robak"], ["accurate", "dokładny"], ["augmentation", "powiększenie"], ["blueprint", "projekt"], ["certainly", "z pewnością"], ["straight", "prosty"], ["outer", "zewnętrzny"],
["beyond", "poza"], ["comprehension", "zrozumienie"], ["amalgamations", "połączenie"], ["prophet", "prorok"], ["unleash", "uwalniać"], ["hang out", "spędzać"], ["mock", "drwić"], ["at some point", "w pewnym momencie"], ["spy", "szpieg"], ["spy on", "szpiegować"], ["entities", "podmioty"], ["species", "gatunek"], ["broadcast", "audycja"], ["intended", "przeznaczony"], ["assessment", "ocena"], ["resemblance", "podobieństwo"],
["weaponry", "broń"], ["in mind", "w zamyśle"], ["precaution", "środek ostrożności"], ["rifle", "karabin"], ["rusty", ["zardzewiały", "zaniedbały"]], ["malfunctioned", "niesprawny"], ["entire", "cały"], ["query", "zapytanie"], ["repetitive", "powtarzalne"], ["regardless", "mimo wszystko"], ["supervisor", "kierownik"], ["odorless", "bezwonny"], ["wisp", "wiązka"], ["homeowner", "właściciel"], ["infested", "zainfekowani"], ["inability", "niezdolność"],
["soul", "dusza"], ["chase", "ścigać"], ["chase down prey", "ścigać zdobycz"], ["pose", "sprawiać"], ["consists", "składa się"], ["mammals", "ssaki"], ["hiss", "syk"], ["growl", "warczenie"], ["lurking", "przyczajony"], ["creaking", "skrzypienie"], ["slug", "ślimak"], ["slippage", "poślizg"], ["sprite", "chochlik"], ["digging", "kopanie"], ["secretions", "wydzieliny"], ["rapid", "szybko"], ["causing", "powodując"], ["ingested", "spożyty"],
["odor", "zapach"], ["susceptible", "podatny"], ["foul", "obrzydliwy"], ["under any circumstances", "pod żadnym pozorem"], ["grieving", "opłakiwać"], ["refrain", "wystrzegać się"], ["fae flu", "grypa"], ["dizziness", "zawroty głowy"], ["fatigue", "zmęczenie"], ["collective", "zbiorowa"], ["consciousness", "świadomość"], ["awareness", "świadomość"], ["silly",  "głupi"], ["slightly", "nieznacznie"], ["suppose", "przypuszczać"], ["cheeks", "policzki"],
["core", "rdzeń"], ["addition", "dodatkowy"], ["in addition", ["ponadto", "oprócz"]], ["inhabit", "zamieszkać"], ["enhanced", "wzmocniony"], ["invoices", "faktury"], ["abandon", "opuścić"], ["shall", "być"], ["convenience", "wygoda"], ["chart", "wykres"], ["figure", "wykres"], ["trunk", ["bagażnik", "trąba słonia", "skrzynia", "tułów", "pień"]], ["appliance", "urządzenie"], ["warranty", "gwarancja"], ["kettle", "czajnik"], ["up on you", "na ciebie"], ["schemes", "schematy"], ["uncovered", "odkryte"],
["baselines", "linie bazowe"], ["reinforce", "wzmocnienie"], ["getting owned", "zostać zdobytym"], ["fella", "kolega"], ["in a bit", "za chwilę"], ["thresholds", "progi"], ["stare", "gapić się"], ["overlay", "nakładka"], ["exhibit", "dowód"], ["flatten", "spłaszczyć"], ["properly", "odpowiednio"], ["ceiling", "sufit"], ["resist", "oprzeć się"], ["proficiency", "biegłość"], ["consent", "zgoda"], ["sink", "zlew"], ["jack", "lewarek"],
["playthrough", "rozgrywka"], ["rotten", "zgniły"], ["beside", "obok"], ["breaks it down", "rozbija to"], ["back and forth", "tam i z powrotem"], ["figure", "wymyślić"], ["independently", "niezależnie"], ["appreciated", "doceniony"], ["curse", "przekleństwo"], ["furnace", "piec"], ["paper clip", "spinacz do papieru"], ["throbbing", "pulsujący"], ["carry", "nosić"], ["tied", "związany"], ["indestructible", "niezniszczalny"],
["digit", "cyfra"], ["root", "pierwiastek"], ["inclusive", "obejmujący"], ["exclusive", "wyłączny"], ["bias", "uprzedzenie"], ["dig", "głębić"], ["riot", "zamieszki"], ["apparently", "najwyraźniej"], ["premise", "przesłanka"], ["tends", "tendencja"], ["needless to say", "nie trzeba dodawać że"], ["unearthed", "odkopany"], ["fae", "wróżka"], ["reboot", "ponowne uruchomienie"], ["rigged", "sfałszowany"], ["lettuce", "sałata"], ["chew", "żuć"], ["digest", "strawić"], ["poll", "głosowanie"], ["change", "drobne"],
["cheesy", ["serowy", "tandetny"]], ["stab", "dźgnięty"], ["buns", "bułki"], ["insulting", "obraźliwy"], ["harassing", "niepokojenie"], ["landlord", "gospodarz"], ["lets get down business", "zabierajmy się do pracy"], ["puberty", "dojrzewanie"], ["heavily", "mocno"], ["tuple", "krotka"], ["blank", "pusty"], ["blank", "czyste"], ["carry-on", "bagaż podręczny"], ["oughta", "powinien"], ["ought to", "powinien"], ["napkin", "serwetka"], ["drowned", "utonął"], ["raw", "surowe"],
["clatter", "brzęk"], ["thy", "twój"], ["beggar", "żebrak"], ["encroacher", "włamywacz"], ["harbinger", "zwiastun"], ["bringer", "przynoszący"], ["pestilence", "zaraza"], ["nuisance", "utrapienie"], ["rejoice", "radować się"], ["abuser", "uzależniona"], ["redeem", "odkupić"], ["decent", "przyzwoity"], ["shuffle", "człapać"], ["crawl", "pełzać"], ["affair", ["romans", "afera"]], ["slight", "niewielki"], ["tough", "trudny"], ["dirtbag", "łajdak"],
["appen", "dodać"], ["align", "wyrównać"], ["alight", "wysiadać"], ["cope", "radzić sobie"], ["drill", "wiertarka"], ["necklace", "naszyjnik"], ["you know the drill", "znasz tę procedure"], ["distort", "zniekształcać"], ["scarecrow", "strach na wróble"], ["digestion", "trawienie"], ["indeed", "rzeczywiście"], ["last but not least", "nie mniej ważny"], ["stitches", "szwy"], ["realm", "królestwo"], ["gaze", "spojrzenie"], ["pale", "blady"],
["intimidating", "onieśmielający"], ["shattered", "rozbity"], ["apex predator", "drapieżnik szczytowy"], ["time lapse", "poklatkowy"], ["neither", "żaden"], ["cage", "klatka"], ["lift up", "podnieś się"], ["wounds", "rany"], ["ribs", "żeberka"], ["cartridges", "wkłady"], ["treasures", "skarby"], ["generous", "hojny"], ["odd", "dziwne"], ["summon", "przywołać"], ["ascend", "wznieść się"], ["quote", ["zacytować", "cudzysłów"]],
["double quote", "podwójny cudzysłów"], ["whispering", "szeptanie"], ["gear", "bieg"], ["homeland", "ojczyzna"], ["mythical", "mityczny"], ["extensive", "rozległe"], ["within you", "w tobie"], ["innocent", "niewinny"], ["chapel", "kaplica"], ["hire", "wynajem"], ["impostor", "oszust"], ["extraterrestrial", "istoty pozaziemskie"], ["invading", "najeżdżający"], ["revives", "ożywia"], ["duty", "obowiązek"], ["farewell", "pożegnanie"],
["capable", "zdolny"], ["caution", ["ostrożność", "pouczenie"]], ["rough", ["szorstki", "przybliżony", "trudny"]], ["lethal", "śmiertelny"], ["severed", "odcięty"], ["remained", "pozostał"], ["safe", "bezpieczny"], ["unharmed", "nieuszkodzony"], ["harmed", "zraniony"], ["consuming her instead", "zamiast tego ją pochłonął"], ["rumors", "plotki"], ["occured", "wystąpił"], ["landing page", "strona docelowa"], ["interrupt", "przerywać"], ["conjecture", "przypuszczenie"],
["havoc", "spustoszenie"], ["fog", "mgła"], ["protruding", "wystające"], ["exhibit", "wystawa"], ["barely", "ledwie"], ["incentive", "zachęta"], ["haunted", "nawiedzany"], ["narrow", "węższy"], ["wider", "szerzej"], ["dodge", "unik"], ["leech", "pijawka"], ["fluttering", "trzepotliwy"], ["exceed", "przekroczyć"], ["chamber", "izba"], ["apart", ["oprócz", "oddalone"]], ["stealth", "podstępny"], ["scorched", "przypalony"], ["embedding", "osadzanie"],
["retrieve", "odzyskać"], ["lectern", "mównica"], ["desert", "pustynia"], ["merit", "zasługa"], ["squirming", "wiercić się"], ["underrated", "niedoceniany"], ["conjuring", "wyczarowywanie"], ["appearance", "wygląd"], ["draught", "przeciągi"], ["wellspring", "źródło"], ["medieval", "średniowieczny"], ["explicit", "wyraźny"], ["leather", "skóra"], ["quarry", "kamieniołom"], ["vows", "śluby"], ["stood", "stał"], ["composure", "opanowanie"],
["excessive", "nadmierny"], ["always have an out", "zawsze mam wyjście"], ["broker", "pośrednik"], ["allies", "sojusznicy"], ["lichess", "szachy"], ["reap", "zbierać"], ["reaper", "żniwiarz"], ["periodically", "cykliczne"], ["pedestals", "postumenty"], ["disable", "wyłącz"], ["enable", "włącz"], ["inference", "wnioskowanie"], ["up to date", "na bieżąco"], ["furry", "puszysty"], ["dart", "strzałka"], ["canva", "płótno"], ["map", "skartografować"],
["manufacture", "produkcja"], ["concludes", "kończy"], ["acquire", "nabyć"], ["loosely", "luźno"], ["resources", "zasoby"], ["left over by", "pozostałe po"], ["basics", "podstawy"], ["plunder", "splądrować"], ["sail", "żeglować"], ["the seas", "po morzach"], ["covenant", "przymierze"], ["fateful", "fatalny"], ["lean on", "oprzeć się"], ["worth", "opłaca się"], ["twilight", "zmierzch"], ["based on", "wzoruje się"], ["debris", "gruz"], ["floating", "ruchomy"],
["exceeding", "nadzwyczajny"], ["extraordinary", "nadzwyczajny"], ["immune", "odporny"], ["anointed", "namaszczony"], ["stalling", "opóźnianie"], ["might", "potęga"], ["belly", "brzuch"], ["tummy", "brzuch"], ["descent", ["upadek", "pochodzenie"]], ["denied", "zaprzeczony"], ["sassiest", "najbezczelniejszy"], ["briefly", "pokrótce"], ["roads", "drogi"], ["get in touch with", "zorientować się w czymś"], ["tales", "opowieści"], ["tomb", "grób"],
["magnificent", "wspaniały"], ["swamp", "bagno"], ["marsh", "bagno"], ["manor", "dwór"], ["sunbeam", "promień słońca"], ["arch", "łuk"], ["heritage", "dziedzictwo"], ["mug", "kubek"], ["replenished", "uzupełniony"], ["grants", "dotacje"], ["evenly", "równomiernie"], ["disperses", "rozprasza się"], ["bonds", "pęta"], ["traces", "ślady"], ["decay", "rozkładające się"], ["elden", "starszy"], ["divine", "boski"], ["looming", "zbliżający się"],
["hideout", "kryjówka"], ["insufficient", "niewystarczający"], ["slate", "łupek"], ["shale", "łupek"], ["alignment", "wyrównanie"], ["exercise", "ćwiczenia"], ["sank", "zatopić"], ["decoy", "wabik"], ["hull", "kadłub"], ["forge", ["kuć", "rozpoczynać"]], ["radiance", "blask"], ["all of a suddan", "nagle"], ["deploy", "wdrożyć"], ["simultaneously", "jednocześnie"], ["requirement", "wymóg"], ["clever", "bystry"], ["mog", "odjeżdżać"], ["spare you", "oszczędzę cię"],
["naive", "naiwny"], ["undisputed", "bezsprzeczny"], ["sight off", "widok z dala"], ["chance", ["szansa", "przypadek"]], ["relive", "przeżyć na nowo"], ["relevance", "znaczenie"], ["wholesome", "zdrowy"], ["cruise", "rejs"], ["exile", "wygnanie"], ["tide", "pływ"], ["major", "główny"], ["minor", "drugorzędny"], ["doomsday", "dzień sądu ostatecznego"], ["revered", "czczony"], ["gismo", "gadżet"], ["although", "aczkolwiek"], ["extrude", "wyciskać"],
["assets", "aktywa"], ["starve", "głodować"], ["curve", "krzywa"], ["curvature", "krzywizna"], ["gather", "zbierać"], ["solely", "wyłącznie"], ["overdrive", "zajeździć"], ["ray tracing", "śledzenie promieni"], ["spooky", "upiorny"], ["fulfillment", "spełnienie"], ["dents", "wgniecenia"], ["upon", "od"], ["encountered", "spotykany"], ["foreign", "obcy"], ["handle it", "poradzić sobie z tym"], ["unsettling", "niepokojący"], ["credits", "zasługi"], ["curtain", "zasłaniać"],
["hint", "wskazówka"], ["tarnish", "zmatowienie"], ["mindscape", "krajobraz umysłu"], ["retention", "zatrzymanie"], ["acquisition", "nabytek"], ["discoverability", "odkrywalność"], ["the vast", "ogromny"], ["funfair", "wesołe miasteczko"], ["overhead", "nad głową"], ["buckle up", "wziąć się do roboty"], ["lit up", "naćpany"], ["demystify", ["demistyfikować", "objaśniać"]], ["hands-on", "praktyczny"], ["wrap it up", ["zawiń to", "zakończyć"]],
["pipeline", "rurociąg"], ["coverage", "zasięg"], ["cover", "relacjonować"], ["intimate", "intymne"], ["smithing", "kucie"], ["smith", "kowal"], ["match", "pasować"], ["traces", "ślady"], ["cashing", "spieniężanie"], ["mimic", "imitować"], ["trailer park", "park przyczep kempingowych"], ["conducting", "przeprowadzanie"], ["subspecies", "podgatunek"], ["consistent", "spójny"], ["overall", "ogólnie"], ["accelerate", "przyspieszać"]]

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