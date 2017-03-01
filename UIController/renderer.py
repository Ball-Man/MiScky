#!/usr/bin/python

import pygame
import os.path

fileFolder = os.path.dirname(os.path.realpath(__file__))
fontsFolder = fileFolder + "/Fonts/"
imagesFolder = fileFolder + "/Images/"

#fontsFolder = "/home/mirror/MiScky/UIController/Fonts/"

def getTextSurface(text, fontFile, size, color = (255,255,255), antiAliasing = True):
    if type(text) is not str:
        raise TypeError("The text is not a string!")
    if type(fontFile) is not str:
        raise TypeError("The font path file is not a string!")
    if type(size) is not int:
        raise TypeError("The text size is not an integer!")
    if type(color) is not tuple:
        raise TypeError("The color is not a tuple!")
    if len(color) != 3:
        raise ValueError("The color is not RGB!")
    for a in color:
        if a < 0 or a > 255:
            raise ValueError("The color must be from 0 to 255!")
    if type(antiAliasing) is not bool:
        raise TypeError("The antialiasing parameter is not a boolean!")
    if not pygame.font.get_init():
        pygame.font.init()
        print("Initialized font module pygame from renderer")

    fontFilePath = fontsFolder + fontFile
    font = pygame.font.Font(fontFilePath, size)
    renderedText = font.render(text, antiAliasing, color)
    return renderedText

def getImageSurface(imageFile):
    if type(imageFile) is not str:
        raise TypeError("The image path is not a string!")

    image = pygame.image.load(fileFolder + imageFile)
    return image

def scaleImage(image, dimensions):
    if type(image) is not pygame.Surface:
        raise TypeError("The image is not a pygame.Surface!")
    if type(dimensions) is not tuple:
        raise TypeError("Dimensions is not a tuple!")
    if len(dimensions) != 2:
        raise ValueError("The dimensions are not 2!")

    newImage = pygame.transform.scale(image, dimensions)
    return newImage
