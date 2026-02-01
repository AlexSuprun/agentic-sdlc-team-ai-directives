---
name: vercel-react-best-practices
description: React and Next.js performance optimization guidelines from Vercel Engineering. Contains 40+ rules across 8 categories prioritized by impact.
license: MIT
metadata:
  source: vercel-labs/agent-skills
  source_url: https://github.com/vercel-labs/agent-skills
  source_skill_path: skills/react-best-practices
---

# Vercel React Best Practices

## What This Skill Provides

React and Next.js performance optimization guidelines with 40+ rules across:
- Eliminating waterfalls (Critical)
- Bundle size optimization (Critical)
- Server-side performance (High)
- Client-side data fetching (Medium-High)
- Re-render optimization (Medium)
- Rendering performance (Medium)
- JavaScript micro-optimizations (Low-Medium)

## When to Use This Skill

- Writing new React components or Next.js pages
- Implementing data fetching (client or server-side)
- Reviewing code for performance issues
- Optimizing bundle size or load times

## Team Context & Overrides

### Prerequisites (Customize Per Project)
- [ ] Define your Next.js version minimum (e.g., 14+)
- [ ] TypeScript strict mode enabled (per constitution)
- [ ] Testing framework specified (Jest, Vitest, etc.)
- [ ] Performance baseline established (Lighthouse score, Core Web Vitals targets)

### Constraints & Priorities (Customize Per Project)
- [ ] Which rule categories apply? (Critical, High, Medium, Low)
- [ ] Any rules to deprioritize based on your stack?
- [ ] Performance metric priorities: (e.g., LCP, CLS, FID)
- [ ] Bundle size constraints?

### Integration with Team Constitution
- **Principle 2 (Build for Observability)**: Ensure performance metrics are logged
- **Principle 4 (Tests Drive Confidence)**: Include performance tests in your review
- **Principle 9 (Simplicity First)**: Prioritize high-impact optimizations over micro-optimizations
- **Principle 11 (Goal-Driven Execution)**: Define success criteria (specific performance targets)

### How to Use This Skill
1. Fetch the remote skill content (see "Fetch Remote Skill" section below)
2. Review Vercel's 40+ rules
3. Filter rules by your team's priorities and constraints
4. Apply rules that align with your project's context and performance goals
5. Measure impact using Lighthouse, Core Web Vitals, or your custom metrics

## Fetch Remote Skill

This skill references content from the Vercel agent-skills repository. To use it:

### Prerequisites
- Git 2.27+ (for sparse checkout)
- Network access to https://github.com/vercel-labs/agent-skills

### Fetch & Read

```bash
# Clone only the react-best-practices skill directory
git clone --depth 1 --filter=blob:none --sparse https://github.com/vercel-labs/agent-skills.git
cd agent-skills
git sparse-checkout set skills/react-best-practices

# Read the full skill content
cat skills/react-best-practices/SKILL.md

# (Optional) View supporting files
ls -la skills/react-best-practices/
```

### Error Handling

If the clone fails:
- Check network connectivity
- Verify GitHub is accessible
- If Vercel's repository is unavailable, this skill cannot be used at this time
- Retry after confirming access to https://github.com/vercel-labs/agent-skills

### Integration
Once fetched, combine Vercel's rules with your team's constraints (defined above) to:
- Select applicable rules for your use case
- Adapt rules to your specific tech stack
- Measure performance improvements per team metrics

## References

- **Vercel Skills Repository**: https://github.com/vercel-labs/agent-skills
- **React Best Practices Skill**: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
- **Team Constitution**: See @constitution.md (Principles 2, 4, 9, 11)
- **External References** (from Vercel):
  - https://react.dev
  - https://nextjs.org
  - https://swr.vercel.app
  - https://vercel.com/blog/how-we-optimized-package-imports-in-next-js