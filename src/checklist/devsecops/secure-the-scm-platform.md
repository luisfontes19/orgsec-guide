# Secure the SCM Platform

[TBD]

## Outcome

- [ ] Repository access is restricted using a least privilege approach, granting only the necessary permissions to each user or team.
- [ ] Pull request merges require approval from designated code owners to ensure proper oversight and code quality.
- [ ] Monitoring is in place to detect and alert on any attempts to bypass access restrictions or review requirements.
- [ ] CI/CD pipelines (e.g., [GitHub Workflows](https://docs.github.com/en/actions/using-workflows), [GitLab CI Pipelines](https://docs.gitlab.com/ee/ci/pipelines/)) are reviewed and hardened to prevent malicious users from impacting deployed environments. Controls are implemented to minimize potential damage.
- [ ] Signed commits are enforced, and a verification process is in place to ensure signatures match a list of trusted users and keys.

## Metrics

- [ ] Number of detected bypasses to the controls applied
- [ ] Number of exceptions to the controls applied
- [ ] Percentage of repositories covered

## Tools & Resources

- [Semgrep](https://semgrep.dev/) (Free)

## Further Reading

- [OWASP's CI/CD Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
- [OWASP's Secure SCM Configuration](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html#secure-scm-configuration)
- [Enforcing device trust [and commit signatures] on code changes](https://www.figma.com/blog/how-we-enforce-device-trust-on-code-changes/)
- [Mitigating Attack Vectors in GitHub Workflows](https://openssf.org/blog/2024/08/12/mitigating-attack-vectors-in-github-workflows)
- [GitHub Actions: A Cloudy Day for Security - Part 1](https://binarysecurity.no/posts/2025/08/securing-gh-actions-part1)
