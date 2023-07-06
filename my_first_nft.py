import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection
import random
import math
def f1(x,y):
    result = random.uniform(-7,8) * x**2 - math.sin(y*2)
    return result

def f2(x,y):
    result = random.uniform(-6,7) * x+5 - math.cos(522*y)
    return result


#create a color array and use it

color_array = ["#d8e2dc", "#ffe5d9", "#ffcad4", "#f4acb7", "#9d8189"]


g = GenerativeImage(f1, f2)
# g.generate(start=-2*math.pi, )  step=0.01, stop=0

g.generate()
g.plot(cmap=color_array, color=g.data2, bgcolor="#001219", projection=Projection.POLAR)
plt.show()



