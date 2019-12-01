# PowerShell script for running the job on a docker container
docker run -v C:\path\to\cti\:/app/cti -v C:\path\to\results\:/app/results image-name pipenv run python job.py /app/cti enterprise-attack/attack-pattern /app/results/foo.json "['id','objects[0].name','objects[0].kill_chain_phases']"
