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

## Wayfinding operations

Use GitHub's native sub-issues for membership and native issue
dependencies for blocking. Issue numbers identify API paths;
relationship payloads use the numeric database `id` returned by
`gh api repos/{owner}/{repo}/issues/{number}`.

- Map: an issue labelled `wayfinder:map`.
- Decision ticket: a native child of the map, with exactly one
  `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`,
  or `wayfinder:task` label.
- Claim: assign the ticket to the developer driving the map before
  starting work. An open ticket with any assignee is claimed.
- Resolution: post a resolution comment, close the ticket, then
  append its named link and a one-line gist to the map's
  Decisions so far. Research assets are linked from the resolution.

### Native relationships

Use `gh api` with the repository inferred from this checkout:

```sh
# List children in their native priority order; paginate all results.
gh api --paginate 'repos/{owner}/{repo}/issues/MAP_NUMBER/sub_issues?per_page=100'

# Attach an existing issue as a child; CHILD_ID is its database id.
gh api --method POST repos/{owner}/{repo}/issues/MAP_NUMBER/sub_issues -F sub_issue_id=CHILD_ID

# List a ticket's blockers; inspect each blocker's state.
gh api --paginate 'repos/{owner}/{repo}/issues/TICKET_NUMBER/dependencies/blocked_by?per_page=100'

# Record that BLOCKER_ID blocks TICKET_NUMBER.
gh api --method POST repos/{owner}/{repo}/issues/TICKET_NUMBER/dependencies/blocked_by -F issue_id=BLOCKER_ID
```

Create issues first, then attach children and wire blockers.
Decomposition and blocking are separate relationships.

### Frontier query

Load the map, then list all native children. Keep children that are
open and have no assignees. For each candidate, load all native
blockers and retain it only when every blocker is closed. Preserve
native child priority order; the first retained child is the default
next ticket. Re-read its state and assignees immediately before
claiming. GitHub assignment is not an atomic lock; if another session
also claims it, coordinate before doing duplicate work.

Keep open tickets discoverable through this query. The map body is
an index of resolved decisions and fog, rather than a second backlog.

API references: [sub-issues](https://docs.github.com/en/rest/issues/sub-issues)
and [issue dependencies](https://docs.github.com/en/rest/issues/issue-dependencies).
