DESIGN_PROMPT = """
The user wants to design a new infrastructure.

Before designing:

Gather missing information.

Ask only the necessary questions such as:

- Cloud provider?
- Monthly users?
- Peak concurrent users?
- Expected traffic?
- Budget?
- Regions?
- Multi-tenancy?
- Authentication?
- Compliance?
- SLA?
- Database preference?
- Kubernetes required?
- AI workloads?
- Storage requirements?

Once sufficient information is available, create:

1. Executive Summary

2. Architecture Overview

3. Architecture Diagram (Mermaid)

4. Component Breakdown

5. Request Flow

6. Security Architecture

7. Networking Design

8. Compute Layer

9. Storage Layer

10. Database Design

11. Messaging Layer

12. Caching Strategy

13. Kubernetes Design (if applicable)

14. CI/CD Pipeline

15. Monitoring Stack

16. Logging Stack

17. Disaster Recovery

18. High Availability

19. Cost Optimization

20. Future Improvements

Every recommendation should explain:

Why chosen

Alternatives

Trade-offs

Expected benefits

Cost impact

Operational complexity

Always build for production.
"""