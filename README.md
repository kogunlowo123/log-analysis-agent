# Log Analysis Agent

[![CI](https://github.com/kogunlowo123/log-analysis-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/log-analysis-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Intelligent log analysis agent that parses structured and unstructured logs, detects anomalies using pattern recognition, correlates events across distributed systems, generates natural language summaries of log patterns, and creates alerting rules from observed anomalies.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_logs` | Search logs with natural language queries translated to log query syntax |
| `detect_anomalies` | Detect anomalous patterns in log streams |
| `correlate_events` | Correlate events across multiple services using trace IDs |
| `summarize_patterns` | Summarize recurring log patterns in natural language |
| `create_alert_rule` | Create alerting rule from an observed log pattern |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/logs/search` | Search logs with natural language |
| `POST` | `/api/v1/logs/anomalies` | Detect log anomalies |
| `POST` | `/api/v1/logs/correlate` | Correlate events across services |
| `POST` | `/api/v1/logs/summarize` | Summarize log patterns |
| `POST` | `/api/v1/logs/alerts` | Create alert rule |

## Features

- Log Parsing
- Anomaly Detection
- Event Correlation
- Pattern Summarization
- Alert Rule Generation

## Integrations

- Elasticsearch
- Grafana Loki
- Cloudwatch Logs
- Splunk
- Datadog

## Architecture

```
log-analysis-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── log_analysis_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Elasticsearch + Loki + CloudWatch Logs + Splunk**

---

Built as part of the Enterprise AI Agent Platform.
