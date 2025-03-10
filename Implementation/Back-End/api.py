#
# To run this API locally to test it, you need to install pydantic and fastapi 
# as well as their dependencies. You can do this by running the following command:
# pip install fastapi[all] pydantic[all] uvicorn openpyxl pandas xlsxwriter
#

import sys
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (or specify your frontend URL, e.g., "http://localhost:3000")
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

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

class GetDataBody(BaseModel):
    databaseName: str
    forename: str = None
    surname: str = None
    regiment: str = None

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



# Serve ../Front-End/index.html
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="../Front-End/static"), name="static")

@app.get("/")
async def root():
    return FileResponse("../Front-End/index.html")

@app.get("/guest_home")
async def guest_home():
    return FileResponse("../Front-End/guest_home.html")

@app.get("/admin_dashboard")
async def admin_dashboard():
    return FileResponse("../Front-End/admin_dashboard.html")

@app.get("/admin_login")
async def admin_login():
    return FileResponse("../Front-End/admin_login.html")

@app.get("/database_view")
async def database_view():
    return FileResponse("../Front-End/database_view.html")

@app.get("/biographies")
async def database_view():
    return FileResponse("../Front-End/biographies.html")

@app.get("/buried")
async def database_view():
    return FileResponse("../Front-End/buried.html")

@app.get("/memorials")
async def database_view():
    return FileResponse("../Front-End/memorials.html")

@app.get("/newspaper")
async def database_view():
    return FileResponse("../Front-End/newspaper.html")

@app.get("/townships")
async def database_view():
    return FileResponse("../Front-End/townships.html")

# Assigned to: ???
from backend import load_xlsx, insert_to_sql
@app.post("/upload_csv")
async def upload_csv(obj: CsvUpload):
    csv_file = obj.csv
    try:
        insert_to_sql(load_xlsx(csv_file))
    except Exception as e:
        return {"status": "error", "code": 400, "message": str(e)}
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

# Assigned to: Charlie
# Should return a JSON object containing the data that matches the filter object
# JSON object should be nested under the variable name "data" in the returned JSON object
from backend import forename_S, surname_S, regiment_S, forename_surname_S, forename_regiment_S, surname_regiment_S, forename_surname_regiment_S
@app.post("/get_data")
async def get_data(obj: GetDataBody):
    databaseName = obj.databaseName
    forename = obj.forename
    surname = obj.surname
    regiment = obj.regiment
    
    if forename and surname and regiment:
        return {"status": "success", "code": 200, "data": forename_surname_regiment_S(databaseName, forename, surname, regiment)}
    elif forename and surname:
        return {"status": "success", "code": 200, "data": forename_surname_S(databaseName, forename, surname)}
    elif forename and regiment:
        return {"status": "success", "code": 200, "data": forename_regiment_S(databaseName, forename, regiment)}
    elif surname and regiment:
        return {"status": "success", "code": 200, "data": surname_regiment_S(databaseName, surname, regiment)}
    elif forename:
        return {"status": "success", "code": 200, "data": forename_S(databaseName, forename)}
    elif surname:
        return {"status": "success", "code": 200, "data": surname_S(databaseName, surname)}
    elif regiment:
        return {"status": "success", "code": 200, "data": regiment_S(databaseName, regiment)}
    else:
        return {"status": "error", "code": 400, "message": "No filter object provided"}

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