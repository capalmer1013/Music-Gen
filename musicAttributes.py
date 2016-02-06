from music21 import *
import sys


def getTimeSignatures(flatStream):

    dictOfTimeSigs = {}
    timeSignatures = flatStream.getElementsByClass(meter.TimeSignature)

    for i in timeSignatures:
        if i.offset in dictOfTimeSigs:
            if dictOfTimeSigs[i.offset].ratioString != i.ratioString:
                print "Time signature errors. Multiple time signatures in the same measure"
                sys.exit()
        else:
            dictOfTimeSigs[i.offset] = i

    return dictOfTimeSigs
    # return a dict indexed by each measure with time changes

