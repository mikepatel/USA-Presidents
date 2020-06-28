"""
Michael Patel
June 2020

Project description:

File description:
    Visualizing age data about USA Presidents

"""
################################################################################
# Imports
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


################################################################################
# Main
if __name__ == "__main__":
    # get data from wikipedia
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_by_age"

    df = pd.read_html(io=url, header=0)
    age_df = df[0]  # first table

    # parse data
    names = []
    ages = []
    start_dates = []

    for index, row in age_df.iterrows():
        name = str(row["President"])
        age = str(row["Age atstart of presidency"])
        if name != "President":
            names.append(name)

            age = re.sub("\xa0", " ", age)
            age, date = age.split("days")
            age, _ = age.split(" years")
            ages.append(int(age))
            start_dates.append(date)

    #print(names)
    #print(ages)
    #print(start_dates)

    # visualize
    x = range(len(names))
    x_labels = []
    for i in range(len(names)):
        #x_labels.append(names[i] + "\n" + start_dates[i])
        x_labels.append(names[i])

    colours = cm.rainbow(np.linspace(0, 1, len(names)))
    plt.style.use("dark_background")
    plt.figure(figsize=(20, 10))
    plt.bar(x, ages, color=colours, zorder=2)
    plt.title("USA Presidents' Ages")
    plt.xlabel("USA President | Inauguration Date")
    plt.xticks(x, x_labels, rotation=75, horizontalalignment="right")
    plt.xlim(left=-1, right=len(names))
    plt.ylabel("Age (years)")
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.grid(axis="y")
    #plt.show()

    # save plot
    plot_filename = "age.png"
    plot_filepath = os.path.join(os.getcwd(), plot_filename)
    plt.savefig(plot_filepath)
    plt.close()

    # sort ages
    # create df
    age_df = pd.DataFrame()
    age_df["Name"] = pd.Series(x_labels)
    age_df["Age"] = pd.Series(ages)

    # sort df
    age_df = age_df.sort_values("Age", ascending=False)
    x_labels = []
    for index, row in age_df.iterrows():
        x_labels.append(row["Name"])

    # plot df
    plt.style.use("dark_background")
    plt.figure(figsize=(20, 10))
    plt.bar(x, age_df["Age"], color=colours, zorder=2)
    plt.title("USA Presidents' Ages - Sorted")
    plt.xlabel("USA President")
    plt.xticks(x, x_labels, rotation=75, horizontalalignment="right")
    plt.xlim(left=-1, right=len(names))
    plt.ylabel("Age (years)")
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.grid(axis="y")

    # save sorted plot
    plot_filename = "age_sorted.png"
    plot_filepath = os.path.join(os.getcwd(), plot_filename)
    plt.savefig(plot_filepath)
    plt.close()
