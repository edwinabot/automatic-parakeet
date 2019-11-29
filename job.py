import ast

import click

from etl.extract import extract_from_files, update_repo
from etl.transform import retrieve_paths
from etl.load import dump_to_json_file


class PythonLiteralOption(click.Argument):
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
@click.argument("fields", cls=PythonLiteralOption)
def run_job(repo_root, repo_files_path, output_destination, fields):
    """
    REPO_ROOT is the path on the filesystem for the git repo.

    REPO_FILES_PATH is the path within the repo where the data sources exists

    OUTPUT_DESTINATION is path for the output json file

    FIELDS is the list of fields to extract from the sources
    """
    update_repo(repo_root)
    raw_data = extract_from_files(repo_root, repo_files_path)
    transformed_data = []
    for rd in raw_data:
        transformed_data.append(retrieve_paths(rd, fields))
    dump_to_json_file(transformed_data, output_destination)


if __name__ == "__main__":
    run_job()
