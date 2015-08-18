from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def eatoutside():
  for n in range(0,32):
    move()
  turn(1)

def rows():
  for n in range(0,4):
    move()
  turn(1)
  turn(-1)

eatoutside()
eatoutside()
eatoutside()
eatoutside()
rows()