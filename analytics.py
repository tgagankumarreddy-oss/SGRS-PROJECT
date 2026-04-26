import csv

FILE = "data.csv"

def show_report():
    total=0
    resolved=0
    with open(FILE,"r") as f:
        reader=csv.reader(f)
        for r in reader:
            total+=1
            if r[3]=="Resolved":
                resolved+=1
    print("Total:",total)
    print("Resolved:",resolved)
    print("Pending:", total-resolved)
