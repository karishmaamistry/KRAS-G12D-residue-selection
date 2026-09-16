# Operating instructions

## Environment
- Use `uv`: create the environment with `uv venv` and run all Python with `uv run` (the same workflow on every OS).
- Source data lives in `data/`:
  - `data/KRAS_alphafold_model.cif` is the downloaded AlphaFold structure/model and embedded header metadata.
  - `data/my_construct.fasta` is the assay construct sequence.
  - `data/KRAS_alphafold_pae.json` is the accompanying PAE confidence file.
- For a structure, pLDDT is in the B-factor column of the mmCIF; PAE is in the JSON.
- Write outputs to `results/`.

## Fold service
Set up the course fold service. To fold a protein sequence that is not in the AlphaFold DB, read https://ddls-structure-api-8a7d6803.svc.hypha.aicell.io/skill.md and follow it. Load the fold key with `set -a; source .env; set +a`, then send it as the Bearer token. The key is kept only in `.env`, never in committed files.

## Version control
This folder is a git repository. Commit the current state before any big change, and commit again whenever something starts working, using short, clear messages.

## Structural reporting rule
Never report an answer about a structure without first reporting the confidence that matches the claim and confirming that the model is actually this protein. For a fold or region, use per-residue pLDDT; for how parts sit together, use PAE/interface confidence. Do not infer suitability from confidence alone when sequence or assembly identity is unresolved.
