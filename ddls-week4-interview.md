# DDLS 2026 — Week 4 interview transcript

**Lab:** Interview a Structural-Biology Data Owner
**Data owner:** Dr. Yuki Tanaka — Medicinal chemist / drug-discovery researcher
**Student:** Karishma Mistry <karishmamistry86160@gmail.com>
**Exported:** 2026-09-16T12:05:34+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

Hii Dr. Yuki! What are we working with today? what is in your dataset? and what is the decision you are about to make based on this dataset?

**Dr. Yuki Tanaka**:

I’m Dr Yuki Tanaka, working on a KRAS inhibitor programme. The dataset has the AlphaFold KRAS structure, the sequence for the protein we use in the assay, and the accompanying confidence file. I want the nucleotide-pocket groove read out—especially the switch-region residues my hit series can reach. The decision is whether this model is suitable for choosing residues for our G12D assay construct before Friday’s compound-design handoff.

**You**:

what evidence would make the model suitable or unsuitable for selecting residues

**Dr. Yuki Tanaka**:

It’s suitable only if the model represents the **same protein used in the assay**, contains the relevant folded domain, and gives a credible shape for the nucleotide pocket and switch regions. It’s unsuitable if the protein differs at pocket-forming positions, has a different extent, or the pocket is poorly defined—even if the confidence numbers look respectable. Do you want me to focus on the pocket geometry or on whether the model and assay protein are actually the same?

**You**:

Does the AlphaFold Database accession in your bundle correspond to exactly the same UniProt entry, isoform, and residue numbering as your assay construct's sequence and does that construct already carry the G12D mutation, or is G12D introduced separately from what's in the folded model?

**Dr. Yuki Tanaka**:

No. **My assay protein is G12D and contains residues 1–169**; the AlphaFold model I downloaded is the standard KRAS sequence, not the G12D construct, and it includes the longer tail. I haven’t checked the database record identifier against the construct sequence—sequence bookkeeping is your side—but residue 12 is the important difference: Asp in my assay protein, Gly in the downloaded model. That matters directly at the nucleotide/switch-region pocket; can you give me the exact yes/no call before Friday?

**You**:

are you asking whether to use the downloaded model as-is, whether it can be mapped/interpreted onto your G12D construct, or whether it should be rejected outright and what would make each of those three outcomes acceptable to you?

**Dr. Yuki Tanaka**:

The real decision is **whether it is safe to choose residues for the G12D, residues 1–169 assay protein from that downloaded model**. Used exactly as downloaded: **no**—it has Gly at 12 and the extra tail. If you can sensibly interpret the pocket with Asp12 and ignore the tail, that could be acceptable; otherwise reject it for this handoff. I need you to tell me which of those is defensible, not give me three labels.

**You**:

What's the exact AlphaFold DB accession number and version/download date for the model you have, and can you send me the FASTA for both the full downloaded model's sequence and your 1–169 G12D construct so I can align them residue-by-residue myself rather than relying on 'standard KRAS' and 'longer tail' as descriptions?

**Dr. Yuki Tanaka**:

I don’t have the exact AlphaFold accession, release/version, or download date recorded here, and I can’t reproduce the two file contents from memory. What I can state precisely is that the assay construct is **KRAS residues 1–169 with Asp at position 12**, whereas the downloaded model is the standard sequence with **Gly12 and a longer tail**. You’ll need to read the identifiers and FASTA strings directly from the bundle; for Friday, treat the downloaded model as a structural template, not as the literal assay protein.

**You**:

Where in the data bundle are the accession/version metadata, both FASTA sequences, and the confidence files actually located and if any of them turn out to be missing or undocumented once I look, should I treat that as unresolved and flag it for Friday, or attempt to derive it myself (e.g. reading the accession from the file header, or aligning the sequences directly) before treating the model as a usable template?

**Dr. Yuki Tanaka**:

The bundle locations are simply:

- `KRAS_alphafold_model.cif` — folded model and any embedded header metadata.
- `my_construct.fasta` — the 1–169 assay construct.
- `KRAS_alphafold_pae.json` — the accompanying confidence data.

There isn’t a separate metadata or second FASTA file that I know of. If the accession, release information, or model sequence is not clearly documented in the CIF, flag provenance as unresolved; comparing the two sequences directly can establish what differs, but it cannot recover a missing database record. For Friday, I’d use it only as a **provisional template**, not declare it validated for residue selection.

**You**:

For the confidence file does your existing familiarity with pLDDT/PAE give you a threshold you already trust for calling a region 'usable' for residue selection (e.g. a pLDDT cutoff, or a PAE value you'd accept at the pocket), or is establishing that threshold also part of what you need from me for Friday?

**Dr. Yuki Tanaka**:

No threshold I trust. The confidence file is there, but deciding whether its numbers support residue-level pocket selection is your side; a good-looking value alone doesn’t make the Gly12 model suitable for my Asp12 assay. For Friday, give me a yes/no on the **actual pocket and switch-region residues**, using the confidence data as supporting evidence rather than the decision itself.

**You**:

For Friday's handoff, what exact deliverable do you need from me — a residue-by-residue yes/no on each switch-region/pocket residue, a confidence-ranked shortlist of which residues are safe to build into the compound-design brief, or an explicit 'cannot assess' verdict if the mismatch can't be resolved and how much residual uncertainty can that handoff actually tolerate before it's unsafe to proceed?

**Dr. Yuki Tanaka**:

I need **one clear overall verdict**: **yes or no** for choosing residues for the G12D, 1–169 assay construct. Include a short residue-level table for the pocket and switch regions, marking each as usable, uncertain, or not defensible, with position 12 called out explicitly.

If the sequence difference or the tail makes that assessment unreliable, the deliverable is **“cannot assess safely,” not a confidence-ranked shopping list**. The handoff cannot tolerate uncertainty at residue 12 or at residues whose side chains define the pocket; uncertainty in the distant, removed tail is irrelevant.

**You**:

What operationally separates 'usable' from 'uncertain' from 'not defensible' for a given residue — is that a pLDDT cutoff you want me to propose and justify, a PAE-to-neighboring-pocket-residue threshold, or does a residue automatically land in 'not defensible' if it's Gly12 itself or anything whose side-chain identity/conformation depends on Gly12 versus Asp12, regardless of what the confidence number says?

**Dr. Yuki Tanaka**:

It is **not a single confidence cutoff**. For this handoff:

- **Usable:** the residue is present in the assay construct, its side chain is the same, and the local pocket geometry is credible.
- **Uncertain:** the chemistry is unchanged but the local shape or side-chain placement is not reliable enough to design against confidently.
- **Not defensible:** residue 12 itself, and any direct pocket contact whose placement or chemistry is materially altered by replacing Gly12 with Asp12. A reassuring confidence value does not rescue that.

I would not automatically discard every nearby residue—only those whose interaction surface depends on the Gly12-to-Asp12 change. Can you identify those direct contacts from the model and mark the rest separately?
