import csv
from samples import SampleFormat


def parse_csv(filename, sample_format):
    result = []
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        header = reader.next()
        for i in range(len(header)):
            header[i] = header[i].strip()
            if header[i] not in sample_format.features:
                print "row not specified as feature: "+header[i]

        for row in reader:
            result.append(sample_format.parse(row))
        return result