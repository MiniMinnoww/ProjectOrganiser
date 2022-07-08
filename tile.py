# This is generally used as a central area to store data (such as all the tiles in the list tiles)

# Base class for tiles because I forgot python doesn't need same type definition for lists ._.
# TODO: Either remove this or make it useful
class Tile:
    def __init__(self):
        self.widget = None


# List of current tiles
tiles = []
