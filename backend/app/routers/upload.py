from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter()


def read_matrix_file(file):

    filename = file.filename

    if filename.endswith(".csv"):
        df = pd.read_csv(file.file, sep=None, engine="python")

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(file.file)

    else:
        return None

    return df


def build_response(df, filename, matrix_type):

    return {
        "matrix_type": matrix_type,
        "filename": filename,
        "rows": len(df),
        "columns": len(df.columns),
        "sector_codes": list(df.iloc[:, 0]),
        "sector_names": list(df.iloc[:, 1]),
        "matrix_dimension": f"{len(df)} x {len(df.columns)-2}"
    }


@router.post("/upload/transaction")
async def upload_transaction(file: UploadFile = File(...)):

    df = read_matrix_file(file)

    return build_response(
        df,
        file.filename,
        "transaction"
    )


@router.post("/upload/environment")
async def upload_environment(file: UploadFile = File(...)):

    df = read_matrix_file(file)

    return build_response(
        df,
        file.filename,
        "environment"
    )


@router.post("/upload/market")
async def upload_market(file: UploadFile = File(...)):

    df = read_matrix_file(file)

    return build_response(
        df,
        file.filename,
        "market"
    )


@router.post("/upload/primary")
async def upload_primary(file: UploadFile = File(...)):

    df = read_matrix_file(file)

    return build_response(
        df,
        file.filename,
        "primary"
    )


@router.post("/upload/final-demand")
async def upload_final_demand(file: UploadFile = File(...)):

    df = read_matrix_file(file)

    return build_response(
        df,
        file.filename,
        "final_demand"
    )
