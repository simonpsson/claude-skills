# claude-skills

A collection of 102 [Claude Agent Skills](https://agentskills.io). Each skill is a folder containing a `SKILL.md` plus any supporting assets, scripts, and references.

## Install

**Claude Code** — copy a skill folder into your skills directory:

```bash
git clone https://github.com/simonpsson/claude-skills.git
cp -r claude-skills/<skill-name> ~/.claude/skills/
```

**Claude chat / Cowork** — upload the matching archive from [`zips/`](zips/) at claude.ai → Settings → Capabilities → Skills.

## Skills

| Skill | Description |
| --- | --- |
| [$(ab-test-analysis.Name)](ab-test-analysis/SKILL.md) | Rigorous A/B test statistical analysis. Use when analyzing experiment results, calculating statistical significance, checking for sample ratio mismatch, or validating test design before launch. |
| [$(analysis-assumptions-log.Name)](analysis-assumptions-log/SKILL.md) | Track and document analytical assumptions and decisions. Use when making analytical choices, documenting trade-offs, ensuring transparency, or creating audit trails for analytical work. |
| [$(analysis-documentation.Name)](analysis-documentation/SKILL.md) | Structured, reproducible analysis documentation. Use when documenting analysis findings, creating analysis notebooks, ensuring reproducibility, or building analysis archives for future reference. |
| [$(analysis-planning.Name)](analysis-planning/SKILL.md) | Structure analysis approach before starting work. Use when receiving new analysis requests, breaking down complex questions into steps, or planning iterative analysis workflows. |
| [$(analysis-qa-checklist.Name)](analysis-qa-checklist/SKILL.md) | Pre-delivery quality assurance for analysis work. Use when reviewing analysis before sharing with stakeholders, checking for completeness, validating assumptions, or ensuring clarity of recommendations. |
| [$(analysis-retrospective.Name)](analysis-retrospective/SKILL.md) | Post-analysis learning and process improvement. Use when completing major analysis projects, documenting lessons learned, or improving team analytical practices. |
| [$(business-metrics-calculator.Name)](business-metrics-calculator/SKILL.md) | Standard business metric calculation with industry benchmarks. Use when calculating SaaS metrics (MRR, churn, LTV, CAC), e-commerce KPIs, or product analytics metrics with proper definitions. |
| [$(cohort-analysis.Name)](cohort-analysis/SKILL.md) | Time-based cohort analysis with retention and behaviour tracking. Activate when you need to measure how groups of users/customers behave over time — retention rates, revenue by cohort, or feature adoption curves. |
| [$(context-packager.Name)](context-packager/SKILL.md) | Efficiently package context for AI-assisted analysis. Use when preparing to work with Claude on analysis, organizing context documents, or structuring prompts for complex analytical tasks. |
| [$(dashboard-specification.Name)](dashboard-specification/SKILL.md) | Design specifications for effective dashboards. Use when planning new dashboards, improving existing ones, or documenting dashboard requirements before development starts. |
| [$(data-catalog-entry.Name)](data-catalog-entry/SKILL.md) | Create standardized metadata for data assets. Use when documenting new datasets, building data catalogs, improving data discoverability, or creating data dictionaries for teams. |
| [$(data-narrative-builder.Name)](data-narrative-builder/SKILL.md) | Build compelling data-driven narratives. Use when presenting analysis results, creating stakeholder reports, or transforming a set of findings into a story that drives a specific decision or action. |
| [$(data-quality-audit.Name)](data-quality-audit/SKILL.md) | Comprehensive data quality assessment against business rules, schema constraints, and freshness expectations. Activate when validating data pipeline outputs before production use, auditing a dataset against defined business rules, or producing a quality scorecard for a data asset. |
| [$(executive-summary-generator.Name)](executive-summary-generator/SKILL.md) | Create concise executive summaries from detailed analysis. Use when preparing board decks, executive briefings, or condensing complex analysis into decision-ready formats for senior audiences. |
| [$(funnel-analysis.Name)](funnel-analysis/SKILL.md) | Conversion funnel analysis with drop-off investigation. Use when analyzing multi-step processes, identifying conversion bottlenecks, comparing segments through a funnel, or optimizing user journeys. |
| [$(gsd-add-tests.Name)](gsd-add-tests/SKILL.md) | Generate tests for a completed phase based on UAT criteria and implementation |
| [$(gsd-ai-integration-phase.Name)](gsd-ai-integration-phase/SKILL.md) | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| [$(gsd-audit-fix.Name)](gsd-audit-fix/SKILL.md) | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| [$(gsd-audit-milestone.Name)](gsd-audit-milestone/SKILL.md) | Audit milestone completion against original intent before archiving |
| [$(gsd-audit-uat.Name)](gsd-audit-uat/SKILL.md) | Cross-phase audit of all outstanding UAT and verification items |
| [$(gsd-autonomous.Name)](gsd-autonomous/SKILL.md) | Run all remaining phases autonomously — discuss→plan→execute per phase |
| [$(gsd-capture.Name)](gsd-capture/SKILL.md) | Capture ideas, tasks, notes, and seeds to their destination |
| [$(gsd-cleanup.Name)](gsd-cleanup/SKILL.md) | Archive accumulated phase directories from completed milestones |
| [$(gsd-code-review.Name)](gsd-code-review/SKILL.md) | Review source files changed during a phase for bugs, security issues, and code quality problems |
| [$(gsd-complete-milestone.Name)](gsd-complete-milestone/SKILL.md) | Archive completed milestone and prepare for next version |
| [$(gsd-config.Name)](gsd-config/SKILL.md) | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| [$(gsd-debug.Name)](gsd-debug/SKILL.md) | Systematic debugging with persistent state across context resets |
| [$(gsd-discuss-phase.Name)](gsd-discuss-phase/SKILL.md) | Gather phase context through adaptive questioning before planning. |
| [$(gsd-docs-update.Name)](gsd-docs-update/SKILL.md) | Generate or update project documentation verified against the codebase |
| [$(gsd-eval-review.Name)](gsd-eval-review/SKILL.md) | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| [$(gsd-execute-phase.Name)](gsd-execute-phase/SKILL.md) | Execute all plans in a phase with wave-based parallelization |
| [$(gsd-explore.Name)](gsd-explore/SKILL.md) | Socratic ideation and idea routing — think through ideas before committing to plans |
| [$(gsd-extract-learnings.Name)](gsd-extract-learnings/SKILL.md) | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| [$(gsd-fast.Name)](gsd-fast/SKILL.md) | Execute a trivial task inline — no subagents, no planning overhead |
| [$(gsd-forensics.Name)](gsd-forensics/SKILL.md) | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| [$(gsd-graphify.Name)](gsd-graphify/SKILL.md) | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| [$(gsd-health.Name)](gsd-health/SKILL.md) | Diagnose planning directory health and optionally repair issues |
| [$(gsd-help.Name)](gsd-help/SKILL.md) | Show available GSD commands and usage guide |
| [$(gsd-import.Name)](gsd-import/SKILL.md) | Ingest external plans with conflict detection against project decisions before writing anything. |
| [$(gsd-inbox.Name)](gsd-inbox/SKILL.md) | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| [$(gsd-ingest-docs.Name)](gsd-ingest-docs/SKILL.md) | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| [$(gsd-manager.Name)](gsd-manager/SKILL.md) | Interactive command center for managing multiple phases from one terminal |
| [$(gsd-map-codebase.Name)](gsd-map-codebase/SKILL.md) | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| [$(gsd-milestone-summary.Name)](gsd-milestone-summary/SKILL.md) | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| [$(gsd-mvp-phase.Name)](gsd-mvp-phase/SKILL.md) | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| [$(gsd-new-milestone.Name)](gsd-new-milestone/SKILL.md) | Start a new milestone cycle — update PROJECT.md and route to requirements |
| [$(gsd-new-project.Name)](gsd-new-project/SKILL.md) | Initialize a new project with deep context gathering and PROJECT.md |
| [$(gsd-ns-context.Name)](gsd-ns-context/SKILL.md) | codebase intelligence | map graphify docs learnings |
| [$(gsd-ns-ideate.Name)](gsd-ns-ideate/SKILL.md) | exploration capture | explore sketch spike spec capture |
| [$(gsd-ns-manage.Name)](gsd-ns-manage/SKILL.md) | config workspace | workstreams thread update ship inbox |
| [$(gsd-ns-project.Name)](gsd-ns-project/SKILL.md) | project lifecycle | milestones audits summary |
| [$(gsd-ns-review.Name)](gsd-ns-review/SKILL.md) | quality gates | code review debug audit security eval ui |
| [$(gsd-ns-workflow.Name)](gsd-ns-workflow/SKILL.md) | workflow | discuss plan execute verify phase progress |
| [$(gsd-pause-work.Name)](gsd-pause-work/SKILL.md) | Create context handoff when pausing work mid-phase |
| [$(gsd-phase.Name)](gsd-phase/SKILL.md) | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases |
| [$(gsd-plan-phase.Name)](gsd-plan-phase/SKILL.md) | Create detailed phase plan (PLAN.md) with verification loop |
| [$(gsd-plan-review-convergence.Name)](gsd-plan-review-convergence/SKILL.md) | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. |
| [$(gsd-pr-branch.Name)](gsd-pr-branch/SKILL.md) | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| [$(gsd-profile-user.Name)](gsd-profile-user/SKILL.md) | Generate developer behavioral profile and create Claude-discoverable artifacts |
| [$(gsd-progress.Name)](gsd-progress/SKILL.md) | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| [$(gsd-quick.Name)](gsd-quick/SKILL.md) | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| [$(gsd-resume-work.Name)](gsd-resume-work/SKILL.md) | Resume work from previous session with full context restoration |
| [$(gsd-review.Name)](gsd-review/SKILL.md) | Request cross-AI peer review of phase plans from external AI CLIs |
| [$(gsd-review-backlog.Name)](gsd-review-backlog/SKILL.md) | Review and promote backlog items to active milestone |
| [$(gsd-secure-phase.Name)](gsd-secure-phase/SKILL.md) | Retroactively verify threat mitigations for a completed phase |
| [$(gsd-settings.Name)](gsd-settings/SKILL.md) | Configure GSD workflow toggles and model profile |
| [$(gsd-ship.Name)](gsd-ship/SKILL.md) | Create PR, run review, and prepare for merge after verification passes |
| [$(gsd-sketch.Name)](gsd-sketch/SKILL.md) | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| [$(gsd-spec-phase.Name)](gsd-spec-phase/SKILL.md) | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| [$(gsd-spike.Name)](gsd-spike/SKILL.md) | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| [$(gsd-stats.Name)](gsd-stats/SKILL.md) | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| [$(gsd-thread.Name)](gsd-thread/SKILL.md) | Manage persistent context threads for cross-session work |
| [$(gsd-ui-phase.Name)](gsd-ui-phase/SKILL.md) | Generate UI design contract (UI-SPEC.md) for frontend phases |
| [$(gsd-ui-review.Name)](gsd-ui-review/SKILL.md) | Retroactive 6-pillar visual audit of implemented frontend code |
| [$(gsd-ultraplan-phase.Name)](gsd-ultraplan-phase/SKILL.md) | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| [$(gsd-undo.Name)](gsd-undo/SKILL.md) | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. |
| [$(gsd-update.Name)](gsd-update/SKILL.md) | Update GSD to latest version with changelog display |
| [$(gsd-validate-phase.Name)](gsd-validate-phase/SKILL.md) | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| [$(gsd-verify-work.Name)](gsd-verify-work/SKILL.md) | Validate built features through conversational UAT |
| [$(gsd-workspace.Name)](gsd-workspace/SKILL.md) | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| [$(gsd-workstreams.Name)](gsd-workstreams/SKILL.md) | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |
| [$(impact-quantification.Name)](impact-quantification/SKILL.md) | Estimate and communicate business impact of insights. Use when sizing opportunities discovered in analysis, calculating ROI of recommended actions, or prioritizing initiatives by potential impact. |
| [$(insight-synthesis.Name)](insight-synthesis/SKILL.md) | Transform data findings into compelling insights. Use when converting analysis results into actionable insights, connecting findings to business impact, or preparing insights for stakeholder communication. |
| [$(methodology-explainer.Name)](methodology-explainer/SKILL.md) | Explain analysis methodology to diverse audiences. Use when documenting 'how we did this' sections, building trust through transparency, or teaching analytical approaches to stakeholders. |
| [$(metric-reconciliation.Name)](metric-reconciliation/SKILL.md) | Cross-source metric validation and discrepancy investigation. Use when metrics from different sources don't match, investigating data quality issues between systems, or validating data migration accuracy. |
| [$(pbip-dependency-analyzer.Name)](pbip-dependency-analyzer/SKILL.md) | Power BI PBIP Dependency Analyzer. Analyzes all Power BI Project (.pbip) files, TMDL exports, and semantic model definitions to map dependencies between measures, columns, tables, M/Power Query, relationships, and report visuals. Use this skill EVERY TIME the user asks to: find unused measures or columns, analyze dependencies, clean up a data model, check what would break if something is deleted, perform impact analysis, identify orphaned objects, audit model quality, or asks 'what can I delete'. Also trigger when the user uploads .pbip files, model.bim files, TMDL exports, or report.json files and wants to understand their structure or dependencies. Trigger phrases include: 'analyze dependencies', 'find unused', 'what can I delete', 'clean up model', 'impact analysis', 'dependency check', 'unused measures', 'unused columns', 'orphaned objects', 'model audit', 'PBIP analysis'. |
| [$(pbi-report-builder.Name)](pbi-report-builder/SKILL.md) | [power-bi] Power BI PBIR Report Builder with IBCS Visuals. Generates Power BI report pages, visuals, and IBCS-compliant variance charts by writing PBIR JSON files directly into PBIP project folders. Use this skill EVERY TIME the user asks to: create a Power BI report page, add visuals to a report, generate KPI cards, create charts or tables in Power BI, build a dashboard layout with visuals, create IBCS variance charts, create actual vs plan visuals, or programmatically create Power BI visuals. Also trigger when the user mentions 'PBIR', 'IBCS', 'variance chart', 'variance table', 'actual vs plan', 'actual vs comparison', 'create visuals', 'add a page', 'build a report', 'KPI cards', 'place visuals', or wants to generate Power BI report content through code. If the user mentions any combination of Power BI + visuals/page/report/KPI/chart/table/IBCS/variance + create/build/generate/add, use this skill. |
| [$(pbi-requirements-gathering.Name)](pbi-requirements-gathering/SKILL.md) | > |
| [$(peer-review-template.Name)](peer-review-template/SKILL.md) | Structured peer review for analytical work. Use when reviewing teammates' analysis, providing constructive feedback, or establishing analysis quality standards. |
| [$(planning-with-files.Name)](planning-with-files/SKILL.md) | Implements Manus-style file-based planning to organize and track progress on complex tasks. Creates task_plan.md, findings.md, and progress.md. Use when asked to plan out, break down, or organize a multi-step project, research task, or any work requiring 5+ tool calls. Supports automatic session recovery after /clear. |
| [$(programmatic-eda.Name)](programmatic-eda/SKILL.md) | Systematic exploratory data analysis. Activate when a dataset needs profiling — structure check, nulls, outliers, distributions, correlations — before deeper analysis begins. |
| [$(query-validation.Name)](query-validation/SKILL.md) | SQL query review for correctness, performance, and best practices. Activate when a query needs review before production use, shows unexpected results, or runs too slowly. |
| [$(root-cause-investigation.Name)](root-cause-investigation/SKILL.md) | Systematic investigation of metric changes and anomalies. Use when a metric unexpectedly changes, investigating business metric drops, explaining performance variations, or drilling into aggregated metric drivers. |
| [$(schema-mapper.Name)](schema-mapper/SKILL.md) | Database schema understanding and relationship mapping. Use when exploring unfamiliar databases, documenting table relationships, identifying join paths, or generating ERD documentation for existing schemas. |
| [$(segmentation-analysis.Name)](segmentation-analysis/SKILL.md) | Customer/user segmentation with actionable insights. Use when identifying distinct customer groups, analyzing segment-specific behavior, profiling high-value segments, or testing segmentation hypotheses. |
| [$(semantic-model-builder.Name)](semantic-model-builder/SKILL.md) | Build structured semantic layer documentation for metrics, dimensions, and entities. Activate when you need to define a business metric, document a data model, or create YAML definitions compatible with dbt Semantic Layer or similar frameworks. |
| [$(sql-to-business-logic.Name)](sql-to-business-logic/SKILL.md) | Translate SQL queries into plain language business logic. Use when documenting queries, explaining analysis to non-technical stakeholders, code reviewing for correctness, or building a query catalog. |
| [$(stakeholder-requirements-gathering.Name)](stakeholder-requirements-gathering/SKILL.md) | Structured requirements elicitation for analysis requests. Use when scoping new analysis projects, clarifying ambiguous business questions, or documenting analysis acceptance criteria with stakeholders. |
| [$(technical-to-business-translator.Name)](technical-to-business-translator/SKILL.md) | Translate technical analysis into business language. Use when explaining statistical concepts to non-analysts, simplifying technical findings, or bridging communication between data teams and business stakeholders. |
| [$(time-series-analysis.Name)](time-series-analysis/SKILL.md) | Temporal pattern detection and forecasting. Use when analyzing trends over time, detecting seasonality, identifying anomalies in time series, or building simple forecasting models for planning. |
| [$(visualization-builder.Name)](visualization-builder/SKILL.md) | Create effective, publication-ready data visualizations. Use when choosing chart types, designing presentation visuals, building dashboard charts, or applying visual design best practices to data output. |
| [$(web-artifacts-builder.Name)](web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts. |

