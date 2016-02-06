import sys
import graphs
import filestream
import musicAttributes
from music21 import *

titanium = "David_Guetta_Feat._Sia_-_Titanium_Piano.xml"
bach = "Minuet-in-G-Minor.xml"

# this will need uncommented in the future
'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "learn-music requires exactly 1 filename as an argument"
'''

filename = bach

flatStream = filestream.getFlatStream(filename)

# make rhythm graph
graphs.createRhythmGraph(flatStream)

# make chord graph

# make soprano graph

# make bass graph