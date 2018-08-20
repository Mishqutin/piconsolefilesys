helpText = """\
Nie uzywaj komend bez wymaganych argumentow!
Pozniej naprawie :)
Aczkolwiek argumenty moga byc nieprawidlowe - jest obsluga bledow.
ls - Listuje dir
ls <sciezka> - Listuje sciezke
cd <sciezka> - Przechodzi do sciezki
cat <sciezka> - Wyswietla zawartosc pliku
mkdir <sciezka> - Tworzy sciezke
write <sciezka> <tekst> - Zapisuje tekst do pliku
rm <sciezka> - Usuwa pliki i katalogi

Sciezka moze byc np. taka:
/./././home/../home/.
czyli /home
"""


c.send(helpText.encode())