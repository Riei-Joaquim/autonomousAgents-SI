# The "Food" class
import random

class Food():

    def __init__(self, maxX, maxY):
        self.acceleration = PVector(0, 0)
        self.velocity =  PVector(0, 0)
        self.EDGE_MARGIN = 6
        self.maxX = maxX -self.EDGE_MARGIN
        self.maxY = maxY -self.EDGE_MARGIN
        self.position = PVector(random.randint(self.EDGE_MARGIN, self.maxX), random.randint(self.EDGE_MARGIN, self.maxY))
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.COLLIDER_THRESHOLD = 4
        self.intercept = False

    # Method to update location
    def update(self, vehiclePos):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        if((vehiclePos- self.position).mag() < self.COLLIDER_THRESHOLD):
            self.intercept = True
            self.position = PVector(random.randint(self.EDGE_MARGIN, self.maxX), random.randint(self.EDGE_MARGIN, self.maxY))
        else:
            self.intercept = False
            
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() #+ PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
