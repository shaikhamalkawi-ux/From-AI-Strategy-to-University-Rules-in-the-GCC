# ICAMAC 2026 Paper 90 — 57-case, eight-page reviewer response (R2, 2026-11-08)

## Direct supplementary-material links for paper readers

**Current author-linked reading copy — R3:** [8-page PDF](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R2_57/manuscript/ICAMAC2026_Paper90_R3_AuthorLinked_8pages.pdf) | [editable LaTeX](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R2_57/latex/ICAMAC2026_8page_R3_Author_Linked_Supplement_Explicit.tex). This editorial R3 version explicitly names and links the companion **Supplementary Materials PDF** in the paper text; it retains the R2 57-case data and does not change the existing scientific results. The older R2 PDF remains available for comparison.

- [**Open/download the 3-page supplementary appendix (57 institutions, PDF)**](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R2_57/supplement/ICAMAC2026_Paper90_57_Institutions_Supplement.pdf)
- [Download the 57-institution linked evidence key (CSV)](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R2_57/data/ICAMAC2026_57_Institution_Clickable_Key.csv)
- [36-source evidence register (PROVISIONAL, CSV)](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R2_57/data/ICAMAC2026_Paper90_36_Source_Register_PROVISIONAL.csv) — documentary audit remains subject to the re-verification limits described below.

The paper's repository link leads here; the items above are the intended supplementary materials for the **57-case** ICAMAC 2026 paper, not the 58-case historical repository-root snapshot.

Paper: **From AI Strategy to University Rules in the GCC**. This folder is the **version-matched research data/code record for the 57-institution R2 conference manuscript**. The separate 58-institution root snapshot in the same GitHub repository is NOT the analytical input for this paper.

**Paper baseline:** 6 GCC jurisdictions, official-source register of 36 records, July 23 2026 evidence cutoff; 57 university cases: E=20, P=12, U=25; L3 explicitly traceable in 1/6, L4 in 6/6; L4E and L3-not-E in 5/6; bounded fuzzy gap 0.500. These counts describe public documentation under declared gates, not implementation, causality, country ranking, compliance, or population prevalence.

## Files
- `data/ICAMAC2026_57_Institution_Clickable_Key.csv`: **the exact 57 labels, states and retained URLs extracted from the submitted six-page paper**, with unlocated cases labelled as search/context locators, not affirmative policy citations.
- `data/ICAMAC2026_6_Jurisdiction_Layer_Matrix.csv`: six locked L1–L4 categorical profiles.
- `data/ICAMAC2026_57_Jurisdiction_State_Counts.csv`: deterministic aggregation.
- `data/ICAMAC2026_57_vs_58_Membership_Crosswalk.csv`: three changed membership rows underlying the 57/58 difference.
- `data/ICAMAC2026_Paper90_36_Source_Register_PROVISIONAL.csv`: exact 36-row source register recovered from the repository history; source-level claims and key passages have **not all been independently reverified** for this version.
- `code/reproduce_57.py`: **Python 3 standard library only**, reruns deterministic categorical counts and bounds.
- `latex/`: editable IEEEtran article source for the R1 blind version and R2 author-linked copy; figures/tables in source or in text.
- `manuscript/`: the author-linked 8-page PDF. The unchanged R1 blind 8-page PDF remains in the controlled local delivery, not in this public author-identifying repository.
- `supplement/`: 3-page 57-link appendix PDF.
- `checks/`: QA records, numerical reproduction JSON, and reviewer-response provenance (R1 reviewer report retained as historical).

## Reproduce
```sh
python3 code/reproduce_57.py
```
The script asserts locked inputs and creates `checks/REPRODUCED_57_COUNTS.json`. This is a **computational reproduction from existing coder decisions**, not human independent double coding or source-level web recovery.

## Avoid cross-version confusion
The older 58-case root data contains American University of Sharjah (E) and University of Dubai (P), while the corrected 57-case table includes the EIBFS (U) case in the UAE private/non-government stratum. The 57-case membership is tied to the documented 1983 founding-year eligibility correction. The old root `reproduce.py` is **not** a reproduction of the Paper 90 57-case results. Do not cite 21/13/24 as results of Paper 90.

## Evidence boundaries / review transparency
The original complete pre-outcome eligible universe is not available. All official source URLs and code gates require auditing; URL retrieval and web layout can change. The 36-row source register provides source identity and coding rationales, but not a verified verbatim passage and authorized archival snapshot for every row. This edition **does not** claim independent intercoder agreement, finished Arabic-English adjudication, or full archival reproducibility. Official source documents are linked, **not redistributed**.

## Review anonymity, rights, citation
The public repository identifies its account owner. **Do not put this repository address in a strictly anonymized review submission without written venue approval.** Use the blind manuscript variant for that workflow; use the R2 author-linked variant for camera ready/author review. The formal software/data license and a DOI still require author decisions, and third-party official PDFs are not included. Please cite the eventual published paper when available rather than assigning a fabricated DOI.

Versioned link: https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/tree/main/ICAMAC2026_Paper90_R2_57
