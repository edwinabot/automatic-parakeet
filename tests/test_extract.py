import json
import pytest

from etls.extract import retrieve_paths

example_json_string_1 = (
    """{
        "guid": "1234",
        "content": {
            "type": "text/html",
            "title": "Challenge 1",
            "entities": [ "1.2.3.4", "wannacry", "malware.com"]
            },
        "score": 74,
        "time": 1574879179
    }""".replace(
        "\n", ""
    )
    .replace(" ", "")
    .strip()
)


def test_retrieving_unindexed_paths():
    expecting = {
        "guid": "1234",
        "content.entities": ["1.2.3.4", "wannacry", "malware.com"],
        "score": 74,
    }
    keys_iterable = ["guid", "content.entities", "score", "score.sign"]
    data = json.loads(example_json_string_1)
    got = retrieve_paths(data, keys_iterable)
    assert expecting == got


def test_retrieving_indexed_paths():
    expecting = {"guid": "1234", "content.entities[0]": "1.2.3.4"}
    keys_iterable = ["guid", "content.entities[0]"]
    data = json.loads(example_json_string_1)
    got = retrieve_paths(data, keys_iterable)
    assert expecting == got


if __name__ == "__main__":
    pytest.main()
