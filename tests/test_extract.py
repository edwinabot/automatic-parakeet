import json

from etls.extract import retrieve_paths


def test_example_case():
    expecting = {
        "guid": "1234",
        "content.entities": ["1.2.3.4", "wannacry", "malware.com"],
        "score": 74,
    }
    json_string = (
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
    keys_iterable = ["guid", "content.entities", "score", "score.sign"]
    data = json.loads(json_string)
    got = retrieve_paths(data, keys_iterable)
    assert expecting == got
