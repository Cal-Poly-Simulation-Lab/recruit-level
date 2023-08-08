# import the vpython module
import vpython as vp

# set up the ball with initial position (.5, 3, 0)
p_0 = vp.vector(.5, 3, 0)
ball = vp.sphere(pos=p_0)
ball.color = vp.color.blue

# set up the pin with position (0, 0, -1.5).
# use the axis input to the cylinder command to make the cylinder 3 units long
pin = vp.cylinder(pos=vp.vector(0,0,-1.5), axis=vp.vector(0, 0, 3))
pin.color = vp.color.red
# set a property of the pin, center, and set it to the VPython vector (0,0,0)
pin.center = vp.vector(0,0,0)

# set up the floor and side walls to form a box of base 10x10 and walls that
# are 5x10.  The floor and the walls should have thinkness .5
floor = vp.box(pos=vp.vector(0, -5, 0), size=vp.vector(10, .5, 10))
floor.color = vp.color.green

left = vp.box(pos=vp.vector(-5.25,-2.75,0), size=vp.vector(.5, 5, 10))
left.color = vp.color.cyan

right = vp.box(pos=vp.vector(5.25,-2.75,0), size=vp.vector(.5, 5, 10))
right.color = vp.color.cyan

# Set the initial conditions of the ball
g = -9.8
ball.accel = vp.vector(0, g, 0)
ball.velocity = vp.vector(0, 0, 0)
# Set the time step dt to .01 seconds and the bounce energy loss, dE to 0.85
dt = 0.01
dE = 0.85

# Start the animation loop
while True:
    # set the rate to 100
    vp.rate(100)

    # find the distance between the ball position and the pin center
    n_dir = ball.pos - pin.center

    # If the ball hits the pin, bounce
    if vp.mag(n_dir) < ball.radius + pin.radius:
        t_dir = vp.cross(vp.hat(n_dir), vp.vector(0,0,1))
        v_t = vp.dot(ball.velocity, vp.hat(t_dir))*vp.hat(t_dir)
        v_n = vp.dot(ball.velocity, vp.hat(n_dir))*vp.hat(n_dir)
        ball.velocity = dE * (v_t - v_n)
        ball.pos = pin.center + (pin.radius+ball.radius)*vp.hat(n_dir)
    # elif the ball hits the floor, bounce    
    elif ball.pos.y - ball.radius < -4.75:
        ball.velocity.y = -1 * ball.velocity.y
        ball.velocity *= dE
        ball.pos.y = -4.75 + ball.radius
    # elif the ball hits a wall, bounce
    elif abs(ball.pos.x) + ball.radius > 5:
            ball.velocity.x = -1 * ball.velocity.x
            ball.velocity *= dE
            ball.pos.x = 4 * ball.pos.x/abs(ball.pos.x)
    # else apply gravitatonal acceleration to update the ball velocity
    else:
        ball.velocity += ball.accel * dt
    
    # update the ball position with the new velocity
    ball.pos += ball.velocity*dt