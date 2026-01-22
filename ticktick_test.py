'''
(ignore) File for manually reading/writing from TickTick
'''

import requests                                                                          
import json                                                                              
                     
# Load oauth token                                                                                         
with open('.token-oauth', 'r') as f:                                                     
    token_data = json.load(f)                                                            
    ACCESS_TOKEN = token_data['access_token']                                       
                                                                                         
# Base URL for TickTick OpenAPI                                                          
BASE_URL = "https://api.ticktick.com/open/v1"                                            
                                                                                         
# Headers for all requests                                                               
headers = {                                                                              
    "Authorization": f"Bearer {ACCESS_TOKEN}",                                           
    "Content-Type": "application/json"                                                   
}                                                                                        
                                                                                         
# Example: Get all projects (lists)                                                      
response = requests.get(f"{BASE_URL}/project", headers=headers)                          
print("Projects:", response.json())                                                      
                                                                                         
# Example: Create a task                                                                 
task_data = {                                                                            
    "title": "Get Groceries",                                                            
    "content": "Buy milk, eggs, bread"  # optional description                                    
}                                                                                        
response = requests.post(f"{BASE_URL}/task", headers=headers, json=task_data)            
print("Created task:", response.json())


