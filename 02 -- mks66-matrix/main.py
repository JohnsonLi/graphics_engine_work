from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix()

m1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

m2 = [[11, 12, 13, 14],
      [15, 16, 17, 18],
      [19, 20, 21, 22],
      [23, 24, 25, 26]
     ]

print('Matrix A')
print_matrix(m1)
print('Matrix B')
print_matrix(m2)
print('\n')

print('Multiplying A and B')
matrix_mult(m1, m2)
print('Matrix A AFTER A*B')
print_matrix(m1)
print('Matrix B AFTER A*B')
print_matrix(m2)
print('\n')

print('Multiplying B and A')
matrix_mult(m2, m1)
print('Matrix A AFTER B*A')
print_matrix(m1)
print('Matrix B AFTER B*A')
print_matrix(m2)
print('\n')

print('Multiplying by identity of A')
identity = []
for i in range(len(m1)):
  new_row = []
  for j in range(len(m1[0])):
    new_row.append(m1[i][j])
  identity.append(new_row)
# print_matrix(m1)
# print('---')
# print_matrix(identity)
ident(identity)
# print('------------')
# print_matrix(m1)
# print('---')
# print_matrix(identity)
matrix_mult(identity, m1)
print('Matrix A AFTER IDENT*A')
print_matrix(m1)

# handle
add_edge(matrix, 242, 12, 0, 262, 12, 0)
add_edge(matrix, 242, 12, 0, 252, 270, 0)
add_edge(matrix, 262, 12, 0, 252, 270, 0)

# blade
add_edge(matrix, 245, 120, 0, 202, 120, 0)
add_edge(matrix, 202, 120, 0, 250, 485, 0)

add_edge(matrix, 260, 120, 0, 303, 120, 0)
add_edge(matrix, 303, 120, 0, 250, 485, 0)

# coils
add_edge(matrix, 265, 375, 0, 240, 404, 0)
add_edge(matrix, 265, 375, 0, 237, 390, 0)


add_edge(matrix, 284, 242, 0, 233, 345, 0)
add_edge(matrix, 233, 345, 0, 278, 295, 0)


draw_lines( matrix, screen, color )
display(screen)
