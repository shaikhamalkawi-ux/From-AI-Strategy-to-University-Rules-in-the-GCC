# From AI Strategy to University Rules in the GCC — reproducibility archive

This repository contains **two distinct analytical snapshots**. **Do not combine their institution counts or scripts.**

## Current ICAMAC 2026 Paper 90 reviewer-response snapshot: **57 institutions**

[**ICAMAC2026 Paper 90 — version-matched 57-case data, source register, code, manuscript and appendix**](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/tree/main/ICAMAC2026_Paper90_R2_57)

- Fixed document cutoff: **23 July 2026**; six GCC jurisdictions; 36 official-source records.
- Panel: **N=57**, E=20, P=12, U=25; L3 explicit=1/6 and L4 explicit=6/6.
- Reader source is eight IEEE pages; supplementary link key is three pages.
- Reproduction: `python3 ICAMAC2026_Paper90_R2_57/code/reproduce_57.py`.
- **Source/independent-coding holds:** historical documentary states were not independently double-coded, nor were all Arabic-English source passages/archival hashes reverified in this revision. Code reproduces finite-corpus arithmetic from locked labels, not missing documents, compliance or causality.
- **Blind-review warning:** this GitHub account is author-identifiable. A separate blind paper exists; do not put the link to the public repository in a strictly anonymous manuscript without conference permission.

## Earlier research snapshot: **58 institutions — not Paper 90's 57-case table**

The original repository-root `data/P2_58_*` files and `reproduce.py` preserve a separate 58-case release candidate (E=21, P=13, U=24). It includes two 1997 UAE private institutions that the corrected 57-case panel excludes, and it omits the 1983 EIBFS case admitted to the 57-case panel. The original 58-case analysis is retained as **historical** for traceability, not as the reproduction data for the ICAMAC Paper 90 revision. See [cross-version note](https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/tree/main/ICAMAC2026_Paper90_R2_57/VERSION_SCOPE_AND_DIFFERENCES.md).

The shared source-level 36-record register is also preserved at `data/P2_ITT2026_36_Source_Register_Current.csv`; a frozen copy with explicit provenance limitations is included in the 57-case folder.

## Rights, DOI and limitations

This repository is **public**, but an explicit author-approved license has not yet been selected. Third-party university/government PDF documents are linked as sources, **not redistributed**. No archival DOI, independent coder agreement coefficient, or full web-source regeneration is claimed. Cite the eventual ICAMAC proceedings article once bibliographic details exist.
