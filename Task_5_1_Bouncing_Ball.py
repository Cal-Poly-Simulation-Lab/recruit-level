import vpython as vp

ball = vp.sphere(pos=vp.vec(0,5,0))
ball.color = vp.color.blue

floor = vp.box(length=5, width=5, height=.5)
floor.color = vp.color.red

g = -9.8
ball.accel = vp.vector(0, g, 0)
ball.velocity = vp.vector(0, 0, 0)
dt = 0.01

while True:
    vp.rate(100)
    
    if ball.pos.y < ball.radius + .25:
        ball.velocity *= -1*.8
        ball.pos = vp.vector(0, ball.radius, 0) + vp.vector(0, .25, 0)
    else:
        ball.velocity += ball.accel * dt
        
    ball.pos += ball.velocity*dt