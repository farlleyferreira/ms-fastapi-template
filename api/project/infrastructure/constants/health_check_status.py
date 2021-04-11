import enum


class Status(enum.Enum):
    """
        Enumerator of status
    """
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class Health(enum.Enum):
    """
        Enumerator of health status
    """
    success = Status.GREEN, "It's all fine! Shine On You Crazy Diamond!!"
    warning = Status.YELLOW, "WARNING: We have one or more problem," + \
        " check logfiles please!!!"
    danger = Status.RED, "Ops!!! houston we have a problem!!! " + \
        "A huge problem!!! check all drivers connection!!!"
