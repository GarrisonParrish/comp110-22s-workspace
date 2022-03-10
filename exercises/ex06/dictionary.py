"""Dictionary functions."""

__author__ = "730324058"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the key-value pairs."""
    result: dict[str, str] = {}
    for key in input_dict:
        value: str = input_dict[key]
        if value in result:
            raise KeyError("Value already exists in inverted dictionary!")
        else:
            result[value] = key
    return result


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns color value that appears most often in the dictionary."""
    frequency_table: dict[str, int] = {}
    for color in input_dict:
        color_value: str = input_dict[color]
        if color_value in frequency_table:
            frequency_table[color_value] += 1  # increase frequency +1
        else:
            frequency_table[color_value] = 1
    max_color: str = ""
    max_frequency: int = 0
    for color in frequency_table:
        if frequency_table[color] > max_frequency:
            max_color = color
            max_frequency = frequency_table[color]
    return max_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count frequencies of each unique item in input_list."""
    frequency_table: dict[str, int] = {}
    for color in input_list:
        if color in frequency_table:
            frequency_table[color] += 1  # increase frequency +1
        else:
            frequency_table[color] = 1
    return frequency_table
