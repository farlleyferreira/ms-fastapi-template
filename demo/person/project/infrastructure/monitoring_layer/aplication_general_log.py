import logging
import logzero


class Log(object):
    def __init__(self):
        """
            Custom log class implementation
            this class implement a logzero custom log
        """
        logzero.logfile(
            filename="./project/logs/logfile.log",
            formatter=logging.Formatter(
                '%(filename)s - %(asctime)s - %(levelname)s: %(message)s'
            )
        )

        self.record = logzero.logger
