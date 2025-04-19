# Code Review Process

Manually reviewing an entire organization's codebase efficiently is often impractical, unless the codebase is relatively small or the security team is unusually large. To avoid bottlenecks and ensure scalability, it’s important to define clear criteria for when and how manual code reviews should be conducted. For example, reviews can be prioritized for major or minor releases, while patch releases may be exempt. Alternatively, reviews could be triggered by the introduction of new features or scheduled at regular intervals.

Manual reviews should complement automated scanning, not duplicate it. Common vulnerabilities are typically covered by [SAST scans](../devsecops/sast-scans.md) and other automated tools. Therefore, manual efforts should focus on areas beyond the reach of static analysis—such as complex control flows, edge cases, and business logic vulnerabilities. This targeted approach ensures that manual reviews add meaningful value to the overall security assurance process.

## Outcome

- [ ] There's a documented process for the code review and common topics to look for
- [ ] There's a process that outlines the requirements for a manual code review and this is enforced

## Metrics

- [ ] Vulnerabilities found in code review
- [ ] Vulnerabilities found by severity
- [ ] Time to review code

## Tools & Resources

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) (Free)
- [OWASP Cheat Sheet Series](https://owasp.org/www-project-cheat-sheets/) (Free)
- [OWASP Mobile Application Security Checklist](https://mas.owasp.org/checklists/MASVS-PLATFORM/) (Free)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) (Free)
- [OWASP API Security Project](https://owasp.org/www-project-api-security/) (Free)

## Further Reading

- [TBD](http://example.com)
