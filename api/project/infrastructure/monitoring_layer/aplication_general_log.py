import logging
import logzero


class Log:
    def __init__(self):
        """[summary]
        """
        logzero.logfile(
            filename="./project/logs/logfile.log",
            formatter=logging.Formatter(
                '%(filename)s - %(asctime)s - %(levelname)s: %(message)s'
            )
        )
        self.record = logzero.logger
