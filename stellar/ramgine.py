import pygame

class Engine:
    def __init__(self):
        self.__screen = None
        self.__clock = None
        self.__windowShouldClose = False
        self.__objects = []

    def revEngines(self, width=800,height=600,title="Stellar Engine"):
        if not pygame.display.get_init():
            pygame.init()
            self.__screen = pygame.display.set_mode((width,height))
            pygame.display.set_caption(title)
            self.__clock = pygame.time.Clock()

    def stopEngines(self):
        pygame.display.quit()
        pygame.quit()
        quit()

    def rebootDisplay(self, width=800,height=600,title="Stellar Engine"):
        if pygame.display.get_init():
            pygame.display.quit()
            pygame.quit()
            self.__screen = pygame.display.set_mode((width,height))
            pygame.display.set_caption(title)

    def setFramerate(self, framerate=60):
        self.__clock.tick(framerate)

    def getActualFramerate(self):
        return self.__clock.get_fps()

    def getTimeSinceLastFrame(self):
        return self.__clock.get_time()

    def getActualTimeSinceLastFrame(self):
        return self.__clock.get_rawtime()

    def changeTitleBarText(self, title="Stellar Engine"):
        pygame.display.set_caption(self.__titleBarText)

    def shouldClose(self):
        return self.__windowShouldClose

    def closeWindow(self):
        self.__windowShouldClose = True

    def pollEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
            print (event)

    def addObject(self, obj):
        self.__objects.append(obj)

    def removeObject(self, obj):
        self.__objects.remove(obj)
        
    def drawEvents(self):
        for obj in self.__objects:
            obj.draw()
    
    def stepEvents(self):
        for obj in self.__objects:
            obj.step()
    
    def singleStep(self):
        self.pollEvents()
        self.stepEvents()
        self.drawEvents()

        
    
e = Engine()
e.revEngines()

while not e.shouldClose():
    e.singleStep()
