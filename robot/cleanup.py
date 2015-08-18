from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
if touch() == 'water':
  move()

if right_side() == 'water':
  move()