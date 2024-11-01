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
pip install -r app/requirements.txt && python setup.py develop

Run db seed
./database-seed/generate.sh

For linux run:
sudo systemctl start docker.service

Then setup Docker
docker-compose up -d database

Run the server
flask --app initiate.py run
```

For a clean installation of all of the python packages run:
```
rm -rf celiac_python.egg-info dist build
python setup.py install
```
