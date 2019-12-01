# Bash script for running the job on a docker container
docker run -v /path/to/cti:/app/cti -v /path/to/results:/app/results image-name pipenv run python job.py /app/cti enterprise-attack/attack-pattern /app/results/foo.json "['id','objects[0].name','objects[0].kill_chain_phases']"
