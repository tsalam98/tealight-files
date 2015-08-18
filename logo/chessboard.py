from tealight.logo import (move, 
                           turn, 
                           color)
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)