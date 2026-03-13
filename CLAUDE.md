# CLAUDE.md

## Project Info

- **Repo**: kimimgo/awesome-ai-cae
- **Type**: Awesome list (curated resource collection)
- **License**: CC0-1.0
- **Owner**: kimimgo (viznoir 개발자, DualSPHysics/OpenFOAM/VTK 도메인)

## What This Is

AI-powered tools for Computer-Aided Engineering 큐레이션 리스트. sindresorhus/awesome 표준 준수.

핵심 차별화: **AI-Ready** — AI 에이전트가 직접 호출 가능한(MCP, Python API, CLI) CAE/CAD/CAM 도구에 집중.

## Structure

```
README.md                    # 메인 리스트 (12 카테고리, 80+ 항목)
CONTRIBUTING.md              # 기여 가이드 (항목 포맷, PR 규칙)
LICENSE                      # CC0-1.0
code-of-conduct.md           # Contributor Covenant 2.1
media/banner.svg             # 커스텀 배너 (다크 테마, 그라데이션)
media/divider.svg            # 섹션 구분선
.github/workflows/lint.yml   # awesome-lint CI
.github/workflows/links.yml  # Lychee 링크 체커 (매주 월요일)
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/add-tool.md
.github/ISSUE_TEMPLATE/report-broken-link.md
```

## Categories (12)

1. MCP Servers — AI-native tool interfaces
2. CFD — Computational Fluid Dynamics
3. FEA — Finite Element Analysis
4. SPH — Smoothed Particle Hydrodynamics
5. Visualization & Post-processing
6. CAD & Geometry
7. Mesh Generation
8. AI/ML for Simulation
9. Surrogate Models & PINNs
10. Optimization
11. Data Formats & I/O
12. Datasets & Benchmarks
13. Learning Resources

## Entry Format

```markdown
- [owner/repo](https://github.com/owner/repo) `Language` `Tag` — Description.
```

- 알파벳 순서 유지
- Language tags: `Python`, `C++`, `Fortran`, `Rust`, `CUDA` 등
- Special tags: `MCP` (Model Context Protocol), `API`

## CI

- `awesome-lint`: README.md 포맷 검증 (push/PR)
- `lychee`: 링크 깨짐 검사 (push/PR + 매주 월요일 06:00 UTC)

## Maintenance Rules

- 12개월 이상 커밋 없는 프로젝트 → 제거 검토
- 링크 깨짐 → 즉시 수정 또는 제거
- viznoir는 MCP Servers + Visualization 카테고리에만 배치 (객관성 유지)
- 새 카테고리 추가 시 최소 3개 항목 필요

## Goals

1. sindresorhus/awesome 메타 리스트 등록 (30일 후)
2. GitHub Stars 100+ (6개월 목표)
3. 외부 PR 유입 (커뮤니티 참여)

## Related

- viznoir: https://github.com/kimimgo/viznoir (MCP server for visualization)
- awesome-mcp-servers: https://github.com/punkpeye/awesome-mcp-servers (MCP 도구 큐레이션)
