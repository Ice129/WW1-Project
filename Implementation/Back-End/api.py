#
# To run this API locally to test it, you need to install pydantic and fastapi 
# as well as their dependencies. You can do this by running the following command:#
# pip install fastapi[all] pydantic[all] uvicorn
#

import sys
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import subprocess

app = FastAPI()

# Data model for the CSV POST request
class CsvUpload(BaseModel):
    authToken: str
    databaseName: str
    csv: bytes

# Data model for individual upload
class IndividualUpload(BaseModel):
    authToken: str
    databaseName: str
    data: dict

##################################################################################################
#
# You should not touch any code above this section as it may interfere with other people's work
# Should code here NEED changing, please contact the team leader so we can verify 
# that the changes are necessary and do not interfere with other people's work
#
##################################################################################################
#
# STATUS CODES & WHERE TO USE THEM:
# 200 - OK
# 403 - Unauthorized / Incorrect or No Auth Token
# 404 - Not Found / Incorrect Database Name
# 400 - Bad Request / Incorrect Data Format (Used for general errors)
#
##################################################################################################

# Assigned to: ???
@app.post("/upload_csv")
async def upload_csv(obj: CsvUpload):
    return {"status": "success", "code": 200}

# Assigned to: ???
@app.post("/upload_individual")
async def upload_individual(obj: IndividualUpload):
    return {"status": "success", "code": 200}

# Assigned to: ???
@app.patch("/change_password")
async def change_password(newPasswordHash: str, authToken: str):
    return {"status": "success", "code": 200}

# Assigned to: ???
@app.delete("/delete_row")
async def delete_row(databaseName: str, filterObject: dict, authToken: str):
    return {"status": "success", "code": 200}

# Assigned to: ???
# Should return a JSON object containing the data that matches the filter object
# JSON object should be nested under the variable name "data" in the returned JSON object
@app.get("/get_data")
async def get_data(databaseName: str, filterObject: dict):
    return {"status": "success", "code": 200}

# Assigned to: ???
# Should return a randomly generated Base64 token (string) of length 256 to be used in further functions as an input
# To verify that the sender is an administrator user
@app.get("/auth_admin")
async def auth_admin(passwordHash: str):
    return {"status": "success", "code": 200}

# Assigned to: ???
@app.get("/download_csv")
async def download_csv(databaseName: str, filterObject: dict, authToken: str):
    return {"status": "success", "code": 200}

# Assigned to: James
@app.get("/close_program")
async def close_program(authToken: str):
    
    # TODO: authenticate token
    
    
    try:
        with open("PID", "r") as f:
            pid = f.read()
    except FileNotFoundError:
        return {"status": "error", "code": 400, "message": "No PID file found"}
    
    subprocess.run(["taskkill", "/f", "/pid", pid])
    subprocess.run(["taskkill", "/f", "/im", "msedge.exe"])
    sys.exit()

if __name__ == "__main__":
    uvicorn.run(app, host="", port=8000)