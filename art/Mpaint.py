from tealight.art import (color, line, spot, circle, rectangle, box, image, text, background)


tool = "small"
brushcolor = "red"

def handle_mousemove(x,y,button):
  print x,y,button
  if button == 'left':
    spot(x,y, 10)
  else : 
    print ("press down")