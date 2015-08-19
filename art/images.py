from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 15
height = 8

for i in range(0,width):
  for j in range(0,height):
    if (i - j) % 5 == 0:
      image(x + i * 60, y + j * 60, "misc/YellowFlower.png")
    else:
      image(x + i * 60, y + j * 60, "misc/Clover.png")
     
