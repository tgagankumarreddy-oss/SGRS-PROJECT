import csv

FILE = "data.csv"

def resolve_grievance():
    gid = int(input("Enter ID: "))
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))

    if gid < len(rows):
        rows[gid][3]="Resolved"
        print("Resolved")
    else:
        print("Invalid")

    with open(FILE,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(rows)
