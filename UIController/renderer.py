#!/usr/bin/python

import pygame
import os.path

fileFolder = os.path.dirname(os.path.realpath(__file__))
fontsFolder = fileFolder + "/Fonts/"
imagesFolder = fileFolder + "/Images/"

#fontsFolder = "/home/mirror/MiScky/UIController/Fonts/"

def getTextSurface(text, fontFile, size, color = (255,255,255), antiAliasing = True):
    assert(type(text) is str)
    assert(type(fontFile) is str)
    assert(type(size) is int)
    assert(type(color) is tuple and len(color) == 3 and all(map(lambda x: type(x) is int, color)))
    assert(type(antiAliasing) is bool)
    
    if not pygame.font.get_init():
        pygame.font.init()
        print("Initialized font module pygame from renderer")

    fontFilePath = fontsFolder + fontFile
    font = pygame.font.Font(fontFilePath, size)
    renderedText = font.render(text, antiAliasing, color)
    return renderedText

def getImageSurface(imageFile):
    assert(type(imageFile) is str)

    image = pygame.image.load(fileFolder + imageFile)
    return image

def scaleImage(image, dimensions):
    assert(type(image) is pygame.Surface)
    assert(type(dimensions) is tuple and len(dimensions) == 2 and all(map(lambda x: type(x) is int, dimensions)))

    newImage = pygame.transform.scale(image, dimensions)
    return newImage
