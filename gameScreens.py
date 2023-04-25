from unit import*
class Logo(pygame.sprite.Sprite):
    def __init__(self, imageref):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('Textures', imageref)).convert()
        img.set_colorkey((0, 0, 0))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()