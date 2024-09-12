class DeviceError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.msg = msg


# Raises an exception (multiple arguments)
raise DeviceError(1, "Not Responding")
