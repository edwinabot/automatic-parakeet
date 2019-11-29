import json
import os
import typing


def dump_to_json_file(
    data: typing.List[dict], destination_path: str, filename: str
) -> str:
    try:
        path = os.path.join(destination_path, filename)
        with open(path, mode="w") as output:
            json.dump(data, output)
        return path
    except Exception as ex:
        print(f"Error while dumping file {ex}")
        raise
