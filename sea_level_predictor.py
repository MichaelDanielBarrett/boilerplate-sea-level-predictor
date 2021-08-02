import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051), reg[0]*range(1880, 2051) + reg[1])

    # Create second line of best fit
    reg2 = linregress(x=df[df['Year'] > 1999]['Year'], y=df[df['Year'] > 1999]['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051), reg2[0]*range(2000, 2051) + reg2[1])

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()