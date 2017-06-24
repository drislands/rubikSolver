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
# The cube that will represent the whole thing. For each face, the 9 elements are considered when looking directly at the face.

Cube = [ [ [w,w,w],
           [w,w,w],     # front
           [w,w,w] ],
         [ [r,r,r],
           [r,r,r],     # top -- the top row is the farthest side from the front
           [r,r,r] ],
         [ [g,g,g],
           [g,g,g],     # right
           [g,g,g] ],
         [ [o,o,o],
           [o,o,o],     # bottom -- the top row is the closest side to the front
           [o,o,o] ],
         [ [b,b,b],
           [b,b,b],     # left
           [b,b,b] ],
         [ [y,y,y],
           [y,y,y],     # back -- the top row is the actual top row
           [y,y,y] ] ]

#
###

###
# Functions -- For all rotate functions, set d to true for clockwise, false for counter.

def swap(a,b):
    return (b,a)

# For ease of swapping individual pieces, as in rotational functions.
# [ 0,0 0,1 0,2 ]   [ 0 1 2 ]
# [ 1,0 1,1 1,2 ]   [ 3 4 5 ]
# [ 2,0 2,1 2,2 ]   [ 6 7 8 ]

def positionSwap(face,a,b):
    a = ((int) (a / 3), a % 3)
    b = ((int) (b / 3), b % 3)
    
    d = face[a[0]][a[1]]
    face[a[0]][a[1]] = face[b[0]][b[1]]
    face[b[0]][b[1]] = d

    return (face[a[0]][a[1]],face[b[0]][b[1]])

def pS(f,a,b):
    return positionSwap(f,a,b)

# face-getters

def fro(cube):
    return cube[0]

def top(cube):
    return cube[1]

def rig(cube):
    return cube[2]

def bot(cube):
    return cube[3]

def lef(cube):
    return cube[4]

def bac(cube):
    return cube[5]

#

def rotateFace(face,d): 
    if d:
        rotateFaceCW(face)
    else:
        rotateFaceCCW(face)

def rotateFaceCW(f):
    pS(f,0,2)
    pS(f,0,8) # rotating the corners first
    pS(f,0,6)

    pS(f,1,5)
    pS(f,1,7) # rotating the sides
    pS(f,1,3)

def rotateFaceCCW(f):
    pS(f,0,6)
    pS(f,0,8) # rotating the corners first
    pS(f,0,2)

    pS(f,1,3)
    pS(f,1,7) # rotating the sides
    pS(f,1,5)
