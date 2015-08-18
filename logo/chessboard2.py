from tealight.logo import (move, 
                           turn, 
                           color)
def square(side):
    for i in range(0,4):
      move(side)
      turn(90)
     move(side)
     turn(140)

square(150)
