import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

ax = plt.gca()
ax.cla()
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

plt.plot(x,y,'ro')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)
ax.add_patch(circle2)
ax.set_aspect('equal')

plt.show() 
