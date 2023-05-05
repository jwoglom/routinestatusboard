from dataclasses import dataclass, field
from typing import List
from .timedate import *

@dataclass
class Routine:
    name: str
    start: Time # HH:MM[am/pm]
    end: Time = None # HH:MM[am/pm]
    days: List[str] = field(default_factory=lambda: DAILY)

    def get_start(self):
        return Time.of(self.start)
    
    def get_end(self):
        if self.end:
            return Time.of(self.end)
        if self.duration:
            return Time.of(self.start).plus(Duration.of(self.duration))
