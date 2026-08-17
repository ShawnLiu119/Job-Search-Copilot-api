# Workspace data model

Use the initialized workspace as the persistent audit trail. Keep paths relative to its root when possible.

## Layout

```text
job-search-workspace/
├── config.json
├── jobs.jsonl
├── contacts.jsonl
├── source/master-resume.ext
├── job-descriptions/
├── tailored-resumes/
├── outreach/
└── runs/
```

## `config.json`

Keep these keys stable:

```json
{
  "schema_version": 1,
  "resume": {"path": "source/master-resume.ext", "sha256": "..."},
  "keywords": [],
  "inferred_role_families": [],
  "preferences": {
    "locations": [],
    "work_arrangements": [],
    "relocation_willingness": "unknown",
    "preferences_confirmed_at": null,
    "industries": [],
    "seniority": [],
    "salary": null,
    "work_authorization": "unknown",
    "sponsorship_required": "unknown"
  },
  "exclusions": [],
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601"
}
```

Require `locations`, `work_arrangements`, and `relocation_willingness` to be explicitly confirmed before first-run sourcing. Allow `locations: ["any"]` and `work_arrangements: ["remote", "hybrid", "on-site"]` when the user has no restrictions. Preserve other unknown values; do not convert them into exclusions.

## `jobs.jsonl`

Write one JSON object per observation. Use `job_key` for de-duplication and retain updated observations as new lines.

Required fields: `job_key`, `observed_at`, `source`, `native_id`, `url`, `company`, `title`, `location`, `posted_at`, `description_path`, `status`, `blockers`, `score`, `score_breakdown`, `resume_evidence`, `gaps`, and `run_id`.

For every `tailored` job, also record `tailored_resume_path` and `change_log_path`. The files must be job-specific rather than aliases of another role's output.

Allowed status progression: `discovered`, `shortlisted`, `tailored`, `approved`, `applied`, `declined`, `closed`. Never mark `applied` without user confirmation.

## `contacts.jsonl`

Required fields: `contact_key`, `observed_at`, `name`, `profile_url`, `company`, `title`, `relationship_type`, `relevance_reason`, `personalization_hooks`, `job_keys`, `status`, and `run_id`.

Allowed statuses: `suggested`, `drafted`, `approved`, `contacted`, `replied`, `declined`. Never mark `contacted` without user confirmation.

## Run files

Use `runs/YYYY-MM-DDTHHMMSSZ/summary.md` and include:

1. Inputs and assumptions
2. Queries and sources
3. New, changed, duplicate, and excluded counts
4. Ranked jobs with evidence and gaps
5. Tailored outputs and change logs
6. Contacts and outreach drafts
7. Errors, access restrictions, and next actions
