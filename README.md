

python3 -m venv venv
.venv/bin/activate
pip install -r req.txt
createdb <dbname>
touch .env
fill .env with:
db_USER = 
PASSWORD = 
HOST=
PORT=
DB_NAME=