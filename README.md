# Job Search Copilot

A human-in-the-loop Codex skill for a traceable job-search workflow:

- discover and rank roles from a resume and optional keywords;
- confirm location, remote-work, and relocation preferences before sourcing;
- scan and normalize weak or non-standard resume layouts;
- create a truthful, clean one-page resume for every shortlisted role;
- identify relevant networking prospects; and
- draft LinkedIn and informational-interview outreach without sending it; and
- generate five evidence-backed mock interview questions for every shortlisted role.

The repository contains the reusable workflow definition, data model, matching and tailoring rules, outreach guidance, and a local workspace initializer. It intentionally excludes real resumes, job-search ledgers, tailored outputs, and contact data.

## User input

Upload your existing resume in PDF or DOCX format. This is the only required starting file. Job-title keywords are optional; when none are provided, the workflow derives suitable role families from the resume.

## Repository layout

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── data-model.md
│   ├── match-and-tailor.md
│   ├── mock-interviews.md
│   ├── outreach.md
│   └── resume-formatting.md
└── scripts/init_workspace.py
```

## Initialize a local workspace

Python 3.10+ is sufficient; the initializer uses only the standard library.

```bash
python3 scripts/init_workspace.py \
  --root ./job-search-workspace \
  --resume /path/to/resume.pdf \
  --keyword "Data Scientist"
```

The command creates a resumable local workspace and preserves the master resume. Before sourcing jobs, the workflow requires confirmation of allowed locations, accepted work arrangements, and relocation willingness.

Before tailoring, the skill renders and scans the source layout. A weak, multi-column, table-based, image-only, clipped, or inconsistently formatted resume is rebuilt as a canonical one-page ATS-safe resume. Every job-specific variant must then pass both text-order and rendered-page quality gates.

For every shortlisted job, the workflow also researches official company material and public candidate-reported interview history, then creates five distinct mock interview questions with competencies, evaluation points, resume evidence hooks, follow-ups, and source labels.

## Privacy and safety

- Resume and contact data stay local unless the user explicitly authorizes another destination.
- The workflow never applies to jobs or sends outreach without separate approval.
- Resume tailoring may reorder or rephrase supported evidence, but must not fabricate experience, titles, tools, credentials, dates, or metrics.
- Missing requirements are recorded as gaps rather than inserted as unsupported keywords.

## Use as a Codex skill

Place this directory in your Codex skills folder, then invoke `$job-search-copilot` with a PDF or DOCX resume. Job keywords are optional; when omitted, the workflow derives role families from resume evidence.
