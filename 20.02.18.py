import os
import pygame
import sys
import random
import time
import math


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.key.set_repeat(200, 10)
fps = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((-10000, 0))
        image.set_colorkey(colorkey)
    return image


def terminate():
    pygame.quit()
    sys.exit()

# основной персонаж
player = None
speed = 3
# группы спрайтов
all_sprites = pygame.sprite.Group()
particles_sprites = pygame.sprite.Group()
indicator_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
koryaga_group = pygame.sprite.Group()
grass_group = pygame.sprite.Group()
volozh_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ch = 0
tile_images = {'water': load_image('not.png')}
koryaga_image = load_image('koryagaa.png')
grass_image = load_image('grasss.png')
player_image_nach = load_image('catt.png')
player_image_right = load_image('catt1.png')
player_image_left = load_image('catt.png')
volozh_image = load_image('fishh.png')
tile_width = 49
tile_height = 70
koryaga_width = koryaga_height = 50
grass_width = grass_height = 50
volozh_width = 100
volozh_height = 82
indicator_width = indicator_height = 100

class koryaga(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__(koryaga_group, all_sprites)
        self.image = load_image('koryaga.png')
        self.rect = self.image.get_rect().move(koryaga_width * posx + 20, koryaga_height * posy - 20)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global speed
        global t
        if pygame.sprite.collide_mask(self, player):
            speed = 1

            t = time.time()



class grass(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__(grass_group, all_sprites)
        self.image = load_image('grasss.png')
        self.rect = self.image.get_rect().move(grass_width * posx + 20, grass_height * posy - 20)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global speed
        global t
        if pygame.sprite.collide_mask(self, player):
            speed = 6

            t = time.time()
            
def startScreen():
    
    # здесь можно вывести красивую картинку
    # ...

    introText = ["¬ этой игре вы можете почувствовать себ€ насто€щим котом."]

    screen.fill(pygame.Color('blue'))
    font = pygame.font.Font(None, 50)
    stringRendered = font.render("ѕоймай рыбку!", 1, pygame.Color('white'))
    introRect = stringRendered.get_rect()
    introRect.top = 20
    introRect.x = 200
    screen.blit(stringRendered, introRect)    
    
    font = pygame.font.Font(None, 30)
    textCoord = 80
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('white'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 20
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)
        
    textCoord += 30
    introText = ["ѕравила игры просты. Ќа поле пр€четс€ рыба, которую кот должен", 
                 "поймать. ѕо пути он может встретить кор€гу, котора€ при касании",
                 "с ним уменьшает его скорость, и траву, при касании с которой", 
                 "скорость увеличиваетс€. Ќа ловлю рыбы отводитс€ врем€ 5 минут",
                 "ј вы сможете найти еЄ быстрее?"]
    for line in introText:
        stringRendered = font.render(line, 1, pygame.Color('white'))
        introRect = stringRendered.get_rect()
        textCoord += 10
        introRect.top = textCoord
        introRect.x = 20
        textCoord += introRect.height
        screen.blit(stringRendered, introRect)    

    cat_begin = load_image('begin.png')
    cat1 = pygame.transform.scale(cat_begin, (149, 148))
    screen.blit(cat1, [400, 400])
    global ch
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        ch += 1
        if ch % 500 == 0:
            for i in range(random.randint(1, 10)):
                grass(random.randint(0, 80), random.randint(0, 80))
    
            for i in range(random.randint(1, 10)):
                koryaga(random.randint(0, 80), random.randint(0, 80))
            ch = 0        
        clock.tick(fps)


startScreen()
all_time = time.time()
screen_rect = (0, 0, width, height)
def endScreen():
    user_time = int(time.time() - all_time)
    ut_min = user_time // 60
    ut_sec = user_time - ut_min
    text = "¬ы поймали рыбу за "
    if ut_min > 0:
        text += str(ut_min) 
        if ut_min > 10 and ut_min < 20:
            text += " минут"
        elif ut_min % 10 == 1:
            text += " минуту"
        elif ut_min % 10 == 2 or ut_min % 10 == 3 or ut_min % 10 == 4:
            text += "минуты"
        else:
            text += " минут"
            
    text += str(ut_sec)
    if ut_sec > 10 and ut_sec < 20:
        text += " секунд"
    elif ut_sec % 10 == 1:
        text += " секунду"
    elif ut_sec % 10 == 2 or ut_sec % 10 == 3 or ut_sec % 10 == 4:
        text += " секунды"
    else:
        text += " секунд"
    text += "!"
    print(text)
    font = pygame.font.Font(None, 50)  
    text = font.render(text, 1, (100, 255, 100))
  
    screen.blit(text, [110, 200])

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.fill((0, 0, 0))
        create_particles([random.randint(150, 250), random.randint(450, 550)])
        create_particles([random.randint(550, 650), random.randint(450, 550)])  
        particles_sprites.draw(screen)
        particles_sprites.update()
        screen.blit(text, [110, 200])
        pygame.display.flip()
        clock.tick(fps)
        
        
class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = []
    image_star = load_image("star.png")
    fire.append(pygame.transform.scale(image_star, (20, 20)))
    fire.append(pygame.transform.scale(image_star, (10, 10)))

    def __init__(self, x, y, dx, dy, size):
        super().__init__(particles_sprites)

        self.image = Particle.fire[random.randint(0, len(Particle.fire) - 1)]

        self.rect = self.image.get_rect()

        # у каждой частицы сво€ скорость
        self.x_velocity = dx
        self.y_velocity = dy

        self.rect.x = x
        self.rect.y = y

        # гравитаци€
        self.gravity = 0.1

    def update(self):
        # примен€ем гравитационный эффект
        self.y_velocity += self.gravity
        # перемещаем частицу
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20

    # возможные скорости
    numbers = list(range(-5, 5))

    for i in range(0, particle_count):
        p = Particle(position[0], position[1], random.choice(numbers), random.choice(numbers), random.randint(1, 5))

def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убира€ символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    maxWidth = max(map(len, level_map))

    # дополн€ем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(maxWidth, '.'), level_map))

# level = load_level("file.txt")


class Indicator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(indicator_sprites)
        self.image = load_image('1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 490

    def update(self):
        print('Indicator:', self.rect.x, self.rect.y)
        min_len_to_fish = 10000000000
        for fish in volozh_group:
            if ((player.rect.x - fish.rect.x) ** 2 + (player.rect.y - fish.rect.y) ** 2) ** 0.5 < min_len_to_fish:
                min_len_to_fish = ((player.rect.x - fish.rect.x) ** 2 + (player.rect.y - fish.rect.y) ** 2) ** 0.5
        print(player.rect.x, fish.rect.x, player.rect.y, fish.rect.y)
        print(min_len_to_fish)

        if min_len_to_fish < 200:
            self.image = load_image('16.png')
        elif min_len_to_fish < 400:
            self.image = load_image('15.png')
        elif min_len_to_fish < 600:
            self.image = load_image('14.png')
        elif min_len_to_fish < 800:
            self.image = load_image('13.png')
        elif min_len_to_fish < 1000:
            self.image = load_image('12.png')
        elif min_len_to_fish < 1100:
            self.image = load_image('11.png')
        elif min_len_to_fish < 1200:
            self.image = load_image('10.png')
        elif min_len_to_fish < 1300:
            self.image = load_image('9.png')
        elif min_len_to_fish < 1400:
            self.image = load_image('8.png')
        elif min_len_to_fish < 1500:
            self.image = load_image('7.png')
        elif min_len_to_fish < 1600:
            self.image = load_image('6.png')
        elif min_len_to_fish < 1800:
            self.image = load_image('5.png')
        elif min_len_to_fish < 2000:
            self.image = load_image('4.png')
        elif min_len_to_fish < 2100:
            self.image = load_image('3.png')
        elif min_len_to_fish < 2200:
            self.image = load_image('2.png')
        else:
            self.image = load_image('1.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, type, posx, posy):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[type]
        self.rect = self.image.get_rect().move(tile_width * posx, tile_height * posy)


class Volozh(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__(volozh_group, all_sprites)
        self.image = volozh_image
        self.rect = self.image.get_rect().move(volozh_width * posx, volozh_height * posy)
        self.mask = pygame.mask.from_surface(self.image)
        print(posx, posy)


class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__(player_group, all_sprites)
        self.count = 0
        self.image = player_image_nach
        self.rect = self.image.get_rect().move(tile_width * posx + 15, tile_height * posy + 5)

    def update(self):
        if pygame.sprite.spritecollideany(self, volozh_group):
            for i in pygame.sprite.spritecollide(self, volozh_group, 0):
                screen.fill(pygame.Color(0, 0, 0))
                print("You are winner!")
                pygame.display.flip()
                endScreen()

                # print(self.count)

        if self.count > 100:
            screen.fill(pygame.Color(0, 0, 0))
            print("You are winner!")
            pygame.display.flip()
            endScreen()
        else:
            # print("noooooooooooooooooooooooo")
            pass


def generate_level(level):
    # global player
    for y in range(len(level)):
        for x in range(len(level[y])):
            Tile('water', x, y)
            if level[y][x] == '@':
                player = Player(x, y)
            elif level[y][x] == '!':
                Volozh(x, y)
            elif level[y][x] == 'g':
                grass(x, y)
            elif level[y][x] == 'k':
                koryaga(x, y)            
                

    return player, x, y


class Camera():
    # зададим начальный сдвиг камеры и размер пол€ дл€ возможности реализации циклического сдвига
    def __init__(self, fieldsize):
        self.dx = 0
        self.dy = 0
        self.fieldsize = fieldsize

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        # вычислим координату клетки, если она уехала влево за границу экрана
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.fieldsize[0] + 1) * obj.rect.width
        # вычислим координату клетки, если она уехала вправо за границу экрана
        if obj.rect.x >= (self.fieldsize[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.fieldsize[0])
        obj.rect.y += self.dy
        # вычислим координату клетки, если она уехала вверх за границу экрана
        if obj.rect.y < -tile_height:
            obj.rect.y += (self.fieldsize[1] + 1) * tile_height
        # вычислим координату клетки, если она уехала вниз за границу экрана
        if obj.rect.y >= (self.fieldsize[1]) * tile_height:
            obj.rect.y += -tile_height * (1 + self.fieldsize[1])

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


player, levelx, levely = generate_level(load_level("file.txt"))
camera = Camera((levelx, levely))
indicator = Indicator()

t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.image = player_image_left
                player.rect.x -= speed
            if event.key == pygame.K_RIGHT:
                player.image = player_image_right
                player.rect.x += speed
            if event.key == pygame.K_UP:
                player.rect.y -= speed
            if event.key == pygame.K_DOWN:
                player.rect.y += speed

    # измен€ем положение камеры
    screen.fill(pygame.Color(0, 0, 0))
    indicator.update()

    camera.update(player)
    # print(player.rect.centerx, player.rect.centery)
    # обновл€ем положение всех спрайтов
    for sprite in all_sprites:
        camera.apply(sprite)

    player.update()


    for i in grass_group:
        i.update()
    for i in koryaga_group:
        i.update()


    backgr = load_image('water.gif')
    backgr1 = pygame.transform.scale(backgr, (800, 600))
    screen.blit(backgr1, [0, 0])

    # tiles_group.draw(screen)
    koryaga_group.draw(screen)
    grass_group.draw(screen)
    volozh_group.draw(screen)
    player_group.draw(screen)
    indicator_sprites.draw(screen)
    # indicator.draw()

    if time.time() - t >= 5:
        speed = 2

    pygame.display.flip()

    clock.tick(fps)

    ch += 1
    if ch % 500 == 0:
        for i in range(random.randint(1, 15)):
            grass(random.randint(0, 80), random.randint(0, 80))

        for i in range(random.randint(1, 15)):
            koryaga(random.randint(0, 80), random.randint(0, 80))
        ch = 0

terminate()