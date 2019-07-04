import math

from display import *
from draw import *

screen = new_screen()

# gap_width  = 15

# color = [ 242, 150, 242 ]
# for x in range(500):
#   x *= gap_width 
#   draw_line(x, 0, 500, 500, screen, color)

# color = [239, 162, 179]
# for x in range(500):
#   x *= gap_width
#   draw_line(0, x, 500, 500, screen, color)

# color = [241, 244, 139]
# for x in range(500):
#   x *= gap_width
#   draw_line(x, 500, 500, 0, screen, color)  

# color = [156, 235, 237]
# for x in range(500):
#   x *= gap_width
#   draw_line(0, 500, 500, x, screen, color)

color = [ 242, 150, 242 ]
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)
draw_line(250, 0, 250, 500, screen, color)
draw_line(0, 250, 500, 250, screen, color)

draw_line(250, 250, 500, 300, screen, color)
draw_line(250, 250, 300, 500, screen, color)

draw_line(250, 250, 200, 500, screen, color)
draw_line(250, 250, 0, 300, screen, color)


draw_line(250, 250, 0, 200, screen, color)
draw_line(250, 250, 200, 0, screen, color)

draw_line(250, 250, 300, 0, screen, color)
draw_line(250, 250, 500, 200, screen, color)


display(screen)
save_extension(screen, 'img.png')
