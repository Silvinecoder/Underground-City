<div align="center"><img src="./icon.svg" /></div>
<h1 align="center">Underground City</h1>

## Setup your environment

```
Create a venv file
python3 -m venv venv

Then activate:
source venv/bin/activate
or for windows:
venv\Scripts\activate

Install dependencies:
pip install -r app/requirements.txt && pip install -e .

Run db seed
./database-seed/generate.sh
or for windows:
sh database-seed/generate.sh

For linux run:
sudo systemctl start docker.service

Then setup Docker
docker compose up -d database

Run the server
flask --app app/handler/lambda_handler.py run
```

For a clean installation of all of the python packages run:
```
rm -rf celiac_python.egg-info dist build
python setup.py install
```
