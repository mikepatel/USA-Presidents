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
import matplotlib.ticker as ticker
import matplotlib.animation as animation


################################################################################
# Main
if __name__ == "__main__":
    """
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
    df = age_df
    df.to_csv(os.path.join(os.getcwd(), "pres.csv"), index=False)

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
    """

    # Racing bar chart of US Pres' ages
    df = pd.read_csv(os.path.join(os.getcwd(), "pres.csv"))

    # create plot figure
    fig, ax = plt.subplots(figsize=(15, 10))

    # function to be called repeatedly to draw on canvas
    def draw_chart(frame):
        # rank oldest > youngest
        df = pd.read_csv(os.path.join(os.getcwd(), "pres.csv"))
        df["Rank"] = df["Age"].rank(method="first", ascending=True)
        df = df.sort_values(by="Rank", ascending=False)
        df = df.reset_index(drop=True)

        ax.clear()
        ax.barh(df["Rank"], df["Age"])
        [spine.set_visible(False) for spine in ax.spines.values()]  # remove border around figure
        ax.get_xaxis().set_visible(False)  # hide x-axis
        ax.get_yaxis().set_visible(False)  # hide y-axis

        for index, row in df.iterrows():
            ax.text(x=0, y=row["Rank"], s=row["Name"], ha="right", va="center")
            ax.text(x=row["Age"], y=row["Rank"], s=row["Age"], ha="left", va="center")

    # colours = cm.rainbow(np.linspace(0, 1, len(df)))
    #ax.tick_params(length=0)  # remove x-axis tick marks

    animator = animation.FuncAnimation(fig, draw_chart, frames=range(len(df)))
    animator.save("presidents.gif", writer="imagemagick")

    quit()

    # concatenate index + Name
    x_labels = []
    for index, row in df.iterrows():
        x_labels.append(str(index+1) + " " + row["Name"])

    #print(df)  # not sorted, Wash > Trump
    #plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(15, 10))

    #ax.grid(True, axis='x', color='white')
    ax.tick_params(length=0)  # remove x-axis tick marks
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]  # remove border around figure
    ax.get_xaxis().set_visible(False)  # hide x-axis

    colours = cm.rainbow(np.linspace(0, 1, len(df)))
    ax.barh(x_labels, df["Age"], color=colours)

    # add text onto bars
    for index, row in df.iterrows():
        ax.text(x=row["Age"], y=index, s=row["Age"], ha="left", va="center")

    plt.show()  # plots up to Trump
