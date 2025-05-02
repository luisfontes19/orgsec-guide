# Infrastructure Scanning

[TBD]

- Cloud Security Posture Management (CSPM): Identifies misconfigurations and compliance risks in cloud infrastructure.
- Cloud Infrastructure Entitlement Management (CIEM): Manages and automates access permissions in cloud environments.
- Cloud Workload Protection Platform (CWPP): Protects cloud workloads, including containers, servers, and serverless functions.
- Infrastructure-as-Code (IaC) Scanning: Detects security issues early in the development process.
- Data Security Posture Management (DSPM): Discovers sensitive data sources and who has access to them.

## Outcome

- [ ] Vulnerability Scanning is performed regularly against the infrastructure
- [ ] The scanning tools are properly customized to reduce false positives
- [ ] Findings are being pushed to the [vulnerability management program](../product-security/vulnerability-management-program.md)
- [ ] Severity/Priority is recalculated based on the asset's criticality/risk

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Nuclei](https://github.com/projectdiscovery/nuclei) (Free)
- [OpenVAS](https://www.openvas.org/) (Free)
- [Prowler](https://github.com/prowler-cloud/prowler) (Free/Paid)
- [SecureCodeBox](https://github.com/secureCodeBox/secureCodeBox) (Free)
- [Wizz](https://www.wiz.io/) (Paid)
- [Nessus](https://www.tenable.com/products/nessus) (Paid)
- [AWS Security MCP](https://github.com/groovyBugify/aws-security-mcp) (Free)

## Further Reading

- [Implementing CNAPP: Tool Selection and Day 1 Focus Areas](https://naman16.github.io/cloud-security/)
- [Testing and evaluating GuardDuty detections](https://aws.amazon.com/blogs/security/testing-and-evaluating-guardduty-detections/)
