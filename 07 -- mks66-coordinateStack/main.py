from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 250, 205]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script', edges, polygons, csystems, screen, color )
