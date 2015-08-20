from tealight.art import (color, line, spot, circle, rectangle, box, image, text, background, line)


tool = 10
brushcolor = "purple"

def handle_mousemove(x,y,button):
  print x,y,button
  if button == 'left':
    color(brushcolor)
    line(90,100, 10, 4 )
  else : 
    print ("press down")