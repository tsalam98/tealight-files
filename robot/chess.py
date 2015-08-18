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
  

def rowsr_():
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

def rowsr():
  turn(1)
  for n in range(0,4):
    move()
  turn(1)
  for j in range(0,32):
    move()

def columnsd():
  turn(-1)
  for n in range(0,3):
    move()
  turn(-1)
  for j in range(0,4):
    move()
  turn(-1)
  for k in range(0,32):
    move()


eatoutside()
eatoutside()
eatoutside()
eatoutside()
rowsr_()
rowsl()
rowsr()
rowsl()
rowsr()
rowsl()
rowsr()
columnsd()