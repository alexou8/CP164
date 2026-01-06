"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-12"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

years = [1600, 1899, 1900, 1901, 1996, 2000, 2004]

for year in years:
    leap_year = is_leap_year(year)
    print(leap_year)