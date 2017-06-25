import curses
import queue

### Curses setup

stdscr = curses.initscr()
curses.noecho()
curses.cbreak() 
stdscr.keypad(True)

###

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

# points to latest version of isValid. To ensure no corruption of the cube

def isValid(cube):
    return isValid1(cube)

def isValid1(cube):
    count = {w:0,r:0,g:0,y:0,o:0,b:0}
    for i in cube:
        for j in i:
            for k in j:
                count[k] = count[k] + 1
    
    return (count[w] == 9 and count[r] == 9 and count[g] == 9 and
            count[y] == 9 and count[o] == 9 and count[b] == 9)

#

def isSolved(cube):
    for i in cube:
        color = i[1][1]
        for j in i:
            for k in j:
                if not k == color:
                    return False
    return isValid(cube)

##

def isFrontSolved(cube):
    f = cube[0]
    color = f[1][1]
    for i in f:
        for j in i:
            if not j == color:
                return False

    f = cube[1]
    color = f[1][1]
    for i in f[2]:
        if not i == color:
            return False
    
    f = cube[2]
    color = f[1][1]
    for i in range(0,3):
        if not f[i][0] == color:
            return False

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
    if d == "cw":
        rotateFaceCW(face)
    elif d == "ccw":
        rotateFaceCCW(face)
    else:
        rotateFace180(face)

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

def rotateFace180(f):
    ps(f,0,8)
    ps(f,2,6)

    ps(f,1,7)
    ps(f,3,5)

#
###
# Solution functions

