# Which changes stock implementation review sees

Research for [Verify which changes the stock implementation review actually sees](https://github.com/manansanghani69/Software-Factory-2/issues/3), a child of [Human-driven AI SDLC — decision map](https://github.com/manansanghani69/Software-Factory-2/issues/1). Inspected on 2026-10-07. This establishes coverage facts and possible adaptations; it does not decide the human's branch, commit, or review policy.

## Finding

The prescribed `git diff <fixed-point>...HEAD` excludes newly written work until committed, whether tracked unstaged, staged, or untracked. The disposable fixture below reproduces that for all three states. If only uncommitted changes exist, the stock empty-diff gate stops review; if previous branch commits exist, that gate passes but still excludes the new work. This is an inference from the pinned contracts and the recorded Git outputs, not an observed execution of an AI review.

## Pinned contracts and installed comparison

Inspected upstream revision: [`6fd947921b935b7e1e69293a200400f0fdd5c15f`](https://github.com/mattpocock/skills/commit/6fd947921b935b7e1e69293a200400f0fdd5c15f). The two primary-source contracts are:

- [implement](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/implement/SKILL.md): implement, test, invoke review, then commit on the current branch. Its text supplies neither a review baseline nor a branch-creation step.
- [code-review](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/code-review/SKILL.md): ask for a missing fixed point; validate its ref and nonempty three-dot diff; give that command and `git log <fixed-point>..HEAD --oneline` to separate Standards and Spec reviewers. It reports findings; it does not specify remediation or a re-review loop. Spec discovery may rely on commit references, then explicit path, then branch-matching files; missing spec may skip that axis.

Local inspection found `/Users/manansanghani/.agents/skills/code-review/SKILL.md` byte-identical to the pinned upstream. `/Users/manansanghani/.agents/skills/implement/SKILL.md` differs in only two invocation lines: “Call the Skill tool” becomes `/tdd` and `/code-review` usage. Review still precedes commit. These are inspection facts about these exact paths; other installations or later edits are not covered.

| File | Upstream SHA-256 | Installed SHA-256 |
| --- | --- | --- |
| implement | `f28bed1a2a7dcf604c802a99869bae9d577b6bfc2061fe655c8b0dbb1ee16cfd` | `6d3fd9e83b8f36e5213854779db49b256a457a7ebb4a503e53fa7dcff696adc3` |
| code-review | `47f4e52c21694def9c7c11cbfbf891ca35eac7a93e395797515be3c8a409ae50` | `47f4e52c21694def9c7c11cbfbf891ca35eac7a93e395797515be3c8a409ae50` |

Recheck a pinned file without following a moving branch:

```sh
gh api 'repos/mattpocock/skills/contents/skills/engineering/code-review/SKILL.md?ref=6fd947921b935b7e1e69293a200400f0fdd5c15f' -H 'Accept: application/vnd.github.raw+json' | shasum -a 256
shasum -a 256 /Users/manansanghani/.agents/skills/code-review/SKILL.md
```

## What each comparison targets

Three-dot diff compares merge-base to the second commit. Plain diff compares index to working tree; `--cached` compares a commit to index; one commit compares that commit to working tree. Two commits compare their trees, and therefore do not include index or working-tree edits. [Git diff reference](https://git-scm.com/docs/git-diff/2.54.0).

A staged snapshot can differ from its working-tree file: adding captures the contents at that moment, and later edits require another add to enter the next commit. [Git add reference](https://git-scm.com/docs/git-add).

Untracked inventory needs separate enumeration. `git ls-files --others --exclude-standard -z` supplies NUL-delimited paths excluding standard ignored files. It supplies names, not their content. [Git ls-files reference](https://git-scm.com/docs/git-ls-files). `git status --porcelain=v1 -uall` provides a state inventory including individual untracked files; ignored files need an explicit check if they could contain intended changes. [Git status reference](https://git-scm.com/docs/git-status).

## Disposable fixture and observed evidence

Ran with `git version 2.54.0 (Apple Git-157)` and Python 3. Each case has its own temporary repository, a baseline commit tagged `baseline`, and independent files for committed, unstaged, and staged modifications. The staged case also adds a new staged file; the mixed case combines all states. Global Git configuration and hooks are disabled for the fixture. No fixture lives in the project.

Command labels in the output:

| Label | Exact command |
| --- | --- |
| stock | `git diff --name-only baseline...HEAD` |
| unstaged | `git diff --name-only` |
| staged | `git diff --cached --name-only HEAD` |
| HEAD worktree | `git diff --name-only HEAD` |
| base index | `git diff --cached --name-only baseline` |
| base worktree | `git diff --name-only baseline` |
| untracked | `git ls-files --others --exclude-standard` |

Observed output (temporary root omitted; `(empty)` is zero output). File lists are fixture evidence, not a quality assessment:

```text
| Case | status | stock | unstaged | staged | HEAD worktree | base index | base worktree | untracked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| committed | (empty) | committed.txt | (empty) | (empty) | (empty) | committed.txt | committed.txt | (empty) |
| tracked-unstaged | M unstaged.txt | (empty) | unstaged.txt | (empty) | unstaged.txt | (empty) | unstaged.txt | (empty) |
| staged | A  new-staged.txt; M  staged.txt | (empty) | (empty) | new-staged.txt; staged.txt | new-staged.txt; staged.txt | new-staged.txt; staged.txt | new-staged.txt; staged.txt | (empty) |
| untracked | ?? untracked.txt | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | untracked.txt |
| mixed | A  new-staged.txt; M  staged.txt;  M unstaged.txt; ?? untracked.txt | committed.txt | unstaged.txt | new-staged.txt; staged.txt | new-staged.txt; staged.txt; unstaged.txt | committed.txt; new-staged.txt; staged.txt | committed.txt; new-staged.txt; staged.txt; unstaged.txt | untracked.txt |
mixed stock patch:
diff --git a/committed.txt b/committed.txt
index df967b9..25cf1ca 100644
--- a/committed.txt
+++ b/committed.txt
@@ -1 +1 @@
-base
+committed change
mixed untracked patch:
diff --git a/untracked.txt b/untracked.txt
new file mode 100644
index 0000000..19c0595
--- /dev/null
+++ b/untracked.txt
@@ -0,0 +1 @@
+untracked change
mixed commit log:
feature change
staged then reverted worktree:
stock => (empty)
unstaged => staged.txt
staged => staged.txt
HEAD worktree => (empty)
base index => staged.txt
base worktree => (empty)
untracked => (empty)
divergent target...HEAD => committed.txt
divergent target HEAD => committed.txt; target-only.txt
divergent merge-base vs worktree => committed.txt
```

The mixed stock patch contains only `committed.txt`, even though status inventories four additional changed files. `git log baseline..HEAD` lists only the existing feature commit. Staging the new file makes it visible to index/working-tree comparisons, but never to the stock comparison before committing.

The staged-then-reverted case demonstrates a subtler difference: `git diff HEAD` is empty although the index still holds `staged candidate`. A review of the working-tree result alone would miss what a plain next commit would contain. Conversely, an index-only review would miss tracked unstaged edits.

The divergent-target case gives `committed.txt` for `target...HEAD`, but `committed.txt; target-only.txt` for `target HEAD`: the latter includes the disappearance of target-only work that is absent on the feature branch. Thus switching to `git diff <fixed-point>` alone silently changes the baseline if that ref has diverged. Explicit merge-base plus a working-tree comparison retains the stock ancestor orientation. These conclusions follow from the fixture outputs; the three-dot equivalence is documented in the [Git diff reference](https://git-scm.com/docs/git-diff/2.54.0).

### Reproduce

Save the following as a temporary `.py` file outside the project and run `python3 /path/to/file.py`. It creates fresh temporary repositories and prints the evidence above. Their random absolute path and commit identifiers are immaterial; the file lists and patches are reproducible. Temporary fixtures are left for inspection and may be removed afterward.

```python
from pathlib import Path
import os, subprocess, tempfile

root = Path(tempfile.mkdtemp(prefix='sdlc-review-fixture-'))
env = os.environ.copy()
env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
           GIT_AUTHOR_NAME='Fixture', GIT_AUTHOR_EMAIL='fixture@example.invalid',
           GIT_COMMITTER_NAME='Fixture', GIT_COMMITTER_EMAIL='fixture@example.invalid',
           GIT_AUTHOR_DATE='2026-10-07T00:00:00+00:00',
           GIT_COMMITTER_DATE='2026-10-07T00:00:00+00:00')

def git(repo, *args):
    p = subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c',
                        'core.autocrlf=false', *args], cwd=repo, env=env,
                       text=True, capture_output=True)
    if p.returncode not in (0, 1):
        raise RuntimeError(p.stderr)
    return p.stdout.strip()

def make_repo(name):
    repo = root / name
    repo.mkdir()
    git(repo, 'init', '-q', '-b', 'feature')
    for name in ['committed.txt', 'unstaged.txt', 'staged.txt']:
        (repo / name).write_text('base\n')
    git(repo, 'add', '.')
    git(repo, 'commit', '-qm', 'baseline')
    git(repo, 'tag', 'baseline')
    return repo

commands = [
    ('stock', ['diff', '--name-only', 'baseline...HEAD']),
    ('unstaged', ['diff', '--name-only']),
    ('staged', ['diff', '--cached', '--name-only', 'HEAD']),
    ('HEAD worktree', ['diff', '--name-only', 'HEAD']),
    ('base index', ['diff', '--cached', '--name-only', 'baseline']),
    ('base worktree', ['diff', '--name-only', 'baseline']),
    ('untracked', ['ls-files', '--others', '--exclude-standard']),
]
print('fixture='+str(root))
print('| Case | status | stock | unstaged | staged | HEAD worktree | base index | base worktree | untracked |')
print('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')
for case in ['committed', 'tracked-unstaged', 'staged', 'untracked', 'mixed']:
    repo = make_repo(case)
    if case in ['committed', 'mixed']:
        (repo / 'committed.txt').write_text('committed change\n')
        git(repo, 'add', 'committed.txt')
        git(repo, 'commit', '-qm', 'feature change')
    if case in ['tracked-unstaged', 'mixed']:
        (repo / 'unstaged.txt').write_text('unstaged change\n')
    if case in ['staged', 'mixed']:
        (repo / 'staged.txt').write_text('staged change\n')
        (repo / 'new-staged.txt').write_text('staged new file\n')
        git(repo, 'add', 'staged.txt', 'new-staged.txt')
    if case in ['untracked', 'mixed']:
        (repo / 'untracked.txt').write_text('untracked change\n')
    values = [git(repo, 'status', '--porcelain=v1', '-uall')]
    values += [git(repo, *args) for _, args in commands]
    print('| '+case+' | '+' | '.join(v.replace('\n', '; ') or '(empty)' for v in values)+' |')
    if case == 'mixed':
        print('mixed stock patch:\n'+git(repo, 'diff', 'baseline...HEAD'))
        print('mixed untracked patch:\n'+git(repo, 'diff', '--no-index', '--', '/dev/null', 'untracked.txt'))
        print('mixed commit log:\n'+git(repo, 'log', 'baseline..HEAD', '--format=%s'))

repo = make_repo('staged-then-reverted-worktree')
(repo / 'staged.txt').write_text('staged candidate\n')
git(repo, 'add', 'staged.txt')
(repo / 'staged.txt').write_text('base\n')
print('staged then reverted worktree:')
for label, args in commands:
    print(label+' => '+(git(repo, *args) or '(empty)'))

repo = make_repo('divergent-baseline')
git(repo, 'branch', 'target')
(repo / 'committed.txt').write_text('feature change\n')
git(repo, 'add', 'committed.txt')
git(repo, 'commit', '-qm', 'feature change')
git(repo, 'switch', '-q', 'target')
(repo / 'target-only.txt').write_text('target change\n')
git(repo, 'add', 'target-only.txt')
git(repo, 'commit', '-qm', 'target change')
git(repo, 'switch', '-q', 'feature')
print('divergent target...HEAD => '+git(repo, 'diff', '--name-only', 'target...HEAD').replace('\n', '; '))
print('divergent target HEAD => '+git(repo, 'diff', '--name-only', 'target', 'HEAD').replace('\n', '; '))
print('divergent merge-base vs worktree => '+git(repo, 'diff', '--name-only', git(repo, 'merge-base', 'target', 'HEAD')).replace('\n', '; '))

```

## Conditional adaptation options

These are viable choices for a later human decision, not recommendations selected by this research. “Complete” below means complete for explicitly included task paths and the chosen reviewed snapshot, not every byte in an arbitrary repository.

| If the human wants… | Possible adaptation | Coverage condition / remaining work |
| --- | --- | --- |
| Stock commit comparison | Capture the intended work in local commit(s), then invoke stock review with a pinned baseline and reviewed HEAD | Override implement's ordering. Intended additions must enter the commit. Account for residual staged, unstaged, and untracked changes separately; review fixes require another reviewed commit. |
| Review before committing, against the proposed next commit | Stage intended changes and adapt both reviewers to `git diff --cached <merge-base-SHA>` | Overrides the stock comparison, not merely its baseline argument. Inspect status so unstaged edits/new files are either included or explicitly outside the candidate. Testing must refer to that candidate, which can differ from working tree. |
| Review before committing, against current working files | Pin `git merge-base <fixed-point> HEAD`; use `git diff <merge-base-SHA>` for tracked/index-known files, enumerate intended untracked files, and review their content separately | Overrides the stock comparison and empty gate. `/dev/null` versus each included new text file with `git diff --no-index` yields an addition patch in this macOS fixture; exit code 1 means difference. Working files do not certify a different staged candidate. |
| Preserve all three states as separate evidence | Supply committed diff, staged diff, unstaged diff, and included untracked contents to both reviewers | More bookkeeping: separate patches can overlap and must be interpreted as successive states, not blindly concatenated into one final patch. Declare which snapshot findings apply to. |

The patch commands and their limitations are confirmed by the fixture. A status inventory is necessary evidence of what was included or excluded; an empty committed diff alone cannot establish that there is nothing to review. Passing the adapted diff only to the parent reviewer is insufficient if either Standards or Spec sub-agent reruns the original stock command.

## Limits and newly sharp questions

- The evidence proves Git coverage, not that a model reviews every hunk correctly. No code-review sub-agent was invoked and no product review finding was fabricated.
- This fixture covers ordinary text additions and modifications. Binary content, renames, deletions, symlinks, submodules, merge conflicts, ignored intended assets, and generated outputs need project-specific inventory/review treatment; no universal content inspection claim is made for them.
- A newly initialized repository with no `HEAD` or common ancestor cannot use the stock fixed-point-to-HEAD procedure as written. An initial-snapshot route needs an explicit contract; the fixture did not test that route.
- Pinning a ref name once does not freeze a branch as it moves. A chosen review policy must bind baseline SHA, candidate snapshot, and completion evidence so later edits cannot inherit earlier review by accident.

Newly precise human question: **Which snapshot is the review approving—committed HEAD, proposed index, or current working files—and what happens when tests, staged content, or later fixes refer to a different snapshot?** Resolve that within the implementation/review decision, alongside who changes the order and who handles findings. This research does not answer it.
