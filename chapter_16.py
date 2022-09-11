class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

def maketime(hour, minute, second):
    """Returns a Time object with attributes hour, minute and second.

    hour: num
    minute: num
    second: num

    returns: Time"""

    time = Time()

    time.hour = hour
    time.minute = minute
    time.second = second

    return time

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """

    if time.hour < 0 or time.minute < 0  or time.second < 0:
        return False

    if time.minute >= 60 or time.second >= 60:
        return False

    return True

def print_time(t):
    """Takes a Time object and prints it in the form hour:minute:second

    t: Time
    """

    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    """Returns True if t1 follows t2 chronologically and False otherwise.

    t1: Time
    t2: Time

    returns: boolean
    """

    assert valid_time(t1) and valid_time(t2)

    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def time_to_int(t):
    """Returns a given Time object as a number of seconds.

    t: Time

    returns: num
    """

    assert valid_time(t)

    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second

    return seconds

def int_to_time(seconds):
    """Returns a given number of seconds as a Time object.

    seconds: num

    returns: Time
    """

    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)

    return t

def increment(t1, increment):
    """Takes a Time object and returns a new one that is equivalent to the original,
    except incremented by a given number of seconds.

    t1: Time
    increment: num

    returns: Time
    """

    assert valid_time(t1)

    seconds = time_to_int(t1)
    seconds += increment
    t2 = int_to_time(seconds)

    return t2

if __name__ == "__main__":

    t1 = maketime(13, 59, 30)
    t2 = maketime(12, 59, 30)

    print_time(t1)