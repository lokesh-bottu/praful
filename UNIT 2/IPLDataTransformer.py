import csv

class IPLDataTransformer:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    def load_data(self, csv_file):
        with open(csv_file, mode='r') as file:
            data = list(csv.DictReader(file))
        return data

    def matches_won_per_year(self):
        matches_count = {}
        for row in self.data:
            year = row["season"]
            if year not in (matches_count.keys()):
                matches_count[year] = {}
            matches_count[year][row["winner"]] = matches_count[year].get(row["winner"],0) +1

        return matches_count