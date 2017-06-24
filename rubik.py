import curses

###
# For the sake of consistency, I will always assume that White is the front face and Red is the top face.
###

###
# Color constants

WHITE = "white"
RED = "red"
GREEN = "green"
ORANGE = "orange"
BLUE = "blue"
YELLOW = "yellow"

# Color shorthands

w = WHITE
r = RED
g = GREEN
o = ORANGE
b = BLUE
y = YELLOW

#
###

###
# The cube that will represent the whole thing.
cube = [ [ [w,w,w],
           [w,w,w],     # front
           [w,w,w] ],
         [ [r,r,r],
           [r,r,r],     # top
           [r,r,r] ],
         [ [g,g,g],
           [g,g,g],     # right
           [g,g,g] ],
         [ [o,o,o],
           [o,o,o],     # bottom
           [o,o,o] ],
         [ [b,b,b],
           [b,b,b],     # left
           [b,b,b] ],
         [ [y,y,y],
           [y,y,y],     # back
           [y,y,y] ] ]
