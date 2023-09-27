import subprocess
from datetime import datetime

from .scan import Scan


class PingScan(Scan):
    def scan(self):
        self.start_time = datetime.now()
        try:
            result = subprocess.run(["ping", "-c", "4", self.target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            self.output_log = result.stdout

            if "0% packet loss" in self.output_log:
                self.result = "stable connection"
            else:
                self.result = "unstable connection"

        except subprocess.CalledProcessError:
            self.result = "Failed to perform test"
            self.output_log = "Failed to perform test"

        self.end_time = datetime.now()
