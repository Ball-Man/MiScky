from .renderer import getTextSurface
from .colors import *
import pygame
import pygame.gfxdraw

class Text:
    def __init__(self, text, size, color, fontfile="Raleway/Raleway-Medium.ttf"):
        assert(type(text) is str)
        assert(type(size) is int)
        assert(type(color) is tuple and len(color) == 3 and all(map(lambda x: type(x) is int, color)))
        assert(type(fontfile) is str)
        self.text = text
        self.size = size
        self.color = color
        self.fontfile = fontfile

    def render(self):
        return getTextSurface(self.text, self.fontfile, self.size, self.color)
	
class Rectangle(pygame.Rect):
	def __init__(self, width, height, color):
		super().__init__((0,0), (width, height))
		self.color = color
	def render(self, rounded=2):
		color = self.color
		r = rounded
		x = self.width
		y = self.height
		surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
		surface = surface.convert_alpha()
		aacircles = ((r,r),(x-r-1,r),(r,y-r-1),(x-r-1,y-r-1))
		circles = ((r,r),(x-r,r),(r,y-r),(x-r,y-r))
		for c, c2 in zip(aacircles, circles):
			pygame.gfxdraw.aacircle(surface, *c, r, color)
			pygame.draw.circle(surface, color, c2, r)
		pygame.draw.rect(surface, color, (r,0,x-2*r,r))
		pygame.draw.rect(surface, color, (0,r,x,y-2*r))
		pygame.draw.rect(surface, color, (r,y-r,x-2*r,r))
		return surface
