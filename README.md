# Test_repo

A personal practice repository for learning and experimenting with software engineering concepts. Nothing here is production code — it's a sandbox for trying things, breaking them, and understanding why.

## Goals

- Practice a real Git workflow: feature/fix branches, commits, pull requests, merges
- Learn defensive programming and error handling
- Understand common pitfalls (e.g. mismatched limits between components)
- Build habits around readable, documented code

## Contents

| File | Description |
|------|-------------|
| [script.py](script.py) | Toy text-chunking and embedding pipeline that demonstrates a chunk-size / embedder-limit mismatch and how to handle it |

### The `script.py` exercise

- `chunk(text, size)` splits text into chunks of at most `size` "tokens" (1 word = 1 token for simplicity).
- `embed(chunk_text)` simulates an embedder with a hard token limit (`EMBEDDER_LIMIT`) and reports how many tokens were kept or lost.
- **Concept illustrated:** if `MAX_CHUNK_TOKENS` is larger than `EMBEDDER_LIMIT`, the embedder silently loses data. Keeping related limits consistent, and failing loudly with `try/except`, avoids this class of bug.

## Running

Requires Python 3.9+ (uses built-in generic types such as `list[str]`).

```bash
python script.py
```

## Workflow

Changes are made on a dedicated branch (e.g. `fix/chunk-size-mismatch`), then merged into `main` via a pull request.

## Concepts practiced so far

- [x] Branching and pull requests
- [x] Error handling with `try/except`
- [x] Type hints
- [ ] Unit tests
- [ ] CI
- [ ] Documentation and code review habits
