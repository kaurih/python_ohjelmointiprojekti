# Tuodaan kirjastot
import pygame as pg # lyhennetty näppäimistön säästämiseksi heheheh
import random

# alustetaan pygame
pg.init()

# peli-ikkunan asetukset (koko ja nimi + kello tickspeedia varten)
screen_width, screen_height = 800, 600 # leveämpi näyttö jättää tilaa pistenäytölle
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Matopeli") # ikkunan nimi!
clock = pg.time.Clock() # kello; hyödynnetään myöhemmin

# fontti
font = pg.font.SysFont("impact", 25) # hakee tietokoneelta impact-fontin, koko 25
# hi-score apumuuttuja
hi_score = 0

# pelialue: mato ja ruoka ovat täällä!
WIDTH = 600
HEIGHT = 600
TILE_SIZE = 15 # tämä on pelin perusyksikkö
carbon = "#0d0d0d"  # ruudukon väri

#*******************************************************************************************************

# pelialueen ruudukon funktio
def draw_grid():
    for x in range(0, WIDTH, TILE_SIZE): # iteroi x-akseli, 0 - WIDTH(600px): koko TILE_SIZE
        for y in range(0, HEIGHT, TILE_SIZE): # kts. ylhäällä
            rect = pg.Rect(x, y, TILE_SIZE, TILE_SIZE) # luo pygame "Rect" objektin, TILE_SIZE x TILE_SIZE neliö!
            pg.draw.rect(screen, carbon, rect, 1) # (näyttö, väri, objekti, reunan paksuus) - piirtää neliöitä

# satunnaiskoordinaattigeneraattori
def random_pos():
    x = random.randint(0, (WIDTH // TILE_SIZE) - 1) * TILE_SIZE # pikselikoordinaatti
    y = random.randint(0, (HEIGHT // TILE_SIZE) - 1) * TILE_SIZE
    return (x, y) # palauttaa satunnaiset koordinaatit

# mato, ensimmäinen segmentti satunnaisiin koordinnaatteihin
def initialize_snake():
    snake_segment = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE) # yksi neliösegmentti madosta
    snake_segment.topleft = random_pos() # madon palanen menee randomposin antamiin koordinaatteihin (topleft = Rect attribuutti)
    return [snake_segment.copy()] # palauttaa listan, jossa kopio ensimmäisestä madon osasta. lista = madon kroppa

# ruoka, syötävä neliö satunnaisiin koordinaatteihin (kts. matofunktio ylhäällä)
def initialize_food():
    food = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE)
    food.topleft = random_pos()
    return food 

# Pääpeliohjelma
def game_loop():
    global hi_score # pidättää korkeimman pistesumman
    snake = initialize_snake() # matofunktio
    food = initialize_food() # ruokafunktio
    direction = [0, 0] # madon suunnan apumuuttuja
    score = 0 # pistesaldo-apumuuttuja
    running = True
    
    # ohjelma käynnissä:
    while running: # events, updates, renderer
        # pygame.QUIT lopettaa ohjelman!
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            # madon ohjaimet (nuolinäppäimet). != estää matoa liikumasta suoraan taaksepäin
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and direction != [0, 1]:
                    direction = [0, -1] # ylös
                elif event.key == pg.K_DOWN and direction != [0, -1]:
                    direction = [0, 1] #alas
                elif event.key == pg.K_LEFT and direction != [1, 0]:
                    direction = [-1, 0] # vasemmalle
                elif event.key == pg.K_RIGHT and direction != [-1, 0]:
                    direction = [1, 0] # oikealle

        # madon liikelogiikka
        if direction != [0, 0]: #jos mato EI OLE paikoillaan...
            new_head = snake[-1].copy() # -1 = madon viimeinen osa (pää), copy = uusi pää uuteen paikkaan
            new_head.move_ip(direction[0] * TILE_SIZE, direction[1] * TILE_SIZE) # dir 0 = horisontaalinen, dir 1 = vertikaalinen, * TILE_SIZE pitää liikkeen madon "palasen" kokoisena könttinä
            snake.append(new_head) # uusi pää "snake" listaan = mato etenee

            # syökö ruokaa?
            if new_head.colliderect(food):
                food.topleft = random_pos()
                score += 1 # +1 piste, jipii!
            else:
                snake.pop(0) # poistaa hännän

            # törmääkö seiniin tai itseensä?
            if (new_head.left < 0 or new_head.right > WIDTH or 
                new_head.top < 0 or new_head.bottom > HEIGHT or # seinät
                new_head in snake[:-1]): # osuuko uusi pää madon kehon osiin?
                if score > hi_score:
                    hi_score = score  # päivittää huippupisteet, jos uusi ennätys
                return True  # aloittaa pelin uudelleen

        # taustan asetukset: taustaväri ja ruudukko
        screen.fill("black")
        draw_grid()

        # piirretään mato
        for segment in snake:
            pg.draw.rect(screen, "white", segment)

        # piirretään ruoka
        pg.draw.rect(screen, "red", food)

        # Pisteet näkyviin oikeaan yläreunaan
        score_text = font.render("Pisteet: " + str(score), True, pg.Color("white"))
        high_score_text = font.render("Ennätys: " + str(hi_score), True, pg.Color("white"))
        screen.blit(score_text, (WIDTH + 20, 10))
        screen.blit(high_score_text, (WIDTH + 20, 50))

        # ruudunpäivitys + madon nopeus (sidottu fps:ään)
        pg.display.flip()
        clock.tick(10) # fps

    return False

# kutsutaan gameloop
running = True
while running:
    running = game_loop()

# ohjelman lopetus
pg.quit()