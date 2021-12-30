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
    def __init__(self):
        return None
    
    def grad_desc(x,y):
        m = 0
        b = 0
        n = len(x)
        steps = 500
        # make learning rate small!!
        learning_rate = 0.0001
        for i in range(steps):
            plt.clf()
            y_pred = m * x + b
            # get partial derivative for m from cost function
            m_der = -(2/n) * (sum(x*(y-y_pred)))
            # get partial derivative for b from cost function
            b_der = -(2/n) * (sum(y-y_pred))
            # m update
            m = m - learning_rate * m_der
            # b update
            b = b - learning_rate * b_der
            cost = (1/n) * sum([i**2 for i in (y - y_pred)])
            cost = round(cost, 4)
            plt.scatter(x,y)
            plt.plot([min(x), max(y)], [min(y_pred), max(y_pred)], color='green')
            plt.text(7.0, 17.5, f'{cost}', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 6})
            plt.pause(0.01)
        plt.show()


if __name__ == '__main__':
    x = random.randint(20, size=(20))
    y = random.randint(20, size=(20))
    Linear_Regression.grad_desc(x,y)





