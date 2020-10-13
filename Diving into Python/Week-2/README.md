# Task 1. Key-values storage 
The data will be saved in the storage.data file. Adding new data to the storage and getting the current values 
is carried out using the <i>storage.py</i> command-line utility. An example of the utility operation:

Storing value by key key_name:

`$ storage.py --key key_name --val value`

Getting value by key key_name:

`$ storage.py --key key_name`


The utility can be called with the inclusion of:

`--key <key name>`, где `<key name>` - the key by which the values are stored/obtained

`--val <value>`, где `<value>` - stored value.

If both keys are passed when starting the utility, the passed value is added by the key and the data is saved in a file.
If only the key name is passed, the storage file is read and the values are printed,
which were saved with this key. The values for one key are not overwritten but added to those already saved.
In other words, several values can be stored in one key. When printed, the values are printed to add them to the repository. Print format for multiple values:

`value_1, value_2`

If no values were found by key - empty string or None.

The <i>argparse</i> module is used to work with command-line arguments. Store data in a JSON file using the <i>json</i> standard library module.


# Task 2. to_json decorator
Data formats are used to transfer data between functions, modules, or different systems. One of the most popular formats is JSON. 
A <i>to_json</i> decorator has been written that can be applied to various functions to convert their return value to JSON format.
