import json
import pytest

from etls.extract import retrieve_paths

example_json_string_1 = """{
        "guid": "1234",
        "content": {
            "type": "text/html",
            "title": "Challenge 1",
            "entities": [ "1.2.3.4", "wannacry", "malware.com"]
            },
        "score": 74,
        "time": 1574879179
    }"""

example_json_string_2 = """{
        "guid": "1234",
        "content": {
            "type": "text/html",
            "title": "Challenge 1",
            "entities": [{
                "type": "text/html",
                "title": "Challenge 2",
                "entities": [ "4.5.6.7", "wannalaugh", "fooware.com"]
                }, {
                "type": "text/html",
                "title": "Challenge 3",
                "entities": [ "4.3.8.7", "wannasleep", "barware.com"]
                }]
            },
        "score": 74,
        "time": 1574879179
    }"""


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


def test_retrieving_mixed_paths():
    keys_iterable = [
        "guid",
        "content.entities[1].title",
        "content.entities[0].entities[2]",
    ]
    expecting = {
        "guid": "1234",
        "content.entities[1].title": "Challenge 3",
        "content.entities[0].entities[2]": "fooware.com",
    }
    data = json.loads(example_json_string_2)
    got = retrieve_paths(data, keys_iterable)
    assert expecting == got


def test_retrieving_some_bad_paths():
    keys_iterable = [
        "foobar",
        "content.entities[1].thisattributeismissing",
        "content.entities[852369].entities[2]",
        "guid",
    ]
    expecting = {"guid": "1234"}
    data = json.loads(example_json_string_2)
    got = retrieve_paths(data, keys_iterable)
    assert expecting == got


if __name__ == "__main__":
    pytest.main(["tests/test_extract.py::test_retrieving_some_bad_paths"])
