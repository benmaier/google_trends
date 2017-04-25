
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import calendar
import time


from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif' # ... for regular text
rcParams['font.sans-serif'] = ['Helvetica'] #, Avant Garde, Computer Modern Sans 
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42

rcParams['xtick.major.pad'] = '8'
rcParams['lines.solid_capstyle'] = 'butt'

# Dates have been removed from the data
dates = pd.read_csv("data/dates_hourly.csv", names=["date"], parse_dates=[0])["date"].tolist()

# Helper function for reading Google trends data
def read_csv(input_filepath, delimiter):
  return pd.read_csv(input_filepath, delimiter=delimiter, header=0)

# Currently only works for two-dimensional embeddings
def plot_series(data, input_filepath, keyword, save_output = True):
  #data['date'] = [date.astype('datetime64[ns]') for date in dates]
  data['date'] = dates

  fig = plt.figure()
  ax = fig.add_subplot(111)
  
  ax.set_ylabel(r"Relative Search Interest")
  ax.set_xlabel(r"Time")

  ax.plot_date(data['date'].values, data[keyword].values, color="blue", ls="solid", ms=2)  
  plt.xticks(rotation=45)
  #ax.plot_date(range(len(data[keyword].values)), data[keyword].values, color="k", ls="solid", ms=2)

  plt.ylim(0, 100)
  fig.tight_layout()

  if save_output:
    plt.savefig("{0}.png".format(input_filepath+".trend")) 

  return [data['date'].values, data[keyword].values]

# Currently only works for two-dimensional embeddings
def plot_embedding(embedded, input_filepath, dimensions, save_output = True):
  x = [row[dimensions[0]] for row in embedded]
  y = [row[dimensions[1]] for row in embedded]

  fig = plt.figure()
  ax = fig.add_subplot(111)
  
  if dimensions[0] == 0:
    ax.set_ylabel(r"$x(t)$")
  elif dimensions[0] == 1:
    ax.set_ylabel(r"$x(t+\tau)$")  
  else:  
    ax.set_ylabel(r"$x(t+{0}*\tau)$".format(dimensions[0]))

  if dimensions[1] == 0:
    ax.set_xlabel(r"$x(t)$")
  elif dimensions[1] == 1:
    ax.set_xlabel(r"$x(t+\tau)$")
  else:
    ax.set_xlabel(r"$x(t+{0}*\tau)$".format(dimensions[1]))
  
  plt.scatter(y, x, s=4, color="blue")

  plt.xlim(0, 100)
  plt.ylim(0, 100)

  if save_output:
    plt.savefig("{0}.png".format(input_filepath+".embed")) 