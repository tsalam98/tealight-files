from tealight.art import *


tool = 60
hue = 0
brushcolor =

x0 = 0
y0 = 0

def handle_mousemove(x,y,button):
  global x0, y0
  print x,y,button
  if button == 'left':
    hue = hue + 1 

    color(brushcolor)
    line_width(tool)
    line(x0,y0,x,y)
    x0 = x
    y0 = y
  else : 
    print ("press down")

    
def handle_mousedown(x,y,button):
  global x0,y0
  print x,y,button
  if button == 'left':
    x0 = x
    y0 = y
  else:
    print("press down")