class SampleFormat(object):
    def __init__(self, features, types):
        self.features = features
        self.types = types

    def parse(self, data):
        if len(data) is not len(self.features):
            print "Malformed sample: not enough features"
            return None
        features = dict()
        for i in range(len(self.features)):
            if data[i] is not None:
                features[self.features[i]] = self.types[i](data[i])
            else:
                features[self.features[i]] = None
        return Sample(features)


class ClassifiedSampleFormat(SampleFormat):
    def __init__(self, features, types, classification_feature):
        super(ClassifiedSampleFormat, self).__init__(features, types)
        self.classification_feature = classification_feature

    def parse(self, data):
        sample = super(ClassifiedSampleFormat, self).parse(data)
        classification = sample.feature(self.classification_feature)
        features = dict(sample.features)
        del features[self.classification_feature]
        return ClassifiedSample(features, classification)


class Sample(object):
    def __init__(self, features):
        self.features = features

    def feature(self, feature):
        return self.features[feature]


class ClassifiedSample(Sample):
    def __init__(self, features, classification):
        super(ClassifiedSample, self).__init__(features)
        self.classification = classification