Project RAID Log

Project: Capstone 05 – IoT Equipment Reliability

Owner: M5 – DataOps Engineer

1. Risks

ID| Risk| Impact| Mitigation| Owner
R01| Azure SQL connectivity unavailable| Reference data ingestion delay| Use approved extracts if permitted| M1
R02| Schema mismatch| Ingestion failure| Validate source schema| M2

2. Assumptions

ID| Assumption| Validation
A01| Source files follow expected schema| Source profiling
A02| Bronze preserves raw records| Contract testing

3. Issues

ID| Issue| Status| Resolution
I01| No issues recorded yet| Open| Update when identified

4. Dependencies

ID| Dependency| Responsible Member
DEP01| Unity Catalog setup| M1
DEP02| Bronze ingestion| M2
DEP03| Source profiling| M3
DEP04| Data dictionary and KPIs| M4
DEP05| Repository and testing| M5

Update this document whenever a risk, assumption, issue or dependency changes.
