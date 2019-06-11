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
    return a
def corregir(boid,width,height,border=25):
    print(boid)
    x,y=boid[0][0],boid[0][1]
    vx,vy=boid[1][0],boid[1][1]
    if x< border and vx<0:
        boid[1][0]=(-1*boid[1][0]*random.randint(1,10))
    if x>(width-border) and vx>0:
        boid[1][0]=(-1*boid[1][0]*random.randint(1,10))
    if x< border and vx<0:
        boid[1][1]=(-1*boid[1][1]*random.randint(1,10))
    if x>(height-border)and vx>0:
        boid[1][1]=(-1*boid[1][1]*random.randint(1,10))
    
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
        x+=(fish[0][0]-v[1][0])
        y+=(fish[0][1]-v[1][1])
    x=x/len(boids)
    y=y/len(boids)
    fish[1][0]-=(x/200)
    fish[1][1]-=(y/200)
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
                difx=-(math.sqrt(min_dist))-difx
            if dify<=0:
                dify=math.sqrt(min_dist)-dify
            else:
                dify=-(math.sqrt(min_dist))-dify
            x+=difx
            y+=dify
    if numerosCercanos==0:
        return fish
    fish[1][0]-= x/len(vecindad)
    fish[1][1]-= y/len(vecindad)
            
    return fish

def move(fish, max_speed):
    if abs(fish[1][0])>max_speed and abs(fish[1][1])>max_speed:
        escala=max_speed/max(abs(fish[1][0]),abs(fish[1][1]))
        fish[1][0]*=escala
        fish[1][1]*=escala
    fish[0][0]+=fish[1][0]
    fish[0][1]+=fish[1][1]
    return fish

def vecindad(pez_i,boids,max_distance):
    if pez_i==0:
        return boids
    else:
        for boid in boids:
            boids1=[]
            for otro_boid in boids:
                if boid==otro_boid:
                    continue
                distancia1=distancia(boid[0][0],otro_boid[0][0],boid[0][1],otro_boid[0][1])
                if distancia1<max_distance:
                    boids1.append(otro_boid)
                
    return boids1
