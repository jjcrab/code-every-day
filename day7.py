# https: // www.codewars.com/kata/5865cff66b5699883f0001aa/train/python
def to_time(seconds):
    hr = int(seconds/3600)
    if hr == 0:
        mi = int(seconds/60)
    if hr > 0:
        if seconds % 3600 >= 60:
            mi = int((seconds % 3600)/60)
        else:
            mi = 0

    return f"{hr} hour(s) and {mi} minute(s)"
