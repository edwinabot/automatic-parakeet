import re

import typing

path_separator = "."
indexed_attribute_regex = re.compile(r"\w+\[\d+\]")
indexed_attribute_extract_regex = re.compile(r"(\w+)\[(\d+)\]")


def retrieve_paths(source: dict, paths_iterable: typing.Iterable) -> dict:
    result = {}
    for path in paths_iterable:  # type: str
        value = retrieve_path(source, path)
        if value is not None:
            result.setdefault(path, value)
    return result


def retrieve_path(source: dict, path: str) -> typing.Any:
    """
    Retrieves from the source dict the value in the path if exists
    """
    keys = path.split(path_separator)
    result = source
    for key in keys:
        result = retrieve_attribute(result, key)
        if result is None:
            break
    return result


def retrieve_attribute(source, attribute):
    try:
        if indexed_attribute_regex.search(attribute):
            attribute, index = indexed_attribute_extract_regex.search(
                attribute
            ).groups()
            result = source.get(attribute)[int(index)]
        else:
            result = source.get(attribute)
    except (AttributeError, IndexError, ValueError) as ex:
        # TODO: log attribute error
        print(ex, attribute)
        result = None
    return result
