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
  

def rowsr():
  for n in range(0,4):
    move()
  turn(1)
  for j in range(0,32):
    move()

def rowsl():
  turn(-1)
  for n in range(0,4):
    move()
  turn(-1)
  for j in range(0,32):
    move()



eatoutside()
eatoutside()
eatoutside()
eatoutside()
rowsr()
rowsl()
rowsr()