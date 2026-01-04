# Log Analyzer Tool

A lightweight Python CLI tool for quickly analyzing log files and counting entries by severity level.

Perfect for getting a fast overview of system logs without opening massive files or manually counting entries.

---

## 🎯 What It Does

- Reads any `.log` file line-by-line
- Counts total log entries
- Categorizes entries by level (ERROR, WARNING, INFO, DEBUG, etc.)
- Displays a clean summary report
- Handles missing files and errors gracefully

---

## 🚀 Quick Start
```bash
python log_analyzer.py
```

When prompted, enter the path to your log file (try `sample.log` to test it).

---

## 📊 Example Output
```
=== Log Analyzer Tool ===
Enter path to log file: sample.log

=== Log Analysis Report ===
Total log entries: 14
ERROR: 5
WARNING: 2
INFO: 6
DEBUG: 1
```

---

## 💡 Use Cases

**Quick Health Checks:**
- See error count at a glance without opening huge log files
- Identify if a system has excessive errors or warnings
- Compare before/after error rates when testing fixes

**Learning & Practice:**
- Understand log file formats
- Practice file I/O and text parsing in Python
- Build foundational skills for DevOps/support work

---

## 🛠 Technical Details

**Built with:**
- Python's `Counter` from `collections` for efficient counting
- Simple string parsing (split on `:` to extract log levels)
- Robust error handling for missing/corrupt files

**Design decisions:**
- Kept it simple and focused — does one thing well
- No external dependencies — runs anywhere Python runs
- Fast processing — handles thousands of entries quickly

---

## 🔮 Possible Enhancements

If I expand this project later:
- Parse timestamps to show errors per hour/day
- Identify most common error messages (not just counts)
- Support multiple log formats (Apache, Nginx, JSON)
- Export reports to CSV or JSON
- Add filtering by date range or severity level

---

## 🎓 What I Learned

- File I/O and line-by-line processing for large files
- Using `Counter` for efficient frequency analysis
- Defensive programming (handling missing files, malformed data)
- Building focused CLI tools that solve a specific problem

This is Day 7 of my 8-day Python portfolio sprint — building practical tools to demonstrate job-ready skills.

---

## 📬 Connect

**Megan Merrigan** | [GitHub](https://github.com/SunshineKeys) | [LinkedIn](https://linkedin.com/in/megan-merrigan-a824a1265)
