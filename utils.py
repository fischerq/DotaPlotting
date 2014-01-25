import csv
from samples import SampleFormat

COLUMNS = 0
ROWS = 1


def parse_csv(filename, sample_format, parse_type=COLUMNS):
    result = {}
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        header = reader.next()
        for i in range(len(header)):
            header[i] = header[i].strip()
            if header[i] not in sample_format.features:
                print "row not specified as feature: "+header[i]

        if parse_type is ROWS:
            for row in reader:
                result.append(sample_format.parse(row))
        else:
            for feature in sample_format.features:
                result[feature]=[]
            for row in reader:
                row = sample_format.parse(row)
                for feature in sample_format.features:
                    result[feature].append(row.feature(feature))
        return result