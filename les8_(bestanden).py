"""
OPDRACHT:
Maak een tekstbestand met de naam, de geboortedatum en het telefoonnummer van je vrienden.
Maak een programma waarbij je de naam van een vriend invoert en het programma de gegevens van die vriend afdrukt
met behulp van het tekstbestand dat je hebt gemaakt.
let op dat je een ty inbouwt zodat zelfs als het bestand niet gevonden wordt je programma blijft draaien.

voorbeeld format txt bestand:
Naam1,Geboortedatum1,Telefoonnummer1
Naam2,Geboortedatum2,Telefoonnummer2
Naam3,Geboortedatum3,Telefoonnummer3

"""

"""
OPDRACHT:
Als docent ben je benieuwd wat het gemiddelde aan cijfers is voor jou klas.
maak met je python programma die dit voor je berekent. 
en een leeg tekstbestand maakt en vervolgens vult met een input voor persoon en cijfer.
maak ook een input voor het vak maar deze hoeft maar 1 keer ingevuld te worden.
maak een functie die het gemiddelde van de cijfers van je tekstbestand berekend en print

"""





"""
OPDRACHT:
Opdrachtbeschrijving:

Je gaat een taalanalysetool maken met behulp van Python.
De taalanalysetool zal een tekstbestand lezen en enkele analyses uitvoeren om informatie over
de taal en het gebruik van woorden in de tekst te achterhalen.
je krijgt van ons een voorbeeld textbestand genaamd tekstbestand.txt zet deze in je project.

Opdracht Eisen:
Je Gaat een Text_Analizer klasse maken met
3 functie hierin en als parameters een input_bestand(bestand met de tekst erin) en een output_bestand.
1.  count_words(): Telt het aantal woorden in het tekstbestand en slaat het
    op in het uitvoerbestand.
2.  detect_language(): Detecteert de taal van de tekst op basis van het aantal voorkomende woorden
    die veel gebruikt worden in een specifieke taal. De gedetecteerde taal wordt opgeslagen in het uitvoerbestand.
    TIP gebruik hier arrays van de lidwoorden van de taal voor.
3.  calculate_word_frequency(): Checkt of de tekst nederlands is en Berekent dan de frequentie van woorden in de tekst.
    Alleen woorden met een frequentie van 5 of meer worden in het uitvoerbestand geschreven.
    Je krijgt hierbij een array van ons van woorden die niet meetellen. verwerk dit in je code.
    function_words = ['ik', 'jij', 'hij', 'zij', 'wij', 'jullie', 'zij', 'mij', 'jou', 'hem', 'haar',
                                        'ons', 'hen', 'mijn', 'jouw', 'zijn', 'haar', 'ons', 'hun', 'de', 'het', 'een',
                                        'in', 'op', 'bij', 'door', 'voor', 'tegen', 'met', 'uit', 'van', 'naar', 'na',
                                        'vanaf', 'tot', 'om', 'over', 'onder', 'naast', 'tussen', 'sinds', 'totdat',
                                        'zodra', 'zolang', 'voordat', 'nadat', 'terwijl', 'hoewel', 'ofschoon',
                                        'indien', 'tenzij', 'mits', 'aangezien', 'daarom', 'bijvoorbeeld', 'althans',
                                        'immers', 'immers', 'namelijk', 'immers', 'ook', 'weliswaar', 'uiteraard',
                                        'natuurlijk', 'eigenlijk', 'feite', 'blijkbaar', 'inderdaad', 'tenminste',
                                        'misschien', 'waarschijnlijk', 'hopelijk', 'helaas', 'wel', 'niet', 'nooit',
                                        'soms', 'vaak', 'altijd', 'wellicht', 'en', 'dat', 'zei', 'aan', 'ze', 'nog',
                                        'te', 'die', 'toen', 'ging', 'is', 'je', 'er', 'maar', 'had', '-', 'moest',
                                        'hele', 'was', 'deden', 'veel', 'we', 'nu', 'daar', 'dan', 'zich', 'heb', 'wat',
                                        'als', "'t", 'zo', 'zou', 'al', 'eens', 'u']

    Stappenplan voor de taalanalysetool in Python:

1.  Lees de opdrachtbeschrijving goed door en maak een plan van aanpak.

2. Maak een nieuwe Python file aan en noem deze text_analyzer.py.

3. Definieer de Text_Analizer klasse en geef de input_file en output_file als parameters.
    De class heeft als instantie variabelen self.word_frequency en self.language die nog niet zijn geïnitialiseerd.

4.  Definieer de count_words methode in de Text_Analizer klasse. Open het input bestand in read mode en lees de inhoud.
    Tel vervolgens het aantal woorden in de tekst en sla dit op in het uitvoerbestand.
    Gebruik hiervoor de len() en split() methoden op de inhoud van het input bestand en schrijf
     het resultaat weg met behulp van
    de write() methode en het "a" argument in de open() methode.

5.  Definieer de detect_language methode in de Text_Analizer klasse.
    Open het input bestand in read mode en lees de inhoud.
    Splits vervolgens de inhoud op in losse woorden. Maak vervolgens lijsten van lidwoorden in verschillende talen
    (dutch_articles, english_articles, german_articles) en tel het aantal keren dat
    deze lidwoorden voorkomen in de tekst.
    Als het aantal keren dat een taal specifiek lidwoord voorkomt, hoger is dan de andere lidwoorden,
    dan wordt de tekst waarschijnlijk in die taal geschreven. Als er geen duidelijke winnaar is,
    is de taal onbekend. Sla de gedetecteerde taal op in self.language en schrijf het weg in het uitvoerbestand.

6.  Definieer de calculate_word_frequency methode in de Text_Analizer klasse.
    Controleer of de taal Nederlands is en open het input bestand in read mode en lees de inhoud.
    Splits vervolgens de inhoud op in losse woorden en maak een lege
    dictionary om de frequentie van de woorden bij te houden.
    Loop door alle woorden in de tekst en als een woord geen lidwoord is en niet in de function_words lijst staat,
    voeg dan het woord toe aan de dictionary of verhoog de frequentie van dat woord als het al bestaat.
    Schrijf alleen de woorden weg in de dictionary waarvan de frequentie 5 of meer is naar het uitvoerbestand.

7.  Test de text_analyzer.py file door de Text_Analizer klasse te initialiseren met de input_file en output_file.
    Roep vervolgens de drie methodes aan in volgorde count_words(), detect_language() en calculate_word_frequency().
    Controleer de output van het uitvoerbestand en kijk of deze overeenkomt met de verwachte resultaten hieronder.

    Word count: 581
    Language: Nederlands
    Word frequencies:
    vosseval: 5
    griet: 6
    geld: 6
    piet,: 5

8.  Maak een tweede test met een ander input bestand om te kijken of de code in het
    algemeen werkt en niet alleen voor een specifieke tekst.

"""
