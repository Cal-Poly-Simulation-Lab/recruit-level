import vpython as vp

ball = vp.sphere(pos=vp.vec(0,5,0))
ball.color = vp.color.blue

pin = vp.sphere(pos=vp.vector(0,0,0))
pin.color = vp.color.red

g = -9.8
ball.accel = vp.vector(0, g, 0)
ball.velocity = vp.vector(0, 0, 0)
dt = 0.01

while True:
    vp.rate(100)
    n_dir = ball.pos - pin.pos
    t_dir = vp.cross(vp.hat(n_dir), vp.vector(0,0,1))
    if vp.mag(n_dir) < ball.radius + pin.radius:
        bounce_angle = vp.diff_angle(-ball.velocity, n_dir)
        bounce_dir = vp.hat(t_dir)*vp.sin(bounce_angle) + vp.hat(n_dir)*vp.cos(bounce_angle)
        ball.velocity = vp.mag(ball.velocity)*bounce_dir
        ball.pos = pin.pos + n_dir
    else:
        ball.velocity += ball.accel * dt
        
    ball.pos += ball.velocity*dt