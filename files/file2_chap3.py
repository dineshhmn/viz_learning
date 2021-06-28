import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

"""
Few advanced features
"""

def create_sample_data():
    x_vals = np.linspace(0,20,20)
    y_vals = [math.sqrt(i) for i in x_vals]
    return x_vals, y_vals

def use_subplot():
    plt.rcParams["figure.figsize"] = [12,8]
    x_v, y_v = create_sample_data()
    plt.subplot(2,2,1)
    plt.plot(x_v, y_v, 'bo-')
    plt.subplot(2,2,2)
    plt.plot(x_v, y_v, 'rx-')
    plt.subplot(2,2,3)
    plt.plot(x_v, y_v, "g*-")
    plt.subplot(2,2,4)
    plt.plot(x_v, y_v,"y^-")
    plt.show()

def use_for_and_save():
    x_v, y_v = create_sample_data()
    fix, axes = plt.subplots(nrows=4,ncols=2)
    for rows in axes:
        for ax1 in rows:
            ax1.plot(x_v, y_v,'g')
            ax1.set_title("sqrt")
    plt.show()

def ex1_func():
    dat = np.linspace(1,60,60)
    plt.subplot(3,1,1)
    plt.plot(dat, np.sin(dat))
    plt.subplot(3,1,2)
    plt.plot(dat, np.cos(dat))
    plt.subplot(3,1,3)
    plt.plot(dat, np.tan(dat))
    plt.show()


def start_execution():
    #use_subplot()
    #use_for_and_save()
    ex1_func()



if __name__=="__main__":
    start_execution()

