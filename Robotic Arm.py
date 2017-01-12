import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

arm1 = 0.40  # 400
arm2 = 0.25  # 250
arm3 = 0.15  # 150
breadth = 0.11

vertices = [
    [0, 0, breadth / 2],
    [0, 0, -breadth / 2],
    [0, arm1, breadth / 2],
    [0, arm1, -breadth / 2],
    [0, arm1 + arm2, breadth / 2],
    [0, arm1 + arm2, -breadth / 2],
    [0, arm1 + arm2 + arm3, breadth / 2],
    [0, arm1 + arm2 + arm3, -breadth / 2]
]

arms = (
    (0, 2),
    (1, 3),
    (0, 1),
    (2, 3),
    (2, 4),
    (3, 5),
    (2, 3),
    (4, 5),
    (4, 6),
    (5, 7)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
)


def arm():
    glBegin(GL_LINES)
    for edge in arms:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3)
    glLineWidth(3.0)
    arm()
    theta1 = 0
    theta2 = 0
    theta3 = 0

    while True:
        for event in pygame.event.get():

            m_theta = 90 - (theta1 + theta2)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:  # 119=w      115=s
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

                if event.key == 119:
                    if (theta1 > (2 * pi)):
                        theta1 = 0
                    theta1 = theta1 + 0.1

                    # theta1=theta1+theta2
                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                if event.key == 115:
                    if (theta1 > (2 * pi)):
                        theta1 = 0

                    theta1 = theta1 - 0.1

                    # theta1=theta1+theta2
                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                if event.key == 105:
                    if (theta2 > (2 * pi)):
                        theta2 = 0

                    theta2 = theta2 + 0.1

                    vertices[4][1] = vertices[2][1] + arm2 * cos(theta2 + theta3)
                    vertices[5][1] = vertices[3][1] + arm2 * cos(theta2 + theta3)
                    vertices[4][0] = vertices[2][0] + arm2 * sin(theta2 + theta3)
                    vertices[5][0] = vertices[3][0] + arm2 * sin(theta2 + theta3)

                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                    # theta1 = theta1+theta2

                if event.key == 107:
                    if (theta2 > (2 * pi)):
                        theta2 = 0

                    theta2 = theta2 - 0.1

                    vertices[4][1] = vertices[2][1] + arm2 * cos(theta2 + theta3)
                    vertices[5][1] = vertices[3][1] + arm2 * cos(theta2 + theta3)
                    vertices[4][0] = vertices[2][0] + arm2 * sin(theta2 + theta3)
                    vertices[5][0] = vertices[3][0] + arm2 * sin(theta2 + theta3)

                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                    # theta1 = theta1+theta2

                if event.key == 111:
                    if (theta2 > (2 * pi)):
                        theta2 = 0

                    theta3 = theta3 + 0.1

                    vertices[2][1] = vertices[0][1] + arm1 * cos(theta3)
                    vertices[3][1] = vertices[1][1] + arm1 * cos(theta3)
                    vertices[2][0] = vertices[0][0] + arm1 * sin(theta3)
                    vertices[3][0] = vertices[1][0] + arm1 * sin(theta3)

                    vertices[4][1] = vertices[2][1] + arm2 * cos(theta2 + theta3)
                    vertices[5][1] = vertices[3][1] + arm2 * cos(theta2 + theta3)
                    vertices[4][0] = vertices[2][0] + arm2 * sin(theta2 + theta3)
                    vertices[5][0] = vertices[3][0] + arm2 * sin(theta2 + theta3)

                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                if event.key == 108:
                    if (theta2 > (2 * pi)):
                        theta2 = 0

                    theta3 = theta3 - 0.1

                    vertices[2][1] = vertices[0][1] + arm1 * cos(theta3)
                    vertices[3][1] = vertices[1][1] + arm1 * cos(theta3)
                    vertices[2][0] = vertices[0][0] + arm1 * sin(theta3)
                    vertices[3][0] = vertices[1][0] + arm1 * sin(theta3)

                    vertices[4][1] = vertices[2][1] + arm2 * cos(theta2 + theta3)
                    vertices[5][1] = vertices[3][1] + arm2 * cos(theta2 + theta3)
                    vertices[4][0] = vertices[2][0] + arm2 * sin(theta2 + theta3)
                    vertices[5][0] = vertices[3][0] + arm2 * sin(theta2 + theta3)

                    vertices[6][1] = vertices[4][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[7][1] = vertices[5][1] + arm3 * cos(theta1 + theta2 + theta3)
                    vertices[6][0] = vertices[4][0] + arm3 * sin(theta1 + theta2 + theta3)
                    vertices[7][0] = vertices[5][0] + arm3 * sin(theta1 + theta2 + theta3)

                if event.key == 97:
                    glRotatef(15, 0, 1, 0)
                if event.key == 100:
                    glRotatef(-15, 0, 1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        arm()
        pygame.display.flip()
        pygame.time.wait(10)


main()
