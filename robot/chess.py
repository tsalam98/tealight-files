from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
move
turn(1)

distance = 10
for n in range(0, 32):
  move()

def eatloop():
  for i in range(0,10):
    turn(-1)
    distance = 10
    for n in range(0, 32):
      move()

eatloop