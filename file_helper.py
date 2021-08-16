# Snake V 1.0

# file_helper.py
# python file containing functions that assist in the reading and writing of files.
#

# Created By: Zack Ross
# Last Updated: May 6, 2017


def read_file(filename):
    """
    reads in data from a text file with a given filename.

    :param filename: the name of the text file (example.txt); string
    :return: the file contents as a list
    """
    file = open(filename, "r")

    data = []
    for line in file:
        data.append(line.rstrip())

    file.close()

    return data


def write_file(filename, data):
    """
    Writes given data to a text file with a given filename.

    :param filename: the name of the text file (example.txt); string
    :param data: a list containing data
    post-conditions: writes data to a text file
    :return: None
    """
    file = open(filename, "w")
    for item in data:
        file.write(str(item))

    file.close()
