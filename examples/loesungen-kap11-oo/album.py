#!/usr/bin/env python3
from datetime import date, datetime, time, timedelta
from dataclasses import dataclass
from typing import List

@dataclass()
class Track:
    title: str
    mp3name: str
    length: time
    
@dataclass()
class Album:
    title: str
    interpret: str
    tracks: List[Track]

    # Albumlänge ausrechnen
    def getTotalTime(self):
        result = timedelta(0, 0, 0)
        for t in self.tracks:
            delta = datetime.combine(date.min, t.length) - datetime.min
            result = result + delta
        return result

    # ganzes Album anzeigen
    def printInfo(self):
        print('Album:  %s' % (self.title))
        print('Von:    %s' % (self.interpret))
        print('Länge:  ', self.getTotalTime())
        print()
        n=1
        for t in self.tracks:
            print('Track %d: %s [%s]' % (n, t.title, t.length))
            n+=1

t1 = Track('Speak to Me', 'fname1.mp3', time(0, 3, 57))
t2 = Track('On the Run', 'fname2.mp3', time(0, 3, 34))
t3 = Track('Time', 'fname3.mp3', time(0, 7, 5))
a = Album('The Dark Side of the Moon', 'Pink Floyd',
          [t1, t2, t3])
a.printInfo()          
