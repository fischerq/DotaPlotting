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


def combine_features(features):
    result = []
    for i in range(0, len(features[0])):
        entry=()
        for j in range(0,len(features)):
            entry = entry + (features[j][i],)
        result.append(entry)
    return result


def filter_samples(samples, check, format=COLUMNS):
    result = []
    if format is ROWS:
        for sample in samples:
            if check(sample):
                result.append(sample)
    else:
        result = {}
        for col in samples.keys():
            result[col] = []
        for i in range(0, len(samples[samples.keys()[0]])):
            sample = []
            for col in samples.keys():
                sample.append(samples[col][i])
            if check(sample):
                for col in samples.keys():
                    result[col].append(samples[col][i])
    return result