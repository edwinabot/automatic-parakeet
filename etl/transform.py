import re
import typing
import logging

logger = logging.getLogger()
path_separator = "."
indexed_attribute_regex = re.compile(r"\w+\[\d+\]")
indexed_attribute_extract_regex = re.compile(r"(\w+)\[(\d+)\]")


def retrieve_mappings(source: dict, mappings: typing.Iterable) -> dict:
    """
    `retrieve_mappings` builds a list of mappings (dicts) containing key:value pairs
    if present on the source dicts.
    Resulting keys are specified by the mappings.
    """
    result = {}
    for path in mappings:  # type: str
        value = retrieve_path(source, path)
        if value is not None:
            result.setdefault(path, value)
    return result


def retrieve_path(source: dict, path: str) -> typing.Any:
    """
    `retrieve_path` traverses the path over the source and returns the element
    if it exists, else it returns None
    """
    keys = path.split(path_separator)
    result = source
    for key in keys:
        result = retrieve_attribute(result, key)
        if result is None:
            logger.info(f"Element missing on path {path} at {key} on {source}")
            break
    return result


def retrieve_attribute(source: dict, attribute: str) -> typing.Any:
    """
    `retrieve_attribute` returns the value of the attribute of the source
    if it exists. If the attribute does not exists returns None.

    `attribute` can be a key of a dict like 'name' or an indexed key like 'names[2]'
    """
    try:
        if indexed_attribute_regex.search(attribute):
            attribute, index = indexed_attribute_extract_regex.search(
                attribute
            ).groups()
            result = source.get(attribute)[int(index)]
        else:
            result = source.get(attribute)
    except (AttributeError, IndexError, ValueError) as ex:
        logger.error(f"{ex}, {attribute}")
        result = None
    return result
