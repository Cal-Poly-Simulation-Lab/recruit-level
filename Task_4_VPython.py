import vpython as vp

# Draw the box with sides length 2 and centered at the origin
# name the variable box
# set the box color to red color to red
box = vp.box(length=2, width=2, height=2)
box.color = vp.color.red

# start an infinite loop and set the rate to 20 frame per second
# rotate the box 0.1 radians per loop iteration around the y-axis (0, 1, 0)
while True:
    vp.rate(20)
    box.rotate(.1, vp.vector(0, 1, 0))