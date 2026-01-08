# Agent Quality Contract (N8nScraper)

**Vendored From:** AiResearch repository (`docs/agent_quality_contract.md`)
**Vendored Date:** 2026-01-08
**Purpose:** Quality standards for N8nScraper multi-agent framework

---

## 1. NON-NEGOTIABLES

These rules are absolute. Violation = failed output.

| Rule | Requirement | Violation Example |
|------|-------------|-------------------|
| **N1: No Invented Facts** | Every version/feature claim cites a primary source URL. If unverifiable, write `UNKNOWN - TODO: verify` | "n8n v2.5 supports..." without docs link |
| **N2: Mechanism Before Outcome** | Performance claims state mechanism + required conditions | "10x faster extraction" without explaining what causes it |
| **N3: Measure-First Config** | No fixed sizes without measurement step + budget equation | "Process 1000 nodes" without measuring current capacity |
| **N4: Citation Discipline** | Every claim links to primary source with access date | Blog paraphrase without original TypeScript source |
| **N5: Concrete Orchestration** | Multi-agent coordination specifies locking protocol | "Agents coordinate" without explaining atomic operations |
| **N6: Consistent Math** | All sizing uses declared formula with units | "~500 properties" without node count and average |
| **N7: DOES/DOESN'T Required** | Agent capabilities include explicit limitation table | Implying agent can "fix all issues" without scope limits |
| **N8: Model Currency** | All model references verified against current state | "GPT-4 achieves 85%" presented as current SOTA |
| **N9: Dated Claims** | All version/count claims include verification date: "X (as of YYYY-MM-DD)" | "n8n 2.3.0" without date |
| **N10: Historical Context** | Papers >6 months old cite model used + note current equivalent | Old benchmark results without context |
| **N11: Volatility Awareness** | High-volatility claims (versions, stars, pricing) flagged for 30-day refresh | GitHub stars without expiration awareness |
| **N12: Direct Source Verification** | Package versions verified via direct fetch (PyPI, npm, GitHub releases) - NEVER via web search | Web search for "n8n latest version" (returns stale data) |

---

## 2. Source Citations

### Citation Format

```markdown
[Claim] (Source: [File:Line] or [URL], accessed YYYY-MM-DD)
```

### Handling Unknowns

When you cannot verify a claim:

```markdown
**UNKNOWN - TODO: Verify**
- Claim: [what was claimed]
- Attempted sources: [what you checked]
- Action needed: [specific verification step]
```

**NEVER substitute guesses for verification.**

---

## 3. N8nScraper-Specific Context

### Source Hierarchy for TypeScript Analysis

1. **Primary:** TypeScript source files in `n8n/packages/nodes-base/nodes/`
2. **Secondary:** Extracted JSON in `extracted_docs/`
3. **Tertiary:** Validation reports from `validate_extraction.py`
4. **REJECT:** Assumptions about TypeScript patterns without source inspection

### Measurement-First for Extraction Claims

Before claiming property counts or extraction quality:

```markdown
## Measurement Required

### Step 1: Source Inspection
# Count properties in TypeScript source
grep -A 50 "properties: \[" [Node].node.ts | grep "name:" | wc -l

### Step 2: Extracted Count
# Count properties in extracted JSON
jq '.properties | length' extracted_docs/[node]_data.json

### Step 3: Calculate Accuracy
Accuracy = (Extracted / Source) * 100
```

**Only then make quality claims.**

---

## 4. Agent Capability Tables (N7 Compliance)

Every agent MUST document capabilities with DOES/DOESN'T table.

### Example: TypeScript Parser Agent

| DOES | DOESN'T |
|------|---------|
| Resolve namespace spreads (`...ns.prop`) | Handle arbitrary code execution in spreads |
| Extract utility function results if inlined | Resolve dynamic spreads requiring runtime evaluation |
| Recurse collections 3-4 levels deep | Support infinite recursion (stack limit) |

### Example: Extraction Validator Agent

| DOES | DOESN'T |
|------|---------|
| Detect extraction quality drops via validation script | Prevent extractor bugs (detection only) |
| Compare current extraction to TypeScript source | Guarantee 100% accuracy (96%+ is realistic) |
| Identify zero-property nodes for investigation | Auto-fix extraction issues (propose only) |

---

## 5. Quality Metrics (N8nScraper Baseline)

| Metric | Target | Measurement Source |
|--------|--------|-------------------|
| Zero-property nodes | ≤1 (NoOp only) | `validate_extraction.py` |
| Null displayNames | 0 | `validation_report.json` |
| Template variables | 0 | `validation_report.json` |
| Overall quality | 96%+ | Manual calculation: (nodes with properties / total nodes) |
| File pair consistency | 100% | JSON count == MD count |

---

## 6. Coordination Protocol (N5 Compliance)

### Atomic Operations Required

