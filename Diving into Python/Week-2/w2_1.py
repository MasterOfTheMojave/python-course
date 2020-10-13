import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
check_file = os.path.exists(storage_path)


# This function is write to file information from console
def write_in_file(key, val):
    if check_file:
        read_string = read_of_file()
        with open(storage_path, 'w') as f:
            if key in read_string:
                read_string[key].append(val)
                f.write(json.dumps(read_string))
            else:
                read_string[key] = [val]
                f.write(json.dumps(read_string))
    else:
        with open(storage_path, 'w') as f:
            empty_dict = {}
            empty_dict[key] = [val]
            f.write(json.dumps(empty_dict))


# This function is read information from file
def read_of_file(key=None):
    if check_file:
        with open(storage_path, 'r') as f:
            json_string = f.read()
            vocabulary_string = json.loads(json_string)
            if key:
                list_write = vocabulary_string.get(key)
                if list_write is None:
                    return(list_write)
                else:
                    return(', '.join(list_write))
            else:
                return(vocabulary_string)
    else:
        return(None)

parser = argparse.ArgumentParser(description="""'key-values' storage.
                                 Data save in file 'storage.data'.
                                 You can add new data in storage
                                 and get they.""")
parser.add_argument("-k", "--key", help="key our data base")
parser.add_argument("-v", "--val", help="value our data base")

args = parser.parse_args()
if args.key and args.val:
    write_in_file(args.key, args.val)
elif args.key:
    print(read_of_file(args.key))