# Mikroelektromechanikai rendszerek - projekt

*

Egy Raspberry Pi-re kötünk egy szenzort – ami a hőmérsékletet méri- és egy 3 színű ledet (Piros, Zöld, Kék), ami a következők alapján ad visszajelzést. Ha a mért hőmérséklet nem éri el a 25 C°-ot kék led világít, ha meghaladja a mért hőmérséklet a 25 C°-o a zöld led világít.
A vezérlés a Raspberry Pi-n futtatott Python kód segítségével történik.
A mérési eredményeket adatbázisban tároljuk és egy API segítségével lekérdezhetjük, az utolsó 10 mérési eredményt egy weblapon, diagramon megjeleníthetjük.


*

A Raspberry-n futtatandó Python scriptet, mely a hőmérséklet lekérdezést, a led vezérlést és az adatbázisba írást végzi innen lehet letölteni. [itt](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/code/main.py)

A weboldalt kiszolgáló API kódja [itt](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/code/api.py) található.

A weboldal pedig [innen](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/web/index.html) tölthető le. (Diagram megjelenítéséhez szükséges [Chart.js](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/web/Chart.js))

Néhány kép a projectről: [1](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/pic/20221128_171347.jpg) [2](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/pic/20221128_181439.jpg) [3](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/pic/20221128_181550.jpg)

[Teljes Dokumentáció](https://github.com/YXLG5V/mikroelektroprojekt/blob/master/doc/ratkairobertYXLG5Vmikroelektroproject.pdf)

