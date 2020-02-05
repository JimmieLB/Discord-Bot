import csv

class Handler:
    def __init__(self, filename):
        self.file = filename
        self.filelength = 0
        with open(self.file, newline="") as f:
            for i in csv.reader(f):
                self.filelength += 1

    def balance(self, name):
        with open(self.file, newline="") as f:
            for row in csv.reader(f):
                if row["name"] == name:
                    return row["currency"]
        return 0

    def includes(self, name):
        with open(self.file, newline="") as f:
            for row in csv.reader(f):
                if row["name"] == name:
                    return True
        self.new(name,0)
        return False
    
    def change(self, name, currency):
        with open(self.file, newline="") as f:
            writer = csv.writer(f)
            for row in range(self.filelength):
                if row["name"] == name:
                    writer.writerow([name,str(currency)])
    
    def new(self, name, currency):
        with open(self.file, newline="") as f:
            writer = csv.writer(f)
            writer.writerow({"name" : name,"currency" : currency})
            self.filelength += 1