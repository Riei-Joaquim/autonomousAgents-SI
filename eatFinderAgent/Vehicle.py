# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 5
        self.maxforce = 0.2
        self.comidas = 0

    # Method to update location
    def update(self, targetPos, matchComida):
        #colidiu com a comida
        if(matchComida):
            self.comidas += 1
        
        #diff vector to target
        vectDiff = targetPos - self.position
        # Update velocity
        self.velocity.add(vectDiff)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()+ PI / 2
        text("Comida: "+ str(self.comidas), 15, 15)
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
