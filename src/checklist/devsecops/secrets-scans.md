# Secrets Scans

Leaked secrets represent one of the most critical security vulnerabilities in modern software development, providing attackers with direct, unauthorized access to systems, databases, cloud services, and APIs. When credentials like API keys, database passwords, or access tokens are exposed in source code, logs, or configuration files, they create immediate pathways for data breaches, system compromise, and lateral movement within organizational infrastructure. The impact extends beyond the initial exposure, as these credentials often provide persistent access that can be exploited long after the initial leak.

Hardcoded secrets are particularly problematic because they embed sensitive credentials directly into application code, making them visible to anyone with access to the codebase. This practice violates fundamental security principles by removing the ability to rotate credentials independently of code deployments, creating permanent security vulnerabilities that persist across all environments where the code is deployed. Additionally, hardcoded secrets often end up in version control systems, build artifacts, and distributed applications, exponentially expanding their exposure surface.

However, implementing effective secrets scanning presents significant operational challenges due to high false positive rates inherent in entropy-based detection algorithms. These algorithms identify strings with high randomness that resemble secrets, but frequently flag legitimate code elements like hashes, IDs, or encoded data that aren't actually sensitive credentials. Organizations must invest significant effort in identifying and filtering common false positive patterns specific to their technology stack and coding practices to make secrets scanning actionable.

The key to effective secrets management lies in combining automated detection with intelligent validation processes. For recognizable token formats like GitHub Personal Access Tokens (PATs), scanning tools can test discovered credentials against their respective services to confirm validity - a live GitHub PAT represents a high-severity finding requiring immediate remediation, while an invalid token can be safely discarded. However, many discovered tokens lack easily recognizable formats or aren't testable against public APIs, requiring manual validation processes to distinguish genuine security risks from benign false positives.

## Outcome

- [ ] Secrets scanning is executed on every contribution to the source code management (SCM) system.
  - [ ] Git history is also scanned periodically to identify any previously committed secrets.
- [ ] All findings are integrated into the [vulnerability management program](../product-security/vulnerability-management-program.md).
- [ ] Scanning tools are properly customized to reduce false positives:
  - [ ] Detection rules are tailored to align with specific business and technical requirements.
  - [ ] Irrelevant or non-applicable rules are disabled based on the project's context.
  - [ ] Known secret patterns are tested against their service to ensure accurate detection.
- [ ] Developers receive immediate feedback on findings, ideally during pull request (PR) reviews within the SCM platform.
- [ ] Secrets following defined patterns are detected and blocked before they can be committed to the SCM.
- [ ] A clear and documented process is in place for properly removing secrets from source control and invalidating exposed credentials.
- [ ] A standardized format is defined for organization-generated secrets, where possible, and custom detection rules are implemented to identify them in code.

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Kingfisher](https://github.com/mongodb/kingfisher) (Free)
- [TruffleHog](https://trufflesecurity.com/trufflehog) (Free)
- [GitLeaks](https://github.com/gitleaks/gitleaks) (Free)
- [Github's Push Protection](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations) (Paid)

## Further Reading

- [Removing sensitive information from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Phantom Secrets: Undetected Secrets Expose Major Corporations](https://www.aquasec.com/blog/undetected-hard-code-secrets-expose-corporations)
