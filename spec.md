# Specification: KRAS model suitability for G12D assay residue selection

## Decision
The owner needs one overall yes/no verdict on whether it is safe to choose nucleotide-pocket and switch-region residues for the assay protein: KRAS residues 1–169 with Asp at position 12 (G12D). If the mismatch or missing provenance prevents a safe assessment, the verdict must be **cannot assess safely**, not a confidence-ranked shopping list.

## Protein and model
- Assay target: KRAS G12D, residues 1–169; the transcript describes it as the assay protein/construct and a monomeric protein, but does not document an assembly beyond that.
- Downloaded model: standard KRAS AlphaFold model, with Gly12 and a longer tail; it is a predicted model, not an experimental structure. The exact AlphaFold accession, release/version, and download date are not recorded in the transcript and must be read from the CIF if present; otherwise provenance remains unresolved.
- The downloaded model must be treated as a structural template, not as the literal assay protein. Used exactly as downloaded it is not acceptable for the G12D construct because residue 12 and the extent differ.

## Files
- `data/KRAS_alphafold_model.cif`: downloaded AlphaFold folded model and any embedded header metadata; pLDDT is in its B-factor column.
- `data/my_construct.fasta`: sequence for the 1–169 assay construct; it must establish the actual sequence, including Asp12.
- `data/KRAS_alphafold_pae.json`: accompanying PAE confidence data, used for confidence in how parts sit together and for interfaces/relative placement.

## Exact claim and affected parts
The claim to assess is whether the downloaded model can defensibly support selecting residues for the G12D, 1–169 assay protein before the compound-design handoff. The relevant parts are the nucleotide-pocket groove, especially switch-region residues reachable by the hit series, and residue 12 explicitly. Residue 12 itself is not defensible from the downloaded model; direct pocket contacts whose placement or chemistry is materially altered by Gly12-to-Asp12 substitution are also not defensible. Nearby residues are not automatically excluded. The removed/distant tail is irrelevant to the pocket unless the evidence shows otherwise.

## Matching confidence to the claim
- For a fold or local region, report per-residue pLDDT from the CIF B-factor column.
- For how regions or parts sit together, report PAE from the JSON, including relevant interface/neighbor relationships.
- Confidence supports the decision but does not rescue a sequence mismatch or establish identity. A single universal cutoff is not specified by the owner.

## Checks that could break the decision
1. Compare the FASTA sequence directly with the model sequence from the CIF: verify identity, residue numbering, length/extent, residue 12, and all pocket/switch-region residues. Do not infer identity from diagnosis or confidence.
2. Verify whether the CIF contains accession, release/version, or download metadata. Missing metadata leaves provenance unresolved; sequence comparison cannot recover a missing database record.
3. Verify the model/assay sequence and numbering before mapping any pocket residue. Check that all reported residues are present in residues 1–169 of the assay construct.
4. Assess local pocket/switch-region geometry with per-residue pLDDT and relevant placement with PAE. Identify direct contacts materially dependent on Gly12 versus Asp12 rather than discarding every nearby residue.
5. Confirm the assembly/model scope; the transcript does not provide evidence for an oligomeric assembly, so do not assume one.

## Definition of done
Produce an auditable result in `results/` with one clear overall verdict (yes/no, or **cannot assess safely** when required), a short residue-level table for pocket and switch-region residues classified as usable, uncertain, or not defensible, and an explicit callout for position 12. Include the sequence/numbering and provenance reconciliation, the pLDDT values matching fold/local claims, PAE values matching placement claims, unresolved limitations, and the reason each classification follows the owner’s rules. Do not call the model validated for residue selection unless the assay-protein identity, relevant sequence/assembly mapping, and confidence evidence support that claim.
