# Sast Scans

Static Application Security Testing (SAST) analyzes source code to detect vulnerabilities early in the Software Development Lifecycle (SDLC). It provides fast feedback, allowing teams to address security issues when they are easier and cheaper to fix.

SAST is often integrated into Source Code Management (SCM) systems, like GitHub, enabling automatic scans during pull requests or commits. This ensures security checks become a seamless part of the development workflow.

To maximize value, chosen SAST tools should support SARIF for better integration with CI/CD pipelines and be fine-tuned to reduce false positives. Configuring tools to recognize the frameworks and libraries developers use (if needed) ensures more accurate results and actionable insights.

SAST tools vary in their ability to support different programming languages and frameworks. While some comprehensive tools can analyze multiple languages effectively, others specialize in specific languages or ecosystems, offering deeper insights and better accuracy. Depending on the organization’s technology stack, a single SAST tool may suffice, or it might be beneficial to use multiple tools, selecting the best one for each language. This tailored approach ensures more accurate results and a stronger overall security posture.

## Outcome

- [ ] Ensure SAST scans are executed for every contribution to the Source Code Management (SCM) system.
- [ ] Integrate SAST findings into the [Vulnerability Management Program](../product-security/vulnerability-management-program.md).
- [ ] Customize SAST tools to minimize false positives:
  - [ ] Adapt rules to align with specific business requirements.
  - [ ] Disable rules that are irrelevant to the project or organization.
- [ ] Provide developers with prompt feedback on findings, ideally during pull requests in the SCM.

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Semgrep](https://semgrep.dev/) (Free/Paid)
- [Mobsfscan](https://github.com/MobSF/mobsfscan) (Free)
- [Breakman](https://brakemanscanner.org/) (Free)
- [Bandit](https://bandit.readthedocs.io/en/latest/) (Free)
- [FindSecBugs](https://find-sec-bugs.github.io/) (Free)
- [KICS](https://www.kics.io/) (Free)
- [Tfsec](https://github.com/aquasecurity/tfsec) (Free)
- [Checkov](https://www.checkov.io/) (Free)
- [Github Code Scanning](https://docs.github.com/en/code-security/code-scanning) (Free/Paid)
- [Snyk Code](https://snyk.io/product/snyk-code/) (Paid)

## Further Reading

- [A Guide On Implementing An Effective SAST Workflow](https://www.anshumanbhartiya.com/posts/sast-workflow?utm_source=pocket_saves)
- [Building a SAST program at Razorpay’s scale](https://engineering.razorpay.com/building-a-sast-program-at-razorpays-scale-719887fe0aec)
- [How to introduce Semgrep to your organization](https://blog.trailofbits.com/2024/01/12/how-to-introduce-semgrep-to-your-organization)
