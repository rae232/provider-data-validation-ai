from fastapi import FastAPI, UploadFile
import pandas as pd
from agents.master_agent import run_agentic_pipeline

app = FastAPI(title="Provider Data Validation AI")

from fastapi import FastAPI, UploadFile
import pandas as pd
from agents.master_agent import run_agentic_pipeline

app = FastAPI(title="Provider Data Validation AI")

@app.post("/validate")
async def validate_providers(file: UploadFile):
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(file.file)
        else:
            return {"error": "Unsupported file format. Upload CSV or XLSX"}

        results = []
        for _, row in df.iterrows():
            provider = row.to_dict()
            processed = run_agentic_pipeline(provider)
            results.append(processed)

        return {
            "total_records": len(results),
            "validated_records": results
        }

    except Exception as e:
        return {"error": str(e)}

