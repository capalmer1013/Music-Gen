from music21 import *


def getTimeSignatures(flatStream):
    timeSignatures = flatStream.getElementsByClass(meter.TimeSignature)
    for i in timeSignatures:
        print i
    # return a dict indexed by each measure with time changes