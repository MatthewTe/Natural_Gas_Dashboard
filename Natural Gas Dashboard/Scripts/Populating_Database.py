# Importing the necessary packages:
import requests
import pandas as pd
import xlrd
import bs4
import lxml
from lxml import html
import csv
import sqlite3

# Declaring the constants: URl and File Path:
url = "https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm"

path = "C:\\Users\\Matthew Teelucksingh\\Desktop\\Projects\
 Repository\\Python Projects\\Natural Gas Dashboard\\Natural Gas Dashboard\\Database"

def nat_gas_populate(path):
    page = requests.get(url)
    page.raise_for_status()
    # Parsing the HTML with the BeautifulSoup package:
    gas_prices = bs4.BeautifulSoup(page.text)
    # Searching the HTML for the .xls download link:
    # Appending each href link into a seachable list:
    counter = 0
    href_list = []
    for a in gas_prices.find_all('a', href=True):
        #print(a['href'])
        href_list.append(a['href'])

    # Creating a for loop that seraches the href_list for the string containing
    # the '.xls' href link:
    for i in href_list:
        if ".xls" in href_list[counter]:
            download_link = href_list[counter].replace('..','')
        else:
            counter = counter + 1
    # Now that we have collected the link, we need to acess the full weblink
    # by appending the full url onto the href link:
    download_link = 'https://www.eia.gov/dnav/ng' + download_link


    # Dowloading the data into a pandas data frame using the download_link:
    df = pd.read_excel(download_link, sheetname=1)
    # Formatting the Excel sheet into a format that can be written as a .csv:
    df = df[2:-1] # Removing unnecessary headers
    df.columns = ['Date', 'Dollars_per_Million_Btu'] # Renaming columns
    df = df.set_index(df['Date']) # Setting the datetime index
    df = df['Dollars_per_Million_Btu'] # Removing the now redundant 'Date' column
    #print(df)


    # Writing this dataframe into the \Database local path as a .csv file:
    df.to_csv( path + '\\Nat_Gas_prices.csv' )

nat_gas_populate(path)
