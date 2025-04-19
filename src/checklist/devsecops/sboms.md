# SBOMs

A Software Bill of Materials (SBOM) is a detailed inventory of all the components, libraries, and dependencies that make up a software application. It functions as a comprehensive list of the "ingredients" used in software development, including open-source and third-party components. This transparency is crucial for organizations to understand what technologies are in use within their software and infrastructure.

The importance of an SBOM lies in its ability to help organizations effectively manage and secure their software assets. By tracking the components within an application, an SBOM enables teams to quickly identify whether any part of their software is affected by specific scenarios, such as newly discovered vulnerabilities, license restrictions, or compliance requirements. This proactive approach reduces the risk of exploitation, ensures legal compliance, and facilitates faster remediation when issues arise.

Having SBOMs is not only essential for internally developed software but also for external tools and third-party applications that an organization relies on, although these may not be easy or even possible to obtain. External tools may include software-as-a-service (SaaS) platforms, open-source libraries, or vendor-provided solutions. An SBOM for these tools provides visibility into potential risks and helps organizations maintain a secure and compliant software ecosystem.

## Outcome

- [ ] Generate SBOMs for all in-house developed applications, including:
  - [ ] Application dependencies
  - [ ] Binaries within containers or servers
  - [ ] Tools used during testing and deployment
- [ ] Utilize a dedicated tool to manage and track SBOMs effectively.
- [ ] Regularly request and review SBOMs for external applications where possible.

## Metrics

- [ ] Percentage of projects covered with SBOM's

## Tools & Resources

- [CycloneDX](https://cyclonedx.org/) (Free)
- [Github Dependency Graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph) (Free)
- [DependencyTrack](https://dependencytrack.org/) (Free)
- [Neo4Cyclone](https://github.com/javixeneize/neo4cyclone) (Free)
- [Syft](https://github.com/anchore/syft/) (Free) - Container Image SBOMS

## Further Reading

- [OWASP SCVS](https://scvs.owasp.org/)
- [Using Open-Source Software Composition Analysis Tool From Google](https://medium.com/@theowni/using-open-source-software-composition-analysis-tool-from-google-70fef62ec104)
