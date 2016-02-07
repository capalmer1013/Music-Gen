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

        for i in range(offsetIndex, len(listOfNoteOffsets)):
            if listOfNoteOffsets[i] > inputNote.offset:
                nextNoteOffset = listOfNoteOffsets[i]
                break
        nextOffsetOfNotes = flatStream.getElementsByOffset(nextNoteOffset)
        nextNote = nextOffsetOfNotes.getElementsByClass(note.Note)
        closestNote = nextNote[0]
        for e in nextNote:
            if interval.notesToGeneric(inputNote, e).undirected < interval.notesToGeneric(closestNote, e).undirected:
                closestNote = nextNote[e]

        notesAtSameOffset = listOfNotes.getElementsByOffset(inputNote.offset)

        lowestNoteElement = notesAtSameOffset[0]
        for noteElement in notesAtSameOffset:
            if lowestNoteElement.pitch.frequency > noteElement.pitch.frequency:
                lowestNoteElement = noteElement

        # for element in notesAtSameOffset:
        #     # figure out the tonality here

        self.nextNoteInterval = interval.notesToGeneric(inputNote, closestNote)
        self.currentTonality = lowestNoteElement
        self.currentRhythmicDissonance = inputNote.beatStrength
        self.thisNote = inputNote
