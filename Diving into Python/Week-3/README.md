# Task 1. Implementing a simple class for reading from a file
Python module <i>solution.py</i>, inside which the code of the <i>FileReader</i> class. The constructor of this class takes one parameter: the path to the file on disk.
The <i>FileReader</i> class implements the read method that returns a string - the contents of the file, the path to which was specified when the class was instantiated.
The Python module is written in such a way that importing the <i>FileReader</i> class from it does not cause errors.

When writing the implementation of the read method, the case is taken into account when the path to a nonexistent file was passed during initialization.
The resulting <i>FileNotFoundError</i> exception is handled and an empty string is returned from the read method.

# Task 2. Classes and inheritance
Suppose there is data about different cars and special equipment. The data are presented in the form of a table with characteristics.
All equipment is divided into three types: special equipment, cars and trucks.
Some characteristics are inherent only in a certain type of technology.
For example, passenger cars have the characteristic “number of passenger seats”, while trucks have body dimensions: “length”, “width” and “height”.


A class hierarchy has been created for the data described above.
The classes should be named CarBase (`base class for all types of cars`), Car (`cars`), Truck (`trucks`), and SpecMachine (`special equipment`).
All objects have the required attributes:

- `car_type`, the value of the object type and can take one of the values: "car", "truck", "spec_machine".

- `photo_file_name`, the name of the file with the image of the car, the names of image files with the extension from the list are allowed: ".jpg", ".jpeg", ".png", ".gif"

- `brand`, brand of the car manufacturer

- `carrying`, carrying capacity

The base class `CarBase` implements the `get_photo_file_ext` method to get the image file extension. I got the file extension using `os.path.splitext`.

For a truck, in the class constructor, I defined the attributes: `body_length`, `body_width`, `body_height`, which are respectively responsible for the dimensions of the body - length, width, and height.
The dimensions are passed in the `body_whl` parameter (a string in which the dimensions are separated by the Latin letter "x").
Body characteristics real numbers and body characteristics may not be valid (for example, an empty string).
In this case, all the attributes responsible for the dimensions of the body are assigned a value equal to zero.

Also, for the truck class, the `get_body_volume` method must be implemented, which returns the volume of the body.

In the `Car` class, the `passenger_seats_count` attribute is defined (the number of passenger seats), and in the `SpecMachine` class - extra (an additional description of the car).

Each object from the hierarchy has its own set of attributes and methods.
For example, the passenger car class does not have a `get_body_volume method`, unlike the truck class.

The implemented `get_car_list` function, which is supplied with a file name in the CSV format.
The file contains data similar to rows from a table. This file is read line by line using the CSV standard library module.
Then the strings are analyzed for validity and a list of objects with cars and special equipment is created. The function returns a list of objects.

The CSV file is used to debug the function `get_car_list`.

The first line in the source file is the CSV header, which contains the column names.
Please note that in some lines of the source file, the data may be filled in incorrectly, for example, required fields are missing or have an invalid value.
In this case, bad trends are ignored. Lines with empty or invalid size for `body_whl` are not ignored.
