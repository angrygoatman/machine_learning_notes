from labelbox import Project, Dataset, Client
from getpass import getpass
import os

#CRUD (CREATE READ UPDATE DESTROY) example 

# If you don't want to give google access to drive you can skip this cell
# and manually set `API_KEY` below.

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3MyMDZ6OXk0b244MHllajh3a3I0ZXI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3MyMDZ6OWg0b243MHllamcxMGQ5NWV4IiwiYXBpS2V5SWQiOiJja3MyajMwbGc2M2MwMHpkNTZ0bmFhdXozIiwic2VjcmV0IjoiMTc2OWEyODIzZDA4NTZkYTNhMDVlMGIyMTYyYzQ3MjciLCJpYXQiOjE2MjgzODYxNzMsImV4cCI6MjI1OTUzODE3M30.83cHXCRe227dqns_zdhqR7XcsFLY73hb-L7uBhXDJEk"
PROJECT_ID = "cks20zpo94sju0yejbghm0wr0"

ENDPOINT = "https://api.labelbox.com/graphql"

client = Client(api_key=API_KEY, endpoint=ENDPOINT)

project = client.get_project(PROJECT_ID)
dataset = next(project.datasets())

#read 
data_rows = dataset.data_rows()
data_row = next(data_rows)

#print("Associated dataset", data_row.dataset())
#print("Associated label(s)", next(data_row.labels()))
#print("External id", data_row.external_id)

data_row = dataset.data_row_for_external_id(data_row.external_id)
print(data_row)

#create

#Add one at a time
dataset = client.create_dataset(name="testing-dataset")
dataset.create_data_row(row_data="https://picsum.photos/200/300")

#print(dataset)
#print(var3)



task1 = dataset.create_data_rows([{
    DataRow.row_data: "https://picsum.photos/200/300"
}, {
    DataRow.row_data: "https://picsum.photos/200/300"
}])


