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

eatloop()
eatloop()
eatloop()
eatloop()

def rows():
  for n in range(0,4)
    move()
  turn(1)
  turn(-1)
 