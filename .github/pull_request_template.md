Pull Request Checklist

1. What does this PR do?

<!-- Describe the changes made in this Pull Request in one or two lines -->2. Member / Task

- Member: M5 – DataOps Engineer
- Day: Day 1
- Task: GitHub Repository Setup and Bronze Contract Testing

3. Checklist

- [ ] Branch name follows "feature/<member>-<what>" naming convention.
- [ ] Notebook runs from beginning to end on a fresh cluster without errors.
- [ ] No hard-coded paths; uses "config/project_config.py".
- [ ] No passwords, tokens or data files committed.
- [ ] Bronze raw values are not modified or deleted.
- [ ] Expected versus actual record counts are documented.
- [ ] Decision log is updated if any rule or assumption changes.

4. Testing Evidence

<!-- Include test results and execution evidence -->- [ ] BR-01: Bronze record counts validated.
- [ ] BR-02: Required columns validated.
- [ ] BR-03: Source lineage validated.
- [ ] BR-04: Duplicate records preserved in Bronze.
- [ ] BR-05: Rescued data checked.
- [ ] BR-06: Ingestion replay test completed.

5. Evidence

Validation| Expected Result| Actual Result
Sensor Events| 11,540| Pending
Status CDC| 520| Pending
Secondary Events| 310| Pending
Plant Reference| 110| Pending
Machine Reference| 150| Pending

6. Reviewer Approval

- [ ] Code reviewed by another team member.
- [ ] All review comments resolved.
- [ ] PR approved before merging.

Reviewer: M1 – Technical Lead

Final Status: Pending Review
