import socket
import pickle
import time

class comm_utils:#a class of handalling comunications

    
    def recive(self,s):


        
        print("waiting for connection")
        s.listen()
        conn, addr = s.accept()
        with conn:
            
            data = conn.recv(4096)
            if not data:
                print("no data given")
                s.close()
                return None
            try:
                data = pickle.loads(data)
            except pickle.UnpicklingError as e:
                print("Error unpickling the data:", e)
                exit()
            except Exception as e:
                print("An unexpected error occurred:", e)
                exit()
            return data
    def send(self,ip,port,data):
        HOST = ip 
        PORT = port 

        with socket.socket() as s:
            
            try:
                s.connect((HOST, PORT))
            except:
                print("cant connect")
                exit()

                
            try:
                data=pickle.dumps(data)
                
            except pickle.PickleError as e:
                    print("Error Pickling the data:", e)
                    exit()
            except Exception as e:
                    print("An unexpected error occurred:", e)
                    exit()
            s.send(data)  
