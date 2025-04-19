# Container Scanning

A container scanner is an essential tool for maintaining the security of containerized applications. Containers package an application along with its dependencies, making them consistent and portable. However, this convenience also comes with potential risks. Developers, either due to time constraints or lack of awareness, may not always adhere to security best practices when building container images. This can inadvertently introduce vulnerabilities, such as misconfigurations, inclusion of unnecessary binaries, or outdated dependencies.

Even if a container is initially built following best practices, the components within it (libraries, binaries, or system tools) can become vulnerable over time as new security issues are discovered. Without continuous scanning, these vulnerabilities might go unnoticed, exposing the organization to risks such as exploitation, data breaches, or service interruptions.

A container scanner mitigates these risks by continuously analyzing container images for known vulnerabilities, insecure configurations, and outdated dependencies. It enables teams to identify and address issues early in the SDLC, reducing the likelihood of deploying insecure containers to production. By integrating container scanning into the CI/CD pipeline, organizations can enforce security standards, maintain compliance, and ensure that the foundation of their applications remains robust and resilient against emerging threats.

## Outcome

- [ ] Perform container scans for every image build to identify potential vulnerabilities early.
- [ ] Regularly scan deployed containers to ensure ongoing security and detect newly discovered issues.
- [ ] Integrate findings into the [vulnerability management program](../product-security/vulnerability-management-program.md) for proper tracking and resolution.
- [ ] Configure container scanning tools to minimize false positives:
  - [ ] Tailor rules to align with specific business needs.
  - [ ] Disable rules that are not relevant to the project or organization.
- [ ] Provide timely feedback to developers on identified findings to enable prompt remediation.

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Trivy](https://trivy.dev/) (Free)
- [Clair](https://github.com/quay/clair) (Free)
- [Anchore](https://anchore.com/opensource/) (Free)
- [Grype](https://github.com/anchore/grype) (Free)
- [Amazon ECR](https://aws.amazon.com/ecr/) (Paid)
- [Wiz](https://www.wiz.io/solutions/container-and-kubernetes-security) (Paid)

## Further Reading

- [TBD](http://example.com)
