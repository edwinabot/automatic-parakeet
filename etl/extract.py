import json
import typing

import git


def extract_from_files(repo_root: str, files_path: str) -> typing.Iterable[dict]:
    try:
        with git.Repo(repo_root) as repo:
            data = retrieve_data(repo, files_path)
        return data
    except git.exc.NoSuchPathError:
        print(f"Repo does not exists in path {repo_root}")
    except Exception as ex:
        print(f"An error occured {ex}")
        raise


def update_repo(repo_root: str):
    with git.Repo(repo_root) as repo:
        repo.remotes["origin"].fetch()
        repo.remotes["origin"].pull()


def retrieve_data(repo: git.Repo, files_path: str) -> typing.Iterable[dict]:
    directory = repo.tree() / files_path
    data = []
    for blob in directory.blobs:
        data.append(json.loads(blob.data_stream.read()))
    return data
