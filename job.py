from etl.extract import extract_from_files, update_repo
from etl.transform import retrieve_paths
from etl.load import dump_to_json_file

if __name__ == "__main__":
    print("Hello TruSTAR!!")
    repo_root = "/mnt/c/Users/edwin/Repos/cti"
    files_path = "enterprise-attack/attack-pattern"
    destination = "/mnt/c/Users/edwin/Repos/automatic-parakeet"
    fields = ["id", "objects[0].name", "objects[0].kill_chain_phases"]

    update_repo(repo_root)
    raw_data = extract_from_files(repo_root, files_path)
    transformed_data = []
    for rd in raw_data:
        transformed_data.append(retrieve_paths(rd, fields))
    dump_to_json_file(transformed_data, destination, "foo_edwin.json")
