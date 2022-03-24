"""Dictionary related utility functions."""

__author__ = "730324058"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of csv file into a list of dictionaries."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    # Read that file

    # Read each row of the csv file into a dictionary
    csv_reader = DictReader(file_handle)

    # Read the dictionary
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all the values in a certain column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]  # index to the "column" key in the "row" dictionary
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a list of dicts (each dict is a row) to a dict of lists (each key is a column name, values are column values)."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]  # This allows us to get the column names (keys in the dict)
    for column in first_row:
        # get all the column values, add column name, column values as a key-value pair to result dictionary
        result[column] = column_values(row_table, column)

    return result


def head(col_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Return the first n rows in the table."""
    if n > len(col_table):
        n = len(col_table)

    result: dict[str, list[str]] = {}

    for col in col_table:
        rows: list[str] = []  # empty rows list to append to
        for i in range(0, n):
            rows.append(col_table[col][i])  # look up the value at this index in the row list at the col index
        result[col] = rows
    return result


def select(col_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Return a column-aligned dictionary with a selection of columns."""
    result: dict[str, list[str]] = {}
    
    for col in col_names:
        result[col] = col_table[col]
    return result


def concat(col_table_1: dict[str, list[str]], col_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenates two column-based dictionaries."""
    result: dict[str, list[str]] = {}
    for col1 in col_table_1:
        result[col1] = col_table_1[col1]
    for col2 in col_table_2:
        if col2 in result:
            for i in col_table_2[col2]:
                result[col2].append(i)
        else:
            result[col2] = col_table_2[col2]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Same as ex06/dictionaries.py."""
    output_list: dict[str, int] = {}
    for key in input_list:
        if key in output_list:
            output_list[key] += 1
        else:
            output_list[key] = 1
    return output_list