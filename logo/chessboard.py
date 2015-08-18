from tealight.logo import (move, 
                           turn, 
                           color)
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

   
    
def more_squares(side):
  for i in range(0,8):
    square(side)
    move(side)
 
    
def rows_squares(side):
  for i in range(0,8):
    more_squares(side)
    turn(180)
    move(20)
    turn(90)
    move(side)
    turn(270)
    move(side)
    turn(90)
    
    
rows_squares(20)
    

