# automatic-parakeet
TruSTAR Screener

### Usage

To run this job you need to have docker installed or a Python 3.7 setup on your machine.

### Using with docker

You have to build the image for this project by executing

`$ docker build . -t image-name`

Adequate one of `launch.example` files for your os and execute it. You need to specify two volumes:

1. Path to the cti repo
1. Path for the output

### Using your Python setup

You need to have installed the folowing on your os:

1. Python 3.7
1. Pipenv

For setting up the environment you need to install the dependencies by running:

`$ pipenv install -dev`

Once this is complete you can check the usage of this program executing:

```
$ pipenv run python job.py --help
Usage: job.py [OPTIONS] REPO_ROOT REPO_FILES_PATH OUTPUT_DESTINATION FIELDS

  REPO_ROOT is the path on the filesystem for the git repo. Example:
  /home/user/cti

  REPO_FILES_PATH is the path within the repo where the data sources exists.
  Example: enterprise-attack/attack-pattern

  OUTPUT_DESTINATION is path for the output json file. Example:
  /home/user/result.json

  FIELDS is the list of fields to extract from the source. Example:
  "["id","objects[0].name","objects[0].kill_chain_phases"]"

Options:
  --help  Show this message and exit.
```

You can also run the unittests executing:

`$ pipenv run pytest`


### Notes

* `etl.transform.retrieve_attribute` can be extended to retrieve "attributes" from any object leveraging the `getattr` BIF.
