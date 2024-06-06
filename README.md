# Matopeli

***Tässä esittelen hieman ohjelmoinnin peruskurssin loppuprojektiani.***

## Idea

### Matopeli Pygamea hyödyntäen!

Itseäni kiinnosti kokeilla jotakin ladattavaa python-kirjastoa. Jonkin suositun pelin tekeminen vaikutti luonnolliselta tavalta toteuttaa idea. 
Harkitsin aluksi sudokua ja klassista matopeliä. Pienen pohdinnan jälkeen matopeli tuntui järkevimmältä, sillä sitä osaa pelata kuka tahansa ja muistelisin että minulla jäi lukiossa matopeli tekemättä ohjelmointikurssilla.
Sitä paitsi Python on myös käärme. Vitsi kirjoittaa itse itsensä.

## Kuvaus

Ohjelma on toteutettu Python-ohjelmointikielellä Pygame-kirjastoa käyttäen. Pygamella on laaja dokumentointi ja siksi helppokäyttöinen aloittelevalle koodaajalle. Itseani juurikin kiinnosti mahdollisuus oppia
käyttämään hieman jotakin ulkoista kirjastoa, jossa kynnys ei olisi kovin korkea. Mikäli olisin päättänyt jatkokehittää peliä, niin pygamella mm. grafiikat ja äänet olisivat suhteellisen helposti toteutettavissa. Tässä ohjelmassa niitä ei kuitenkaan ole, muutamaan neliöobjektia lukuun ottamatta.

Tässä matopelissä on kaikki perinteiset ominaisuudet: matoa kasvatetaan syömällä palluroita (tai tässä tapauksessa punaisia ruutuja). Onnistuneesti syöty ruutu kerryttää pistepankiisi yhden pisteen. 
Peli päättyy, jos mato osuu pelikentän seiniin tai omaan häntäänsä. Tätä peliä voi jatkaa loputtomiin ja pelikerran paras tulos tallentuu ikkunan sivuun. Jos kisaat kavereitasi vastaan korkeimmasta pistemäärästä, ota omasta ennätyksestäsi vaikka kännykällä kuva - pisteitä ei nimittäin voi tallentaa, jos peli-ikkuna suljetaan.

**Huomaathan, että peli vaatii toimiakseen oikein asennetun pygame-kirjaston!**

## Miten ohjelma toimii?

Koodin pituuden vuoksi käyn tätä tarkemmin läpi videodemolla, mutta lyhykäisyydessään:

1. Ohjelma alustaa kirjastot ja muuttujat
2. Ohjelma luo madon ja ruuan näytölle
3. Kun mato liikkuu, ohjelma tarkistaa törmääkö se esteeseen tai ruokaan.
4. A. Jos mato törmää esteeseen, peli päättyy ja ohjelma luo uuden madon.
4. B. Jos mato syö ruokaa, madon häntä pitenee (ohjelma kasvattaa listaa, joka on madon "keho".)
5. Ohjelma luo uuden ruuan.


### Vuokaavio

![Vuokaavio](https://github.com/kaurih/python_ohjelmointiprojekti/blob/main/matopeli.png?raw=true)



## Ohje

1. Käynnistä ohjelma painamalla "Run" -näppäintä editorissa (VSCODE) tai syöttämällä komento Komentokehotteeseen.
2. Kun ohjelma käynnistyy, paina mitä tahansa nuolinäppäintä liikuttaaksesi matoa.
3. Syö punaisia ruokaneliöitä kasvattaaksesi madon pituutta. Peli päättyy, jos osut seiniin tai madon häntään.
4. Voit poistua pelistä painamalla peli-ikkunan ylänurkassa olevaa ruksia (X).

## Linkit ja lähteet

https://www.pygame.org/docs/ Luettu 29.5.

https://youtu.be/y9VG3Pztok8?si=xtVqtN1ETGPcQuat Katsottu 29.5.

https://youtu.be/9bBgyOkoBQ0?si=w9Zw9zV_NwirrM3q Katsottu 30. 5.

https://youtu.be/ebVV-6QMUIU?si=h6MFmqjH90TISVcK Katsottu 30. 5.

https://youtu.be/BkJD-ddq0dw?si=k7eRjhOjzYYNOc-P Katsottu 30. 5.

https://youtu.be/aLxJM-cfqnc?si=R1XvIEv054zUI6yU Katsottu 31. 5.


Tätä koodia on muokattu tekoälyllä (OpenAI ChatGPT 3.5).