import api_handaling  
import sys
import os
import json
import time
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'comunication'))
sys.path.append(parent_dir)
from comunication import comm_utils as cu
class main:
    def __main__(self):#using predefine conigurations
        print("starting main")
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                
        except:
            print("can't open configurations")
        self.ip_database=config["comunication"]["ip_database"]
        self.port=config["comunication"]["port"]
        self.api_url=config["api_settings"]["api_url"]
        self.start_date=config["api_settings"]["start_date"]
        self.end_date=config["api_settings"]["end_date"]
        self.api_key=config["api_settings"]["api_key"]
        self.is_example=config["api_settings"]["is_example"]
        self.run_prog(self)
    def run_prog(self):
        df=api_handaling.get_data_from_api(self.api_url,self.start_date,self.end_date,self.api_key,"near_earth_objects",self.is_example)#getting the data from the api into a data-frame

        data = {"func":"add_data",'df': df}
        cu.send(cu,self.ip_database,self.port,data)#sending to the database the data
        
        data={"func":"print_5_largest_astroid","current_date":self.start_date}
        cu.send(cu,self.ip_database,self.port,data)#sending the database a request to print the 5 largest asteroids
        print("sended the packet")

main.__main__(main)        