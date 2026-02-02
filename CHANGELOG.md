# Changelog

## [v1.1.0] - 2025-02-01

### Skills Simplification & External Skills Registry
- **Added skills/external_skills.md**: URL-based registry for external skills from vercel-labs and other sources
- **Simplified skills frontmatter**: Removed complex metadata, keeping only name + description (vercel-labs format)
- **Refactored skills/ directory structure**: Moved vercel-react-best-practices to skills/ root, removed fullstack/ directory
- **Updated skills/AGENTS.md**: Removed metadata references, added external skills section
- **Updated CONTRIBUTING.md**: Removed metadata requirements, added external skills contribution guidelines
- **Updated README.md**: Removed skills.manifest.yml references, added external skills explanation
- **Simplified vercel-react-best-practices skill**: Updated frontmatter to vercel-labs simple format

### Key Features
- **External Skills**: URL-based registry for skills from other repositories, fetched on-demand via agent webfetch
- **Simple Frontmatter**: Adopted vercel-labs format (name + description only) for better LLM compatibility
- **LLM-Based Discovery**: Skills discovered using natural language matching instead of structured metadata
- **Flattened Structure**: Simplified skills directory structure following vercel-labs patterns

### Breaking Changes
- Removed complex skill metadata (category, platforms, keywords, requires_context, use_cases)
- Deleted skills.manifest.yml - skills discovered via LLM matching instead
- Deleted docs/SKILL_METADATA_STANDARD.md - no longer needed with simple format
- External skills now referenced via URL instead of being copied/wrapped

### Migration Notes
- Existing skills with complex metadata will still work but should be simplified gradually
- Teams using git submodules will automatically get new external skills registry
- Skill discovery now relies on LLM matching rather than structured metadata
- External skills are fetched on-demand via agent webfetch capabilities

## [Unreleased] - 2025-01-10
- Refactored repository structure to match final layout
- Merged principles into constitution.md at root
- Moved templates to context_modules/examples/patterns/
- Added skills/ and prompts/ directories
- Moved skills/ from context_modules/skills/ to skills/ (same level as context_modules/)
- Updated README.md to reflect new structure
- Restructured constitution: moved language-specific items (dependency injection, null safety) to rules/style-guides/
- Generalized dependency injection as neutral rule
- Renamed examples/patterns/ to examples/prompts/ for clarity (contains prompt templates)
- Moved constitution.md from root to context_modules/ for better organization of guidance content
## [Unreleased] - 2025-01-16
- Added Spring Boot framework patterns (constructor injection, JPA, testing, configuration)
- Added DevOps Engineer persona (generic DevOps philosophy, tool-agnostic)
- Added AGENTS.md meta-pattern for skills (self-contained, portable, progressive disclosure)
- Added DevOps rules directory with 7 generic patterns:
  - GitHub Actions workflows and reusable actions
  - Helm packaging and values design principles
  - Helm chart library pattern for DRY template management
  - Helm wrapper charts for extending upstream charts
  - Helm template helpers for consistent naming and labels
  - External Secrets Operator patterns for secret management
  - GKE Workload Identity for cloud authentication
- Added Phase 2 generic patterns with complete abstraction:
  - Generic DRY secrets management pattern with standalone Helm templates
  - Generic Crossplane compositions with provider-agnostic examples
  - Updated DevOps Engineer persona with complete rule references
  - All patterns work with any cloud provider without competitive advantage loss
- Added Phase 3 comprehensive externalization:
  - Added Python testing rule with pytest patterns and class-based organization
  - Added orchestration rules directory with generic Airflow and Airbyte patterns
  - Added generic skill templates for skill development patterns
  - Added Cloud Native Platform Architect persona with generic rule references
  - Updated DevOps Engineer persona with complete rule coverage
  - All patterns work with any cloud provider without competitive advantage loss