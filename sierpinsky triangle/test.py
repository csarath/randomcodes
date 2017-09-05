import random
import matplotlib.pyplot as plt

min = 1
max = 6

a = (0.0,0.0)
ax = 0.0
ay = 0.0
b = (8.0,8.0)
bx = 8.0
by = 8.0
c = (0.0,8.0)
cx = 0.0
cy = 8.0


currentx = 16.0/3.0
currenty = 16.0/3.0

plist = []

plist.append(a)
plist.append(b)
plist.append(c)

for i in range(0,10000):
    plist.append((currentx,currenty))
    rand = random.randint(min,max)
    if rand == 1 or rand == 2:
        currentx = (currentx + ax)/2.0
        currenty = (currenty + ay)/2.0
    elif rand == 3 or rand == 4:
        currentx = (currentx + bx)/2.0
        currenty = (currenty + by)/2.0
    else:
        currentx = (currentx + cx)/2.0
        currenty = (currenty + cy)/2.0

plt.scatter(*zip(*plist))
plt.show()




