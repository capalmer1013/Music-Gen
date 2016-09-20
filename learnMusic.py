import networkx as nx
import rhythmGraph
import chordGraph
import filestream

titanium = "David_Guetta_Feat._Sia_-_Titanium_Piano.xml"
bach = "Minuet-in-G-Minor.xml"
goldberg = 'Goldberg_Variations.xml'
clavier = 'Prelude_I_in_C_major_BWV_846_-_Well_Tempered_Clavier_First_Book.xml'

# this will need uncommented in the future
'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print "learn-music requires exactly 1 filename as an argument"
'''

filename = bach

# flatStream = filestream.getFlatStream(filename)
flatStream = filestream.getStream(filename).parts.elements[0].flat
# make rhythm graph
G = nx.DiGraph()
rhythmMatrix = rhythmGraph.createRhythmGraph(flatStream)
states = rhythmGraph.getRhythmicStates(flatStream)

# make chord graph
chordMatrix = chordGraph.createChordGraph(flatStream)

noteGraph, noteStates = chordGraph.createNoteGraph(flatStream)


