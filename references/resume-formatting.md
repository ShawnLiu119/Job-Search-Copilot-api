# Resume format preflight and one-page normalization

Use this reference before tailoring any resume. Treat extracted text as content evidence and rendered pages as layout evidence. Never overwrite the master resume.

## 1. Source-format preflight

Use the PDF skill for PDF inputs and the Documents skill for DOCX inputs. Extract the text, render every page to PNG, and inspect the images at normal reading size.

Record these findings in `source/resume-format-report.md`:

- File type, page count, page size, and whether text extraction succeeds.
- Whether the extracted reading order matches the visible reading order.
- Whether name, contact line, summary, experience, education, and skills are recognizable.
- Whether employment titles, employers, dates, and bullets stay paired correctly.
- Multi-column layout, tables used for positioning, text boxes, icons, charts, skill bars, photos, or header/footer contact data.
- Clipped, overlapping, missing, unusually small, or low-contrast text.
- Inconsistent margins, fonts, spacing, bullets, date alignment, or section hierarchy.
- Dense sections, excessive empty space, orphan headings, awkward page breaks, and repeated content.

Set `source_format_status` to:

- `pass`: extraction order is reliable, the layout is readable and ATS-safe, and the source is a sound layout base.
- `normalize`: any material reading-order, structure, legibility, consistency, or ATS risk exists. When uncertain, normalize.

Do not declare a layout sound from text extraction alone.

## 2. Canonical one-page resume

When normalization is required, rebuild the resume from verified source content rather than repairing fragile positioning. Save an editable DOCX and a rendered PDF when the runtime supports both.

Use this order unless the candidate's evidence strongly supports a different one:

1. Name and single-line contact block
2. Target headline or two-to-three-line professional summary
3. Core skills grouped into compact, truthful categories
4. Professional experience in reverse chronology
5. Education and relevant certifications

Use a single-column, ATS-safe structure. Do not use tables for layout, text boxes, sidebars, icons, photos, charts, logos, skill bars, decorative headers, or contact details in headers/footers. Use real text and standard bullets.

## 3. Formatting contract

- Page: US Letter for US searches; use A4 only when the target market or user requires it.
- Length: exactly one page.
- Margins: 0.50–0.70 inches; never below 0.45 inches.
- Body font: Arial, Calibri, Aptos, Helvetica, or another conservative sans serif at 9.5–11 pt.
- Name: 16–20 pt. Section headings: 10.5–12 pt, bold.
- Line spacing: 1.0–1.12. Keep consistent paragraph spacing and visible separation between sections.
- Color: black or near-black body text; at most one restrained dark accent with sufficient contrast.
- Dates: use one consistent format and align them consistently without floating text boxes.
- Bullets: concise action + scope/method + outcome where evidence allows. Preserve every original metric and qualifier.
- Links: use human-readable LinkedIn or portfolio labels; ensure the visible text remains meaningful when printed.

Do not solve overflow by shrinking the body below 9.5 pt, reducing margins below 0.45 inches, hiding text, tightening lines until they collide, or deleting evidence essential to role chronology.

## 4. One-page content budget

Fit the page through relevance, not visual compression:

1. Remove duplicated summary and skill language.
2. Prefer the most recent and role-relevant achievements.
3. Keep three to five strong bullets for the most relevant recent role and one to three for other roles.
4. Compress older or less relevant roles to title, employer, dates, and at most one high-value bullet when needed.
5. Remove generic soft-skill claims and unsupported proficiency labels.
6. Keep education and certifications compact.

Preserve employer names, official historical titles, dates, education, credentials, and factual continuity. Record material omissions in the job-specific change log.

## 5. Final acceptance gates

For the canonical resume and every tailored variant:

1. Reopen the final file successfully.
2. Confirm the document has exactly one page.
3. Extract text and confirm the reading order is name/contact, summary or headline, skills, experience, then education/certifications.
4. Confirm titles, employers, dates, bullets, and metrics remain correctly associated.
5. Render the latest version to PNG and visually inspect the entire page.
6. Confirm no clipping, overlap, broken glyphs, awkward wrapping, orphan headings, excessive whitespace, or edge-hugging text.
7. Confirm consistent margins, font hierarchy, spacing, bullets, and date alignment.
8. Confirm body text is at least 9.5 pt and visually readable at normal zoom.
9. Confirm the resume contains no hidden text, keyword stuffing, unsupported claims, or accidental job-description content.
10. Compare tailored variants and confirm each has material, evidence-backed job-specific differences.

If any gate fails, revise and repeat extraction plus visual rendering. Do not deliver a file with a failed or unverified gate.
