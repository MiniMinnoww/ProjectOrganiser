import tile
import random
# A place to generate unique IDs.
def get_uid():
    UIDs = []
    for _tile in tile.tiles:
        UIDs.append(_tile.UID)
    randomID = random.randint(0, 1000000000)
    while randomID in UIDs:
        randomID = random.randint(0, 1000000000)
        print("1 in a billion chance!?!?")
    return randomID