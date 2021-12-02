# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data[0], data[1:]


def save_csv(csvpath, data, data_header):
    """Writes the data to the CSV file with path provided.

    Args:
        csvpath (Path): The csv file path.
        data (list of lists): Data to be written to the CSV file
        data_header (list): The list of the data headers

    """
    with open(csvpath, "w+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write a header
        csvwriter.writerow(data_header)

        # Write the data
        for row in data:
            csvwriter.writerow(row)
    return data