## Task 5 - More Advancd Simulation - The Game of Plinko

Now let's simulate a more complex physical system.  Then we can take the basic ideas and create the start of a simple game.

### Bouncing Ball
We can use the VPython library and a little bit of physics to simulate the motion of a ball bouncing off a floor.  We will complete what amounts to a 1-dimentional simulation, but notice the code you develop can be used for 2- and 3-dimentional simulations with only a few modifications.

First, we need to lay out the basic physics we will use.  First, an object falling on Earth obeys the simple Newtonian physics of $F = ma$ with $F = mg$ and $g = 9.8 \frac{m}{s^2}$.  There are several ways to determine the resulting motion of the object [^1].  From basic physics, we know:

$$r = r_0 + v \cdot t = r_0 + v_0 \cdot t + a \cdot t^2$$

$$v = v_0 + a \cdot t$$

Using a more advanced concept you will learn about later on in your classes, we can use [Euler Integration](https://en.wikipedia.org/wiki/Euler_method) to update the position and velocity of the object over small time periods.  When we put these updates together, we can approximate the motion of the object over longer periods of time.  In otherwords, over a small amount of time, say $dt$, the object moves $dr = dr_0 + dv \cdot dt$ and the velocity changes by $dv = dv_0 + a \cdot dt$.  In this case the acceleration $a$ is constant.

- [ ] Task 5_2 - Basic Plinko - Plinko is a basic game where the player drops a ball that bounces off a set of pins and then lands at the bottom in a bin.  Each bin has some number of points.  The points are based on the probability the ball will land in the bin [Plinko](https://priceisright.fandom.com/wiki/Plinko).  Use the template code *Task_5_2_Plinko.py* to create the start of a basic Plinko game.  Push your code for feedback and completion of task 5_2.

[^1]: By resulting motion, we mean the position and velocity of the object as a function of time. In general we call the resulting differential equation $F=mg=ma$ the *Equations of Motion* of the object, and the resulting equations for position and velocity are the *solutions* to the Equations of Motion.
