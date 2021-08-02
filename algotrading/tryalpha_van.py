import csv
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from pandas.plotting import register_matplotlib_converters

ts = TimeSeries(key='FT8Y0BBHZIZPLSTX')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

k = open('/Users/stefan.yeung/algotrading_stefan/test.csv', 'wb')
writer_stock = csv.writer(k)
number = len(data)
datetime_list = []
price_action = []
for element in data:
    datetime_list.append(element)
    price_action.append(data[element])

for date in datetime_list:
    print(date)

df = pd.DataFrame(datetime_list, columns=["colummn"])
df.to_csv('/Users/stefan.yeung/algotrading_stefan/test.csv', index=False)

k.close()

# try and plot graph

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 1),
    datetime(2019, 5, 4),
    datetime(2019, 5, 7),
    datetime(2019, 5, 15),
    datetime(2019, 5, 19),
    datetime(2019, 5, 17),
    datetime(2019, 5, 28)
]

y = [0, 1, 3, 4, 6, 7, 5]

plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.show()