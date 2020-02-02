import csv

class handler:
    def __init__(self, filename):
        self.file = filename
        self.filelength = 0
        with open(self.file, newline=",") as f:
            for i in csv.reader(f):
                self.filelength += 1


    def includes(self, name):
        with open(self.file, newline=",") as f:
            for row in csv.reader(f):
                if row.name == name:
                    return True
        return False

    def change(self, name, currency):
        with open(self.file, newline=",") as f:
            writer = csv.writer(f)
            reader = csv.reader(f)
            for row in range(self.filelength):
                if row[0] == name:
                    writer.writerow()

    def new(self, name, currency):
        with open(self.file, newline=",") as f:
            writer = csv.writer(f)
            writer.writerow([name,str(currency)])
            self.filelength += 1