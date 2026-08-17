---
name: job-search-copilot
description: Find and rank suitable jobs from a resume and optional job keywords, confirm geographic and remote-work preferences before sourcing, create a truthful job-specific resume for every shortlisted role, identify 3–5 relevant networking prospects at target companies, and draft personalized informational-interview outreach. Use when Codex needs to run a one-time or recurring job-search workflow, compare a resume with job postings, adapt resumes for ATS relevance, research LinkedIn networking contacts, or prepare connection notes and emails without automatically applying or sending messages. Supports PDF and DOCX resumes and resume-first discovery when the user provides no keywords.
---

# Job Search Copilot

Run a traceable, human-in-the-loop job search. Require only a resume; treat job keywords as optional. Never apply, send a message, or alter an external account unless the user explicitly asks for that separate action.

## Start the workspace

1. Locate the resume attachment or path. If several resumes are present and no master version is evident, ask which one to use.
2. Choose an output root supplied by the user. Otherwise use `job-search-workspace/` in the current workspace.
3. Run `scripts/init_workspace.py --root <root> --resume <resume>`. Add each explicit keyword with `--keyword`. Re-running must preserve ledgers and prior outputs.
4. Read `references/data-model.md` before writing or updating state.
5. Use the PDF or Documents skill to extract the resume while preserving the source file. Keep all resume and contact data local unless the user authorizes another destination.

## Build the search profile

Extract evidence-backed fields from the resume: current/recent titles, seniority, functional strengths, industries, hard skills, location, education, certifications, languages, and measurable outcomes. Do not infer protected traits.

If keywords are present, normalize them into titles, skills, industries, and exclusions. If they are absent, infer 3–8 plausible role families from the strongest recent evidence. Include adjacent roles only when at least two resume signals support them. Record inferred queries and assumptions in `config.json` so the user can correct them later.

Before sourcing jobs, ask one compact preference question covering:

- Allowed locations or geographic radius
- Accepted work arrangements: remote, hybrid, and/or on-site
- Willingness to relocate or commute beyond the stated area

Treat this as a required first-run checkpoint because it materially changes the candidate set. Offer `no geographic restriction` as a valid answer. Save the answer in `config.json` and reuse it on later runs; ask again only when the user changes it or requests a broader search. Do not infer that the resume address is a hard location constraint.

Do not block on other missing preferences such as salary, work authorization, or sponsorship. Mark them `unknown` and avoid using them as hard filters until known.

## Source jobs

1. Prefer a purpose-built connector or API when one is available. Otherwise use the Browser or Chrome skill with the user's existing signed-in session.
2. Search LinkedIn and any other user-approved platforms with title, skill, and role-family variants. For a recurring run, prioritize postings not previously recorded.
3. Stop and ask the user to sign in if authentication is required. Stop on CAPTCHA, access restrictions, or requests to bypass platform protections.
4. Capture only information visible to the user: native job ID when available, URL, source, title, company, location, work arrangement, posting date, description, compensation, and application method.
5. De-duplicate first by native ID, then canonical URL, then normalized company + title + location. Append evidence to `jobs.jsonl`; never silently replace history.

Aim for 10–20 fresh postings per run, then retain the best 5–10 after scoring. Return fewer when evidence is limited instead of padding the list.

## Score matches

Read `references/match-and-tailor.md`. Check explicit blockers first, such as an incompatible work location, required license, required clearance, or work authorization constraint. Do not invent a blocker when the user's preference is unknown.

Score non-blocked roles from 0–100:

- Role and title alignment: 0–30
- Required skills backed by resume evidence: 0–30
- Responsibility and achievement similarity: 0–20
- Seniority and scope: 0–10
- Industry/domain relevance: 0–10

For every component, cite the relevant job requirement and resume evidence. Label missing requirements as `gap`, not as possessed skills. Use `strong` for 80–100, `possible` for 65–79, and `low` below 65. Shortlist preference-compatible strong matches and preference-compatible possible matches with a credible evidence path. Exclude low matches from tailoring unless the user explicitly selects one.

## Tailor the resume

Create a separate resume version for every shortlisted job. Never use one generic tailored resume for several postings. Preserve the master resume unchanged and retain the original file type when practical.

Allowed edits:

- Align the headline or target title without changing an actual employment title.
- Reorder truthful skills and bullets to surface relevant evidence.
- Use job-description terminology when it accurately describes existing experience.
- Tighten summaries and bullets, and replace vague wording with existing measured outcomes.

Never fabricate employment, dates, titles, responsibilities, tools, credentials, education, metrics, or proficiency. Never insert keywords invisibly or create keyword stuffing. If a useful requirement lacks evidence, place it in the gap report rather than the resume.

For each shortlisted job:

1. Extract that posting's distinct required skills, responsibilities, seniority signals, industry language, and repeated ATS terms.
2. Create a dedicated resume whose headline, summary, skill ordering, and bullet ordering/wording respond to that posting's evidence.
3. Save it as `tailored-resumes/<company>__<role>__<native-id>.<ext>` using filesystem-safe slugs.
4. Save a companion `tailored-resumes/<company>__<role>__<native-id>__changes.md` containing original text, revised text, job requirement addressed, evidence basis, and risk.
5. Reopen and verify the output, then mark only that job `tailored`.

Do not satisfy this requirement by copying the same file under different names. Each resume must contain material, evidence-backed differences tied to its job description. If no truthful change is available for a section, preserve it and say so in the change log.

Use the Documents skill for every DOCX variant's rendering and verification; use the PDF skill for every PDF variant's rendering and inspection. Return a manifest mapping each job URL to its resume and change log.

## Find networking prospects

For each priority company, identify 3–5 visible, relevant people. Prefer this order:

1. People in the same or closely adjacent function
2. Potential peers or team members in similar roles
3. Shared school, former employer, professional group, or location
4. Likely hiring manager when the reporting relationship is supported
5. Relevant recruiter or talent partner

Record name, public profile URL, current title, relevance reason, personalization hooks, and evidence source. Do not collect private contact information, guess email addresses, or claim a relationship that is not visible. De-duplicate against `contacts.jsonl` and avoid repeatedly suggesting previously declined contacts.

## Draft outreach

Read `references/outreach.md`. Produce for each recommended contact:

- A LinkedIn connection note no longer than 300 characters
- A follow-up LinkedIn message of roughly 60–120 words
- An optional email subject and message of roughly 90–160 words when a user-provided or publicly authorized address exists

Ask for 15–20 minutes and seek perspective, not a referral or job. Use one specific, verifiable personalization hook. Never imply that the person reviewed the resume or invited contact.

Save all drafts for review. Do not send them.

## Finish each run

Write a run summary containing search queries, sources checked, new and duplicate counts, blockers, ranked jobs, tailored files, suggested contacts, draft locations, and recommended next actions. Include source links beside claims.

For recurring operation, reuse the workspace ledgers and process only new or materially changed postings. If the user explicitly asks to schedule the workflow but provides no cadence, propose Monday/Wednesday/Friday at 9:00 AM local time. Create or change an automation only after the user authorizes scheduling.

## Human approval gates

Require explicit user approval before:

- Submitting an application
- Sending a LinkedIn request, message, or email
- Changing a public profile
- Uploading a resume or personal data to a new service
- Replacing the master resume
