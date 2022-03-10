from Environment.cart import Cart, Vector2, pygame
from Environment.object_static import StaticObj
from Environment.object_dynamic import DynamicObj


class Map:
    # define the colors
    BLACK = (25, 25, 25)
    WHITE = (255, 255, 255)
    RED = (255, 80, 80)
    BLUE = (80, 80, 255)

    def __init__(self, width: int, length: int, start_point: Vector2):
        """Initializes the map"""
        pygame.init()  # starts the environment
        pygame.display.set_caption('RiCart')  # title of the simulator
        self.width = width  # width of the screen
        self.length = length  # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.length))  # set the screen dimensions
        self.screen.fill(self.WHITE)    # set the background as white
        self.static_object = StaticObj(80, 40, Vector2(300, 300), self.BLACK, self.screen)
        self.dynamic_object = DynamicObj(20, 60, Vector2(100, 100), self.BLUE, self.screen)
        self.cart = Cart(20, 20, Vector2(400, 400), self.RED, self.screen)  # initializes the car class
        self.render()  # render the environment

        self.running = False  # is the game running or not

    def render(self):
        """Renders the environment on the first run"""
        self.screen.fill(self.WHITE)    # reset screen
        self.static_object.render(self.screen)  # render static object
        self.cart.render(self.screen)  # render the car
        self.dynamic_object.render(self.screen)  # render dynamic object
        pygame.display.flip()  # shows on screen

    def draw(self):
        """Draws the movements"""
        self.screen.fill(self.WHITE)
        #self.screen.blit(self.screen, (0, 0))
        self.cart.render(self.screen)  # draw cart
        self.static_object.render(self.screen)  # draw static object
        self.dynamic_object.render(self.screen)  # draw dynamic object
        pygame.display.flip()

    def handle_events(self):
        """Handle the press key events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

        keys = pygame.key.get_pressed()     # return pressed key

        if keys[pygame.K_w] and keys[pygame.K_a]:  # check 'w' and 'a' key
            self.cart.NW = True     # NW movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_w] and keys[pygame.K_d]:  # check 'w' and 'd' key
            self.cart.NE = True     # NE movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_s] and keys[pygame.K_a]:  # check 's' and 'a' key
            self.cart.SW = True     # SW movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_s] and keys[pygame.K_d]:  # check 's' and 'd' key
            self.cart.SE = True     # SE movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_w]:     # check 'w' key
            self.cart.N = True  # N movement enabled
            self.cart.move()    # movement call
        elif keys[pygame.K_a]:   # check 'a' key
            self.cart.W = True  # W movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_s]:   # check 's' key
            self.cart.S = True  # S movement enabled
            self.cart.move()  # movement call
        elif keys[pygame.K_d]:   # check 'd' key
            self.cart.E = True  # E movement enabled
            self.cart.move()  # movement call
        else:
            self.cart.reset_movement()  # reset all movements
        self.render()   # render the simulation

    def run(self):
        """Starts the environment loop"""
        self.running = True
        while self.running:
            self.handle_events()  # handles the events of the game

        pygame.quit()