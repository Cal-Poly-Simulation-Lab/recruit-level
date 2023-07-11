import vpython as vp

# Draw the box and set the color to red
box = vp.box()
box.color = vp.color.red

# start an infinite loop and set the rate to 20 frame per second
# rotate the box 0.1 radians per loop iteration
while True:
    vp.rate(20)
    box.rotate(.1)