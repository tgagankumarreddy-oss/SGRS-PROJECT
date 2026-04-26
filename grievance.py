import csv

FILE = "data.csv"

def add_grievance(data):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print("Added")

def view_grievances():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            print(i, row)

def track_grievance():
    gid = int(input("Enter ID: "))
    with open(FILE,"r") as f:
        rows=list(csv.reader(f))
        if gid < len(rows):
            print(rows[gid])
        else:
            print("Not found")
