
#  Former Employees

- Using SQLAlchemy and Flask, design the tables to hold the data from the CSV files, import the CSV files into a SQL database, and perform data modeling, data engineering, and data analysis.

## Dependencies and Setup

```bash
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import scipy.stats as st
from flask import Flask, jsonify


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
```


## Roadmap

### Part one
- Filter the database by the most recent 12 months, only loading the date and prcp values into a new dataframe

- Plot the results by using the dataframe
![App Screenshot](https://raw.githubusercontent.com/gnimeth/Hawaii_climate/main/Output/Screenshot_20230205_052613.png)

- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id
![App Screenshot](https://raw.githubusercontent.com/gnimeth/Hawaii_climate/main/Output/Screenshot_20230205_052723.png)

- Design a query to get the previous 12 months of temperature observation (TOBS) data

- Plot the results as a histogram
![App Screenshot](https://raw.githubusercontent.com/gnimeth/Hawaii_climate/main/Output/Screenshot_20230205_052651.png)

### Part two

- Design a Flask API based on the queries, with three routes

![App Screenshot](https://raw.githubusercontent.com/gnimeth/Hawaii_climate/main/Output/Screenshot_20230205_052751.png)
## Acknowledgements

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1
