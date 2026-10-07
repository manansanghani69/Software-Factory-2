# Issue tracker: GitHub

Issues and specs live in GitHub Issues for
`manansanghani69/Software-Factory-2`. Use the `gh` CLI
from this repo; it infers the repository from the remote.

## Conventions

- Create: `gh issue create --title "..." --body-file <file>`.
- Read: `gh issue view <number> --comments`; also fetch labels.
- List: `gh issue list --state open --json number,title,body,labels`.
- Comment: `gh issue comment <number> --body-file <file>`.
- Label: `gh issue edit <number> --add-label "..."`.
- Remove label: `gh issue edit <number> --remove-label "..."`.
- Close: `gh issue close <number> --comment "..."`.

Use a temporary UTF-8 file for multiline bodies.

## Skill instructions

When a skill says "publish to the issue tracker", create
a GitHub issue. When it says "fetch the relevant ticket",
read the issue, its comments, and labels.

## Pull requests as a triage surface

**PRs as a request surface: no.**
