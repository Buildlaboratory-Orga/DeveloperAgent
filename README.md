# DeveloperAgent

Test repository for an autonomous bug-fixing agent, built for the module "Artificial Intelligence and Virtual Robotics".
A Jira bug ticket starts an agent workflow in archmax. The agent reproduces the bug in a Daytona sandbox, fixes it, tests it and opens a pull request. A human reviews and approves it, then the agent merges.

## How the agent works with this repository

| Account | Role |
|---|---|
| `developeragent-bot` | The agent. Pushes `fix/<ticket key>` branches, opens pull requests and squash-merges them after approval. Its token is limited to this repository (code and pull requests only). |
| `BuildLaboratory` | Organization owner, human code reviewer and code owner. Only this account can approve a pull request. As owner it may push directly to `main`; this is used only to set up and clean up test bugs for test runs and to maintain the repository setup (e.g. workflow, `CODEOWNERS`). |

Rules on `main` (ruleset `protect-main`):

- changes only via pull request, no direct push by the agent
- one approval by the code owner, stale approvals are dismissed after a new push
- required check `tests` (`.github/workflows/tests.yml`): runs the unit tests and fails if a pull request of the agent changes `tests/` or `.github/`
- squash merge only

Commits made from the maintainer's machine (setting up and cleaning up test bugs) show the author `louis0403`, because the local Git e-mail is linked to that account; they were pushed with the owner account.

All fixes by the agent are visible under **Pull requests → Closed** (author `developeragent-bot`). Each pull request describes the cause, the change and the test result; since #11 it also contains the reproduction script the agent used.

## Contents

`mathtools/` contains 13 small modules with simple math functions. They are the test object for the agent workflow.

| Module | Functions |
|---|---|
| `basic_ops.py` | `add`, `subtract`, `multiply`, `divide` |
| `powers.py` | `square`, `cube`, `power`, `square_root` |
| `stats.py` | `mean`, `median`, `minimum`, `maximum`, `value_range` |
| `geometry.py` | `rectangle_area`, `rectangle_perimeter`, `triangle_area`, `circle_area`, `circle_circumference` |
| `percentages.py` | `percent_of`, `percent_change`, `apply_discount`, `add_vat` |
| `number_theory.py` | `is_even`, `is_prime`, `gcd`, `lcm` |
| `sequences.py` | `factorial`, `fibonacci`, `sum_up_to` |
| `conversions.py` | `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, `km_to_miles`, `miles_to_km` |
| `finance.py` | `simple_interest`, `compound_interest`, `annuity_payment`, `break_even_units` |
| `vectors.py` | `add_vectors`, `scale_vector`, `dot_product`, `vector_length` |
| `matrix.py` | `transpose`, `multiply`, `determinant`, `solve` |
| `regression.py` | `normal_matrix`, `polynomial_fit`, `predict`, `r_squared` |
| `trend.py` | `is_stable`, `trend_report` |

Each module has a test file in `tests/`.

## Running the tests

Requires only Python 3.10+ (no extra packages). In the root folder of the repository:

```bash
python3 -m unittest discover -s tests -v
```

Green tests do not prove that the code is free of bugs: some functions are only tested for simple cases. That is why the agent writes its own reproduction script for every ticket.
