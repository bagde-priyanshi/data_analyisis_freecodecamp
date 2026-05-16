import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit for all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = list(range(1880, 2051))
    y_values = [res.slope * x + res.intercept for x in x_values]
    ax.plot(x_values, y_values)

    # Line of best fit from year 2000 onward
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_values_2000 = list(range(2000, 2051))
    y_values_2000 = [res_2000.slope * x + res_2000.intercept for x in x_values_2000]
    ax.plot(x_values_2000, y_values_2000)

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return ax
