# Attribution

## fullstack-dev-skills (40 skills)

The following 40 skills were added from
[**Jeffallan/claude-skills**](https://github.com/Jeffallan/claude-skills)
(the `fullstack-dev-skills` pack), licensed under the **MIT License**
(© Jeffallan). The full upstream license text is in
[`LICENSE-fullstack-dev-skills`](LICENSE-fullstack-dev-skills), and each skill's
`SKILL.md` retains its original `license: MIT` and `author` frontmatter.

Only the subset relevant to data/BI, Python, SQL/Databricks, React/TypeScript,
MCP, Azure/DevOps, security, and testing was included (off-domain skills such as
mobile, game, CMS/e-commerce, and non-React frontend frameworks were not).

**API & architecture:** api-designer, architecture-designer, microservices-architect, mcp-developer
**Backend:** fastapi-expert
**Data & ML:** pandas-pro, spark-engineer, ml-pipeline, fine-tuning-expert, rag-architect, prompt-engineer
**Frontend (React/TS):** react-expert, nextjs-developer, typescript-pro, javascript-pro
**Infrastructure:** cloud-architect, database-optimizer, kubernetes-specialist, postgres-pro, terraform-engineer
**Languages:** python-pro, sql-pro
**DevOps & SRE:** devops-engineer, monitoring-expert, sre-engineer, chaos-engineer, cli-developer
**Quality:** code-reviewer, code-documenter, debugging-wizard, test-master, playwright-expert
**Security:** secure-code-guardian, security-reviewer, fullstack-guardian
**Platform:** atlassian-mcp
**Specialized & workflow:** legacy-modernizer, spec-miner, feature-forge, the-fool

## Data, cloud & infrastructure (18 skills)

Curated from official vendor skill repos (discovered via the
[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
index). Each skill retains its upstream `SKILL.md` and frontmatter; full upstream
license texts are in [`licenses/`](licenses/).

| Source repo | License | License file | Skills |
| --- | --- | --- | --- |
| [microsoft/skills](https://github.com/microsoft/skills) | MIT | `licenses/microsoft-skills-MIT.txt` | azure-storage-blob-py, azure-storage-file-datalake-py, azure-monitor-query-py, azure-mgmt-fabric-py, azure-search-documents-py, azure-identity-py, azure-keyvault-py, fastapi-router-py, pydantic-models-py, azure-ai-projects-py, azure-ai-ml-py |
| [ClickHouse/agent-skills](https://github.com/ClickHouse/agent-skills) | Apache-2.0 | `licenses/clickhouse-agent-skills-APACHE-2.0.txt` (+ `-NOTICE.txt`) | clickhouse-best-practices, clickhouse-architecture-advisor, chdb-sql, chdb-datastore |
| [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) | Apache-2.0 | `licenses/neon-agent-skills-APACHE-2.0.txt` | neon-postgres |
| [hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) | MPL-2.0 | `licenses/hashicorp-agent-skills-MPL-2.0.txt` | terraform-style-guide, azure-verified-modules |

> Tinybird skills (tinybirdco/tinybird-agent-skills) were intentionally **not** included:
> that repo has no license, so redistribution terms are unclear. Install locally if needed via
> `npx skills add https://github.com/tinybirdco/tinybird-agent-skills --skill <name>`.
