import pandas as pd

# Declaring the global variable as the path to the \\Database folder on local machine:
nat_gas_csv = 'C:\\Users\\Matthew Teelucksingh\\Desktop\\Projects Repository\
\\Python Projects\\Natural Gas Dashboard\\Natural Gas Dashboard\\Database\\Nat_Gas_prices.csv'

"""
MODULE NAME: gas_prices():
FUNCTION: The module accesses the \\Database folder on the local machine and
reads the .csv file containing historical nat gas prices and returns the .csv file
as a dataframe for use in other scripts and modules
OUTPUT: returns pandas dataframe
"""
def gas_prices():
    # Creating a dataframe that contains the historical nat gas price data from the
    # \\Database folder:
    df = pd.read_csv(nat_gas_csv, parse_dates=True)

    # Formatting the .csv file correctly:
    df.columns = ['Date', 'Dollars_per_Million_Btu'] # naming the columns
    df['Date'] = pd.to_datetime(df['Date']) # Converting the dates into datetime
    df = df.set_index(df['Date']) # setting the date time index
    df = df['Dollars_per_Million_Btu'] # Dropping the now redundant 'Date' column
    return df

gas_prices()
