from matplotlib import matplotlib_fname
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
# gradient descent from scratch

# equation for a straight line: y = mx + b
# slope-intercept form
# m = slope
# b = intercept

class Linear_Regression:
    def __init__(self, m, b, n, steps, l_rate):
        self.m = m
        self.b = b
        self.n = n
        self.steps = steps
        self.l_rate = l_rate

    def grad_desc(self, x,y):
        # make learning rate small!!
        for i in range(self.steps):
            plt.clf()
            y_pred = self.m * x + self.b
            # get partial derivative for m from cost function
            m_der = -(2/self.n) * (sum(x*(y-y_pred)))
            # get partial derivative for b from cost function
            b_der = -(2/self.n) * (sum(y-y_pred))
            # m update
            self.m = self.m - self.l_rate * m_der
            # b update
            self.b = self.b - self.l_rate * b_der
            cost = round((1/self.n) * sum([i**2 for i in (y - y_pred)]), 4)
            #cost = round(cost, 4)
            plt.scatter(x,y)
            plt.plot([min(x), max(y)], [min(y_pred), max(y_pred)], color='green')
            plt.text(7.0, 17.5, f'{cost}', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 6})
            plt.pause(0.01)
        return plt.show()

if __name__ == '__main__':
    x = random.randint(20, size=(20))
    y = random.randint(20, size=(20))
    Linear_Regression(0, 0, len(x), 100, 0.0001).grad_desc(x,y)





