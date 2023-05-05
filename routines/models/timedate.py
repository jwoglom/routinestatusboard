from dataclasses import dataclass

MON = 'MON'
TUE = 'TUE'
WED = 'WED'
THU = 'THU'
FRI = 'FRI'
SAT = 'SAT'
SUN = 'SUN'

DAILY = [MON, TUE, WED, THU, FRI, SAT, SUN]
WEEKDAYS = [MON, TUE, WED, THU, FRI]
WEEKENDS = [SAT, SUN]

@dataclass
class Time:
    hour: int
    min: int

    @staticmethod
    def of(inp):
        if type(inp) == Time:
            return inp

        if type(inp) == int:
            hour = inp//100
            min = inp%100
            return Time(hour, min)

        parts = inp.split(':')
        if len(parts) != 2:
            if inp.endswith('pm'):
                parts = [inp.removesuffix('pm'), '0pm']
            elif inp.endswith('am'):
                parts = [inp.removesuffix('am'), '0am']
            else:
                parts = [inp, '0']

        hour = int(parts[0])
        if parts[1].endswith('pm') and hour != 12:
            hour += 12
        elif parts[1].endswith('am') and hour == 12:
            hour = 0
        
        min = int(parts[1].removesuffix('am').removesuffix('pm'))

        return Time(hour, min)

    def plus(self, dur):
        hrs = self.hour + dur.hours
        mins = self.min + dur.mins
        return Time(hrs + mins//60, mins%60)


@dataclass
class Duration:
    hours: int = 0
    mins: int = 0
    
    @staticmethod
    def of(inp):
        if type(inp) == Duration:
            return inp

        mins = 0
        cnum = ''
        for c in inp:
            if '0' <= c <= '9':
                cnum += c
            elif c == 'm':
                mins += int(cnum)
                cnum = ''
            elif c == 'h':
                mins += int(cnum)*60
                cnum = ''
        
        return Duration(mins//60, mins%60)
