import pygame
import time

def vari(v: int):
    if v == None:
        return (0, 255, 0)
    elif v:
        return (255,255,255)
    else:
        return (0, 0, 0)


pyora  = pygame.image.load(f"pyora.jpg")
tausta = pygame.image.load(f"tausta.png")

sijainti = 1
def sijainnit(x: int, y: int): 
    return \
    (
        75 - pyora.get_width() / 2,
        225 - pyora.get_width() / 2,
        375 - pyora.get_width() / 2,
    )[x], (len(kartta) * 50) - (y * 50) - pyora.get_height()

kartta = [
    [True ,True ,True ],
    [True ,True ,True ],
    [True ,True ,False],
    [False,True ,True ],
    [True ,True ,True ],
    [True ,True ,True ],
    [True ,False,True ],
    [False,True ,True ],
    [True ,True ,True ],
    [None ,None ,False],
    [None ,None ,None ],
    [None ,None ,None ]
]

pygame.init()
naytto = pygame.display.set_mode((450, len(kartta) * 50))

indeksi = 0

kello = pygame.time.Clock()

voitti = False
havisi = False

aika = time.time()

while True:
    if time.time() - aika > 0.5 and not (voitti or havisi):
        aika = time.time()
        indeksi += 1
    if kartta[indeksi][sijainti] == None:
        voitti = True
    naytto.fill((255, 255, 255))

    if voitti:
        pygame.draw.rect(naytto, vari(None), (0, 0, 450, 600))
        teksti = pygame.font.SysFont("Arial", 100).render("VOITTO", True, (0, 0, 0))
        naytto.blit(teksti, (225 - teksti.get_width() / 2, 0))
    elif havisi:
        pygame.draw.rect(naytto, vari(False), (0, 0, 450, 600))
        teksti = pygame.font.SysFont("Arial", 100).render("HÄVISIT", True, (255, 255, 255))
        naytto.blit(teksti, (225 - teksti.get_width() / 2, 0))
    else:
        naytto.blit(tausta, (0, 0))
 
    if not havisi:
        naytto.blit(pyora, sijainnit(sijainti, indeksi))

    pygame.display.flip()

    if kartta[indeksi][sijainti] == False:
        havisi = True

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT and sijainti > 0:
                sijainti -= 1
            if tapahtuma.key == pygame.K_RIGHT and sijainti < 2:
                sijainti += 1