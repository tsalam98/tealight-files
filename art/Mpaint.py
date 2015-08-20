from tealight.art import (color, line, spot, circle, rectangle, box, image, text, background, line)


tool = 10
brushcolor = "green"

def handle_mousemove(x,y,button):
  print x,y,button
  if button == 'left':
    color(brushcolor)
    line(x,y, tool)
  else : 
    print ("press down")