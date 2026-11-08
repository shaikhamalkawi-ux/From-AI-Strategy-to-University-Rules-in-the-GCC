# ICAMAC 2026 Paper 90 — R4 reader-oriented scientific revision

Paper: **From AI Strategy to University Rules in the GCC**. Fixed 23 July 2026 evidence cutoff. The title is unchanged.

## What's new and why it matters
- A reusable named **Four-Layer Public-Evidence Audit (4L-PEA)**: Freeze -> Find -> Decide -> Release.
- A one-glance E/P/U rulebook and a worked UAE E/E/P/E classification; a grayscale-readable workflow figure.
- Separate instrument availability, directly documented policy links, and implementation evidence; only availability is measured in this study.
- Clear L3 (HE-sector control) versus L4 (at least one HEI rule) gate asymmetry.
- Simpler main-text tables and less technical prose; interval-valued fuzzy sensitivity remains secondary, explicitly not a ranking or error/recall estimate.
- A new **8-page companion PDF**: 4-page method guide + 4-page 57-institution full-name clickable evidence/search appendix.
- A **9-sheet workbook** for a reader to repeat a similar audit: layer gates, 57 locked cases, live formula-driven country summary, blank source log, bilingual search templates, independent coding form and eight public-rule fields.

## Files
- `manuscript/ICAMAC_Paper90_R4_AuthorLinked.pdf` — 4-page IEEE reader-facing version with author-linked GitHub and supplement references. **Not for blind reviewer submission.**
- `manuscript/ICAMAC_Paper90_R4_Blind.pdf` — separate 4-page blind manuscript, with no GitHub account identity in the rendered paper.
- `supplement/ICAMAC_Paper90_R4_FieldGuide_and_57_Appendix.pdf` — 8-page public companion (4-page practical guide + 4-page full-name 57-institution appendix).
- `supplement/ICAMAC_Paper90_R4_FieldGuide_and_57_Appendix_BLIND.pdf` — independent, identity-safe 8-page version for confidential review.
- `ICAMAC_Paper90_R4_Reusable_Audit_Workbook.xlsx` — editable practical field-level workbook with 57 data records and blank user forms.
- `data/` — original unchanged 57-institution key, jurisdiction matrix, scenario crosswalk, prospective blank search/source/coder templates.
- `code/` — 57-case deterministic count verifier, standard Python, no network dependency.
- `source/` — author-linked and anonymous reproducible IEEEtran LaTeX source.

## Locked empirical results
- 6 jurisdictions, 36 source records, L3 E in 1/6, L4 E in 6/6, documentary L4E/L3notE in 5/6.
- 57 selected HEIs: 20 E, 12 P, 25 U. An alternative broader UAE L3 interpretation reduces the 5/6 mismatch to 4/6.
- Fuzzy bounds represent partial categories, not uncertainty about coder accuracy or source recovery. 4L-PEA does not establish causal policy translation, university policy compliance or national population prevalence.

## Reproduce counts (from locked labels)
```sh
python3 code/reproduce_57.py
python3 code/verify_locked_outcomes.py
```
Run from any directory with the package intact. `data/` and `checks/` must be writable to save generated JSON. To redo the qualitative audit, use the blank templates and direct source URLs.

## Limitations that must remain visible
- The public 36-row source register is provisional: not every official document's exact passage and archive hash has been independently reverified.
- Historical exact web queries and the complete original pre-outcome institution-eligibility universe were not fully frozen.
- There has been no independent double-coding, Cohen kappa or independent bilingual adjudication.
- No DOI or author-approved code/data license is asserted.
- Third-party official documents are linked, not redistributed.

**Public reproducibility branch:** https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/tree/main/ICAMAC2026_Paper90_R4_57
**Direct linked companion:** https://github.com/shaikhamalkawi-ux/From-AI-Strategy-to-University-Rules-in-the-GCC/blob/main/ICAMAC2026_Paper90_R4_57/supplement/ICAMAC_Paper90_R4_FieldGuide_and_57_Appendix.pdf
