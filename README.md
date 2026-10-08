# BAS preparation and lodgment support prototype

A five-agent Python prototype for small-business BAS preparation. It uses evidence-linked records, independent compliance review, client approval, and simulated lodgment. It does not lodge with the ATO or provide professional tax advice.

## Workflow

`A1 onboarding -> A2 ledger -> A3 BAS preparation -> A4 compliance -> A5 approval and simulated lodgment`

The supervisor coordinates handoffs. Agents do not approve their own work or overwrite an earlier approved version. Shared services will own audit records, versioned data, and common interfaces.

## Layout

| Path | Responsibility |
| --- | --- |
| `bas/agents/a1_onboarding/` | Client profile, evidence requests, workflow access |
| `bas/agents/a2_ledger/` | Evidence-linked ledger, GST classification, verified snapshot |
| `bas/agents/a3_bas_preparation/` | Deterministic BAS draft, insights, optional forecast |
| `bas/agents/a4_compliance/` | Independent transaction and BAS verification |
| `bas/agents/a5_lodgment/` | Client approval, simulated submission, status |
| `bas/shared/` | Common records and services |
| `bas/supervisor/` | Workflow routing and handoffs |
| `tests/` | Automated tests |
| `data/` | Synthetic development data only |

## Local setup

Use Python 3.11 or newer. No third-party packages are required yet.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m unittest discover -s tests
```

The framework, persistence layer, and package contracts have not been selected. Agree on those before implementing agent logic. See [CONTRIBUTING.md](CONTRIBUTING.md) for team conventions.
