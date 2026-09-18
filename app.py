from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
DATA = ROOT / "data"
app = FastAPI(title="KRAS structure handoff")

@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse((ROOT / "index.html").read_text(encoding="utf-8"))

@app.get("/api/results")
def results():
    return JSONResponse(json.loads((RESULTS / "results.json").read_text(encoding="utf-8")))

@app.get("/data/pae")
def pae():
    return JSONResponse(json.loads((DATA / "KRAS_alphafold_pae.json").read_text(encoding="utf-8")))

@app.get("/structure/model.cif")
def structure():
    return FileResponse(DATA / "KRAS_alphafold_model.cif", media_type="chemical/x-mmcif")

@app.get("/structure/g12d.pdb")
def g12d_structure():
    p = ROOT / "construct.pdb"
    if not p.exists(): raise HTTPException(404, "G12D structure not available")
    return FileResponse(p, media_type="chemical/x-pdb")

@app.get("/artifacts/{name}")
def artifact(name: str):
    allowed={"G12D_structure_plddt.png","WT_AlphaFold_structure_plddt.png","G12D_PAE_heatmap.png"}
    if name not in allowed: raise HTTPException(404)
    return FileResponse(RESULTS / name)
