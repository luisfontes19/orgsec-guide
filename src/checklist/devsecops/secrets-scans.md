# Secrets Scans

[TBD]

## Outcome

- [ ] Secrets scanning is executed on every contribution to the source code management (SCM) system.
- [ ] All findings are integrated into the [vulnerability management program](../product-security/vulnerability-management-program.md).
- [ ] Scanning tools are properly customized to reduce false positives:
  - [ ] Detection rules are tailored to align with specific business and technical requirements.
  - [ ] Irrelevant or non-applicable rules are disabled based on the project's context.
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
