import pandas as pd
import os
from datetime import date

# This is the main function that calls other functions and provides an order to the application for easier debugging.
def main():

# The date function below currently is not used, but I was thinking it might be handy for the final output file so you can sort by date if you need to double-check something.
    today = date.today()
    todayDate = today.strftime('%m/%d/%Y')

# The functions below will return data to be used by other functions. Your function that 
    formInfo = processForm()
    validateURL(formInfo)

# This function reads the URLForm Excel file into a pandas dataframe and converts the URL and Submitter email columns into a dictionary and returns it for the next function.
def processForm():
    URLForm = pd.read_excel('URLForm.xlsx')
    formURLs = URLForm.set_index('URL').to_dict()['Submitter email']

    return formURLs

# This function compares info from the returned dictionary to the output file and creates a list of unique URLs for processing.
def validateURL(formInfo):
    newURLs = []
    urlFile = pd.read_csv('urls.csv')
    parentURLs = urlFile['Parent URL'].values.tolist()
    for key in formInfo:
         if key in parentURLs:
             continue
         else:
            newURLs.append(key)

if __name__ == "__main__":
    main()
