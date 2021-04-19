"""
Hey, i tried to optimie your code so it should work now.
hope my explanatiosn are understandable.
"""
import pygame,random,sys
pygame.init()

#i call the display screen but u can also name it dp

car_main = pygame.image.load("car_main.png")
car_red = pygame.image.load("car_red.png")
car_blue = pygame.image.load("car_blue.png")
car_orange = pygame.image.load("car_orange.png")
car_pink = pygame.image.load("car_pink.png")
car_white = pygame.image.load("car_white.png")
car_gray = pygame.image.load("car_gray.png")
car_yellow = pygame.image.load("car_yellow.png")
truck_peq = pygame.image.load("truck_peq.png")
truck_long = pygame.image.load("truck_long.png")
truck_med = pygame.image.load("truck_med.png")
truck_med_red = pygame.image.load("truck_med_red.png")
truck_short_blue = pygame.image.load("truck_short_blue.png")
truck_short_gray = pygame.image.load("truck_short_gray.png")
truck_short_green = pygame.image.load("truck_short_green.png")
tree = pygame.image.load("tree.png")

screen = pygame.display.set_mode([600,720])
clock = pygame.time.Clock()

class Car:
##    width = 50
##    height = 100
    speed = 5
    def __init__(self,posx,posy,width,height,carimg):
        self.pos = posx,posy
        print(self.pos)
##        #creating surface isntead of images and convert to safe performance
##        self.image = pygame.Surface([self.width,self.height]).convert()
        self.image = carimg
##        #fill surface
##        self.image.fill(color)
        #define rect for rect collision (later)
        self.rect = self.image.get_rect()
        #set position of rect
        self.rect.topleft = self.pos

    def draw(self):
        #this will blit our car on the same position as the rect
        screen.blit(self.image,self.rect)

#doing same as in car class
class Line:
    width = 10
    height = 75
    color = (255,255,255)
    def __init__(self,x,y):
        self.pos = (x,y)
        self.image = pygame.Surface([self.width,self.height]).convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        screen.blit(self.image,self.rect)

class Tree:
    def __init__(self,x,y):
        self.pos = (x,y)
        self.image = pygame.image.load("tree.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
    def draw(self):
        screen.blit(self.image,self.rect)


"""inti all cars""" 
car1 = Car(200,500,50,100,car_main)
car2 = Car(210,0,50,100,car_red)
car3 = Car(210,0,50,100,car_blue)
car4 = Car(210,0,50,100,car_orange)
car5 = Car(210,0,50,100,car_pink)
car6 = Car(210,0,50,100,car_white)
car7 = Car(210,0,50,100,car_gray)
car8 = Car(210,0,50,100,car_yellow)
car9 = Car(210,0,50,100,truck_peq)
car10 = Car(210,0,74,230,truck_long)
car11 = Car(210,0,72,193,truck_med)
car12 = Car(210,0,72,193,truck_med_red)
car13 = Car(200,500,73,173,truck_short_blue)
car14 = Car(200,500,73,173,truck_short_gray)
car15 = Car(200,500,73,173,truck_short_green)



"""inti lines"""
#didnt changed sthg.
Line1 = Line(190,50) #1. line, 1. line
Line2 = Line(285,50) #2. line 1. line
Line3 = Line(190,-250)#1. line 2. line
Line4 = Line(285,-250)#2. line 2. line
Line5 = Line(385,50) #3. line 1. line
Line6 = Line(385,-250) #3. line 2. line
Line7 = Line(190,-550) #1. line 3. line
Line8 = Line(285,-550) #2. line 3. line
Line9 = Line(385,-550) #3. line 3. line
Line10 = Line(190,-850) #1. line 4. line
Line11 = Line(285,-850) #2. line 4. line
Line12 = Line(385,-850) #3. line 4. line


Tree1 = Tree(515,-200)
Tree2 = Tree(515,-800)
Tree3 = Tree(20,-150)
Tree4 = Tree(20,-650)
"""create a list with all cars inside"""
car_list = [car2,car3,car4,car5,car6,car7,car8,car9,car10,
            car11,car12,car13,car14,car15]
##,car15]
"""lsit with all liens isnide"""
line_list = [Line1,Line2,Line3,Line4,Line5,Line6,Line7,Line8,Line9,Line10,Line11,Line12]
tree_list = [Tree1,Tree2,Tree3,Tree4]

font1 = pygame.font.SysFont("Gadugi",200)
font2 = pygame.font.SysFont("Gadugi",50)
##class Street:
##    left = [110,-300]
##    left_middle = [205,-300]
##    right_middle = [310,-300]
##    right = [410,-300]
##    way_list = [left,left_middle,right_middle,right]
##    single_car = random.choice(car_list)
##    random_way = random.choice(way_list)
##    single_car.draw(random_way)

def text(msg,x,y,color,font):
    text = font.render(msg,True,color)
    screen.blit(text,[x,y])
running = True
Start = False
while running and not Start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Start = True
                print("Start Game")

        screen.fill((255,255,255))
        text("Hi",50,50,(0,0,0),font1)
        text("press space",50,300,(0,0,0),font2)
        pygame.display.update()
        clock.tick(60)

#mainloop
line_speed = 5
speed = 5
points = 0
randomcar = random.choice(car_list)
for car in car_list:
    car.rect.y = -300
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        car1.rect.y -= car1.speed
    if keys[pygame.K_s]:
        car1.rect.y += car1.speed
    if keys[pygame.K_a]:
        if car1.rect.x > 110:
            car1.rect.x -= car1.speed
    if keys[pygame.K_d]:
        if car1.rect.x < 440:
            car1.rect.x += car1.speed

    #refreseh bg
    screen.fill((0,0,0))
    #border
    pygame.draw.rect(screen,(0,220,0),(0,0,100,720))
    pygame.draw.rect(screen,(0,220,0),(500,0,120,720))

    #draw lines
    for line in line_list: #thsi call every line object from list and call draw function
        line.draw()
        line.rect.y += line_speed
        if line.rect.y >= 720:
            line.rect.y = - 400
    for tree in tree_list:
        tree.draw()
        tree.rect.y += line_speed
        if tree.rect.y >= 750:
            tree.rect.y = - 300
    car1.draw()
    randomcar.draw()
    randomcar.rect.y += speed
    mouse = pygame.mouse.get_pos()
    print(mouse)
    if randomcar.rect.y >= 720:
        points += 1
##        print(points)
        randomcar.rect.y = -300
        randomcar = random.choice(car_list)
##        randomcar.rect.y = -300
        rr = [110,205,310,410]
##        randomcar.rect.x = random.randrange(130,400,90)
        randomcar.rect.x = random.choice(rr)
    
    #checks with pygame rect collision if rect of car1 and random car collided
    if car1.rect.colliderect(randomcar.rect):
        print("you are a terrible driver xd ")
        pygame.quit()
        sys.exit()

    speed += 0.01
    line_speed = speed
    car1.speed += 0.005

    text(str(points),10,10,(255,255,255),font2)
    pygame.display.update()
    clock.tick(30)    
