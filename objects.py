from music21 import *
class rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = -1

    def getFloat(self):
        return float(self.numerator)/float(self.denominator)


class myNote:
    def __init__(self, inputNote, flatStream ):
        self.note = inputNote.name
        listOfNotes = flatStream.getElementsByClass(note.Note)
        notesAtSameOffset = [] # this will be for determining the tonality
        listOfNoteOffsets = [] # this will be for finding the next note
        offsetMapStream = flatStream.offsetMap

        for element in listOfNotes:
            listOfNoteOffsets.append(element.offset)
        listOfNoteOffsets.sort()
        offsetIndex = listOfNoteOffsets.index(inputNote.offset)

        for element in listOfNotes:
            if element.offset == inputNote.offset:
                notesAtSameOffset.append(element)

        for element in notesAtSameOffset:
            # figure out the tonality here
            



        self.nextNoteInterval
        self.currentTonality
        self.currentRhythmicDissonance
        self.thisNote = inputNote
