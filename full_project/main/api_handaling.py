import json,requests
import pandas as pd
def put_dic_in_file(data):
    with open('examples/data_api.json', 'w') as file:
        json.dump(data, file)
def get_dic_from_file():
    with open('examples/data_api.json', 'r') as file:
        data = json.load(file)
        return data
def get_data_from_api_url(api,start_date,end_date,api_key,is_example):#the func that extracts the data from the api
    
    if(is_example=="True"):
        try:
            data=get_dic_from_file()
            return data
        except:
            print("cant open the data example")
            exit()
    url=api.format(start_date,end_date,api_key)
    try:
        requestss=requests.get(url)
        result=requestss.json()
        try:
            put_dic_in_file(result)
        except:
            print("cant crete example from api")
        return result
    except:
        print("cant get the api")
        print("insted use the example")
        try:#if the api extractio didnt work then use the examples of the api data
            data=get_dic_from_file()
            return data
        except:
            print("cant open the data example")
            exit()
        
def get_data_from_api(api,start_date,end_date,api_key,desire_key_in_data,is_example):
    data=get_data_from_api_url(api,start_date,end_date,api_key,is_example)
    result=data[desire_key_in_data]
    list_dates=[]
    for date in result:
        list_dates.append(date)
    data =dict()
    #print(result[list_dates[0]][0])
    df=pd.DataFrame(columns=['id','name','Diameter','closest_date','velocity/s'])
    for date in range(len(result)):
        for asteroid in range (len(result[list_dates[date]])):
            #getting the data per parameter
            try:
                data['id']=result[list_dates[date]][asteroid]['id']
                data['name']=result[list_dates[date]][asteroid]['name']
                data['Diameter']=(result[list_dates[date]][asteroid]['estimated_diameter']['meters']['estimated_diameter_min']+result[list_dates[date]][asteroid]['estimated_diameter']['meters']['estimated_diameter_min'])/2.0
                data['closest_date']=result[list_dates[date]][asteroid]['close_approach_data'][0]['close_approach_date']
                data['velocity']=result[list_dates[date]][asteroid]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
                if(date==0 and asteroid==0):
                    df=pd.DataFrame(data, index=[0])
                else:
                    df=pd.concat([df,pd.DataFrame(data, index=[0])])
            except:
                pass
    return df