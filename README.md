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


## Questionnaire

1) Please check `etl.transform.retrieve_mappings` function implementation. I’ve made an effort to produce a KISS implementation. It also covers points 2 and 3.

4) Please check `job.py`. This is a CLI program that runs a job that extracts the files from the repository, transforms the data as per the provided set of mappings and dumps the resulting data set to a json file on the provided destination.

5) Analyzing the specs and thinking of how to make it less error prone, the first thing that popped into my head was “magic values”. The data mappings are lists of strings (the magic values), it might be easy to leave behind a typo and miss data because of it. This might be one of many improvement points, but not the most important.

    A more robust data modeling might solve most of the problems before these materialize. In the CTI MITRE repo (https://github.com/mitre/cti) they state that CTI is expressed in STIX2.0, so using a STIX2 tool might help. MITRE provides a link to cti-python-styx (https://github.com/oasis-open/cti-python-stix2) and instructions on how to consume the data on CTI with it.

    Exploring a little more https://stix2.readthedocs.io/en/latest/guide/patterns.html#STIX2-Patterns, it seems that the functionality to create the mappings is already there for us to use.

    I think also that an estimation of the data volume might have been necessary, that piece of information would have conditioned some design and implementation details.
