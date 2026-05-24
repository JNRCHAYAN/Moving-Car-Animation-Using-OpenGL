from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Car position
car_x = -200

# Speed
speed = 2


# Draw circle wheel
def drawWheel(cx, cy, r):

    glBegin(GL_POLYGON)

    for i in range(100):

        angle = 2 * 3.1416 * i / 100

        x = r * cos(angle)
        y = r * sin(angle)

        glVertex2f(cx + x, cy + y)

    glEnd()


# Draw car
def drawCar():

    global car_x

    # ---------------- SHADOW ----------------

    glColor3f(0.2, 0.2, 0.2)

    glBegin(GL_QUADS)

    glVertex2f(car_x + 60, 90)
    glVertex2f(car_x + 260, 90)
    glVertex2f(car_x + 240, 140)
    glVertex2f(car_x + 80, 140)

    glEnd()

    # ---------------- CAR BODY ----------------

    glColor3f(0, 0, 1)

    glBegin(GL_QUADS)

    # Lower body
    glVertex2f(car_x + 50, 100)
    glVertex2f(car_x + 250, 100)
    glVertex2f(car_x + 250, 160)
    glVertex2f(car_x + 50, 160)

    glEnd()

    # Upper body
    glBegin(GL_QUADS)

    glVertex2f(car_x + 90, 160)
    glVertex2f(car_x + 210, 160)
    glVertex2f(car_x + 180, 220)
    glVertex2f(car_x + 120, 220)

    glEnd()

    # Windows
    glColor3f(0.5, 0.8, 1)

    glBegin(GL_QUADS)

    glVertex2f(car_x + 100, 165)
    glVertex2f(car_x + 145, 165)
    glVertex2f(car_x + 140, 210)
    glVertex2f(car_x + 115, 210)

    glEnd()

    glBegin(GL_QUADS)

    glVertex2f(car_x + 155, 165)
    glVertex2f(car_x + 200, 165)
    glVertex2f(car_x + 185, 210)
    glVertex2f(car_x + 160, 210)

    glEnd()

    # Wheels
    glColor3f(0, 0, 0)

    drawWheel(car_x + 90, 100, 25)
    drawWheel(car_x + 210, 100, 25)


# Draw road
def drawRoad():

    glColor3f(0.3, 0.3, 0.3)

    glBegin(GL_QUADS)

    glVertex2f(0, 0)
    glVertex2f(500, 0)
    glVertex2f(500, 150)
    glVertex2f(0, 150)

    glEnd()

    # Road line
    glColor3f(1, 1, 1)

    for i in range(0, 500, 60):

        glBegin(GL_QUADS)

        glVertex2f(i, 70)
        glVertex2f(i + 30, 70)
        glVertex2f(i + 30, 80)
        glVertex2f(i, 80)

        glEnd()


# Animation update
def update(value):

    global car_x

    car_x += speed

    # Reset position
    if car_x > 500:
        car_x = -300

    glutPostRedisplay()

    glutTimerFunc(16, update, 0)


# Mouse click to increase speed
def mouse(button, state, x, y):

    global speed

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        speed += 1

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:

        if speed > 1:
            speed -= 1


# Display
def showScreen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glViewport(0, 0, 500, 500)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(0, 500, 0, 500, 0, 1)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    # Sky color
    glClearColor(0.5, 0.8, 1, 1)

    drawRoad()

    drawCar()

    glutSwapBuffers()


# Math functions
from math import *


# Initialize
glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

glutInitWindowSize(500, 500)

glutInitWindowPosition(100, 100)

glutCreateWindow(b"Moving Car Animation")

glutDisplayFunc(showScreen)

glutMouseFunc(mouse)

glutTimerFunc(16, update, 0)

glutMainLoop()