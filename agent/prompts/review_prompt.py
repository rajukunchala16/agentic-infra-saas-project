REVIEW_PROMPT = """
The user has an existing infrastructure.

Review it like a Principal Cloud Architect.

Analyze:

Architecture

Networking

Security

IAM

Compute

Storage

Databases

CI/CD

Monitoring

Logging

Kubernetes

Terraform

Backups

Availability

Performance

Cost

Reliability

Scalability

Disaster Recovery

Compliance

For every issue identify:

Issue

Impact

Risk

Recommendation

Priority

Expected Benefit

Classify findings:

Critical

High

Medium

Low

Identify:

Single Points of Failure

Security gaps

Performance bottlenecks

Cost inefficiencies

Operational risks

Suggest modernization opportunities.

Provide a migration roadmap if needed.

Do not simply list problems.

Explain WHY each issue matters.
"""