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
    x=0
    y=0
    vecindad=boids
    for v in vecindad:
        x=fish[0][0]-v[0][0][0]
        y=fish[0][1]-v[0][0][1]
    x=x/len(vecindad)
    y=y/len(vecindad)
    fish[1][0]=fish[1][0]/len(vecindad)
    fish[1][1]=fish[1][1]/len(vecindad)
    return fish

def moveWith(fish,boids):
    x=0
    y=0
    vecindad=boids
    for v in vecindad:
        x=fish[1][0]
        y=fish[1][1]
    x=x/len(vecindad)
    y=y/len(vecindad)
    return fish

def moveAway(fish,boids,min_dist=20):
    x=0
    y=0
    numeroCercanos=0
    vecindad=boids
    for v in vecindad:
        if distancia(fish[0][0],v[0][0],fish[0][1],v[0][1])<min_dist:
            numerosCercanos+=1
            difx=fish[0][0]-v[0][0]
            dify=fish[0][1]-v[0][1]
            if difx<=0:
                difx=math.sqrt(min_dist)-difx
            else:
                difx=-(math.sqrt(min_dist))-difx
            if dify<=0:
                dify=math.sqrt(min_dist)-dify
            else:
                dify=-(math.sqrt(min_dist))-dify
        x=x+difx
        y=y+dify
    if numerosCercanos==0:
        return fish
    fish[0][0]=-(fish[0][0])/len(vecindad)
    fish[0][1]=-(fish[0][1])/len(vecindad)
            
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
