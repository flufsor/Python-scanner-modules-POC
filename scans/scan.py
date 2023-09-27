from abc import ABC, abstractmethod
import json

class Scan(ABC):
    def __init__(self, target: str):
        self.target = target
        self.start_time = None
        self.end_time = None
        self.result = None
        self.output_log = None

    @abstractmethod
    def scan(self):
        pass

class ScanEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Scan):
            return {
                "target": obj.target,
                "start_time": obj.start_time.isoformat() if obj.start_time else None,
                "end_time": obj.end_time.isoformat() if obj.end_time else None,
                "result": obj.result,
                "output_log": obj.output_log
            }
        return super().default(obj)