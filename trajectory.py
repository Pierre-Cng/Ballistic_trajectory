'''
Docstring
ref: https://fr.wikipedia.org/wiki/Trajectoire_d%27un_projectile
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


g = 9.81

class projectile():
    alpha = math.radians(45)
    beta = math.radians(0)
    v0 = 1000
    h = 0

    def alpha_init(self, value_in_degree):
        self.alpha = math.radians(value_in_degree)
        return self.alpha
    
    def beta_init(self, value_in_degree):
        self.beta = math.radians(value_in_degree)
        return self.beta
    
    def v0_init(self, value_in_m_per_s):
        self.v0 = value_in_m_per_s
        return self.v0
    
    def h_init(self, value_in_m):
        self.h = value_in_m
        return self.h
    
    def x(self,t): 
        x = round(math.cos(self.alpha), 5)*self.v0*t
        return x
    
    def y(self,t):
        y = -0.5*g*(t**2)+round(math.sin(self.alpha), 5)*self.v0*t+self.h
        return y
    
    def z(self,t):
        z = round(math.cos(self.beta), 5)*self.v0*t
        return z 
    
    def distance(self):
        d = (self.v0 / g) * round(math.cos(self.alpha), 5)*(self.v0*round(math.sin(self.alpha),5)+ math.sqrt((self.v0*round(math.sin(self.alpha),5))**2+2*g*self.h))
        return d
    
    def duration(self):
        t = self.distance() / (self.v0*round(math.cos(self.alpha), 5))
        return t 

    def peak(self):
        h = (self.v0**2)*(round(math.sin(self.alpha),5)**2)/(2*g)
        return h
    
    def angle_to_distance(self, targeted_distance):
        alpha = 0.5*round(math.asin(g*targeted_distance/(self.v0**2)),5)
        return alpha
    
    def velocity_at_distance(self,x):
        v = math.sqrt((self.v0**2)-2*g*x*round(math.tan(self.alpha),5)+(g*x/(self.v0*round(math.cos(self.alpha),5)))**2)
        return v
    
    def angle_to_target(self, x, y):
        alpha = round(math.atan(((self.v0**2)+abs(math.sqrt((self.v0**4)-g*(g*(x**2)+2*y*self.v0**2))))/(g*x)),5)
        return alpha
    
obj = projectile()   
t = np.arange(0, obj.duration(), 0.01)
fig, ax = plt.subplots()
#plot default data:
ax.plot(obj.x(t), obj.y(t))
ax.plot(obj.x(t), [obj.velocity_at_distance(x) for x in obj.x(t)])
ax.text(10, 0, f'distance = {obj.distance()}, \nduration = {obj.duration()}, \npeak = {obj.peak()}')

#plot trajectory to reach specified distance:
targeted_distance = 100000
angle_distance = obj.angle_to_distance(targeted_distance)
obj.alpha = angle_distance
ax.plot(obj.x(t), obj.y(t))
ax.plot(obj.x(t), [obj.velocity_at_distance(x) for x in obj.x(t)])

#plot trajectory to reach specified coordinate:
targeted_coordinate = (37000, 25000)
angle_target = obj.angle_to_target(targeted_coordinate[0], targeted_coordinate[1])
obj.alpha = angle_target
ax.plot(obj.x(t), obj.y(t))
ax.plot(obj.x(t), [obj.velocity_at_distance(x) for x in obj.x(t)])

ax.set_ylim(0)
plt.show()






'''

def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression)
    l.set_ydata(ydata)
    
    
    ax.relim()
    ax.autoscale_view()
    plt.draw()


axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t")  # Trigger `submit` with the initial string.

plt.show()'''