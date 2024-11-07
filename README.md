# Home-Assignment-api-db

Home-Assignment-api-db is a Python project for getting data from an api and inserting it into a database.

## Usage

for running the programm enter this lines.

```bash
# clone repository into your computer
git clone https://github.com/y6ui/Home-Assignment-api-db.git

# move into the project directory
cd Home-Assignment-api-db/full_project

# build the main image
docker build -t main:latest -f dockerfile.main.sh .

# build the database image
docker build -t database:latest -f dockerfile.db.sh .

# run both of the images into 2 containers
docker-compose up -d

# see the output of the containers
docker-compose logs -f

```

## description

content of the project:

the project contains 2 running programs:

1)main.py

2)database_handaling.py

**main**:

main is the program that sends the requests to the api_handaling and database_handaling

**database_handaling**:

database_handaling is the program that communicates with the database

**database_handaling has a few functions**:

1)listen: the initializer of the program and handles the listening communications- after every response it opens a thread to the function handle_packet

2)handle_packet: the function that orginized the contents of the packet and sends to a function accordingly

3)__init__: the function that initialize the used table in the database if not existed

4)add_data: the function that gets a data-frame and insert it into the database

5)print_5_largest_astroid: the funcction that prints the 5 largest astroids

6)print_asteroids: prints a list of asteroids

**comunication**:

comunication is the program that handles the communications between the programs

**config.json**:

config.json is a configuration file for the programs

is_example should be "True" for adding examples

**dockerfile.db.sh and dockerfile.main.sh**:

dockerfile.db.sh and dockerfile.main.sh are the docker files that create the images

**requirements.txt**:

requirements.txt is a file for configurations to python



