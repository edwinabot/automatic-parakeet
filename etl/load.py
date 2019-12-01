import json
import typing
import logging

logger = logging.getLogger()


def dump_to_json_file(data: typing.List[dict], destination_path: str) -> str:
    """
    `dump_to_json_file` writes the content of data to the destination_path
    """
    try:
        with open(destination_path, mode="w") as output:
            json.dump(data, output)
        return destination_path
    except Exception as ex:
        logger.error(f"Error while dumping file {ex}")
        raise
