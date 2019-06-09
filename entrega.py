import random
import math

def generarCardumen(n,w,h,speed=10):
    boids=[]
    for i in range(n):
        x, y=random.randint(1,w),random.randint(1,h)
        course=random.uniform(-1,1)
        vx,vy=random.randint(1,speed)/speed, random.randint(1,speed)/speed
        boids.append([[x,y],[vx,vy],])
    return boids

def distancia(x1,x2,y1,y2):
    distx=x1-x2
    disty=y1-y2
    a=math.sqrt((distx**2)+(disty**2))
    print(a)
    return a
def corregir(boid,width,height,border=25):
    return boid

def moveCloser(fish,boids):
    return fish

def moveWith(fish,boids):
    return fish

def moveAway(fish,boids,min_dist=20):
    return fish

def move(fish, max_speed):
    if abs(fish[1][0])>max_speed and abs(fish[1][1])>max_speed:
        escala=max_speed/max(fish[1][0],fish[1][1])
        fish[1][0]+=escala
        fish[1][1]+=escala
    fish[0][0]+=fish[1][0]
    fish[0][1]+=fish[1][1]
    return fish

def vecindad(pez_i,boids,max_distance):
    if pez_i==0:
        return boids
    else:
        for i in range(pez_i):
            boids1=[]
            for otro_boid in boids:
                if boids[pez_i]==otro_boid:
                    continue
                distancia1=distancia(boids[i][0][0],otro_boid[0][0],boids[i][0][1],otro_boid[0][1])
                if distancia1<max_distance:
                    boids1.append(otro_boid)
                
    return boids1
