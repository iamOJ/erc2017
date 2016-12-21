import pygame

import time
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

List=[60.00,90.00,10.00,50.00,85.00,6,7,35.00,45.00,10.00] #[link1,link2,x,theta2,theta1,dl/dt,mini,distanceOFacctuatortoLink1,distanceOFacctuatortoLink2,basedistaanceacc]
def draw_link1(theta1,theta):
    ci=(-(List[2]/List[6]*math.cos(theta*3.14/180)),0,List[2]/List[6]*math.sin(theta*3.14/180))
    r=List[0]/List[6]
    x=ci[0]+r*math.cos(theta1*3.14/180)
    y=ci[1]+r*math.sin(theta1*3.14/180)
    co=(x*math.cos(theta*3.14/180),y,x*math.sin(theta*3.14/180))
    l1=(ci,co)
    l3=((0,0,0),ci)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    
    glColor3fv((0,0,1))
    
    
    for i in l3:
        glVertex3fv(i)
    glEnd()
    glBegin(GL_LINES)
    
    glColor3fv((1,1,0))  
    
    for i in l1:
        glVertex3fv(i)
    glEnd()
    ciacc1=((List[2]/List[6]*math.cos(theta*3.14/180)),0,List[2]/List[6]*math.sin(theta*3.14/180))
    racc1=List[7]/List[6]
    
    xacc1=ci[0]+racc1*math.cos(theta1*3.14/180)
    yacc1=ci[1]+racc1*math.sin(theta1*3.14/180)
    coacc1=(xacc1*math.cos(theta*3.14/180),yacc1,xacc1*math.sin(theta*3.14/180))
    l1acc=(ciacc1,coacc1)
    acctuator1=math.sqrt((xacc1-ciacc1[0])*(xacc1-ciacc1[0])+(yacc1-ciacc1[1])*(yacc1-ciacc1[1]))
    acctuator1=acctuator1*List[6]
    
    glBegin(GL_LINES)
    
    glColor3fv((0,1,0))  
    
    for i in l1acc:
        glVertex3fv(i)
    glEnd()
    racc2b=List[9]/List[6]
    
    xacc2b=ci[0]+racc2b*math.cos(theta1*3.14/180)
    yacc2b=ci[1]+racc2b*math.sin(theta1*3.14/180)
    coacc2b=(xacc2b*math.cos(theta*3.14/180),yacc2b,xacc1*math.sin(theta*3.14/180))
    
    return (co,coacc2b)
def draw_link2(theta1,theta2,theta):
    creturn=draw_link1(theta1,theta)
    r=List[1]/List[6]
    c=creturn[0]
    x2=c[0]-r*math.cos((theta1-theta2)*3.14/180)
    y2=c[1]-r*math.sin((theta1-theta2)*3.14/180)
    c2=(x2*math.cos((theta)*3.14/180),y2,x2*math.sin((theta)*3.14/180))
    rb=20/List[6]
    
    l2=(c2,c)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3fv((1,0,0))
    
    for i in l2:
        glVertex3fv(i)

    glEnd()
    rb=List[8]/List[6]
    x1=c[0]-rb*math.cos((theta1-theta2)*3.14/180)
    y1=c[1]-rb*math.sin((theta1-theta2)*3.14/180)
    c1=(x1*math.cos((theta)*3.14/180),y1,x1*math.sin((theta)*3.14/180))
    l2=(c1,creturn[1])
    glBegin(GL_LINES)
    glColor3fv((0,1,0))
    
    for i in l2:
        glVertex3fv(i)

    glEnd()
    c=creturn[1]
    acctuator2=math.sqrt((x1-c[0])*(x1-c[0])+(y1-c[1])*(y1-c[1]))
    acctuator2=acctuator2*List[6]
    
    

def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,4/3,0.0001,100)
    glTranslatef(0.0,0.0,-50)
    theta1=List[4]
    theta2=List[3]
    theta=0
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 116:    #t
                    theta1 = theta1 - 5
                    print "Actuator I down"
                if event.key == 103:    #g
                    theta1 = theta1 + 5
                    print "Actuator I up"
                if event.key == 121:
                    theta2 = theta2 + 5
                    print "Actuator II up"
                if event.key == 104:
                    theta2 = theta2 - 5
                    print "Actuator II down"
                if event.key == 122:
                    theta = theta + 10
                    print "Base ANTIclockwise"
                if event.key == 120:
                    theta = theta - 10
                    print "Base clockwise"


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_link2(theta1,theta2,theta)
        glBegin(GL_LINES)
        glColor3fv((0,1,1))
        ground=((-100,-44.5/List[6],0),(100,-44.5/List[6],0))
        for i in ground:
                glVertex3fv(i)
        glEnd()

        
        
                
        pygame.display.flip()
        pygame.time.wait(10)
    
main()
