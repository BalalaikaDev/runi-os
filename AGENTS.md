## graphify knowledge graph

An orientation report for this repo lives in `graphify-out/GRAPH_REPORT.md`
(community hubs, god-nodes, file map). Read it before grepping.

The full queryable graph (`graph.json`) is gitignored because it is ~3 MB.
Regenerate it locally with `graphify update .` (needs the `graphifyy` package;
AST-only, no API cost), then `graphify query "<question>"`.
