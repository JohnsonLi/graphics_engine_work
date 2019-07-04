from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 242, 133, 252 ]
edges = []
transform = new_matrix()



parse_file( 'script', edges, transform, screen, color )
