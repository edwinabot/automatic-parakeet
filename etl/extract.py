import json
import typing
import logging

import git

logger = logging.getLogger()


def extract_from_files(repo_root: str, files_path: str) -> typing.Iterable[dict]:
    try:
        with git.Repo(repo_root) as repo:
            data = retrieve_data(repo, files_path)
        return data
    except git.exc.NoSuchPathError:
        logger.error(f"Repo does not exists in path {repo_root}")
    except Exception as ex:
        logger.error(f"An error occured {ex}")
        raise


def update_repo(repo_root: str):
    """
    `update_repo` performs fetch and pull on the current franch of the repo
    """
    with git.Repo(repo_root) as repo:
        repo.remotes["origin"].fetch()
        repo.remotes["origin"].pull()


def retrieve_data(repo: git.Repo, files_path: str) -> typing.Iterable[dict]:
    """
    `retrieve_data` traverses the repository tree up to the files_path and
    loads all the files
    """
    directory = repo.tree() / files_path
    data = []
    for blob in directory.blobs:
        try:
            data.append(json.loads(blob.data_stream.read()))
        except json.decoder.JSONDecodeError:
            logger.error(f"Error decoding {blob.path}")
    return data
