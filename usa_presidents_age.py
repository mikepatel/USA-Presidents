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
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_by_age"

    with urllib.request.urlopen(url) as response:
        page = response.read()

    page = re.sub('<!--|-->', "", str(page))

    # html soup
    soup = BeautifulSoup(page, "html.parser")
    
