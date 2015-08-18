from tealight.logo import move, turn


def triangle(side):
  for i in range(0,3):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    triangle(decoration)
    turn(angle)

turn(-60)
waterwheel(12,75)
