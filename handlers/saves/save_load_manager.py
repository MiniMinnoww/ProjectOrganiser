import info
from gui import tiles
import json

id_to_object = {
        0: tiles.Note,
        1: tiles.Board,
        2: tiles.ToDo,
        3: tiles.Header,
        4: tiles.Image,
        5: tiles.ClassDiagram
    }

def save_data(main):
    # Oh boy, we got this... right..?
    # Most of the incoming data will be from the tiles get_save_info() method itself
    data = []

    for _tile in info.tiles:
        data.append(_tile.get_save_info())
    data.append(main.arrowHandler.get_save_data())

    with open("json/saves/save_data.json", "w") as save_file:
        # Clear file
        save_file.write("")

        # Save data
        json.dump(data, save_file, indent=4)


def load_data(root, main):
    with open("json/saves/save_data.json", "r") as save_file:
        try: data = json.load(save_file)
        except: return
        # Need to loop through all the parts in dictionary, and get their tile ID. Then, create their object.
        for index, _data in enumerate(data):
            # If its arrow info, then ignore it
            if index == len(data) - 1: continue
            # Get its ID
            ID = _data[0]

            # Create object
            info.tiles.append(id_to_object[ID](root, main))
            info.tiles[index].load_save_info(_data[1])


        try: main.arrowHandler.load_save_data(data[-1])
        except: pass