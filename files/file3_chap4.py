import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

sns.set_style("darkgrid")
"""
Introduction to seaborn
"""

iris = sns.load_dataset('iris')
titanic = sns.load_dataset('titanic')
tips = sns.load_dataset('tips')

def dist_ploter():
    """Plots distribution of the column """
    sns.distplot(tips.total_bill)
    plt.plot
    plt.subplot(5,1,1)
    plt.show()

def joint_plot():
    """plots joint distributions, has more types too"""
    #sns.jointplot(tips.total_bill, tips.tip)
    sns.jointplot(tips.total_bill, tips.tip, kind="kde")
    plt.show()

def barploter():
    """create barplots of two columns easily"""
    group = titanic.pclass.unique()
    hue = titanic.groupby(["pclass","sex"]).fare.mean().reset_index().sex.unique()
    gh_zip = [str(g) + "_" + str(h) for g in group for h in hue]
    sns.barplot(gh_zip,
                titanic.groupby(["pclass","sex"]).fare.mean().values)
    plt.show()

def barplotter2():
    """
    need to create side by side charts
    """
    dat = titanic.groupby(["pclass","sex"]).fare.mean().reset_index()
    sns.barplot("pclass","fare",hue="sex", data=dat)
    plt.show()

def barplotter3():
    "side by side barplots"
    dat = titanic.groupby(["pclass","sex","embarked"]).fare.mean().reset_index()
    sns.catplot("pclass","fare",hue="sex", col="embarked", data=dat, kind="bar")
    plt.show()

def countploter():
    """simple count plot"""
    sns.countplot(titanic.pclass, hue="sex", data=titanic)
    plt.show()

def heatmapper():
    """
    simple heat map
    """
    corr_values = titanic.corr()
    sns.heatmap(corr_values, annot=True)
    plt.show()

def pairgridder():
    """
    create relationships between variables using different types of charts
    """
    pgrids = sns.PairGrid(tips)
    pgrids.map_diag(sns.distplot)
    pgrids.map_upper(sns.kdeplot)
    pgrids.map_lower(plt.scatter)
    plt.show()

def start_execution():
    #dist_ploter()
    #joint_plot()
    #barploter()
    #barplotter2()
    #barplotter3()
    #countploter()
    #heatmapper()
    pairgridder()

if __name__ == "__main__":
    start_execution()
