from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue" , "yellow"]

for i in range(0,100):
  move(i)
  turn(60)
  color(colors[i%3])