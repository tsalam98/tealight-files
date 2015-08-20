from tealight.art import (color, line, spot, circle, rectangle, box, image, text, background, line)


tool = 30
brushcolor = "purple"

x0 = 0
y0 = 0

    
def handle_mousedown(x,y,button):
  global x0,y0
  print x,y,button
  if button == 'left':
    color(brushcolor)
    line(x0, y0,x,y)
  else:
    print("press down")