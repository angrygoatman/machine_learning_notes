from labelbox import Project, Dataset, Client
from getpass import getpass
import os

#connecting to the API example

# If you don't want to give google access to drive you can skip this cell
# and manually set `API_KEY` below.

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3MyMDZ6OXk0b244MHllajh3a3I0ZXI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3MyMDZ6OWg0b243MHllamcxMGQ5NWV4IiwiYXBpS2V5SWQiOiJja3MyajMwbGc2M2MwMHpkNTZ0bmFhdXozIiwic2VjcmV0IjoiMTc2OWEyODIzZDA4NTZkYTNhMDVlMGIyMTYyYzQ3MjciLCJpYXQiOjE2MjgzODYxNzMsImV4cCI6MjI1OTUzODE3M30.83cHXCRe227dqns_zdhqR7XcsFLY73hb-L7uBhXDJEk"
PROJECT_ID = "cks20zpo94sju0yejbghm0wr0"
DATASET_ID = "cks21as7y4xtt0zd5fwgf7cl1"
PROJECT_NAME = "test1"
DATASET_NAME = "fish"

# Only update this if you have an on-prem deployment
ENDPOINT = "https://api.labelbox.com/graphql"

client = Client(api_key=API_KEY, endpoint=ENDPOINT)

project = client.get_project(PROJECT_ID)
dataset = client.get_dataset(DATASET_ID)

print(project)

print(project.name)
print(project.description)
print(dataset.name)


labels_paginated_collection = project.labels()
labels_paginated_collection
print(labels_paginated_collection)

# Note that if you selected a `project_id` without any labels this will raise `StopIteration`
# Iterate over them to get the items out.
next(labels_paginated_collection)
# list(paginated...) should be avoided for queries that could return more than a dozen results

datasets = client.get_datasets(where=Dataset.name == DATASET_NAME)

projects = client.get_projects(
    where=((Project.name == PROJECT_NAME) &
           (Project.description == "new description field")))

# The above two queries return PaginatedCollections because the filter parameters aren't guaranteed to be unique.
# So even if there is one element returned it is in a paginatedCollection.
print(projects)
print(next(projects, None))
print(next(projects, None))
print(next(projects, None))
# We can see there is only one.

var1 = list(dataset.projects())
print(var1)

sample_project_datasets = project.datasets()
var2 = list(sample_project_datasets)
print(var2)



#   cks20zpo94sju0yejbghm0wr0

#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJja3MyMDZ6OXk0b244MHllajh3a3I0ZXI1Iiwib3JnYW5pemF0aW9uSWQiOiJja3MyMDZ6OWg0b243MHllamcxMGQ5NWV4IiwiYXBpS2V5SWQiOiJja3MyajMwbGc2M2MwMHpkNTZ0bmFhdXozIiwic2VjcmV0IjoiMTc2OWEyODIzZDA4NTZkYTNhMDVlMGIyMTYyYzQ3MjciLCJpYXQiOjE2MjgzODYxNzMsImV4cCI6MjI1OTUzODE3M30.83cHXCRe227dqns_zdhqR7XcsFLY73hb-L7uBhXDJEk"