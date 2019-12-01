import ast
import logging
import click

from etl.extract import extract_from_files, update_repo
from etl.transform import retrieve_paths
from etl.load import dump_to_json_file

logging.basicConfig(filename="job.log", level=logging.INFO)


class PythonListLiteralArgument(click.Argument):
    """
    PythonListLiteralArgument parses a string literal into a Python list.
    """

    def type_cast_value(self, ctx, value):
        try:
            ax = ast.literal_eval(value)
            if not isinstance(ax, list):
                raise
            return ax
        except Exception:
            raise click.BadParameter(value)


@click.command()
@click.argument("repo_root")
@click.argument("repo_files_path")
@click.argument("output_destination")
@click.argument("fields", cls=PythonListLiteralArgument)
def run_job(repo_root, repo_files_path, output_destination, fields):
    """
    REPO_ROOT is the path on the filesystem for the git repo.
    Example: /home/user/cti

    REPO_FILES_PATH is the path within the repo where the data sources exists.
    Example: enterprise-attack/attack-pattern

    OUTPUT_DESTINATION is path for the output json file.
    Example: /home/user/result.json

    FIELDS is the list of fields to extract from the source.
    Example: "[\"id\",\"objects[0].name\",\"objects[0].kill_chain_phases\"]"
    """
    update_repo(repo_root)
    raw_data = extract_from_files(repo_root, repo_files_path)
    transformed_data = []
    for rd in raw_data:
        transformed_data.append(retrieve_paths(rd, fields))
    dump_to_json_file(transformed_data, output_destination)


if __name__ == "__main__":
    run_job()
