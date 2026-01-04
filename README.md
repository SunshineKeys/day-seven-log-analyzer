# Log Analyzer & System Report Tool

A Python CLI tool for parsing server logs and generating diagnostic reports. Built to understand how DevOps and support teams troubleshoot production issues.

When systems break at 2am, engineers need to quickly identify patterns in thousands of log entries. This tool automates that process — parsing logs, categorizing errors, and surfacing what matters most.

---

## 🎯 The Problem This Solves

Production logs can contain tens of thousands of entries. Finding patterns manually is time-consuming and error-prone. This tool:

- **Quickly identifies error hotspots** — which errors occur most frequently
- **Categorizes by severity** — ERROR vs WARNING vs INFO
- **Generates actionable reports** — see what's broken at a glance
- **Handles messy real-world data** — safely processes malformed entries

Perfect for troubleshooting, monitoring system health, and identifying recurring issues before they escalate.

---

## ✨ Features

- Parse standard log file formats (Python, Apache, system logs)
- Count entries by log level (ERROR, WARNING, INFO)
- Identify most common error messages
- Generate clean summary reports
- Robust error handling for malformed log entries
- Includes sample log file for testing

---

## 🚀 Quick Start
```bash
# Run the analyzer
python log_analyzer.py

# When prompted, enter log file path
# Try the included sample.log to see it in action
```

---

## 📊 Example Output
```
=== Log Analysis Report ===

Total entries analyzed: 247

Breakdown by level:
  ERROR: 45 entries (18.2%)
  WARNING: 23 entries (9.3%)
  INFO: 179 entries (72.5%)

Top 5 errors:
  [12x] Database connection timeout
  [8x] Failed to authenticate user session
  [7x] Memory limit exceeded in worker process
  [6x] API rate limit reached
  [5x] Null pointer exception in payment module

Analysis complete. Review errors above to prioritize fixes.
```

---

## 💡 Real-World Use Cases

**DevOps & SRE:**
- Monitor production system health
- Identify recurring failures before they cause outages
- Automate log analysis in CI/CD pipelines

**Technical Support:**
- Quickly diagnose customer issues from logs
- Identify patterns across multiple support tickets
- Provide data-driven troubleshooting

**Development:**
- Debug applications by analyzing test/dev logs
- Track error trends across releases
- Validate fixes by comparing before/after log patterns

---

## 🛠 Technical Details

**Technologies:**
- Python (file I/O, string parsing, data aggregation)
- Regex for pattern matching
- Dictionary-based frequency analysis
- Defensive programming with error handling

**Handles:**
- Various log formats (Python, Apache, system logs)
- Malformed or incomplete log entries
- Large files (thousands of entries)
- Empty files and edge cases

---

## 🎓 What I Learned Building This

This project taught me how operations teams approach system reliability:

- **Pattern recognition** — Most production issues follow patterns
- **Data-driven debugging** — Frequency matters more than individual errors
- **Defensive coding** — Real-world logs are messy and unpredictable
- **Practical automation** — This tool saves hours of manual log review

It also reinforced core Python skills: file handling, text processing, data structures, and building tools that solve real problems.

---

## 🔮 Future Enhancements

- Support for JSON and structured log formats
- Time-based analysis (errors per hour/day)
- Export reports to CSV for spreadsheet analysis
- Integration with monitoring tools (Datadog, Splunk)
- Web dashboard for visualizing trends

---

## 📝 Why This Project Matters

As someone transitioning from healthcare to tech, I wanted to understand the day-to-day challenges DevOps and support engineers face. This tool demonstrates that I can:

- Build practical automation that solves real problems
- Think like an operations engineer
- Write code that handles messy, real-world data
- Create tools that improve team efficiency

---

## 📬 Connect

Built by **Megan Merrigan** | [GitHub](https://github.com/SunshineKeys) | [LinkedIn](https://linkedin.com/in/megan-merrigan-a824a1265)

Part of my 8-day Python portfolio sprint — building tools that demonstrate job-ready skills for technical support, DevOps, and development roles.
