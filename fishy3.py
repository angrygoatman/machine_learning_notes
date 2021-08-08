from labelbox import Client, Label
import json
import os

# Pick a project that has labels
PROJECT_ID = "cks20zpo94sju0yejbghm0wr0"
# Only update this if you have an on-prem deployment
ENDPOINT = "https://api.labelbox.com/graphql"

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3MyMDZ6OXk0b244MHllajh3a3I0ZXI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3MyMDZ6OWg0b243MHllamcxMGQ5NWV4IiwiYXBpS2V5SWQiOiJja3MyajMwbGc2M2MwMHpkNTZ0bmFhdXozIiwic2VjcmV0IjoiMTc2OWEyODIzZDA4NTZkYTNhMDVlMGIyMTYyYzQ3MjciLCJpYXQiOjE2MjgzODYxNzMsImV4cCI6MjI1OTUzODE3M30.83cHXCRe227dqns_zdhqR7XcsFLY73hb-L7uBhXDJEk"



client = Client(api_key=API_KEY, endpoint=ENDPOINT)
project = client.get_project(PROJECT_ID)

labels = project.labels()

# Get the first label in the dataset
label = next(labels)

print(label)

#y = json.loads(str(label))

#print(y["created_at"]) 
#problems with json parsing 

#### Review
a = label.create_review(score=1)

#print(a) 

b = next(label.reviews()).score

print(b)

c = label.create_benchmark()

print(c)






