from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 - x0 < 0:
        x0,y0,x1,y1 = x1,y1,x0,y0

    x = x0
    y = y0

    dx = x1 - x0
    dy = y1 - y0

    a = dy;
    b = -1 * dx

    # octant 1, 2
    if dy >= 0:
        if dx >= dy:
            d = 2 * a + b

            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2 * b
                x += 1
                d += 2 * a
        if dx < dy:
            d = a + 2 * b

            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1;
                    d += 2 * a
                y += 1
                d += 2 * b

    # octant 7, 8
    if dy < 0:
        if -1 * dy > dx:
            d = a + -2 * b

            while y >= y1:
                plot(screen, color, x, y)
                if d >= 0:
                    x += 1
                    d += a * 2
                y -= 1
                d += -2 * b

        if -1 * dy <= dx:
            d = 2 * a - b

            while x <= x1:
                plot(screen, color, x, y)
                if d <= 0:
                    y -= 1
                    d += -2 * b
                x += 1
                d += 2 * a
