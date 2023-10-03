from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import yfinance as yfin

yfin.pdr_override()

print(f'Hello! This program will show you the trends and correlation between stocks you provide it!\n')

date_entry = input(f'Please enter a start date in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
start = dt.datetime(year, month, day)
end = dt.datetime.now()

input_str = input(f"Enter a list of tickers separated by spaces: ")
tickers = input_str.split()
colnames = []

for ticker in tickers:
    data = pdr.get_data_yahoo(ticker, start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data["Adj Close"])
    colnames.append(ticker)
    combined.columns = colnames

# print(combined)

plt.yscale("log")

for ticker in tickers:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")
plt.show()

corr_data = combined.pct_change().corr(method="pearson")
sns.heatmap(corr_data, annot=True, cmap="coolwarm")
plt.show()