# Supply Chain Management

A supply chain refers to the pieces involved in in the creation and deployment of a product. A weak link in the supply chain can compromise the entire application, and even impact a wield range of applications. A well-known example is the log4j incident, where a vulnerability was discovered in the log4j library, a common piece of software used in countless applications. This critical severity flaw had a huge ripple effect because the library was a part of so many products, making them all vulnerable.

Understanding and securing the supply chain is crucial because a single weak link can pose risks to the entire chain. In the case of log4j, the vulnerability exposed numerous systems to potential cyber attacks, showcasing the importance of vigilance at every stage.

Although supply chain security includes a broad range of topics beyond just software and dependencies, the most common focus is in the software realm and specifically implementing [SCA](../devsecops/sca-scans.md) tools to analyze the dependencies used in projects.

A key part of this approach regularly missed by organizations involves creating a policy that defines which libraries are acceptable for use in a project. One effective method is implementing scorecards that assign a basic score to each library based on a set of criteria. These criteria can be used as a sanity check to determine if an open-source library is properly maintained and secure.

These scorecards evaluate factors such as:

- **Maintenance Activity**: Frequency of updates and responsiveness to issues.
- **Security Practices**: Implementation of security best practices and presence of known vulnerabilities.
- **Community Support**: Level of community engagement and support.
- **Documentation Quality**: Availability and comprehensiveness of documentation.

By using scorecards, organizations can make informed decisions about which dependencies to include in their projects, ensuring that the libraries they rely on are both secure and well-maintained which can decrease the risk of a compromised supply chain.

## Outcome

- [ ] Define and implement an acceptance criteria for choosing open source projects to be included in projects
- [ ] Validate that open source project's license can be used for the intended use.
- [ ] Developers have a flow or instructions to check the Open Source projects they intend to use are acceptable under the policy
- [ ] Detect usage of open source projects not compliant with the acceptance policy
- [ ] Scorecards/Risk scores for the used open source projects are created and tracked (in [Assets Inventory](../grc/asset-inventory.md)  or in [SBOM tools](../devsecops/sboms.md))
- [ ] [SCA scans](../devsecops/sca-scans.md) are run for all projects and integrated in the [vulnerability management program](../product-security/vulnerability-management-program.md)
- [ ] [SBOM](../devsecops/sboms.md)'s are generated and processed
- [ ] Create controls to prevent (if applicable) dependency confusion

## Metrics

- [ ] Percentage of compliant/non compliant libraries
- [ ] Number of libraries per license
- [ ] Top libraries with higher Risk Score
- [ ] Top Libraries with more reported (and open) vulnerabilities
- [ ] Percentage of new libraries onboarded with the defined process

## Tools & Resources

- [SecurityScoreCards](https://securityscorecards.dev/) - Generate or query a risk score card for open source projects (Free)
- [DependencyTrack](https://dependencytrack.org/) - Supply Chain management for Dependencies and Risk Classification tool (Free)
- [tldrLegal](https://www.tldrlegal.com/) - Tool to help identifying permissions for open source licenses (Free)
- [Deps.dev](https://deps.dev/) (Free) - Provides a lot of information, including scorecards for libraries (API available) (Free)
- [OSV Database](https://osv.dev/list) - Open Source Vulnerabilities Database (Free)
- [Semgrep Supply Chain](https://semgrep.dev/products/semgrep-supply-chain/) (Paid)
- [package-analysis](https://github.com/ossf/package-analysis?tab=readme-ov-file) - Tool to look for some malware related behaviors in open source packages (Free)
- [supply-chain-firewall](https://github.com/DataDog/supply-chain-firewall) (Free)
- [GuardDog](https://github.com/DataDog/guarddog) - Check for malicious dependencies (Free)

## Further Reading

- [Open Source Security](https://snyk.io/series/open-source-security/)
- [Dependency Management Best Practices from Google](https://cloud.google.com/blog/topics/developers-practitioners/best-practices-dependency-management%20#)
- [The State of Software Supply Chain Security 2024](https://www.reversinglabs.com/sscs-report-thank-you)
- [Defining a secure open source policy](https://snyk.io/series/open-source-security/open-source-policy/)
- [[A Step-by-step Guide to Preventing Dependency Confusion Attacks](https://www.jit.io/blog/preventing-dependency-confusion-attacks)]
