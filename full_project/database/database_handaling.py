import sqlite3
import sys
import os
import json
import socket
try:
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'comunication'))
    sys.path.append(parent_dir)
except:
    print("cant find comunication")
    exit()

from comunication import comm_utils as cu
import threading

def handle_packet(data,database_name,is_example):#a function that recives the sended packet and the database file_name and does according tho the func in the packet
    if(type(data)==dict and "func" not in data):#checking for correct structure
        print("invalid data structure")
        return None
    func=data["func"]
    if(func=="add_data"):#a function that adds data to the database
        add_data(data["df"],database_name)
    elif(func=="print_5_largest_astroid"):#a function that prints the 5 largest asteroids that will pass near earth in the near 30 days
        print_5_largest_astroid(data["current_date"],database_name,is_example)
def listen():#a function that waits for requests(put data in databse/print 5 largest asteroids)
    
    database_name=""
    port=0
    ip="0.0.0.0"
    is_example="False"
    try:
        with open('config.json', 'r') as file:#using predefine configurations
            config = json.load(file)
            database_name=config["database"]["database_file_name"]
            port=config["comunication"]["port"]
            is_example=config["database"]["is_example"]
    except:
        print("can't load configurations")
        exit()
    __init__(database_name)
    print("database listenig")
    s=socket.socket()
    s.bind((ip, port))
    while(True):
        data=cu.recive(cu,s)
        print("recived a connection")
        t=threading.Thread(target=handle_packet,args=[data,database_name,is_example,])
        t.start()
def __init__(table_name):#creating database
    try:
        connection = sqlite3.connect(table_name)
        print("connected to the database")

    except:
        print("can't load database")
        return None

    connection.execute(f'''
    CREATE TABLE IF NOT EXISTS earth_asteroids(
    id INT PRIMARY KEY ,
    Name VARCHAR, 
    diameter int, 
    closest_date VARCHAR , 
    velocity INT
    );                
    ''')

    connection.commit()
    connection.close()
def print_asteroids(asteroids):#a function that prints asteroids
    print("\n\n-------------------------")
    try:
        for i in asteroids:
            print(f"name: {i[0]}")
            print(f"diameter of the asteroid: {i[1]} meters")
            print(f"closest date in distence to earth: {i[2]}")
            print(f"velocity: {i[3]} km/s")
            print("-------------------------")
    except:
        print("invalid astroids structure")

def add_data(df, table_name):#a function that turns the given data in data-frame to the sql database

    try:
        conn = sqlite3.connect(table_name)
        # Insert the data into the SQL table
        df.to_sql('earth_asteroids', conn,if_exists='append', index=False)
        print("Data inserted successfully into earth_asteroids table.")
    except Exception as e:
        print("df hasnt been inserted compleatly into the database(id hasnt inseted)")       
    finally:
        # Close the database connection
        conn.close()

def print_5_largest_astroid(current_date,database_name,is_example):#the function that prints the 5 largest asteroids
    if(is_example=="True"):
        try:
            connection = sqlite3.connect("examples/example_database.db")
        except:
            print("can't connect to databse example")
    else:
        try:
            connection = sqlite3.connect(database_name)
        except:
            print("can't open database")
            print("use example database")
            try:
                connection = sqlite3.connect("examples/example_database.db")
            except:
                print("can't connect to databse example")
    month=int(current_date[5:7])
    month+=1
    if(month==13):

        current_date=str(current_date[:4]+1)+"11"+current_date[7:]
    else:
        current_date=current_date[:4]+str(month)+current_date[7:]
    with connection:
        cursor = connection.cursor()
        cursor.execute(f'''
        SELECT name,diameter,closest_date,velocity from earth_asteroids
        where closest_date <={current_date} 
        ORDER BY diameter DESC
        LIMIT 5;             
        ''')
        rows = cursor.fetchall()

        # Print the results
        print_asteroids(rows)
    connection.commit()
    connection.close()

listen()
    