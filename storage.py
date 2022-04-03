# a sophisticated storage utilizing python's pickle module
# pretty much a trivial "SQLite"/"JSON" storage clone

# WARNING: not suitable for large data sets
#      * In-Memory storage, ....loads-in the entire data set in memory upon startup
#      * re-writes the entire data set each time an item is updated
#      * no indexing
#      * no great Big-O search guaranteed (linear search)

import pickle
import pathlib

from storable import Storable
import faculty

PICKLE_FILE = 'my_db'

dataset = {}


def get(cls: type):
    if dataset is not None:
        cls_collection = dataset.get(cls.__name__)
        return cls_collection if cls_collection is not None else []


def get_one(cls: type, _id: str):
    collection = get(cls)
    matches = list(filter(lambda x: x.get_unique_id() == _id, collection))
    if len(matches) >= 1:
        return matches[0]
    return None


def save(obj: Storable):
    if get_one(type(obj), obj.get_unique_id()) is None:
        _append_obj(obj)
    else:
        _replace_obj(obj)

    _write_dataset()


def _replace_obj(obj):
    # todo: replace an existing object
    pass


def _append_obj(obj):
    col_name = type(obj).__name__
    if col_name not in dataset:
        dataset[col_name] = []

    dataset[col_name].append(obj)


def _initialize():
    global dataset
    if not pathlib.Path(PICKLE_FILE).exists():
        with open(PICKLE_FILE, 'wb') as file:
            pickle.dump(dataset, file)
    else:
        with open(PICKLE_FILE, 'rb') as file:
            dataset = pickle.load(file)
            print('[Startup]: done reading data set', len(dataset))


def _write_dataset():
    print("Writing dataset ...")
    with open(PICKLE_FILE, 'wb') as file:
        pickle.dump(dataset, file)
    print("Done.")


_initialize()
