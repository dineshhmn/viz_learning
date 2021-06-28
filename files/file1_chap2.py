import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

"""
basic matplotlib plotting
"""

iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')

def create_sample_data():
    x_vals = np.linspace(0,20,20)
    y_vals = [math.sqrt(i) for i in x_vals]
    return x_vals, y_vals

def example_one(x_v, y_v):
    """Simple linear plot"""
    plt.plot(x_v, y_v)
    plt.show()

def example_two(x_v, y_v):
    """Naming axes and plots, colors and labels"""
    plt.xlabel("X-values")
    plt.ylabel("Y-values")
    plt.title('Example Two')
    plt.plot(x_v, y_v, color="green", label="sqrt")
    plt.legend(loc='upper center') # needed for sqrt to show
    plt.show()

def example_three(x_v, y_v):
    """Multiple line plots"""
    y2_v = x_v * 3
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('sqrts')
    plt.plot(x_v, y_v, color='green', label='green')
    plt.plot(x_v, y2_v, color='red', label='red')
    plt.legend(loc='upper center')
    plt.show()

def example_four():
    """using iris data and pandas"""
    global iris
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Legth")
    plt.title("Sepal vs Petal length")
    plt.plot(iris.sepal_length, iris.petal_length, "green")
    plt.plot(iris.sepal_width, iris.petal_width, "red")
    plt.show()

def scatter_plot():
    """scatter plot, just change to plt.scatter(...
    and add marker
    """
    global iris
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Legth")
    plt.title("Sepal vs Petal length")
    plt.scatter(iris.sepal_length, iris.petal_length,
                color="green", marker= "x")
    plt.scatter(iris.sepal_width, iris.petal_width,
                color= "red", marker="+")
    plt.show()

def bar_ploter():
    """Stacked bar plot"""
    global titanic
    plt.title("pclass Vs Fare")
    plt.xlabel("pclass")
    plt.ylabel("Fare")
    plt.bar(titanic.pclass.unique(),
            titanic.groupby(["pclass","sex"]).fare.mean().unstack().female,
            width=0.3, label=titanic.sex.unique()[0])
    plt.bar(titanic.pclass.unique(),
            titanic.groupby(["pclass","sex"]).fare.mean().unstack().male,
            width=0.3, label=titanic.sex.unique()[1])
    plt.legend(loc='upper center')
    plt.show()

def hist_ploter():
    """histogram plotter"""
    global titanic
    plt.title("Age histogram")
    #plt.title("Fare HIstogram")
    plt.hist(titanic.age)
    #plt.hist(titanic.fare)
    plt.show()

def pie_charter():
    """create pie chart"""
    global iris
    counts = iris.species.value_counts()
    plt.pie(counts, labels=iris.species.unique())
    plt.show()

def ex1_func():
    """titanic"""
    global titanic
    counts = titanic.sex.value_counts()
    plt.pie(counts,labels=titanic.sex.unique())
    plt.show()

def execute_above():
    print("Start job")
    x_v, y_v = create_sample_data()

    #Done
    #example_one(x_v, y_v)
    #example_two(x_v, y_v)
    #example_three(x_v, y_v)
    #example_four()
    #scatter_plot()
    #bar_ploter()
    #hist_ploter()
    #pie_charter()
    #ex1_func()

    #Current
    ex1_func()


if __name__ == "__main__":
    execute_above()