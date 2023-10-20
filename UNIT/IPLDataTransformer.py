import csv

class IPLDataTransformer:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    def load_data(self, csv_file):
        with open(csv_file, mode='r') as file:
            data = list(csv.DictReader(file))
        return data

    def matches_per_year(self):
        matches_count = {}
        for row in self.data:
            year = row['season']
            if year in matches_count:
                matches_count[year] += 1
            else:
                matches_count[year] = 1
        return matches_count
