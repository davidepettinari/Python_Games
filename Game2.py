import pygame
import random

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra di gioco
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Creazione della finestra di gioco
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gioco Pygame")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font per il punteggio
score_font = pygame.font.SysFont(None, 30)

# Caricamento delle immagini
player_image = pygame.image.load('player.png')
obstacle_image = pygame.image.load('obstacle.png')
object_image = pygame.image.load('object.png')
background_image = pygame.image.load('background.png')

# Velocità del gioco
game_speed = 5

# Classe per il personaggio del giocatore
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        # Movimento del personaggio a destra e sinistra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Limiti della schermata
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Classe per gli ostacoli che il giocatore deve evitare
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)

# Classe per gli oggetti che il giocatore deve raccogliere per guadagnare punti
class Game_object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = object_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)

# Funzione per il disegno del punteggio
def draw_score(score):
    score_text = score_font.render("Punteggio: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Creazione dei gruppi di sprite
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
game_objects = pygame.sprite.Group()

# Creazione del personaggio del giocatore
player = Player()
all_sprites.add(player)

# Creazione degli ostacoli
for i in range(10):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Creazione degli oggetti
for i in range(5):
    game_object = Game_object()
    all_sprites.add(game_object)
    game_objects.add(game_object)

# Inizializzazione del punteggio
score = 0

# Ciclo di gioco
running = True
while running:
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aggiornamento degli sprite
    all_sprites.update()

    # Rilevamento delle collisioni tra il giocatore e gli ostacoli
    collisions = pygame.sprite.spritecollide(player, obstacles, False)
    if collisions:
        running = False

    # Rilevamento delle collisioni tra il giocatore e gli oggetti
    collisions = pygame.sprite.spritecollide(player, game_objects, True)
    for collision in collisions:
        score += 10

    # Aggiornamento del punteggio
    draw_score(score)

    # Disegno degli sprite e dello sfondo
    screen.blit(background_image, [0, 0])
    all_sprites.draw(screen)

    # Aggiornamento della finestra di gioco
    pygame.display.update()

    # Controllo della velocità del gioco
    pygame.time.Clock().tick(game_speed)

# Uscita dal gioco
pygame.quit()
