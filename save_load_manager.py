import tile
import tiles
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

    for _tile in tile.tiles:
        data.append(_tile.get_save_info())
    data.append(main.arrowHandler.get_save_data())

    with open("save_data.json", "w") as save_file:
        # Clear file
        save_file.write("")

        # Save data
        json.dump(data, save_file, indent=4)


def load_data(root, main):
    with open("save_data.json", "r") as save_file:
        try: info = json.load(save_file)
        except: return
        # Need to loop through all the parts in dictionary, and get their tile ID. Then, create their object.
        for index, data in enumerate(info):
            # If its arrow info, then ignore it
            if index == len(info) - 1: continue
            # Get its ID
            ID = data[0]

            # Create object
            tile.tiles.append(id_to_object[ID](root, main))
            tile.tiles[index].load_save_info(data[1])

        print(info[-1])
        main.arrowHandler.load_save_data(info[-1])