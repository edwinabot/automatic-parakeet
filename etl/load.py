import json
import typing


def dump_to_json_file(data: typing.List[dict], destination_path: str) -> str:
    try:
        with open(destination_path, mode="w") as output:
            json.dump(data, output)
        return destination_path
    except Exception as ex:
        print(f"Error while dumping file {ex}")
        raise
