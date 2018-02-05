import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt


def countRows(states, years):
    num_rows = 0
    for year in years:
        for state in states:
            csv_file = state + "_nat_" + year + ".csv"
            csv_name = state + "_" + year
            csv_name = pd.read_csv(csv_file)
            num_rows += csv_name.shape[0]
    print(("number of rows = ") + str(num_rows))
    return num_rows

def merge(states, years):
    merged = []
    for year in years:
        for state in states:
            csv_file = state + "_nat_" + year + ".csv"
            csv_name = state + "_" + year
            csv_name = pd.read_csv(csv_file)
            # Added a column "state"
            csv_name['state'] = state
            merged.append(csv_name)

    result = pd.concat(merged)
    result.to_csv("merged.csv")

states = ["nc", "ny", "oh", "tx", "wi"]

years = ["1933", "1939"]

countRows(states, years)

merge(states, years)

mergedData = pd.read_csv("merged.csv")

def loanAssetRatio(mergedData):
    mergedData = mergedData.assign(loanratio=(mergedData["loans"] / mergedData["assets"]))
    mergedData.to_csv("merged.csv")

loanAssetRatio(mergedData)
mergedData = pd.read_csv("merged.csv")

def bottom10(mergedData):
    mergedData = mergedData[["name", "city", "state", "loanratio"]]
    mergedData = mergedData.sort_values("loanratio")
    print ("Bottom 10 Banks for loan-ratio:")
    print (mergedData[:10])

bottom10(mergedData)

def top10Graph(mergedData):
    mergedData = mergedData[["id", "loanratio"]]
    mergedData = mergedData.sort_values("loanratio")
    mergedData = mergedData[-10:]
    print (mergedData)

    plt.figure()
    mergedData["loanratio"].plot(kind="bar")
    plt.xlabel("Bank ID")
    plt.ylabel("Loan-Asset Ratio")
    plt.title("Top 10 Banks for Loan-Asset Ratio")
    plt.show()


def top10(mergedData):
    mergedData = mergedData[["name", "city", "state", "loanratio"]]
    mergedData = mergedData.sort_values("loanratio")
    print ("Top 10 Banks for loan-ratio:")
    print (mergedData[-10:])

top10(mergedData)
top10Graph(mergedData)
