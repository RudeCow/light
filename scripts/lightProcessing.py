import numpy as np
import matplotlib.pyplot as plt
import imageio 
from numpy.core.fromnumeric import size
import module1 as j
import matplotlib.pylab as plt


j.readIntensity("blue-tungsten.png", "REZ-blue-tungsten", "лампа накаливания", "синий лист")
j.readIntensity("green-tungsten.png", "REZ-green-tungsten", "лампа накаливания", "зеленый лист")
j.readIntensity("red-tungsten.png", "REZ-red-tungsten", "лампа накаливания", "красный лист")
j.readIntensity("white-tungsten.png", "REZ-white-tungsten", "лампа накаливания", "белый лист")
j.readIntensity("yellow-tungsten.png", "REZ-yellow-tungsten", "лампа накаливания", "желтый лист")
j.readIntensity("white-mercury.png", "REZ-white-mercury.png", "ртутная лампа", "белый лист")


nomer_pika = [160, 219, 250, 290, 330, 380]
dlina_volni = [405, 436, 490, 546, 578, 610]
otnos = [0, 0, 0, 0, 0, 0]
sum = 0.0
for i in range(6): 
    otnos[i] = dlina_volni[i] / nomer_pika[i]
for i in range(6):
    sum = sum + otnos[i]
k = sum / 6

