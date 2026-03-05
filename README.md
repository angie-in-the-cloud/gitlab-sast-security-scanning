# GitLab SAST Security Scanning

Extends the [compliance pipeline](https://github.com/angie0120/gitlab-compliance-pipeline) with GitLab's built-in SAST scanning using Semgrep, automatically detecting vulnerabilities on every commit.

--- 

### What Was Added
- `vulnerable_app.py` - intentionally insecure Python file containing a SQL injection vulnerability (for demo purposes only)
- SAST stage added to `.gitlab-ci.yml` using GitLab's built-in template

---

### What Semgrep Found
| Field | Detail |
|---|---|
| Vulnerability | SQL Injection |
| Severity | High |
| File | vulnerable_app.py, line 8 |
| Rule | Bandit B608 |
| Standard | CWE-89, OWASP A03:2021 Injection |

---

### How to View the SAST Report
1. Go to **Build → Pipelines**
2. Click the latest pipeline
3. Click the **semgrep-sast** job
4. On the right side under **Job artifacts**, click **"Download SAST report"**
5. Open `gl-sast-report.json` to see full vulnerability details

---

### Key Takeaway
SAST tools catch what their ruleset covers. The scan caught the SQL injection as a High severity finding mapped to OWASP A03:2021, but missed the hardcoded credential, which is a realistic reminder that no single tool catches everything, and layered security controls are essential.

---

### GRC/Compliance Alignment
| Pipeline Behavior | GRC Concept |
|---|---|
| SAST runs on every commit | Continuous security testing vs. point-in-time pen tests |
| High severity finding flagged | Risk identification and prioritization |
| Mapped to OWASP/CWE standards | Compliance framework alignment |
| Artifact report generated | Audit evidence and documentation |

---

## Screenshots
### SAST findings in job log

![Job-log](./screenshots/job-log.png)

### Download SAST report location

![SAST-Report](./screenshots/sast-report.png)

---
