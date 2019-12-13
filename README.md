# Smart toilet


Met de smart toilet willen wij de onoverzichtelijkheid van de openbare toiletten verbeteren. Doormiddel van verschillende sensoren kunnen wij de data versturen naar de backend. Met een knop kunnen wij een lichtje laten branden als iemand in de toilet zit en tegelijk word er een bezoek moment opgestuurd. Daarnaast kunnen wij met de afstandssensor berekenen hoeveel toiletpapier er nog over is, op deze manier kunnen de sanitaire medewerkers zien welke toiletten een refill nodig hebben.
Wanneer een medewerkers de toiletten refilled kan hij zijn kaart scannen om aan te geven dat het toiletpapier is hervuld en ook wanneer dit is gebeurt. De tijd van papieren registratie lijsten zijn voorbij.

# Systeem opbouw
Het smart toilet systeem bestaat globaal uit drie verschillende onderdelen:
* Een scanner die gebruikt wordt door schoonmakers/ medewerkers om aan te geven dat een toilet schoongemaakt / wc papier bijgevuld is.
* Een toilet rol dispenser die bijhoudt hoeveel wc rollen er nog in zitten
* Een toilet die aangeeft of hij bezet of beschikbaar is.

# Bestand structuur
De bestand structuur is opgebouwd uit globaal drie folders en een docker-compose.yml en een env file in de root van het project.

 de scanner wordt aangestuurd door middel van de code die in de pyscan folder staat. de toilet beschikbaarheid en de aantal toiletrollen worden aangestuurd door middel van de code in de afstandssensor folder. De server is een Django project wat aangestuurd wordt door middel van de code in de server folder.
