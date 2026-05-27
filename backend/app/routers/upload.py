from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    filename = file.filename

    if filename.endswith(".csv"):
        df = pd.read_csv(file.file, sep=";")

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(file.file)

    else:
        return {
            "error": "Format file tidak didukung"
        }

    return {
        "filename": filename,
        "rows": len(df),
        "columns": len(df.columns),
        "sector_codes": list(df.iloc[:, 0]),
        "sector_names": list(df.iloc[:, 1]),
        "matrix_dimension": f"{len(df)} x {len(df.columns)-2}"
    }
