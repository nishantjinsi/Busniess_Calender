import pandas as pd
import numpy
index = pd.date_range('01-01-1970', '31-12-2015', freq='B')

year = list(index.year)
day = list(index.day)
week = list(index.week)
month = list(index.month)
qtryear = list(index.quarter)

busiend = index.shift(1,freq='BM')
previousend = index.shift(-1, freq='BM')
busiendqtr = index.shift(1,freq = 'BQ')
previousbusiendqtr = index.shift(-1, freq = 'BQ')
data = {'Date': index.day,
        'Week': week,
        'Month':month,
        'Quater':qtryear,
        'BusinessEndOfMonth':busiend,
        'PreviousBusinessEndOfMonth':previousend,
        'BusinessEndOFQuater': busiendqtr,
        'PreviousBusinessEndOfQuarter':previousbusiendqtr
        }
frame = pd.DataFrame(data )
frame
frame.to_csv('dim_Date.csv', sep=',')