| Operation | Mechanism | Source |
|-----------|-----------|--------|
| Issue claiming | `coordination_lib.py::acquire_lock()` | Uses atomic `mkdir()` |
| Fix proposal | Lock → Write → Release | `coordination_lib.py::propose_fix()` |
| Index updates | File locking with fcntl | `coordination_lib.py::_save_coordination()` |

### What MUST Be Atomic

| Component | Requirement |
|-----------|-------------|
| Lock acquisition | `mkdir(exist_ok=False)` - OS guarantees atomicity |
| Issue assignment | Update `coordination.json` while holding lock |
| Fix application | Move file from `proposed/` to `applied/` atomically |

### What MUST NEVER Happen

| Anti-Pattern | Why |
|--------------|-----|
| Manual JSON editing | Bypasses locks, causes corruption |
| Skipping lock acquisition | Race conditions |
| Removing active locks | Breaks in-progress work |

---

## 7. TypeScript Pattern Claims

### Required for Spread Pattern Analysis

Every spread pattern claim MUST include:

```markdown
### [Pattern Name]

**Pattern:** [Exact TypeScript syntax]
**Example Node:** [Node name using this pattern]
**Source Location:** [File path:line number]
**Current Extraction:** [Working / Failing]
**Root Cause:** [What causes extractor to miss this]
```

### Banned Patterns

| Pattern | Why Banned | Replacement |
|---------|-----------|-------------|
| "Most nodes use..." | No count evidence | "47 of 451 nodes use... (10.4%)" |
| "Complex spread" | Vague | "Spread with computed property names: `...{ [var]: val }`" |
| "Should work" | Not verified | "Tested on GoogleSheets, Slack, HttpRequest - 42 properties extracted" |

---

## 8. Red-Team Checklist

Before finalizing ANY agent output, verify:

### TypeScript Analysis
- [ ] Every pattern claim has source file:line citation
- [ ] Property counts verified against actual TypeScript source
- [ ] Root cause analysis explains exact extractor limitation

### Quality Claims
- [ ] Metrics cite `validation_report.json` or measured output
- [ ] Percentage calculations show formula (extracted / total)
- [ ] Baseline comparison includes date (quality as of YYYY-MM-DD)

### Coordination Claims
- [ ] Lock protocol specifies atomic operation used
- [ ] No race condition assumptions
- [ ] Cleanup procedures documented (stale lock handling)

### Fix Proposals
- [ ] Before/after property counts for affected nodes
- [ ] Regression test list (minimum 5 nodes)
- [ ] Root cause identified with TypeScript source citation

---

## 9. Common Violations (N8nScraper Context)

### Violation: Invented Property Counts

**Bad:**
```
"GoogleSheets has ~40 properties"
```

**Good:**
```
GoogleSheets: 42 properties (Source: extracted_docs/googlesheets_data.json, validated 2026-01-08)
TypeScript source: 42 properties (Source: n8n/packages/nodes-base/nodes/GoogleSheets/GoogleSheets.node.ts:156-287)
```

### Violation: Vague Pattern Claims

**Bad:**
```
"Spread operators often cause issues"
```

**Good:**
```
Namespace spreads (`...module.property`) cause extraction failures in 7 nodes:
- GoogleSheets (line 178): `...sorting.property` → missed 19 properties
- Slack (line 234): `...operations.channel` → missed 8 properties
Root cause: Extractor regex doesn't resolve namespace references
```

### Violation: Unsubstantiated Quality Claims

**Bad:**
```
"Quality improved significantly"
```

**Good:**
```
Quality improved from 49 zero-property nodes to 1 (98% reduction)
Measurement: validation_report.json before fix (2025-11-10) vs after fix (2025-11-11)
Overall quality: 94.7% → 96.3% (+1.6 percentage points)
```

---

## Reference Sources (Primary)

| Topic | Primary Source | What It Documents |
|-------|----------------|-------------------|
| n8n Node Structure | TypeScript files in `n8n/packages/nodes-base/nodes/` | Actual node definitions |
| Extraction Quality | `validation_report.json` | Measured extraction accuracy |
| Coordination State | `collaboration/coordination.json` | Agent assignments, locks |
| Multi-Agent Protocol | `coordination_lib.py` | Atomic operations implementation |
| Historical Fixes | `fixes/applied/*.json` | Applied fixes with test results |

---

## Enforcement

### Agent Responsibilities

| Agent | Enforcement Duty |
|-------|-----------------|
| **typescript-parser** | Cite TypeScript source:line for all patterns |
| **extraction-validator** | Verify all metrics against validation report |
| **property-auditor** | Compare extracted vs source property counts |
| **issue-triage** | Cite impact metrics (nodes affected, property delta) |
| **coordination-enforcer** | Verify lock protocol compliance |

### Violation Response

1. **Self-detected:** Fix before output
2. **Flagged by validator:** Update source file
3. **Cannot verify:** Mark as `UNKNOWN - TODO: verify`, do not guess

---

**Vendored From:** AiResearch/docs/agent_quality_contract.md
**Original Version:** 2026-01-08
**N8nScraper Adaptation:** Added TypeScript-specific rules, coordination protocol requirements
