## Task 5 - Putting it all together

Let's use physics and code to model and simulate a bouncing ball.

We know from basic physics that an object in a gravitational field will obey the following equations for verticle position and velocity:

$r = r_0 + v*\detla t$
$v = v_0 + a*\delta t$

In our case, the object is a ball, $a = g = -9.8 m/s^2$, and we assume the change in time, $\delta t$ is small.

We can also assmue the ball will loose some small amount of energy on each bounce and will eventually come to rest.  We can model this loss of energy as a fractional change in the velocity of the ball.  Remember the Kinetic Energy of a point mass is given by, $KE = 1/2mv^2$.  So after a bounce with some energy loss, we can say $KE_2 = \mu KE_1 = \mu  1/2mv^2$ where $0 <= \mu <= 1$.  In this case, let $\mu = 0.95$.

- [ ] Task 5_1 - Simple ball bounce - use VPython and the template code *Task_5_1_Bouncing_Ball.py* to create a simulation of a bouncing ball.  Push your code for feedback and completion of task 5_1

- [ ] Task 5_2 - Basic Plinko - Plinko is a basic game where the player drops a ball that bounces off a set of pins and then lands at the bottom in a bin.  Each bin has some number of points.  The points are based on the probability the ball will land in the bin (NEED LINK TO PLINKO RULES).  Use the template code *Task_5_2_Plinko.py* to create the start of a basic Plinko game.  Push your code for feedback and completion of task 5_2.