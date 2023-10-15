# %% [markdown]
# ### Setup
# 
# > Packages + Global variables

# %%
import requests
import pymongo as mg
import json, os

host:str = "mongodb://localhost:27017/"
data_save_folder:str = "data/"

cats_api:str = "https://api.thecatapi.com/v1/images/search?limit=30"
venue_api:str = "https://opendata.arcgis.com/api/v3/datasets/1f538e9e89e642f1b077872933401d8d_0/downloads/data?format=geojson&spatialRefId=4326&where=1=1"

# %% [markdown]
# > Useful Functions

# %%
def download_dataset(file_name:str, db_url: str) -> None:

    response = requests.get(db_url)
    with open(os.path.join(data_save_folder, file_name), "wb") as f:
        f.write(response.content)

def load_dataset(file_name:str):

    with open(os.path.join(data_save_folder, file_name), encoding='utf-8') as json_file:
        fl_dt = json.load(json_file)
        
    return fl_dt

# %% [markdown]
# ---
# ### MongoDB Client Connection

# %%
## Connect to Mongo 
client = mg.MongoClient(host)

## Create database
database = client['MyDBs']

# %% [markdown]
# ---
# ### Cats' Images Database
# 
# #### Create dataset

# %%
## Download data
file_name = "cat_data.json"
download_dataset(file_name, cats_api)

## Create colelction
collection = database['CATS']
cats_info = load_dataset(file_name)

## Add many data
collection.insert_many(cats_info)

# %% [markdown]
# View data in MongoDB

# %% [markdown]
# #### Query dataset (***In python & Mongosh***)
# 
# Get images larger than 500px in height

# %%
query = {
    "height": {"$gt": 800} ## gt = greater than
}

list(collection.find(query, {"_id": False, "url":True}))

# %% [markdown]
# Get images with widths greater than or equals to 450px and heights less than 600px

# %%
query = {
    "width": {"$gte": 600},
    "height": {"$lt": 600},
}

list(collection.find(query, {"_id": False, "url":True}))

# %% [markdown]
# In mongosh:
# 
# ```
# use MyDB;
# ```
# 
# - Get images larger than 500px in height
#     ```
#        db.CATS.find({"height": {"$gt": 500}}).projection({"url": 1, "_id": 0})
#     ```
# - Get images with widths greater than or equals to 450px and heights less than 600px
#     ```
#         db.CATS.find({"width": {"$gte": 450}, "height": {"$lt": 600}}).projection({"url": 1, "_id": 0})
#     ```

# %% [markdown]
# ---
# ### Venue Database
# 
# #### Create dataset

# %%
## Download data
file_name = "venue_data.json"
download_dataset(file_name, venue_api)

## Create colelction
collection = database['VENUES']
venue_info = load_dataset(file_name)["features"]

## Add many data
collection.insert_many(venue_info)
collection.create_index([("geometry", "2dsphere")])

# %% [markdown]
# View data in MongoDB

# %% [markdown]
# #### Query dataset (***In python & Mongosh***)
# 
# Get all venues within 2 km from Purdue

# %%
query = {
    "geometry": {"$near": { 
        "$geometry":
            {"type": 'Point', "coordinates": [-86.9206582, 40.4236401]},
        "$maxDistance": 2000
    }}
}

list(collection.find(query, {"properties.NAME":True, "properties.ADDRESS": True, "properties.CITY": True}))

# %% [markdown]
# Get 10 venues that can sits more the 5000 people

# %%
query = {
    "properties.STATE": "IN",
    "properties.POPULATION": {"$gt": 5000}
}

list(collection.find(query, {"_id": False, "properties.NAME":True, "properties.ADDRESS": True, "properties.CITY": True}, limit = 10))

# %% [markdown]
# In mongosh:
# 
# - Get all venues within 2 km from Purdue
#     ```
#         db.VENUES.find({"geometry": {"$near": { "$geometry":{"type": 'Point', "coordinates": [-86.9206582, 40.4236401]}, "$maxDistance": 2000}}}).projection({"properties.NAME": 1, "properties.ADDRESS": 1, "properties.CITY": 1})
#     ```
# - Get all venues that can sits more the 5000 people
#     ```
#         db.VENUES.find({"properties.STATE": "IN", "properties.POPULATION": {"$gt": 5000}}).projection({"properties.NAME": 1, "properties.ADDRESS": 1, "properties.CITY": 1})
#     ```


