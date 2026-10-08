# Team conventions

- Create a branch per Jira story and include its key, for example `SCRUM-12-ledger-import`.
- Include the same key in commits and pull request titles so Jira can link the work.
- Keep each change within its agent or shared ownership boundary. Coordinate shared contract changes before merging.
- Run `python -m unittest discover -s tests` before a pull request. Add tests for new behaviour.
- Use synthetic or anonymised data only. Do not commit client records, credentials, `.env` files, or local databases.
- A4 alone records compliance decisions. A5 requires A4 approval and client approval for the same package version before simulated submission.
