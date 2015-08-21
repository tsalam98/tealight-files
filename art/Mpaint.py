from tealight.art import *
from github.alexinder.art.alexpaint import *
from github.bbenny0211.art.paint import *

hue = 0
x0 = 0
y0 = 0
rainbow = False

def handle_mousemove(x,y,button):
  global x0, y0, hue, rainbow, c
  #print x,y,button
  if button == 'left':
    if rainbow :
      color("hsl(%d,100%%,50%%)" % hue)
    else:
      color(c)
    hue += 1
    line(x0,y0,x,y)
    x0 = x
    y0 = y
  elif button == 'right':
    c = 'white'
  else : 
    print ("press down")
    
def handle_mousedown(x,y,button):
  global rainbow, c
  new_color = color_click(x,y)
  if new_color != None:
    if new_color == "rainbow":
      rainbow = True
    else:
      rainbow = False
      c = new_color
  thick_click(x,y)
  global x0,y0
  #print x,y,button
  if button == 'left':
    x0 = x
    y0 = y
  elif button == 'right':
    c = 'white'
    x0 = x
    y0 = y
  else:
    print("press down")
    
rectangle(170, 0, 1050, 815)
