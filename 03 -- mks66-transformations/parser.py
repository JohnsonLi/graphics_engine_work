from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as file:
        line = file.readline().rstrip('\n')
        while line:
            print(line)
            if line == 'line':
                coords = [int(i) for i in file.readline().rstrip('\n').split()]
                add_edge(points, coords[0], coords[1], coords[2], coords[3], coords[4], coords[5])
            elif line == 'ident':
                ident(transform)
            elif line == 'scale':
                factors = [int(i) for i in file.readline().rstrip('\n').split()]
                m_scale = make_scale(factors[0], factors[1], factors[2])
                matrix_mult(m_scale, transform)
            elif line == 'translate' or line == 'move':
                coords = [int(i) for i in file.readline().rstrip('\n').split()]
                m_translate = make_translate(coords[0], coords[1], coords[2])
                matrix_mult(m_translate, transform)
            elif line == 'rotate':
                rotation = file.readline().rstrip('\n').split()
                if rotation[0] == 'x':
                    m_rotate = make_rotX(int(rotation[1]))
                if rotation[0] == 'y':
                    m_rotate = make_rotY(int(rotation[1]))
                if rotation[0] == 'z':
                    m_rotate = make_rotZ(int(rotation[1]))
                matrix_mult(m_rotate, transform)
            elif line == 'apply':
                matrix_mult(transform, points)
                points = [[int(i) for i in row] for row in points]
            elif line == 'display':
                clear_screen(screen)
                draw_lines(points, screen, color)
                display(screen)
            elif line == 'save':
                clear_screen(screen)
                draw_lines(points, screen, color)
                name = file.readline().rstrip('\n')
                save_extension(screen, name)
            elif line == 'end':
                return
                
            line = file.readline().rstrip('\n')

