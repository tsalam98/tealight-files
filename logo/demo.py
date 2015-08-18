from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,360):
  move(i)
  turn()
  color(colors[i%3])