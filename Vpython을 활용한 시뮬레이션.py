# 코드1 #########################################
Web VPython 3.2

sphere(pos=vector(-5,0,0), color=vector(1,0,0), radius=1)
sphere(pos=vector(5,0,0), color=vector(0,0,1), radius=1)



# 코드2 #########################################
Web VPython 3.2

lball = sphere(pos=vector(-5,0,0), color=vector(1,0,0), radius=1) 
rball = sphere(pos=vector(5,0,0), color=vector(0,0,1), radius=1)

# 객체에 새로운 변수 추가
lball.cnsh = "충남과학고등학교"   # cnsh라는 변수 추가

rball.mass = 1.0                  # 질량 변수 추가
rball.velocity = vector(1, 0, 0)  # 속도 변수 추가

print(lball.cnsh)
print(rball.velocity)



# 코드3 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)


# 코드4 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)

t = 0
delta_t = 0.005
ball.velocity = vector(25,0,0)   # ball에 속도를 저장할 velocity 변수 추가
ball.pos = ball.pos + ball.velocity * delta_t   # ball의 처음 위치 + (delta_t초 동안 움직인 거리)



# 코드5 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)

t = 0
delta_t = 0.005
ball.velocity = vector(25,0,0)

while t <= 3:
    ball.pos = ball.pos + ball.velocity * delta_t
    t = t + deltat


# 코드6 ######################################### 
Web Vpython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)

t = 0
delta_t = 0.005
ball.velocity = vector(25,0,0)

while t <= 3:
    rate(100)

    if ball.pos.x > wallR.pos.x :
        ball.velocity.x = -ball.velocity.x

    ball.pos = ball.pos + ball.velocity * delta_t 
    t = t + delta_t


  
# 코드7 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)

ball.velocity = vector(25,0,0)
deltat = 0.005
t = 0

while t <= 3:
    rate(100)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat



# 코드8 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan, make_trail=True, retain=30)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)

ball.velocity = vector(25,0,0)
deltat = 0.005
t = 0

while t <= 3:
    rate(100)
    if ball.pos.x > wallR.pos.x or ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    ball.pos = ball.pos + ball.velocity*deltat
    t = t + deltat


# 코드9 #########################################
Web VPython 3.2

ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan, make_trail=True, retain=30)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)
wallT = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.blue)
wallB = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.blue)
wallF = box(pos=vector(0,0,6), size=vector(12,12,0.2), color=color.red, opacity=0.2)
wallRE = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.red)


#ball.velocity = vector(25, 0, 0)
ball.velocity = vector(25, 30, -35)
delta_t = 0.005
t = 0

while True:
    rate(100)
    
    if ball.pos.x > wallR.pos.x or ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallT.pos.y or ball.pos.y < wallB.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z > wallF.pos.z or ball.pos.z < wallRE.pos.z:
        ball.velocity.z = -ball.velocity.z
        
    ball.pos = ball.pos + ball.velocity*delta_t
    t = t + delta_t


# 코드10 #########################################
Web VPython 3.2

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box(pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallT = box(pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball = sphere (color = color.green, radius = 0.4, make_trail=True, retain=200)
ball.mass = 1.0
ball.p = vector (-0.15, -0.23, +0.27)

side = side - thk*0.5 - ball.radius

dt = 0.3
def move():
    rate(200, move)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.p.x = -ball.p.x
    if not (side > ball.pos.y > -side):
        ball.p.y = -ball.p.y
    if not (side > ball.pos.z > -side):
        ball.p.z = -ball.p.z

move()



# 코드11 #########################################
Web VPython 3.2

g = gcurve()
for x in arange(-2.0, 2.1, 0.1):
    g.plot(pos=(x, -2*x+1))



# 코드12 #########################################
Web VPython 3.2

g = gcurve()
for x in arange(-pi, pi+0.1, 0.1):
    g.plot(pos=(x, sin(x)))


# 코드13 #########################################
Web VPython 3.2

m = 0.1         	# Kg
g = vector(0,-9.8,0) 	# m/s^2; 중력가속도
r0 = vector(0,0,0) 	# m
v0 = vector(50,120,0)   # m/s
h = gdots(color=color.blue, size=10)
dt = 0.01

for t in arange(0, 10+dt, dt):
    v = v0 + g * t
    r = r0 + v * t + (g/2) * t ** 2
    
    rate(1/dt)

    if r.y >= 0:
        if(int(t/dt) % 20 == 0):
            h.plot(pos=(t,r.y))
            
    if r.y<0:
        print("t=",t , "V=", v.x, v.y, "r=", r.x, r.y)
        break


# 코드14 #########################################
Web VPython 3.2

g=vector(0,-9.8,0) # m/s^2
vm=100     	   # m/s
r0=vector(0,0,0)
h=gdots(color=color.blue, size=5)

for angle in arange(0, 90+5, 5):
    theta=angle*pi/180. #radian
    v0=vector(vm*cos(theta), vm*sin(theta), 0)
    for t in arange(0, 16, 0.1):
        rate(50)
        v=v0+g*t
        r=r0+v*t+(g/2)*t**2
        if r.y>=0:
            h.plot(pos=(r.x, r.y))
        elif r.y<=0:
            print("각도=", angle, "체공시간=", t, "수평도달거리=", r.x)
            break
