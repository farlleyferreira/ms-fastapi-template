import enum


class SystemStatus(enum.Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class ApiHealth(enum.Enum):
    success = SystemStatus.GREEN, "It's all fine, good job!"
    warning = SystemStatus.YELLOW, "WARNING: We have one or more problem," + \
        " check logfiles please!!!"
    danger = SystemStatus.RED, "Ops!!! houston we have a problem!!! " + \
        "A huge problem!!! check all drivers connection!!!"
