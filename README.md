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
pip install -r requirements.txt && python setup.py develop

Run db seed and setup Docker
./database-seed/generate.sh
docker-compose up -d database
```

For a clean installation of all of the python packages run:
```
rm -rf celiac_python.egg-info dist build
python setup.py install
```
