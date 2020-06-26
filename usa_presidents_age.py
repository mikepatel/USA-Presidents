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
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool


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
            print(age)
            age, date = age.split("days")
            age, _ = age.split(" years")
            ages.append(age)
            start_dates.append(date)

    print(names)
    print(ages)
    print(start_dates)

