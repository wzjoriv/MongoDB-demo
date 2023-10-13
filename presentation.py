# %% [markdown]
# ### Setup
# 
# > Packages + Global variables

# %%
import requests
import pymongo as mg
import json, os

host:str = "mongodb://localhost:27017/"
data_save_folder = "data/"

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

    with open(os.path.join(data_save_folder, "cat_data.json"), encoding='utf-8') as json_file:
        fl_dt = json.load(json_file)
        
    return fl_dt

# %% [markdown]
# ---
# ### MongoDB Client Connection

# %%
## Connect to Mongo 


## Create database


# %% [markdown]
# ---
# ### Cats' Images Database
# 
# #### Create dataset

# %%
## Download data


## Create colelction


## Add many data


# %% [markdown]
# View data in MongoDB

# %% [markdown]
# #### Query dataset (***In python & Mongosh***)
# 
# Get images larger than 500px in height

# %%


# %% [markdown]
# Get images with widths greater than or equals to 450px and heights less than 600px

# %%


# %% [markdown]
# In mongosh:
# 
# ```
# use MyDB;
# ```
# 
# - Get images larger than 500px in height
#     ```
#         db.collection('CATS').find({height: {$gt: 400}}).project({ url: 1, _id: 0 })
#     ```
# - Get images with widths greater than or equals to 450px and heights less than 600px
#     ```
#         db.collection('CATS').find({width: {$gte: 450}, height: {$lt: 600}}).project({ url: 1, _id: 0 })
#     ```

# %% [markdown]
# ---
# ### Venue Database
# 
# #### Create dataset

# %%
## Download data


## Create colelction


## Add many data


# %% [markdown]
# View data in MongoDB

# %% [markdown]
# #### Query dataset (***In python & Mongosh***)
# 
# Get all venues within 2 km from Purdue

# %%


# %% [markdown]
# Get all venues that can sits more the 5000 people

# %%


# %% [markdown]
# In mongosh:
# 
# - Get all venues within 2 km from Purdue
#     ```
#         db.collection('VENUES').find({geometry: {$near: { $geometry:{type: 'Point', coordinates: [-86.9206582, 40.4236401]}, $maxDistance: 2000}}}).project({ NAME: 1, ADDRESS: 1, CITY: 1})
#     ```
# - Get all venues that can sits more the 5000 people
#     ```
#         db.collection('VENUES').find({STATE: 'IN', POPULATION: {$gt: 5000}}).project({ NAME: 1, ADDRESS: 1, CITY: 1, POPULATION: 1})
#     ```


