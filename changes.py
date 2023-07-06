import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection
import random
import math
def f1(x,y):
    result = random.uniform(-7,3) * x**5 - math.sin(y*2)
    return result

def f2(x,y):
    result = random.uniform(2,7) * x+5 - math.cos(2*y)
    return result


def f3(x,y):
    result = random.uniform(-2,2) * x**5 - math.sin(y*200)
    return result

def f4(x,y):
    result = random.uniform(100,70) * x+5 - math.cos(200*y)
    return result


def f5(x,y):
    result = random.uniform(-9,100) * x**5 - math.sin(y*12)
    return result

def f6(x,y):
    result = random.uniform(1,2) * x+5 - math.cos(75*y)
    return result


def f7(x,y):
    result = random.uniform(1,2) * x+5 - math.cos(75*y)
    return result

def f8(x,y):
    result = random.uniform(1000,20) * x+900 - math.cos(755*y)
    return result

def f9(x,y):
    result = random.uniform(123,231) * x+50 - math.cos(15*y)
    return result

def f10(x,y):
    result = random.uniform(101213,287) * x+5213 - math.cos(5*y)
    return result


#create a color array and use it

color_array = ["#d8e2dc", "#ffe5d9", "#ffcad4", "#f4acb7", "#9d8189"]


g = GenerativeImage(f1, f2)
g1 = GenerativeImage(f3, f4)
g2 = GenerativeImage(f5, f6)
g3 = GenerativeImage(f7, f8)
g4 = GenerativeImage(f9, f10)
# g.generate(start=-2*math.pi, )  step=0.01, stop=0

g.generate()
g1.generate()
g2.generate()
g3.generate()
g4.generate()


g.plot( color = "#669bbc", bgcolor="black", projection=Projection.MOLLWEIDE)
g1.plot( color = "pink", bgcolor="black", projection=Projection.POLAR)
g2.plot( color = "white", bgcolor="black", projection=Projection.POLAR)
g3.plot( color = "yellow", bgcolor="black", projection=Projection.POLAR)
g4.plot( color = "green", bgcolor="black", projection=Projection.RANDOM)

x = g and g1 and g2 and g3 and g4
x.save_image(file_adr="hello.png", depth=5)


plt.show()



# cmap=color_array, color=g.data2,
