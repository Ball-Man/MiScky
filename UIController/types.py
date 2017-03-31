from .renderer import getTextSurface

class Text:
    def __init__(self, text, size, color, fontfile="Raleway/Raleway-Thin.ttf"):
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
