import regex

import typing

ATTRIBUTE_SEPARATOR = "."
INDEX_READ_REX = regex.compile(r"\[\d+\]")


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
    keys = path.split(ATTRIBUTE_SEPARATOR)
    result = source
    for key in keys:
        result = retrieve_attribute(result, key)
        if result is None:
            break
    return result


def retrieve_attribute(source, attribute):
    try:
        result = source.get(attribute)
    except AttributeError:
        # TODO: log attribute error
        result = None
    return result
