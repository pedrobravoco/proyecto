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
    a=math.sqrt(distx*distx+disty*disty)
    return a
def corregir(boid,width,height,border=25):
    if boid[0][0]< border and boid[1][0]<0:
        boid[1][0]=-boid[1][0]*random.randint(1,10)
    if boid[0][0]>(width-border) and boid[1][0]>0:
        boid[1][0]=-boid[1][0]*random.randint(1,10)
    if boid[0][1]< border and boid[1][1]<0:
        boid[1][1]=-boid[1][1]*random.randint(1,10)
    if boid[0][1]>(height-border)and boid[1][1]>0:
        boid[1][1]=-boid[1][1]*random.randint(1,10)
    
    return boid

def moveCloser(fish,boids):
    if len(boids)<1:
        return
    x=0
    y=0
    vecindad=boids
    for v in vecindad:
        if v[0][0]==fish[0][0] and v[0][1]==fish[0][1]:
            continue
        x+=(fish[0][0]-v[0][0])
        y+=(fish[0][1]-v[0][1])
    x=x/len(vecindad)
    y=y/len(vecindad)
    fish[1][0]-=(x/100)
    fish[1][1]-=(y/100)
    return fish

def moveWith(fish,boids):
    if len(boids)<1:
        return
    x=0
    y=0
    vecindad=boids
    for v in vecindad:
        x+=v[1][0]
        y+=v[1][1]
    x=x/len(vecindad)
    y=y/len(vecindad)

    fish[1][0]+=(x/40)
    fish[1][1]+=(y/40)
    return fish

def moveAway(fish,boids,min_dist=20):
    if len(boids)<1:
        return
    x=0
    y=0
    numerosCercanos=0
    vecindad=boids
    for v in vecindad:
        if distancia(fish[0][0],v[0][0],fish[0][1],v[0][1])<min_dist:
            numerosCercanos+=1
            difx=(fish[0][0]-v[0][0])
            dify=(fish[0][1]-v[0][1])
            if difx<=0:
                difx=math.sqrt(min_dist)-difx
            else:
                difx=-math.sqrt(min_dist)-difx
            if dify<=0:
                dify=math.sqrt(min_dist)-dify
            else:
                dify=-math.sqrt(min_dist)-dify
            x+=difx
            y+=dify
    if numerosCercanos==0:
        return 
    fish[1][0]-= x/5
    fish[1][1]-= y/5
            
    return fish

def move(fish, max_speed):
    if abs(fish[1][0])>max_speed or abs(fish[1][1])>max_speed:
        escala=max_speed/max(abs(fish[1][0]),abs(fish[1][1]))
        fish[1][0]*=escala
        fish[1][1]*=escala
    fish[0][0]+=fish[1][0]
    fish[0][1]+=fish[1][1]
    return fish

def vecindad(pez_i,boids,max_distance):
    pez=boids[pez_i]
    boids1=[]
    for otro_boid in boids:
        if pez==otro_boid:
            continue
        distancia1=distancia(pez[0][0],otro_boid[0][0],pez[0][1],otro_boid[0][1])
        if distancia1<max_distance:
            boids1.append(otro_boid)
                
    return boids
