# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width/2, height/2, velocity)
    food = Food(width, height)

def draw():
    background(255)
    targetPos = food.position
    
    vehicle.update(targetPos, food.intercept)
    vehicle.display()
    
    food.update(vehicle.position)
    food.display()
