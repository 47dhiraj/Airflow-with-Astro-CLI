from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

from pendulum import datetime

import requests                                 

from airflow.models import Variable             
                                                


# Test API "i.e boredapi"
API = "https://www.boredapi.com/api/activity"   



# Declaring/Defining a DAG object using @dag decorator 
@dag(
    start_date=datetime(2024, 2, 18),       
    schedule="@daily",                     
    tags=["activity"],                      
    catchup=False,                        
)



def find_activity():                                            
    
    @task                                           
    def get_response_activity():       
        
        response = requests.get(API, timeout=10)
        
        # print(response)
        return response.json()                      


    @task
    def write_response_activity_to_file(response):  
        
        filepath = Variable.get("activity_file")    

        with open(filepath, "a") as f:           
            f.write(f"Hey, Today u will: {response['activity']} \r\n")
        
        return filepath                           


    @task
    def read_response_activity_from_file(filepath):

        with open(filepath, "r") as f:              
            print(f.read())


    # using bit-shift operators for task dependencies, for the execution order 
    get_response_activity() >> write_response_activity_to_file() >> read_response_activity_from_file()



# calling find_activity() dag
find_activity()                                         