from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from datastructures import Serviceman
from dataimport import process_csv
from io import StringIO
import uvicorn

from test_funcs import dict_to_csv

app = FastAPI()

# Define a Pydantic model for the request body
class CSVFile(BaseModel):
	file: str

# STATUS 200 = ALL GOOD
# STATUS 400 = BAD REQUEST
@app.post("/import")
def import_file(request: CSVFile):
    try:
        # Convert the CSV string into a DataFrame
        csv_data = StringIO(request.file)
        df = pd.read_csv(csv_data)

        # Convert the DataFrame to a dictionary
        data_dict = df.to_dict(orient="records")

        # Process the data received
        process_csv(data_dict)

        # Write to a file for verification
        dict_to_csv(data_dict, "test/dict.csv")

        return {
            "message": "File imported successfully!",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")

if __name__ == "__main__":
    print(dict_to_csv)
    uvicorn.run(app, host="0.0.0.0", port=8000)