# Session handoff

Use repository-relative paths (or stable URLs) and an immutable revision for every
authoritative record. `working-tree` is allowed only for an uncommitted draft; an
approved record must name a commit, tag, or review snapshot. Do not write vague
labels such as “current brief” without its exact path and revision.

Project root:
Definition index: <path> @ <revision>
Active slice record: <path> @ <revision>
Current brief: <path> @ <revision>
Latest gate record: <path> @ <revision> (or none)
Active map/frontier index: <path> @ <revision> (or none)
Current document manifest: <path> @ <revision> (or none)
Existing source documents consulted:
- <path or URL> @ <revision>

Scope / slice:
Artifacts changed:
- <repository-relative path> @ <revision>
Settled decisions and evidence:
- <decision or claim> — <authoritative source path/URL> @ <revision>
Open frontier / fog:
- <question or next frontier>
Stale records or blocking prerequisites:
- <record/path and reason>, or `none`
Latest valid gate and approved revisions:
- <gate> — <pass/revise/spike/defer/stop>, <record path> @ <revision>
Next valid manual invocation: <skill name> for <project/slice>
Required inputs for that invocation:
- <exact path or URL> @ <revision>
Expected output / gate or human decision:
- <artifact, gate result, or decision>
