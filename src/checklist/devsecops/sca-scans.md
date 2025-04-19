# SCA Scans

Software Composition Analysis (SCA) is a critical part of application security focused on identifying vulnerabilities in third-party libraries and dependencies used throughout a codebase. Modern software development heavily relies on open-source components, which can introduce risks if not properly monitored. SCA tools help teams detect known vulnerabilities, license issues, and outdated components, ensuring that software remains secure and compliant.

When selecting an SCA tool, it's recommended to choose one that can output results using the [OpenSSF OSV](https://ossf.github.io/osv-schema/) format. This standardized schema simplifies integration with other tools and platforms, improving automation and reporting across the vulnerability management lifecycle.

A common mistake in SCA practices is excluding vulnerabilities found in development dependencies under the assumption that they don't affect production environments. However, this approach can expose developer machines to serious threats. For example, the [Wrangler vulnerability](https://github.com/advisories/GHSA-f8mp-x433-5wpf) demonstrated how even non-production dependencies can be exploited to compromise local environments.

To ensure comprehensive security coverage, it's important to assess and address vulnerabilities across all dependencies, production and development alike.

## Outcome

- [ ] SCA scans are executed on every contribution to the source code management (SCM) system and on a regular schedule.
- [ ] All findings are integrated into the [vulnerability management program](../product-security/vulnerability-management-program.md) for centralized tracking and remediation.
- [ ] Vulnerability severity and priority are recalculated based on the project's criticality and risk profile.
- [ ] Developers receive immediate feedback on findings, ideally during pull request (PR) reviews within the SCM platform.
- [ ] Aim to use [EPSS](https://www.first.org/epss/) scores to help prioritize vulnerabilities based on their likelihood of exploitation in the wild.
- [ ] Implement reachability analysis to determine whether the vulnerable code is actually used in the application, helping reduce false positives and focus on actionable issues.

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Google OSV-Scanner](https://google.github.io/osv-scanner/) Client tool for [OSV](https://osv.dev/) (Free)
- [OWASP DepScan](https://github.com/owasp-dep-scan/dep-scan) Project to find vulnerabilities in dependencies  (free)
- [Renovate](https://www.mend.io/renovate/) Tool for dependency updates (Free)
- [Devs.dev](https://deps.dev/) Insights about open source projects, includes OpenSSF scorecards (free)
- [OSV](https://osv.dev/) Vulnerability database (Free)
- [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot) Open source tool to find vulnerabilities in dependencies (Free)
- [OpenSSF Scorecards](https://scorecard.dev/) Database with scorecards for open source (free)
- [OWASP Dependency Track](https://dependencytrack.org/) Tool to manage dependencies (Free)
- [Datadog's malicious-software-packages-dataset](https://securitylabs.datadoghq.com/articles/introducing-supply-chain-firewall/) (Free)
- [Snyk SCA](https://snyk.io/product/open-source-security-management/) (Free/Paid)

## Further Reading

- [TBD](http://example.com)
