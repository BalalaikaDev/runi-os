# Graph Report - runi-os  (2026-10-23)

## Corpus Check
- 187 files · ~346,341 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 51 file(s) not represented in the graph (top: (none) 20, .css 15, .woff2 10)

## Summary
- 3491 nodes · 7136 edges · 173 communities (140 shown, 33 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 551 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6af90d9a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- backend/app/main.py
- get
- _val_case_id
- _audit
- motion.js
- cytoscape.min.js
- httpx
- news/view.js
- graph_intel.py
- time
- hashlib
- co
- delete
- re
- get_json
- asyncio
- BackgroundTasks
- ner_pipeline.py
- GraphDB
- quant-engine/server.py
- shell/backend/app/main.py
- agent/view.js
- agent/routes.py
- _tasks_for
- shell/backend/app/llm_bridge.py
- logging
- ModuleManifest
- news/vendor/leaflet/leaflet.js
- pivot.py
- gigs/routes.py
- presence/routes.py
- shell.js
- json
- n
- e
- tempfile
- patch
- fastapi
- vl
- static/vendor/leaflet/leaflet.js
- NewsService
- yn
- en
- DeepSeeker
- documents.py
- search.py
- piper/app.py
- quant/routes.py
- fn
- news/service.py
- identity/routes.py
- bias.py
- me
- extract_iocs_from_file
- intel.py
- recon/app.py
- cr
- pdf_export.py
- ke
- dashboard.py
- backend/app/llm_bridge.py
- _compute_risk_score
- monitor.py
- maltego_transforms.py
- auth.py
- mn
- passive_dns.py
- mount
- switchTab
- app/llm.py
- SpiderFootClient
- esc
- build_router
- _compute_indicators
- build_router
- markets/view.js
- presence/view.js
- reports/view.js
- claude_bridge.py
- voidaccess.py
- dedup.py
- verify_api_key
- semantic_search.py
- pydantic
- markets/routes.py
- gigs/view.js
- scheduler.py
- opensky.py
- _fire_webhook_formatted
- timeline.py
- risk_scoring.py
- geo.py
- m
- email_headers.py
- deep_investigate
- F
- _fetch_ohlcv
- W
- F
- ho
- mailaccess.py
- restore_backup
- users.py
- m
- Runi-OS
- classify_topics
- refresh
- Runi Shell
- asn.py
- NoClaudeError
- Shell modules
- Jt
- Fieldwork stack operations
- p
- deep_research
- cryptoCard
- oi
- ga
- rdap.py
- link_analysis.py
- Contributing to Runi-OS
- OSINT API keys — what to set to un-blind the crawlers
- Jt
- identity/view.js
- maritime.py
- lifespan
- run_all_active
- pathlib
- analyze_image
- Add / modify a Runi Shell module
- bi
- i
- _get_cfg
- news/routes.py
- TDChart
- etherscan.py
- geocode.py
- wikidata.py
- scan_username
- Verifying Fieldwork changes
- Publishing Runi-OS — go-public checklist
- OllamaClient
- _digest
- Demo & screenshot guide
- LLM engine resolution
- Investigation eval harness
- pull_request_template.md
- _get_macro_context
- _startChassisLife
- bi
- dedup_candidates
- graph_health
- ollama_status
- map_locations_endpoint
- monitor_alert_count
- monitor_get_alerts
- monitor_list_watches
- oi
- oi
- torbot/entrypoint.sh
- voidaccess/entrypoint.sh

## God Nodes (most connected - your core abstractions)
1. `_audit()` - 67 edges
2. `_val_case_id()` - 44 edges
3. `_tasks_for()` - 37 edges
4. `e()` - 34 edges
5. `co()` - 34 edges
6. `n()` - 27 edges
7. `NewsService` - 25 edges
8. `en` - 25 edges
9. `fn()` - 25 edges
10. `mount()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `TWO bridge modules (different config stores)` --references--> `call_claude_api_vision()`  [INFERRED]
  docs/kb/llm-engines.md → backend/app/llm_bridge.py
- `API keys` --references--> `_save_runtime_keys()`  [INFERRED]
  .claude/skills/fieldwork-osint-tool/SKILL.md → backend/app/main.py
- `Adding a shell module` --references--> `ModuleManifest`  [INFERRED]
  CONTRIBUTING.md → shell/backend/app/registry.py
- `AI investigation layer (added 2026-07; modules in `backend/app/`)` --references--> `search_sec_filings()`  [INFERRED]
  docs/kb/architecture.md → backend/app/crawlers/sec.py
- `Working discipline` --references--> `persist_investigation()`  [INFERRED]
  .claude/skills/osint-investigation/SKILL.md → backend/app/graph_intel.py

## Import Cycles
- None detected.

## Communities (173 total, 33 thin omitted)

### Community 0 - "backend/app/main.py"
Cohesion: 0.02
Nodes (113): create_access_token(), add_case_evidence(), add_entity_note(), add_to_watchlist(), AhmiaRequest, analyze_email_headers_endpoint(), analyze_text(), auth_login() (+105 more)

### Community 1 - "get"
Cohesion: 0.02
Nodes (61): get_audit_log(), adverse_by_name(), aleph_search(), arkham_wallet(), audit_case_log(), audit_my_log(), auth_config(), auth_list_users() (+53 more)

### Community 2 - "_val_case_id"
Cohesion: 0.02
Nodes (68): add_note(), add_subject(), add_task(), create_case(), delete_note(), export_case_markdown(), _frag(), get_case() (+60 more)

### Community 3 - "_audit"
Cohesion: 0.02
Nodes (50): _audit(), brute_subdomains(), capture_entity_evidence(), companies_house_company_ep(), companies_house_search_ep(), create_professional_report(), domain_certs(), domain_hunter() (+42 more)

### Community 4 - "motion.js"
Cohesion: 0.03
Nodes (58): adopt(), As(), br(), collectTargets(), constructor(), Dr(), ec(), Es() (+50 more)

### Community 5 - "cytoscape.min.js"
Cohesion: 0.06
Nodes (61): a(), ac(), Ao(), b(), Ba(), Bn(), bo(), cc() (+53 more)

### Community 6 - "httpx"
Cohesion: 0.05
Nodes (33): search_aleph(), _creds(), get_host(), search_hosts(), _auth(), companies_house_company(), search_companies_house(), _creds() (+25 more)

### Community 7 - "news/view.js"
Cohesion: 0.08
Nodes (61): Editing discipline, Fieldwork legacy frontend, Markup + class conventions, Navigation model, Orientation: how to find things fast, Related, The standard tool-handler shape, Theming (there are TWO theme blocks) (+53 more)

### Community 8 - "graph_intel.py"
Cohesion: 0.06
Nodes (33): _as_list(), get_investigation_subgraph(), merge_entities(), _merge_node(), _merge_rel(), persist_investigation(), link(), _slug() (+25 more)

### Community 9 - "time"
Cohesion: 0.06
Nodes (26): bulk_import_entities(), _canon_label(), detect_type(), _entity_id(), normalise_rows(), _parse_csv(), parse_file(), _parse_json() (+18 more)

### Community 10 - "hashlib"
Cohesion: 0.05
Nodes (21): _audit_id(), log_event(), check_malwarebazaar(), check_urlhaus(), _is_ip(), search_threatfox(), _extract_onion_from_redirect(), _fetch_ahmia() (+13 more)

### Community 11 - "co"
Cohesion: 0.05
Nodes (8): Ao(), bo(), co(), Eo(), Li(), So(), ur, vo()

### Community 12 - "delete"
Cohesion: 0.04
Nodes (32): archive_case(), remove_subject(), unshare_case(), get_document(), add_entity_tag(), auth_deactivate_user(), case_archive(), case_remove_subject() (+24 more)

### Community 13 - "re"
Cohesion: 0.06
Nodes (22): _classify_article(), _parse_results(), search_adverse_media(), _detect_chain(), enrich_wallet_arkham(), _fetch_arkham(), enrich_ip_ipinfo(), _is_private() (+14 more)

### Community 14 - "get_json"
Cohesion: 0.06
Nodes (17): get_json(), _reachable(), _require_stack(), test_locales(), test_persona_save_list_delete(), test_investigate_detect(), test_ipinfo_private_ip_is_graceful(), test_ipinfo_public_ip() (+9 more)

### Community 15 - "asyncio"
Cohesion: 0.06
Nodes (17): _scrape_page(), scrape_telegram_channel(), federated_search(), analyse_media(), extract_frames_and_search(), _ffmpeg_available(), _frame_interval(), reverse_image_links() (+9 more)

### Community 16 - "BackgroundTasks"
Cohesion: 0.06
Nodes (25): bulk_ioc_import(), BulkIOCRequest, _classify_ioc(), _compute_freshness(), entity_freshness(), _feed_enabled(), get_watchlist_schedule(), ioc_parse_preview() (+17 more)

### Community 17 - "ner_pipeline.py"
Cohesion: 0.06
Nodes (15): CrtShCrawler, GitHubCrawler, NewsCrawler, _slug(), OpenCorporatesCrawler, SECCrawler, crawl_person(), _run_crawler() (+7 more)

### Community 18 - "GraphDB"
Cohesion: 0.08
Nodes (9): AlephCrawler, GraphDB, slugify(), After changing the schema or storage shape, Debugging "my data isn't in the graph", Fieldwork shared graph (Neo4j), Schema (`neo4j/init.cypher`), The id-keyed MERGE + provenance convention (follow this when writing) (+1 more)

### Community 19 - "quant-engine/server.py"
Cohesion: 0.10
Nodes (13): backtest(), BtReq, _claude(), CodeReq, _fetch_ohlcv(), generate(), GenReq, health() (+5 more)

### Community 20 - "shell/backend/app/main.py"
Cohesion: 0.09
Nodes (15): Shell backend structure (`shell/backend/app/`), build_deps(), EventBus, Settings, health(), lifespan(), list_modules(), _piper_tts() (+7 more)

### Community 21 - "agent/view.js"
Cohesion: 0.16
Nodes (32): appendLog(), _clearLog(), _clearPlan(), _closeSettings(), _connectStream(), el(), _esc(), _fetchTaskStatus() (+24 more)

### Community 22 - "agent/routes.py"
Cohesion: 0.09
Nodes (20): init(), build_router(), clear_setting(), create_task(), get_capabilities(), get_settings(), stream_task(), update_settings() (+12 more)

### Community 23 - "_tasks_for"
Cohesion: 0.09
Nodes (15): search_court_records(), search_github_users(), check_domain_hibp(), check_email_hibp(), _strip_html(), _summarise_breach(), search_opencorporates(), _auth_note() (+7 more)

### Community 24 - "shell/backend/app/llm_bridge.py"
Cohesion: 0.13
Nodes (13): api_configured(), _auth_headers(), bridge_enabled(), bridge_healthy(), bridge_url(), call_bridge(), call_claude_api(), claude_complete() (+5 more)

### Community 25 - "logging"
Cohesion: 0.10
Nodes (6): _ct_clean(), _ct_node_id(), domain_cert_transparency(), _rel_for_form(), search_sec_filings(), enrich_domain_wayback()

### Community 26 - "ModuleManifest"
Cohesion: 0.08
Nodes (10): Conventions & gotchas, Fieldwork / Runi Shell, Layout (top level), Project knowledge base — READ THIS FIRST, Backend (2 files under `shell/backend/app/modules/<id>/`), Adding a module (checklist), init(), ModuleManifest (+2 more)

### Community 27 - "news/vendor/leaflet/leaflet.js"
Cohesion: 0.08
Nodes (12): a(), at(), Ci(), d(), ei(), ht(), ii(), l() (+4 more)

### Community 28 - "pivot.py"
Cohesion: 0.10
Nodes (13): expand_node(), _fetch_edges(), _fmt_node(), full_graph_sample(), _node_size(), subgraph_around(), graph_viz_endpoint(), _display() (+5 more)

### Community 29 - "gigs/routes.py"
Cohesion: 0.13
Nodes (20): init(), build_router(), draft_proposal(), _ensure_init(), get_gig(), gig_stats(), list_gigs(), refresh_gigs() (+12 more)

### Community 30 - "presence/routes.py"
Cohesion: 0.12
Nodes (23): init(), build_router(), delete_item(), generate_listing(), generate_outreach(), generate_post(), get_platforms(), list_calendar() (+15 more)

### Community 31 - "shell.js"
Cohesion: 0.11
Nodes (22): _animateIn(), _attachIframeBridge(), _boot(), chunkText(), _fallback(), _initPalette(), _M(), off() (+14 more)

### Community 32 - "json"
Cohesion: 0.13
Nodes (14): evidence_text(), load_fixtures(), main(), run_live(), run_offline(), run_selftest(), write_report(), consistency_score() (+6 more)

### Community 33 - "n"
Cohesion: 0.10
Nodes (22): i(), Mi(), r(), zi(), c(), ca(), dn(), er() (+14 more)

### Community 34 - "e"
Cohesion: 0.11
Nodes (24): ai(), animateVisualElement(), ci(), e(), ei(), fi(), gi(), Gr() (+16 more)

### Community 35 - "tempfile"
Cohesion: 0.09
Nodes (9): harvest(), HarvestRequest, health(), _normalise_list(), health(), search(), SearchRequest, health() (+1 more)

### Community 36 - "patch"
Cohesion: 0.08
Nodes (18): delete_task(), toggle_task(), update_case(), annotate_edge(), auth_update_role(), case_delete_task(), case_toggle_task(), case_update() (+10 more)

### Community 37 - "fastapi"
Cohesion: 0.12
Nodes (3): init(), build_router(), ReportsService

### Community 38 - "vl"
Cohesion: 0.10
Nodes (24): ml(), Ql(), vl(), Al(), be(), cl(), dl(), fl() (+16 more)

### Community 39 - "static/vendor/leaflet/leaflet.js"
Cohesion: 0.09
Nodes (6): a(), Ci(), l(), me(), x(), ze()

### Community 40 - "NewsService"
Cohesion: 0.11
Nodes (4): init(), _article_id(), NewsService, NewsSource

### Community 41 - "yn"
Cohesion: 0.11
Nodes (6): Ae(), Cn, sn(), vn(), xn, yn

### Community 44 - "documents.py"
Cohesion: 0.13
Nodes (14): _dms_to_decimal(), _extract_content(), _extract_docx(), _extract_eml(), _extract_exif(), _extract_pdf(), _extract_text_file(), _guess_mime() (+6 more)

### Community 45 - "search.py"
Cohesion: 0.12
Nodes (11): _search_internal(), fuzzy_search(), global_search(), related_search(), _escape(), _first_label(), full_text_search(), _make_query() (+3 more)

### Community 46 - "piper/app.py"
Cohesion: 0.16
Nodes (13): audition(), health(), _ids(), _installed(), _load(), _phonemize(), _russify(), _synth() (+5 more)

### Community 47 - "quant/routes.py"
Cohesion: 0.14
Nodes (16): init(), BtReq, build_router(), backtest(), delete_strategy(), generate(), list_strategies(), _proxy() (+8 more)

### Community 49 - "news/service.py"
Cohesion: 0.12
Nodes (6): build_articles_context(), _utc_now(), _classify_topic(), _clean_html(), _parse_date(), _parse_feed()

### Community 50 - "identity/routes.py"
Cohesion: 0.15
Nodes (13): audit(), init(), _avatar_svg(), _backstory(), build_router(), delete_persona(), _generate(), save_persona() (+5 more)

### Community 51 - "bias.py"
Cohesion: 0.15
Nodes (11): ai_lookup(), bias_for(), build_estimation_prompt(), coverage_balance(), is_rated(), _load_ai_cache(), _match(), _norm() (+3 more)

### Community 52 - "me"
Cohesion: 0.10
Nodes (11): de(), fe(), Gt(), Ht(), le(), me(), p, pe() (+3 more)

### Community 53 - "extract_iocs_from_file"
Cohesion: 0.10
Nodes (10): analyze_image_intel_endpoint(), analyze_media_endpoint(), case_bulk_import(), document_upload(), extract_iocs_from_file(), _extract_text_from_docx(), _extract_text_from_eml(), _extract_text_from_pdf() (+2 more)

### Community 54 - "intel.py"
Cohesion: 0.17
Nodes (11): cluster_articles(), _cosine(), extract_entities(), get_last_brief_at(), match_watchlist(), set_last_brief_at(), watchlist_add(), watchlist_all() (+3 more)

### Community 55 - "recon/app.py"
Cohesion: 0.20
Nodes (12): health(), httpx_probe(), HttpxRequest, nmap_scan(), NmapRequest, nuclei_scan(), NucleiRequest, _parse_nmap_xml() (+4 more)

### Community 56 - "cr"
Cohesion: 0.11
Nodes (11): ar(), bl(), Bs(), cr, gs(), hi(), Ie(), lr() (+3 more)

### Community 57 - "pdf_export.py"
Cohesion: 0.16
Nodes (9): build_pdf_html(), _dt(), _e(), export_case_pdf(), _findings_section(), generate_professional_report(), _md(), _ollama_summary() (+1 more)

### Community 59 - "dashboard.py"
Cohesion: 0.14
Nodes (9): get_dashboard_stats(), get_entity_timeline(), get_recent_activity(), get_top_connected(), _run(), dashboard_recent(), dashboard_stats(), dashboard_timeline() (+1 more)

### Community 60 - "backend/app/llm_bridge.py"
Cohesion: 0.27
Nodes (13): api_configured(), _auth_headers(), bridge_enabled(), bridge_healthy(), bridge_url(), call_bridge(), call_claude_api(), call_claude_api_vision() (+5 more)

### Community 61 - "_compute_risk_score"
Cohesion: 0.11
Nodes (8): build_html_report(), _compute_risk_score(), correlation_shared_entities(), domain_full_profile(), export_graph_extended(), get_entity_risk_score(), graph_risk_overlay(), ReportRequest

### Community 62 - "monitor.py"
Cohesion: 0.14
Nodes (9): add_watch(), _alerted_ids(), check_watch(), _create_alerts(), mark_alerts_seen(), _mark_checked(), remove_watch(), _slug() (+1 more)

### Community 63 - "maltego_transforms.py"
Cohesion: 0.16
Nodes (10): _api(), _build_response(), main(), _parse_request(), transform_domain_to_history(), transform_domain_to_ips(), transform_ip_to_shodan(), transform_person_to_aleph() (+2 more)

### Community 64 - "auth.py"
Cohesion: 0.15
Nodes (7): decode_token(), get_current_user(), hash_password(), optional_user(), require_admin(), _to_bytes(), verify_password()

### Community 65 - "mn"
Cohesion: 0.11
Nodes (5): He(), Je(), mn(), Qe(), tn()

### Community 66 - "passive_dns.py"
Cohesion: 0.19
Nodes (9): _ht_hostsearch(), _ht_reverse_ip(), _merge_domain(), _merge_ip(), _node_id(), passive_dns_domain(), reverse_ip_lookup(), _vt_domain_resolutions() (+1 more)

### Community 67 - "mount"
Cohesion: 0.22
Nodes (17): closeEditModal(), closeTrackModal(), fetchPortfolioData(), fetchRangeSparklines(), getCurrentPrice(), handleAddPosition(), handleEditPosition(), loadPortfolio() (+9 more)

### Community 68 - "switchTab"
Cohesion: 0.18
Nodes (17): _initAnalysisTab(), _initOrderForm(), _initResearchTab(), _initScreenerTab(), _loadAccount(), _loadMacroBar(), _loadPositions(), _loadScreener() (+9 more)

### Community 69 - "app/llm.py"
Cohesion: 0.19
Nodes (8): _bundle_to_text(), extract_entities(), _generate(), _parse_json_array(), pull_model(), suggest_hypotheses(), summarize_case(), Other AI entry points (`llm.py`, Fieldwork bridge)

### Community 70 - "SpiderFootClient"
Cohesion: 0.18
Nodes (4): spiderfoot_promote(), SpiderFootPromoteRequest, promote_scan_to_graph(), SpiderFootClient

### Community 71 - "esc"
Cohesion: 0.14
Nodes (14): Shared helpers — always reuse these (grep to confirm signatures), Add an OSINT enrichment tool (full stack), API keys, Definition of done, Layer 0 — Vendored tool that isn't a hosted API (sibling container), Layer 1 — Crawler (`backend/app/crawlers/<name>.py`), Layer 2 — Route (`backend/app/main.py`), Layer 3 — UI (`frontend/index.html`) (+6 more)

### Community 72 - "build_router"
Cohesion: 0.15
Nodes (8): init(), build_router(), overview(), quote(), sparklines(), _refresh_crumb(), _sparkline_for(), _yget()

### Community 73 - "_compute_indicators"
Cohesion: 0.17
Nodes (11): _bollinger(), _screen_one(), screener(), _compute_indicators(), _ema(), _macd(), _max_drawdown(), _pct_return() (+3 more)

### Community 74 - "build_router"
Cohesion: 0.12
Nodes (4): build_router(), watchlist_create(), watchlist_delete(), watchlist_list()

### Community 75 - "markets/view.js"
Cohesion: 0.28
Nodes (14): _qapi(), _qBacktest(), _qDrawCurve(), _qFmt(), _qGenerate(), _qInitLab(), _qLoadEngine(), _qLoadLibrary() (+6 more)

### Community 76 - "presence/view.js"
Cohesion: 0.31
Nodes (13): _deleteItem(), _esc(), focusContent(), _generateContent(), _generateListing(), _generateOutreach(), _getRoot(), _loadCalendar() (+5 more)

### Community 77 - "reports/view.js"
Cohesion: 0.29
Nodes (14): deleteReport(), escapeHtml(), formatRelative(), generate(), highlightActive(), loadList(), mount(), openReport() (+6 more)

### Community 78 - "claude_bridge.py"
Cohesion: 0.20
Nodes (5): _cli_version(), Handler, _logged_in(), main(), _run_claude()

### Community 79 - "voidaccess.py"
Cohesion: 0.18
Nodes (6): check_ip(), _verdict(), _base_url(), crawl_voidaccess(), _summarize(), _top_entities()

### Community 80 - "dedup.py"
Cohesion: 0.18
Nodes (6): dismiss_duplicate(), _find_attribute_candidates(), _find_name_candidates(), _merge_candidate_scores(), merge_persons(), run_duplicate_detection()

### Community 81 - "verify_api_key"
Cohesion: 0.14
Nodes (8): get_api_key_status(), _load_runtime_keys(), _load_verifications(), _save_runtime_keys(), _save_verifications(), _test_api_key(), update_api_keys(), verify_api_key()

### Community 82 - "semantic_search.py"
Cohesion: 0.19
Nodes (6): batch_index_all(), generate_embedding(), index_entity(), _node_text(), pull_embed_model(), semantic_search()

### Community 83 - "pydantic"
Cohesion: 0.18
Nodes (5): _collect_labels(), CrawlRequest, health(), _parse_tree(), search()

### Community 84 - "markets/routes.py"
Cohesion: 0.19
Nodes (7): AnalyzeRequest, _annualized_vol(), _daily_returns(), _get_sector_spending(), OrderRequest, ResearchRequest, _sharpe()

### Community 85 - "gigs/view.js"
Cohesion: 0.29
Nodes (11): _esc(), _loadGigs(), _loadStats(), mount(), _platformBadge(), refresh(), _renderGigCard(), _scoreBar() (+3 more)

### Community 86 - "scheduler.py"
Cohesion: 0.18
Nodes (4): due_watches(), _monitor_cycle(), _run_crawlers_for(), start_scheduler()

### Community 87 - "opensky.py"
Cohesion: 0.18
Nodes (5): enrich_aircraft_faa(), enrich_aircraft_flights(), _fetch_opensky_flights(), _scrape_faa(), enrich_faa()

### Community 88 - "_fire_webhook_formatted"
Cohesion: 0.17
Nodes (6): _broadcast_event(), _detect_webhook_format(), _fire_webhook(), _fire_webhook_formatted(), _format_webhook_payload(), test_webhook_rich()

### Community 89 - "timeline.py"
Cohesion: 0.24
Nodes (7): global_timeline(), _action_category(), get_case_timeline(), get_global_timeline(), _ms_to_iso(), _normalise_audit(), _ts_to_ms()

### Community 90 - "risk_scoring.py"
Cohesion: 0.22
Nodes (6): risk_high_entities(), _compute_score(), get_high_risk_entities(), _run(), score_all_entities(), score_entity()

### Community 91 - "geo.py"
Cohesion: 0.18
Nodes (5): _compile_patterns(), country_name(), detect_all(), detect_countries(), detect_from_url()

### Community 92 - "m"
Cohesion: 0.21
Nodes (13): be(), c(), De(), e(), hi(), m(), p(), pe() (+5 more)

### Community 93 - "email_headers.py"
Cohesion: 0.29
Nodes (7): _all_header_values(), analyze_and_store(), _header_value(), _ips_from_text(), _is_public(), parse_headers(), _parse_hop()

### Community 94 - "deep_investigate"
Cohesion: 0.17
Nodes (7): deep_investigate(), _node_summary(), _pivots(), How synthesis works (the pipeline to tune), Improving the Claude integration — the levers, Operating: the endpoints, OSINT investigation engine (operate + improve)

### Community 95 - "F"
Cohesion: 0.24
Nodes (12): F(), G(), h(), j(), k(), ke(), ne(), e() (+4 more)

### Community 96 - "_fetch_ohlcv"
Cohesion: 0.17
Nodes (9): analyze(), indicators(), _compute_indicators_for_symbol(), _fetch_ohlcv(), Layout, Markers, Run, Setup (once) (+1 more)

### Community 97 - "W"
Cohesion: 0.27
Nodes (10): arc(), build(), frame(), mount(), readBins(), resize(), unmount(), Li() (+2 more)

### Community 98 - "F"
Cohesion: 0.24
Nodes (12): F(), G(), h(), j(), k(), ke(), ne(), e() (+4 more)

### Community 100 - "mailaccess.py"
Cohesion: 0.27
Nodes (6): _base_url(), enrich_email_mailaccess(), _headers(), _is_finished(), _len(), _normalize()

### Community 101 - "restore_backup"
Cohesion: 0.18
Nodes (7): create_backup(), _serialize(), delete_backup(), download_backup(), restore_backup(), RestoreRequest, _safe_backup_filename()

### Community 102 - "users.py"
Cohesion: 0.20
Nodes (5): get_user_by_id(), get_user_by_username(), list_users(), register_user(), _user_id()

### Community 103 - "m"
Cohesion: 0.24
Nodes (11): at(), d(), ht(), Li(), m(), v(), ve(), W() (+3 more)

### Community 104 - "Runi-OS"
Cohesion: 0.18
Nodes (10): Architecture, Feature highlights, How it compares, License, Quick start, Runi-OS, Screenshots, Security & scope (+2 more)

### Community 105 - "classify_topics"
Cohesion: 0.24
Nodes (5): classify_topics(), _one(), embed_text(), _ensure_anchors(), _do()

### Community 106 - "refresh"
Cohesion: 0.24
Nodes (11): addSymbol(), bindEvents(), fetchCrypto(), fetchStocks(), _flashChangedPrices(), refresh(), removeSymbol(), renderGrid() (+3 more)

### Community 107 - "Runi Shell"
Cohesion: 0.18
Nodes (10): Adding a new native module, File layout, How modules are wired, Iframe module (for legacy code only), Native module (recommended for all new ones), News module — first-use, Roadmap, Run it (+2 more)

### Community 108 - "asn.py"
Cohesion: 0.29
Nodes (5): _asn_node_id(), _bgpview_lookup(), enrich_ip_asn(), _ip_node_id(), _ipapi_lookup()

### Community 109 - "NoClaudeError"
Cohesion: 0.22
Nodes (5): NoClaudeError, chat(), investigate(), _safe(), client()

### Community 110 - "Shell modules"
Cohesion: 0.20
Nodes (9): agent, fieldwork (iframe), gigs — "Gig Hunter", identity — "Identity Forge", markets, news — "News & Brief", presence, reports (+1 more)

### Community 111 - "Jt"
Cohesion: 0.20
Nodes (10): Ae(), Ie(), Jt(), Le(), O(), Qt(), Re(), $t() (+2 more)

### Community 112 - "Fieldwork stack operations"
Cohesion: 0.22
Nodes (8): Data & keys, Everyday commands, Fieldwork stack operations, Service & port map, The apply-a-change matrix (the part that trips people up), The Claude Code bridge (host, not Docker), Verifying a change actually works, When Docker / WSL won't start

### Community 113 - "p"
Cohesion: 0.22
Nodes (9): Ae(), be(), De(), ei(), Ie(), ii(), p(), pe() (+1 more)

### Community 114 - "deep_research"
Cohesion: 0.22
Nodes (5): deep_research(), get_contracts(), _call_claude(), _get_single_quote(), _search_usaspending()

### Community 115 - "cryptoCard"
Cohesion: 0.33
Nodes (9): _blockBar(), cryptoCard(), fmtPct(), fmtPrice(), _hexId(), positionSparkSVG(), sparklineSVG(), _stepPolyline() (+1 more)

### Community 116 - "oi"
Cohesion: 0.28
Nodes (4): At(), bi(), oi(), Q()

### Community 118 - "rdap.py"
Cohesion: 0.36
Nodes (4): enrich_domain(), _looks_like_privacy_shield(), _simple_slug(), _vcard_field()

### Community 119 - "link_analysis.py"
Cohesion: 0.36
Nodes (4): analyze(), _digest(), _duplicate_candidates(), _shared_entities()

### Community 120 - "Contributing to Runi-OS"
Cohesion: 0.25
Nodes (7): Adding a shell module, Before opening a PR, Contributing to Runi-OS, Conventions, Layout, Run the stack, Scope & ethics

### Community 121 - "OSINT API keys — what to set to un-blind the crawlers"
Cohesion: 0.25
Nodes (7): After setting keys, OSINT API keys — what to set to un-blind the crawlers, Priority list (value × availability), Tier 1 — free + high impact (set these first), Tier 2 — freemium / cheap, high impact, Tier 3 — paid, situational, Where keys go

### Community 122 - "Jt"
Cohesion: 0.25
Nodes (8): Jt(), Le(), O(), Qt(), Re(), $t(), te(), Ft()

### Community 123 - "identity/view.js"
Cohesion: 0.61
Nodes (6): api(), generate(), loadSaved(), mount(), renderPersona(), savePersona()

### Community 124 - "maritime.py"
Cohesion: 0.43
Nodes (4): _classify(), track_vessel(), _tracking_links(), _ts_ms()

### Community 125 - "lifespan"
Cohesion: 0.29
Nodes (4): lifespan(), stop_scheduler(), ensure_fulltext_index(), ensure_vector_index()

### Community 126 - "run_all_active"
Cohesion: 0.29
Nodes (3): monitor_run_now(), all_active_watches(), run_all_active()

### Community 129 - "Add / modify a Runi Shell module"
Cohesion: 0.29
Nodes (6): Add / modify a Runi Shell module, After shipping, Deploy & verify, Frontend (folder `shell/frontend/modules/<id>/`), nginx — nothing to do, The id is the contract

### Community 130 - "bi"
Cohesion: 0.29
Nodes (7): bi(), e(), hi(), Pi(), Qe(), Ti(), u()

### Community 131 - "i"
Cohesion: 0.33
Nodes (5): t(), i(), Mi(), r(), zi()

### Community 132 - "_get_cfg"
Cohesion: 0.43
Nodes (6): _alpaca_headers(), _alpaca_url(), alpaca_account(), alpaca_positions(), _get_cfg(), _load_agent_config()

### Community 133 - "news/routes.py"
Cohesion: 0.43
Nodes (4): AskRequest, InvestigateRequest, RetroRequest, WatchAddRequest

### Community 134 - "TDChart"
Cohesion: 0.38
Nodes (7): _drawAnalysisChart(), _drawPortfolioChart(), interpolate(), TDChart(), drawHover(), drawStatic(), poly()

### Community 135 - "etherscan.py"
Cohesion: 0.47
Nodes (3): _eth(), trace_eth_address(), _ts()

### Community 138 - "scan_username"
Cohesion: 0.40
Nodes (3): MaigretClient, scan_username(), UsernameScanRequest

### Community 139 - "Verifying Fieldwork changes"
Cohesion: 0.33
Nodes (5): 0. Is the stack up?, 1. Pick the checks for what you touched, 2. Driving the UI (browser), 3. Before saying "done", Verifying Fieldwork changes

### Community 140 - "Publishing Runi-OS — go-public checklist"
Cohesion: 0.33
Nodes (5): ✅ Already done (on `showcase-prep`), 📋 Final human steps (when you decide to publish), ⚠️ Git history still contains, Publishing Runi-OS — go-public checklist, 🎨 Rebrand: Fieldwork → Runi-OS

### Community 143 - "Demo & screenshot guide"
Cohesion: 0.40
Nodes (4): Demo & screenshot guide, Reset to a clean demo state, Screenshots to capture, The 60-second demo reel

### Community 144 - "LLM engine resolution"
Cohesion: 0.40
Nodes (4): LLM engine resolution, The bridge: `shell/host-bridge/claude_bridge.py`, Translation, TWO bridge modules (different config stores)

### Community 145 - "Investigation eval harness"
Cohesion: 0.40
Nodes (4): Fixtures, Investigation eval harness, Run it, What `--selftest` guarantees

### Community 146 - "pull_request_template.md"
Cohesion: 0.40
Nodes (4): Checklist, Notes for the reviewer, Type, What & why

### Community 147 - "_get_macro_context"
Cohesion: 0.40
Nodes (3): get_macro(), _get_fred_series(), _get_macro_context()

### Community 148 - "_startChassisLife"
Cohesion: 0.40
Nodes (4): _rndByte(), _rndHex(), _startChassisLife(), _updateHex()

### Community 149 - "bi"
Cohesion: 0.40
Nodes (4): bi(), Pi(), Ti(), u()

### Community 157 - "oi"
Cohesion: 0.67
Nodes (4): Je(), ni(), oi(), si()

### Community 158 - "oi"
Cohesion: 0.67
Nodes (4): Je(), ni(), oi(), si()

## Knowledge Gaps
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `esc()` connect `esc` to `cryptoCard`, `mount`, `markets/view.js`?**
  _High betweenness centrality (0.366) - this node is a cross-community bridge._
- **Should `backend/app/main.py` be split into smaller, more focused modules?**
  _Cohesion score 0.01911480259415178 - nodes in this community are weakly interconnected._
- **Why does `Layer 2 — Route (`backend/app/main.py`)` connect `esc` to `_audit`?**
  _High betweenness centrality (0.355) - this node is a cross-community bridge._
- **Should `get` be split into smaller, more focused modules?**
  _Cohesion score 0.017241379310344827 - nodes in this community are weakly interconnected._
- **Should `_val_case_id` be split into smaller, more focused modules?**
  _Cohesion score 0.021367521367521368 - nodes in this community are weakly interconnected._
- **Should `_audit` be split into smaller, more focused modules?**
  _Cohesion score 0.024708304735758406 - nodes in this community are weakly interconnected._
- **Should `motion.js` be split into smaller, more focused modules?**
  _Cohesion score 0.03225806451612903 - nodes in this community are weakly interconnected._