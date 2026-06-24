# claude-skills

A curated collection of **162 [Claude Agent Skills](https://agentskills.io)**. Each skill is a folder with a `SKILL.md` plus any supporting `references/`, `scripts/`, or `assets/`.

## Install

**Claude Code** — copy a skill folder into your skills directory, then restart Claude Code:

```bash
git clone https://github.com/simonpsson/claude-skills.git
cp -r claude-skills/<skill-name> ~/.claude/skills/
```

**Claude chat / Cowork** — zip a skill folder and upload it at claude.ai → Settings → Capabilities → Skills:

```bash
cd claude-skills && zip -r <skill-name>.zip <skill-name>
```

## Skills

162 skills, grouped by area. Click a name for its `SKILL.md`. Regenerate this list with `python scripts/gen_readme.py`.

### Analysis, BI & general (35)

| Skill | Description |
| --- | --- |
| [ab-test-analysis](ab-test-analysis/SKILL.md) | Rigorous A/B test statistical analysis. |
| [analysis-assumptions-log](analysis-assumptions-log/SKILL.md) | Track and document analytical assumptions and decisions. |
| [analysis-documentation](analysis-documentation/SKILL.md) | Structured, reproducible analysis documentation. |
| [analysis-planning](analysis-planning/SKILL.md) | Structure analysis approach before starting work. |
| [analysis-qa-checklist](analysis-qa-checklist/SKILL.md) | Pre-delivery quality assurance for analysis work. |
| [analysis-retrospective](analysis-retrospective/SKILL.md) | Post-analysis learning and process improvement. |
| [business-metrics-calculator](business-metrics-calculator/SKILL.md) | Standard business metric calculation with industry benchmarks. |
| [cohort-analysis](cohort-analysis/SKILL.md) | Time-based cohort analysis with retention and behaviour tracking. |
| [context-packager](context-packager/SKILL.md) | Efficiently package context for AI-assisted analysis. |
| [dashboard-specification](dashboard-specification/SKILL.md) | Design specifications for effective dashboards. |
| [data-catalog-entry](data-catalog-entry/SKILL.md) | Create standardized metadata for data assets. |
| [data-narrative-builder](data-narrative-builder/SKILL.md) | Build compelling data-driven narratives. |
| [data-quality-audit](data-quality-audit/SKILL.md) | Comprehensive data quality assessment against business rules, schema constraints, and freshness expectations. |
| [executive-summary-generator](executive-summary-generator/SKILL.md) | Create concise executive summaries from detailed analysis. |
| [funnel-analysis](funnel-analysis/SKILL.md) | Conversion funnel analysis with drop-off investigation. |
| [image-gen](image-gen/SKILL.md) | Generate images from a text prompt via Hugging Face. |
| [impact-quantification](impact-quantification/SKILL.md) | Estimate and communicate business impact of insights. |
| [insight-synthesis](insight-synthesis/SKILL.md) | Transform data findings into compelling insights. |
| [methodology-explainer](methodology-explainer/SKILL.md) | Explain analysis methodology to diverse audiences. |
| [metric-reconciliation](metric-reconciliation/SKILL.md) | Cross-source metric validation and discrepancy investigation. |
| [peer-review-template](peer-review-template/SKILL.md) | Structured peer review for analytical work. |
| [planning-with-files](planning-with-files/SKILL.md) | Implements Manus-style file-based planning to organize and track progress on complex tasks. |
| [programmatic-eda](programmatic-eda/SKILL.md) | Systematic exploratory data analysis. |
| [query-validation](query-validation/SKILL.md) | SQL query review for correctness, performance, and best practices. |
| [root-cause-investigation](root-cause-investigation/SKILL.md) | Systematic investigation of metric changes and anomalies. |
| [schema-mapper](schema-mapper/SKILL.md) | Database schema understanding and relationship mapping. |
| [segmentation-analysis](segmentation-analysis/SKILL.md) | Customer/user segmentation with actionable insights. |
| [semantic-model-builder](semantic-model-builder/SKILL.md) | Build structured semantic layer documentation for metrics, dimensions, and entities. |
| [sql-to-business-logic](sql-to-business-logic/SKILL.md) | Translate SQL queries into plain language business logic. |
| [stakeholder-requirements-gathering](stakeholder-requirements-gathering/SKILL.md) | Structured requirements elicitation for analysis requests. |
| [sv3d](sv3d/SKILL.md) | Stable Video 3D (SV3D) — turn a SINGLE image of an object into an orbital novel-view VIDEO (image→video/3D). |
| [technical-to-business-translator](technical-to-business-translator/SKILL.md) | Translate technical analysis into business language. |
| [time-series-analysis](time-series-analysis/SKILL.md) | Temporal pattern detection and forecasting. |
| [visualization-builder](visualization-builder/SKILL.md) | Create effective, publication-ready data visualizations. |
| [web-artifacts-builder](web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). |

### Power BI (3)

| Skill | Description |
| --- | --- |
| [pbi-report-builder](pbi-report-builder/SKILL.md) | [power-bi] Power BI PBIR Report Builder with IBCS Visuals. |
| [pbi-requirements-gathering](pbi-requirements-gathering/SKILL.md) | [power-bi] Power BI Requirements Gathering — a structured, conversation-driven skill that captures everything needed before building a Power BI solution. |
| [pbip-dependency-analyzer](pbip-dependency-analyzer/SKILL.md) | Power BI PBIP Dependency Analyzer. |

### Data, cloud & infrastructure (18)

> Curated from official vendor skill repos (Microsoft, ClickHouse, Neon, HashiCorp). See [ATTRIBUTION.md](ATTRIBUTION.md).

| Skill | Description |
| --- | --- |
| [azure-ai-ml-py](azure-ai-ml-py/SKILL.md) | Azure Machine Learning SDK v2 for Python. |
| [azure-ai-projects-py](azure-ai-projects-py/SKILL.md) | Build AI applications using the Azure AI Projects Python SDK (azure-ai-projects). |
| [azure-identity-py](azure-identity-py/SKILL.md) | Azure Identity SDK for Python authentication with Microsoft Entra ID. |
| [azure-keyvault-py](azure-keyvault-py/SKILL.md) | Azure Key Vault SDK for Python. |
| [azure-mgmt-fabric-py](azure-mgmt-fabric-py/SKILL.md) | Azure Fabric Management SDK for Python. |
| [azure-monitor-query-py](azure-monitor-query-py/SKILL.md) | Azure Monitor Query SDK for Python. |
| [azure-search-documents-py](azure-search-documents-py/SKILL.md) | Azure AI Search SDK for Python. |
| [azure-storage-blob-py](azure-storage-blob-py/SKILL.md) | Azure Blob Storage SDK for Python. |
| [azure-storage-file-datalake-py](azure-storage-file-datalake-py/SKILL.md) | Azure Data Lake Storage Gen2 SDK for Python. |
| [azure-verified-modules](azure-verified-modules/SKILL.md) | Azure Verified Modules (AVM) requirements and best practices for developing certified Azure Terraform modules. |
| [chdb-datastore](chdb-datastore/SKILL.md) | Use when the user has tabular data (pandas DataFrame, parquet, csv, Arrow, json) and wants to filter, group, aggregate, join, or speed up slow pandas. |
| [chdb-sql](chdb-sql/SKILL.md) | Use when the user wants to run SQL — especially analytical SQL — on local files (parquet/csv/json), URLs, S3 paths, or remote databases (Postgres, MySQL, MongoDB, ClickHouse Cloud, Iceberg, Delta Lake) without setting... |
| [clickhouse-architecture-advisor](clickhouse-architecture-advisor/SKILL.md) | MUST USE when designing ClickHouse architectures, selecting between ingestion or modeling patterns, or translating best practices into workload-specific system designs. |
| [clickhouse-best-practices](clickhouse-best-practices/SKILL.md) | MUST USE when reviewing ClickHouse schemas, queries, or configurations. |
| [fastapi-router-py](fastapi-router-py/SKILL.md) | Create FastAPI routers with CRUD operations, authentication dependencies, and proper response models. |
| [neon-postgres](neon-postgres/SKILL.md) | Guides and best practices for working with Neon Serverless Postgres. |
| [pydantic-models-py](pydantic-models-py/SKILL.md) | Create Pydantic models following the multi-model pattern with Base, Create, Update, Response, and InDB variants. |
| [terraform-style-guide](terraform-style-guide/SKILL.md) | Generate Terraform HCL code following HashiCorp's official style conventions and best practices. |

### Full-stack development (40)

> Added from [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) (MIT). See [ATTRIBUTION.md](ATTRIBUTION.md).

| Skill | Description |
| --- | --- |
| [api-designer](api-designer/SKILL.md) | Use when designing REST or GraphQL APIs, creating OpenAPI specifications, or planning API architecture. |
| [architecture-designer](architecture-designer/SKILL.md) | Use when designing new high-level system architecture, reviewing existing designs, or making architectural decisions. |
| [atlassian-mcp](atlassian-mcp/SKILL.md) | Integrates with Atlassian products to manage project tracking and documentation via MCP protocol. |
| [chaos-engineer](chaos-engineer/SKILL.md) | Designs chaos experiments, creates failure injection frameworks, and facilitates game day exercises for distributed systems — producing runbooks, experiment manifests, rollback procedures, and post-mortem templates. |
| [cli-developer](cli-developer/SKILL.md) | Use when building CLI tools, implementing argument parsing, or adding interactive prompts. |
| [cloud-architect](cloud-architect/SKILL.md) | Designs cloud architectures, creates migration plans, generates cost optimization recommendations, and produces disaster recovery strategies across AWS, Azure, and GCP. |
| [code-documenter](code-documenter/SKILL.md) | Generates, formats, and validates technical documentation — including docstrings, OpenAPI/Swagger specs, JSDoc annotations, doc portals, and user guides. |
| [code-reviewer](code-reviewer/SKILL.md) | Analyzes code diffs and files to identify bugs, security vulnerabilities (SQL injection, XSS, insecure deserialization), code smells, N+1 queries, naming issues, and architectural concerns, then produces a structured... |
| [database-optimizer](database-optimizer/SKILL.md) | Optimizes database queries and improves performance across PostgreSQL and MySQL systems. |
| [debugging-wizard](debugging-wizard/SKILL.md) | Parses error messages, traces execution flow through stack traces, correlates log entries to identify failure points, and applies systematic hypothesis-driven methodology to isolate and resolve bugs. |
| [devops-engineer](devops-engineer/SKILL.md) | Creates Dockerfiles, configures CI/CD pipelines, writes Kubernetes manifests, and generates Terraform/Pulumi infrastructure templates. |
| [fastapi-expert](fastapi-expert/SKILL.md) | Use when building high-performance async Python APIs with FastAPI and Pydantic V2. |
| [feature-forge](feature-forge/SKILL.md) | Conducts structured requirements workshops to produce feature specifications, user stories, EARS-format functional requirements, acceptance criteria, and implementation checklists. |
| [fine-tuning-expert](fine-tuning-expert/SKILL.md) | Use when fine-tuning LLMs, training custom models, or adapting foundation models for specific tasks. |
| [fullstack-guardian](fullstack-guardian/SKILL.md) | Builds security-focused full-stack web applications by implementing integrated frontend and backend components with layered security at every level. |
| [javascript-pro](javascript-pro/SKILL.md) | Writes, debugs, and refactors JavaScript code using modern ES2023+ features, async/await patterns, ESM module systems, and Node.js APIs. |
| [kubernetes-specialist](kubernetes-specialist/SKILL.md) | Use when deploying or managing Kubernetes workloads. |
| [legacy-modernizer](legacy-modernizer/SKILL.md) | Designs incremental migration strategies, identifies service boundaries, produces dependency maps and migration roadmaps, and generates API facade designs for aging codebases. |
| [mcp-developer](mcp-developer/SKILL.md) | Use when building, debugging, or extending MCP servers or clients that connect AI systems with external tools and data sources. |
| [microservices-architect](microservices-architect/SKILL.md) | Designs distributed system architectures, decomposes monoliths into bounded-context services, recommends communication patterns, and produces service boundary diagrams and resilience strategies. |
| [ml-pipeline](ml-pipeline/SKILL.md) | Designs and implements production-grade ML pipeline infrastructure: configures experiment tracking with MLflow or Weights & Biases, creates Kubeflow or Airflow DAGs for training orchestration, builds feature store sch... |
| [monitoring-expert](monitoring-expert/SKILL.md) | Configures monitoring systems, implements structured logging pipelines, creates Prometheus/Grafana dashboards, defines alerting rules, and instruments distributed tracing. |
| [nextjs-developer](nextjs-developer/SKILL.md) | Use when building Next.js 14+ applications with App Router, server components, or server actions. |
| [pandas-pro](pandas-pro/SKILL.md) | Performs pandas DataFrame operations for data analysis, manipulation, and transformation. |
| [playwright-expert](playwright-expert/SKILL.md) | Use when writing E2E tests with Playwright, setting up test infrastructure, or debugging flaky browser tests. |
| [postgres-pro](postgres-pro/SKILL.md) | Use when optimizing PostgreSQL queries, configuring replication, or implementing advanced database features. |
| [prompt-engineer](prompt-engineer/SKILL.md) | Writes, refactors, and evaluates prompts for LLMs — generating optimized prompt templates, structured output schemas, evaluation rubrics, and test suites. |
| [python-pro](python-pro/SKILL.md) | Use when building Python 3.11+ applications requiring type safety, async programming, or robust error handling. |
| [rag-architect](rag-architect/SKILL.md) | Designs and implements production-grade RAG systems by chunking documents, generating embeddings, configuring vector stores, building hybrid search pipelines, applying reranking, and evaluating retrieval quality. |
| [react-expert](react-expert/SKILL.md) | Use when building React 18+ applications in .jsx or .tsx files, Next.js App Router projects, or create-react-app setups. |
| [secure-code-guardian](secure-code-guardian/SKILL.md) | Use when implementing authentication/authorization, securing user input, or preventing OWASP Top 10 vulnerabilities — including custom security implementations such as hashing passwords with bcrypt/argon2, sanitizing... |
| [security-reviewer](security-reviewer/SKILL.md) | Identifies security vulnerabilities, generates structured audit reports with severity ratings, and provides actionable remediation guidance. |
| [spark-engineer](spark-engineer/SKILL.md) | Use when writing Spark jobs, debugging performance issues, or configuring cluster settings for Apache Spark applications, distributed data processing pipelines, or big data workloads. |
| [spec-miner](spec-miner/SKILL.md) | Reverse-engineering specialist that extracts specifications from existing codebases. |
| [sql-pro](sql-pro/SKILL.md) | Optimizes SQL queries, designs database schemas, and troubleshoots performance issues. |
| [sre-engineer](sre-engineer/SKILL.md) | Defines service level objectives, creates error budget policies, designs incident response procedures, develops capacity models, and produces monitoring configurations and automation scripts for production systems. |
| [terraform-engineer](terraform-engineer/SKILL.md) | Use when implementing infrastructure as code with Terraform across AWS, Azure, or GCP. |
| [test-master](test-master/SKILL.md) | Generates test files, creates mocking strategies, analyzes code coverage, designs test architectures, and produces test plans and defect reports across functional, performance, and security testing disciplines. |
| [the-fool](the-fool/SKILL.md) | Use when challenging ideas, plans, decisions, or proposals using structured critical reasoning. |
| [typescript-pro](typescript-pro/SKILL.md) | Implements advanced TypeScript type systems, creates custom type guards, utility types, and branded types, and configures tRPC for end-to-end type safety. |

### GSD project workflow (66)

| Skill | Description |
| --- | --- |
| [gsd-add-tests](gsd-add-tests/SKILL.md) | Generate tests for a completed phase based on UAT criteria and implementation |
| [gsd-ai-integration-phase](gsd-ai-integration-phase/SKILL.md) | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| [gsd-audit-fix](gsd-audit-fix/SKILL.md) | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| [gsd-audit-milestone](gsd-audit-milestone/SKILL.md) | Audit milestone completion against original intent before archiving |
| [gsd-audit-uat](gsd-audit-uat/SKILL.md) | Cross-phase audit of all outstanding UAT and verification items |
| [gsd-autonomous](gsd-autonomous/SKILL.md) | Run all remaining phases autonomously — discuss→plan→execute per phase |
| [gsd-capture](gsd-capture/SKILL.md) | Capture ideas, tasks, notes, and seeds to their destination |
| [gsd-cleanup](gsd-cleanup/SKILL.md) | Archive accumulated phase directories from completed milestones |
| [gsd-code-review](gsd-code-review/SKILL.md) | Review source files changed during a phase for bugs, security issues, and code quality problems |
| [gsd-complete-milestone](gsd-complete-milestone/SKILL.md) | Archive completed milestone and prepare for next version |
| [gsd-config](gsd-config/SKILL.md) | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| [gsd-debug](gsd-debug/SKILL.md) | Systematic debugging with persistent state across context resets |
| [gsd-discuss-phase](gsd-discuss-phase/SKILL.md) | Gather phase context through adaptive questioning before planning. |
| [gsd-docs-update](gsd-docs-update/SKILL.md) | Generate or update project documentation verified against the codebase |
| [gsd-eval-review](gsd-eval-review/SKILL.md) | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| [gsd-execute-phase](gsd-execute-phase/SKILL.md) | Execute all plans in a phase with wave-based parallelization |
| [gsd-explore](gsd-explore/SKILL.md) | Socratic ideation and idea routing — think through ideas before committing to plans |
| [gsd-extract-learnings](gsd-extract-learnings/SKILL.md) | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| [gsd-fast](gsd-fast/SKILL.md) | Execute a trivial task inline — no subagents, no planning overhead |
| [gsd-forensics](gsd-forensics/SKILL.md) | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| [gsd-graphify](gsd-graphify/SKILL.md) | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| [gsd-health](gsd-health/SKILL.md) | Diagnose planning directory health and optionally repair issues |
| [gsd-help](gsd-help/SKILL.md) | Show available GSD commands and usage guide |
| [gsd-import](gsd-import/SKILL.md) | Ingest external plans with conflict detection against project decisions before writing anything. |
| [gsd-inbox](gsd-inbox/SKILL.md) | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| [gsd-ingest-docs](gsd-ingest-docs/SKILL.md) | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| [gsd-manager](gsd-manager/SKILL.md) | Interactive command center for managing multiple phases from one terminal |
| [gsd-map-codebase](gsd-map-codebase/SKILL.md) | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| [gsd-milestone-summary](gsd-milestone-summary/SKILL.md) | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| [gsd-mvp-phase](gsd-mvp-phase/SKILL.md) | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| [gsd-new-milestone](gsd-new-milestone/SKILL.md) | Start a new milestone cycle — update PROJECT.md and route to requirements |
| [gsd-new-project](gsd-new-project/SKILL.md) | Initialize a new project with deep context gathering and PROJECT.md |
| [gsd-ns-context](gsd-ns-context/SKILL.md) | codebase intelligence \| map graphify docs learnings |
| [gsd-ns-ideate](gsd-ns-ideate/SKILL.md) | exploration capture \| explore sketch spike spec capture |
| [gsd-ns-manage](gsd-ns-manage/SKILL.md) | config workspace \| workstreams thread update ship inbox |
| [gsd-ns-project](gsd-ns-project/SKILL.md) | project lifecycle \| milestones audits summary |
| [gsd-ns-review](gsd-ns-review/SKILL.md) | quality gates \| code review debug audit security eval ui |
| [gsd-ns-workflow](gsd-ns-workflow/SKILL.md) | workflow \| discuss plan execute verify phase progress |
| [gsd-pause-work](gsd-pause-work/SKILL.md) | Create context handoff when pausing work mid-phase |
| [gsd-phase](gsd-phase/SKILL.md) | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases |
| [gsd-plan-phase](gsd-plan-phase/SKILL.md) | Create detailed phase plan (PLAN.md) with verification loop |
| [gsd-plan-review-convergence](gsd-plan-review-convergence/SKILL.md) | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. |
| [gsd-pr-branch](gsd-pr-branch/SKILL.md) | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| [gsd-profile-user](gsd-profile-user/SKILL.md) | Generate developer behavioral profile and create Claude-discoverable artifacts |
| [gsd-progress](gsd-progress/SKILL.md) | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| [gsd-quick](gsd-quick/SKILL.md) | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| [gsd-resume-work](gsd-resume-work/SKILL.md) | Resume work from previous session with full context restoration |
| [gsd-review](gsd-review/SKILL.md) | Request cross-AI peer review of phase plans from external AI CLIs |
| [gsd-review-backlog](gsd-review-backlog/SKILL.md) | Review and promote backlog items to active milestone |
| [gsd-secure-phase](gsd-secure-phase/SKILL.md) | Retroactively verify threat mitigations for a completed phase |
| [gsd-settings](gsd-settings/SKILL.md) | Configure GSD workflow toggles and model profile |
| [gsd-ship](gsd-ship/SKILL.md) | Create PR, run review, and prepare for merge after verification passes |
| [gsd-sketch](gsd-sketch/SKILL.md) | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| [gsd-spec-phase](gsd-spec-phase/SKILL.md) | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| [gsd-spike](gsd-spike/SKILL.md) | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| [gsd-stats](gsd-stats/SKILL.md) | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| [gsd-thread](gsd-thread/SKILL.md) | Manage persistent context threads for cross-session work |
| [gsd-ui-phase](gsd-ui-phase/SKILL.md) | Generate UI design contract (UI-SPEC.md) for frontend phases |
| [gsd-ui-review](gsd-ui-review/SKILL.md) | Retroactive 6-pillar visual audit of implemented frontend code |
| [gsd-ultraplan-phase](gsd-ultraplan-phase/SKILL.md) | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| [gsd-undo](gsd-undo/SKILL.md) | Safe git revert. |
| [gsd-update](gsd-update/SKILL.md) | Update GSD to latest version with changelog display |
| [gsd-validate-phase](gsd-validate-phase/SKILL.md) | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| [gsd-verify-work](gsd-verify-work/SKILL.md) | Validate built features through conversational UAT |
| [gsd-workspace](gsd-workspace/SKILL.md) | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| [gsd-workstreams](gsd-workstreams/SKILL.md) | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |

## Attribution & license

Skills retain their original `license` and `author` frontmatter. The full-stack development skills come from [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) (MIT) — full text in [`LICENSE-fullstack-dev-skills`](LICENSE-fullstack-dev-skills) and [`ATTRIBUTION.md`](ATTRIBUTION.md).
