## Task 5 - Putting it all together

Let's use physics and code to model and simulate a bouncing ball.

We know from basic physics that an object in a gravitational field will obey the following equations for verticle position and velocity:

$$ r_1 = r_0 + v_0 \cdot \delta t $$

$$ v_1 = v_0 + a_0 \cdot \delta t $$

When we are in a gravitational field, $a_0 = -g = 9.8 \frac{m}{s^2}$ and is constant.  Therefore, if we were to drop a ball, the ball would start with $v_0 = 0 \frac{m}{s}$ and would accelerate until it hits the ground.  If the ball was purely elastic, the ball would bounce back straight up with the same magnitude velocity.  If the ball is not (more realalistic) some amount of the velocity of the ball would be lost in the collision.  We can model this as some fractional loss of velocity (or energy really) as, $v_1 = v_0 + \gamma \cdot g \cdot \delta t$.  Here, $\gamma$ is the fractional loss of velocity.  For this simulation, let $\gamma=0.85$ (no units).

Using the template provided *Task_5_1_Bouncing_Ball.py* create code that models and simulates a ball bouncing off a simulated floor.  The template will help guide you through the modeling process (the physics) as well as how to express the model in code.

- [ ] 
