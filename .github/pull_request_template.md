## Add `owner/repo`

<!-- Replace owner/repo with the actual repository -->

> 🤖 **Auto-ranking:** when you open this PR, a bot computes your tool's
> **AI-Readiness Score** from the entry below and posts it as a comment.
> Score = agent-callability (MCP / Python / CLI / pip / maintenance), not stars.
> See [READINESS.md](../blob/main/READINESS.md) for the full ranking.

### Entry

<!-- Paste the exact line you added to README.md, e.g.:
- [owner/repo](https://github.com/owner/repo) `Python` `MCP` - One-line description. -->

```
- [owner/repo](https://github.com/owner/repo) `Lang` `Tag` - Description.
```

### Interface tags (these drive your score — include all that apply)

- [ ] `MCP` — ships a Model Context Protocol server (+35)
- [ ] `Python` — native Python API (+25)
- [ ] `API` — CLI or REST/agent interface (+15)
- [ ] pip/conda installable (auto-detected from PyPI, +15)

### Required (enforced by CI — PR is blocked until all pass)

- [ ] **Open source** with a clear license (commercial/closed tools are out of scope)
- [ ] **Actively maintained** — commit within 12 months
- [ ] Has a **README** with install instructions
- [ ] Relevant to **AI + CAE/CAD/CAM** workflows
- [ ] **Alphabetical order** within the section
- [ ] Correct format: `- [Name](url) \`Lang\` \`Tag\` - Description.` (ASCII ` - ` separator, description starts with a capital)
- [ ] `awesome-lint` + link check pass

### Category

<!-- Which section? e.g. CFD, FEA, MCP Servers, Visualization... -->

### Why this is AI-ready

<!-- How can an AI agent actually call this tool (MCP / Python / CLI)? -->
