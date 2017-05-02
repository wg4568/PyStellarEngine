#for python 2.7.13
import pygame
import stellarEngine as se

engine = se.engine.Engine()
engine.revEngines(1366,768,"test")

while not engine.shouldClose():
        engine.singleStep()

engine.stopEngines()
