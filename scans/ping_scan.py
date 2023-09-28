import re
import subprocess
from datetime import datetime

from .scan import Scan


class PingScan(Scan):
    def scan(self) -> None:
        """
        Perform a ping scan on the specified target and capture the result in ms.
        """
        self.start_time = datetime.now()
        try:
            result = subprocess.run(["ping", "-c", "4", self.target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            self.output_log = result.stdout

            pattern = "r'(?<=rtt min/avg/max/mdev = [0-9.]/)', '([0-9.])'"
            match = re.search(pattern, self.output_log)

            if match:
                self.result = match.group(1)
            else:
                self.result = "Ping failed"

        except subprocess.CalledProcessError:
            self.result = "Failed to perform test"
            self.output_log = "Failed to perform test"

        self.end_time = datetime.now()
