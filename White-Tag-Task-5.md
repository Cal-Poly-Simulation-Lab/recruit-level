# Task 5 - Putting it all together

Let's use physics and code to model and simulate a bouncing ball.

We know from basic physics that an object in a gravitational field will obey the following equations for verticle position and velocity:

$$ r_1 = r_0 + v_0 \cdot \delta t $$

$$ v_1 = v_0 + a_0 \cdot \delta t $$

When we are in a gravitational field, $a_0 = -g = 9.8 \frac{m}{s^2}$ and is constant.  Therefore, if we were to drop a ball, the ball would start with $v_0 = 0 \frac{m}{s}$ and would accelerate until it hits the ground.  If the ball was purely elastic, the ball would bounce back straight up with the same magnitude velocity.  If the ball is not (more realalistic) some amount of the velocity of the ball would be lost in the collision.  We can model this as some fractional loss of velocity (or energy really) as, $v_1 = v_0 + \gamma \cdot g \cdot \delta t$.  Here, $\gamma$ is the fractional loss of velocity.  For this simulation, let $\gamma=0.85$ (no units).

## Task 5_1 - Bouncing Ball Simulation
Using the template provided *Task_5_1_Bouncing_Ball.py* create code that models and simulates a ball bouncing off a simulated floor.  The template will help guide you through the modeling process (the physics) as well as how to express the model in code.

- [ ] Task 5_1 - Complete the code template and commit and synch your changes for review.


## Task 5_2 - Start of the Game of Plinko
Using the same physics from *Task 5_1* we can model and simulate what happens with the ball drops onto a pin and deflects at the proper angle.  In this case, all the physical quanties above (position, velocity, acceleration) are vectors.  We need to use vectors because we need to track the direction the ball moves as well.

The starter code *Task_5_2_Plinko.py* will help you work through this task.  The code is similar to *Task_5_1* but here we need to calculate when the ball hits the pin, and what direction the ball will bounce according to Newton's Laws.

- [ ] Task 5_2 - Complete the code template and commit and synch your changes for review.

$r = r_0 + v*\detla t$
$v = v_0 + a*\delta t$

In our case, the object is a ball, $a = g = -9.8 m/s^2$, and we assume the change in time, $\delta t$ is small.

We can also assmue the ball will loose some small amount of energy on each bounce and will eventually come to rest.  We can model this loss of energy as a fractional change in the velocity of the ball.  Remember the Kinetic Energy of a point mass is given by, $KE = 1/2mv^2$.  So after a bounce with some energy loss, we can say $KE_2 = \mu KE_1 = \mu  1/2mv^2$ where $0 <= \mu <= 1$.  In this case, let $\mu = 0.95$.

- [ ] Task 5_1 - Simple ball bounce - use VPython and the template code *Task_5_1_Bouncing_Ball.py* to create a simulation of a bouncing ball.  Push your code for feedback and completion of task 5_1

- [ ] Task 5_2 - Basic Plinko - Plinko is a basic game where the player drops a ball that bounces off a set of pins and then lands at the bottom in a bin.  Each bin has some number of points.  The points are based on the probability the ball will land in the bin (NEED LINK TO PLINKO RULES).  Use the template code *Task_5_2_Plinko.py* to create the start of a basic Plinko game.  Push your code for feedback and completion of task 5_2.