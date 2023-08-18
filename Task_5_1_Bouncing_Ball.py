import vpython as vp

# Create a blue ball or radius 1 and position (0,5,0)
ball = vp.sphere(pos = vp.vector(0,5,0))

# Create a red floor using a box of (l,h,w)=(5,.5,5) at position (0,0,0)

# Set initial conditions and values
g = -9.8
#ball.accel = vp.vector(0, g, 0)
#ball.velocity = vp.vector(0, 0, 0)
dt = 0.01

while True:
    # set the frame rate to 100 fps
    vp.rate(100)
    
    # if the edge of hte ball hits the floor, bounce by changing the velocity
    if ball.pos.y < ball.radius + x:
        pass
    # else, update velocty with a * dt
    else:
        pass
    
    # update the position of the ball with v * dt
    
    
    pass