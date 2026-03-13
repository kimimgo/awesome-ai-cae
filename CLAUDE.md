# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Info

- **Repo**: kimimgo/awesome-ai-cae
- **Type**: Awesome list (curated resource collection) — sindresorhus/awesome 표준 준수
- **License**: CC0-1.0
- **핵심 차별화**: **AI-Ready** — AI 에이전트가 직접 호출 가능한(MCP, Python API, CLI) CAE/CAD/CAM 도구에 집중

## CI — Lint & Link Check

```bash
# awesome-lint: README.md 포맷 검증 (push/PR 시 자동 실행)
npx awesome-lint

# lychee: 링크 깨짐 검사 (push/PR + 매주 월요일 06:00 UTC)
# 로컬 실행 시:
lychee --verbose --no-progress '*.md'
```

## Entry Format

```markdown
- [owner/repo](https://github.com/owner/repo) `Language` `Tag` — Description.
```

- **알파벳 순서** 유지 (섹션 내)
- Language tags: `Python`, `C++`, `Fortran`, `Rust`, `CUDA` 등
- Special tags: `MCP` (Model Context Protocol), `API` (REST/gRPC)
- Description은 마침표로 끝남

## awesome-lint 주의사항

awesome-lint는 README.md에 엄격한 규칙을 적용한다. 비자명한 제약:

- 리스트 항목은 반드시 `- [Name](url)` 형식으로 시작해야 함 (name은 대문자 시작)
- 항목 설명(description)은 대문자로 시작, 마침표로 끝나야 함
- 중복 링크 허용되지만 `<!--lint disable double-link-->` 주석 필요 (파일 상단에 이미 설정됨)
- Contents 섹션의 링크 텍스트와 실제 heading이 정확히 일치해야 함
- `<!--lint disable awesome-heading awesome-github awesome-toc double-link-->` — 파일 상단의 이 주석을 제거하지 말 것

## Categories (13)

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

새 카테고리 추가 시 최소 3개 항목 필요.

## Maintenance Rules

- 12개월 이상 커밋 없는 프로젝트 → 제거 검토
- 링크 깨짐 → 즉시 수정 또는 제거
- viznoir는 MCP Servers + Visualization 카테고리에만 배치 (객관성 유지)
- README.md 편집 시 Contents 목차와 실제 섹션 heading 동기화 필수
- `<sup>[back to top](#contents)</sup>` 패턴이 매 섹션 끝에 있어야 함

## Goals

1. sindresorhus/awesome 메타 리스트 등록 (30일 후)
2. GitHub Stars 100+ (6개월 목표)
3. 외부 PR 유입 (커뮤니티 참여)

## Related

- viznoir: https://github.com/kimimgo/viznoir (MCP server for visualization)
- awesome-mcp-servers: https://github.com/punkpeye/awesome-mcp-servers (MCP 도구 큐레이션)
