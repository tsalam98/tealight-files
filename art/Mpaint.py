from tealight.art import *


tool = 60
brushcolor = "purple"

x0 = 0
y0 = 0

def handle_mousemove(x,y,button):
  global x0, y0
  print x,y,button
  if button == 'left':
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