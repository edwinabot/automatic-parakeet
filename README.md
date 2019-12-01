# automatic-parakeet
TruSTAR Screener

### Usage

To run this job you need to have docker installed or a Python 3.7 setup on your machine.

### Using with docker

You have to build the image for this project by doing

`docker build . -t image-name`

Adequate one of `launch.example` files for your os and execute it. You need to specify two volumes:

1. Path to the cti repo
1. Path for the output

### Using your Python setup

You need to have installed the folowing on your os:

1. Python 3.7
1. Pipenv

For setting up the environment you need to install the dependencies by doing:

`pipenv install -dev`

Once this is complete you can check the usage of this program by doing:

`pipenv run python job.py --help`

You can also run the unittests by executing:

`pipenv run pytest`
