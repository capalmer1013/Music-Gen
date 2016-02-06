import sys
import filestream
import musicAttributes
from music21 import *

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "learn-music requires exactly 1 filename as an argument"

flatStream = filestream.getFlatStream(filename)

musicAttributes.getTimeSignatures(flatStream)
