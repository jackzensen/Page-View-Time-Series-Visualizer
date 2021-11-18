import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
# Clean data
df['date'] = pd.to_datetime(df['date'])
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]
cleaned = df.copy()


def draw_line_plot():
    # Draw line plot
    fig, _ = plt.subplots()
    plt.plot(cleaned['date'], cleaned['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)  
    df_bar['year']=pd.DatetimeIndex(df_bar['date']).year
    df_bar['month']=pd.DatetimeIndex(df_bar['date']).month_name()
    df_bar_group = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    fig = sns.catplot(x="year", y="value", hue="month", height = 10, 
                data=df_bar, saturation=.5, 
                kind="bar", ci=None, aspect=.6, legend=True, hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.ylabel("Average Daily Views")
    fig.set_axis_labels("Years", "Average Daily Views", )



    # Save image and return fig (don't change this part)
    fig.figure.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 15))
    axs[0] = sns.boxplot(x="Year", y="value",
                data=df_box, saturation=.5, ax=axs[0])
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_ylabel("Page Views")

    axs[1] = sns.boxplot(x="Month", y="value",
                data=df_box, saturation=.5, ax = axs[1], order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_ylabel("Page Views")

    # fig.set_axis_labels("Years", "Average Daily Views", )
    # axs[1].set_title('Month-wise Box Plot (Seasonality')
    # axs[1].boxplot(x="month", y="value",
    #             data=df_box, saturation=.5,
    #             kind="box", aspect=.7, )
    # fig.set_axis_labels("Months", "Average Daily Views", )


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
