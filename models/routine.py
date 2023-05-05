from dataclasses import dataclass, field, asdict
from typing import List
import base64
from .timedate import *

@dataclass
class Routine:
    name: str
    start: Time # HH:MM[am/pm]
    end: Time = None # HH:MM[am/pm]
    days: List[str] = field(default_factory=lambda: DAILY)
    sticky: bool = False
    sticky_for: Duration = None # 0h0m

    def get_start(self):
        return Time.of(self.start)
    
    def id(self) -> str:
        inp = '%s-%s:%s' % (self.name, self.start.hour, self.start.min)
        return base64.b64encode(inp.encode()).decode()

    def to_json(self):
        d = asdict(self)
        d['id'] = self.id()
        return d
