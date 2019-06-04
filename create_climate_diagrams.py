import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path
import numpy as np


"""
by morphi01
"""


    # TASK 1: Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]

basedir = Path("C:/Users/HomeBase/git/exercise-4-morphi01/data")
garmisch_dir = basedir / "produkt_klima_tag_20171010_20190412_01550.txt"
zugspitze_dir = basedir / "produkt_klima_tag_20171010_20190412_05792.txt"
# data index identification based on online source: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/
# 01550 as Garmisch-Partenkirchen in Bavaria
# 05792 as Zugspitze in Bavaria
# Date: 3rd June 2019

garmisch  = pd.read_csv(garmisch_dir, parse_dates = ["MESS_DATUM"], index_col = "MESS_DATUM", sep = ";", na_values = "-999")
zugspitze = pd.read_csv(zugspitze_dir, parse_dates = ["MESS_DATUM"], index_col = "MESS_DATUM", sep = ";", na_values = "-999")


    # TASK 2: Clip the tables to the year 2018: [1P]
    
garmisch_2018  = garmisch.loc["2018-01":"2018-12"]
zugspitze_2018 = zugspitze.loc["2018-01":"2018-12"]
# set new variable names (x_2018) to keep meta data sets (instead of overwriting var "garmisch" and var "zugspitze")


    # TASK 3: Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]
    
garmisch_agg  = garmisch_2018.resample("1M").agg({" TMK" : "mean"}).values
zugspitze_agg = zugspitze_2018.resample("1M").agg({" TMK" : "mean"}).values
# using "garmisch_2018" and "zugspitze_2018" as both "garmisch" and "zugspitze" would have been clipped by now (in TASK 2)
# to_list() does not work as DataFrame has not 'to_list' attribute .. whatever that means
# .values returns the monthly averages of temperatures as list; values are in chronological order (Jan to Dez)


    # TASK 4: Define a plotting function that draws a simple climate diagram
    # Add the arguments as mentioned in the docstring below [1P]
    # Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]

garmisch_agg1  = garmisch_2018.resample("1M").agg({" TMK" : "mean", " RSK" : "mean"})
zugspitze_agg1 = zugspitze_2018.resample("1M").agg({" TMK" : "mean", " RSK" : "mean"})
# adding mean of RSK to the data frame
# column names identified via online source: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/recent/DESCRIPTION_obsgermany_climate_daily_kl_recent_en.pdf

garmisch_agg1 = garmisch_agg1.rename(columns={' TMK': 'TMK'})
garmisch_agg1 = garmisch_agg1.rename(columns={' RSK': 'RSK'})
zugspitze_agg1 = zugspitze_agg1.rename(columns={' TMK': 'TMK'})
zugspitze_agg1 = zugspitze_agg1.rename(columns={' RSK': 'RSK'})
#print(garmisch_agg1.columns)
#print(zugspitze_agg1.columns)
# renaming column names since nothing works with spaces



x = 0
y = zugspitze_agg1

def create_climate_diagram(df = garmisch_agg1, temp_col = "TMK", prec_col = "RSK", 
                           title = "Klimadiagramm Garmisch Partenkirchen", filename = "Climate_Diagram", temp_min = "-15",
                           temp_max = "20", prec_min = "0", prec_max = "370"):
    
    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

    label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    index = np.arange(len(label))
    
        # TASK 4.1: Draw temperature values as a red line and precipitation values as blue bars: [1P]
        # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
        # x-axis labels (month shortnames).

    ax2.bar(index, garmisch_agg1.RSK, color = "blue")
    ax1.plot(index, garmisch_agg1.TMK, color = "red")
    plt.xticks(index, label, fontsize=5, rotation=30)
    
        # TASK 4.2: Set appropiate limits to each y-axis using the function arguments: [1P]

    ######################################################################################
    
        # TASK 4.3: Set appropiate labels to each y-axis: [1P]

    ax2.set_ylabel("Niederschlagsfaktor")
    ax1.set_ylabel("Temperatur")
        
        # TASTK 4.4: Give your diagram the title from the passed arguments: [1P]
       
    plt.title(title) 
    
        # TASK 4.5: Save the figure as png image in the "output" folder with the given filename. [1P]
        
    ######################################################################################
    return fig

    

plt.show(create_climate_diagram(garmisch_agg1))
 


    # TASK5: Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
    
create_climate_diagram(...)#######################
create_climate_diagram(...)#######################

