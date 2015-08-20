from tealight.art import *
from github.alexinder.art.alexpaint import *
from github.bbenny0211.art.paint import *

hue = 0
x0 = 0
y0 = 0

def handle_mousemove(x,y,button):
  global x0, y0, hue
  print x,y,button
  if button == 'left':
    #color("hsl(%d,100%%,50%%)" % hue)
  
    hue += 1
    line(x0,y0,x,y)
    x0 = x
    y0 = y
  else : 
    print ("press down")
    
def handle_mousedown(x,y,button):
  color_click(x,y)
  global x0,y0
  print x,y,button
  if button == 'left':
    x0 = x
    y0 = y
  else:
    print("press down")