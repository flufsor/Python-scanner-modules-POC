import json
from abc import ABC, abstractmethod


class Scan(ABC):
    """
    This abstract class represents a scan operation.

    Attributes:
        target (str): The target IP address or hostname to ping.
        start_time (datetime): The timestamp when the ping scan operation started.
        end_time (datetime): The timestamp when the ping scan operation ended.
        result (str): The formated formated result of the scan
        output_log (str): The standard output log of the ping command.
    """
    def __init__(self, target: str):
        self.target = target
        self.start_time = None
        self.end_time = None
        self.result = None
        self.output_log = None

    @abstractmethod
    def scan(self) -> None:
        """
        Perform a scan operation on the specified target and capture the result.
        """
        ...

class ScanEncoder(json.JSONEncoder):
    """
    JSON encoder for encoding Scan objects into JSON format.
    """
    def default(self, obj: object) -> dict:
        """
        Override the default method to handle encoding of Scan objects.
        """
        if isinstance(obj, Scan):
            return {
                "target": obj.target,
                "start_time": obj.start_time.isoformat() if obj.start_time else None,
                "end_time": obj.end_time.isoformat() if obj.end_time else None,
                "result": obj.result,
                "output_log": obj.output_log
            }
        return super().default(obj)