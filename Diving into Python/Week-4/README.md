# Task 1. Magic methods file
In this task, an interface for working with files is created.
The interface provides the following options for working with files:

- reading from a file, the `read` method returns a string with the current content of the file;

- writing to a file, the `write` method accepts a string with the new contents of the file as an argument;

- addition of objects of type `File`, the result of the addition is an object of class `File`, while a new file and a file object are
created in which the contents of the second file are added to the contents of the first file.
The new file is created in the directory obtained with the `tempfile.gettempdir` function.
`os.path.join` is used to get the new path;

- return the full path to the file as a string representation of an object of the `File` class;

- maintain the iteration protocol, with the iteration going through the lines of the file.

When an instance of the `File` class is created, the full path to the file on the file system is passed to the constructor.
If a file with this path does not exist, it is created on initialization.


# Task 2. Descriptor with commission
Often, when crediting some funds to the account, we are charged a commission.
Implemented a similar mechanism using descriptors.
The `Value` descriptor that is used in our `Account` class.

The account has a `commission` attribute. It is this commission that needs to be deducted when assigning values to the `amount`.
