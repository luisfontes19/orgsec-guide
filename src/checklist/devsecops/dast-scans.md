# Dast Scans

DAST is a controversial topic that divides security engineers. On one side, some argue that DAST provides little to no real value due to the overwhelming noise it generates and low confirmed findings, making it not worth the effort. On the other side, many engineers rely on DAST to assess the effectiveness of security controls and uncover real, exploitable vulnerabilities.

One key issue with DAST is that many people still recommend outdated tools, some over a decade old, with little to no maintenance. These tools are unlikely to provide good value. However, even modern DAST solutions require significant fine-tuning and configuration to deliver meaningful results. When properly optimized, though, DAST can be a valuable asset.

A few years ago, DAST was more effective in monolithic applications, where it could easily crawl websites, detect endpoints, and test parameters. With the shift to microservices and single-page applications, DAST has become less effective, as it struggles to identify all relevant endpoints and parameters.

Choosing the right DAST tool is crucial, but just as important is ensuring it has context of the necessary endpoints and parameters for scanning. This can significantly impact its effectiveness. Using standards like [OpenAPI](https://www.openapis.org/what-is-openapi) and tools like [Swagger](https://swagger.io/) simplifies this process since they provide structured information about APIs. If such tools or standards aren’t in place, DAST can still be useful but will require more manual effort to maximize its value.

In web applications, DAST can provide immediate value by identifying low-hanging fruit, such as misconfigured security headers. While these may not be critical vulnerabilities, properly configured headers enhance overall security.

Additionally, script kiddies often report these issues without understanding their context. Addressing them proactively helps reduce unnecessary noise in reports and prevents distractions from more serious security concerns.

## Outcome

- DAST is performed regularly against the applications
- The scanning tools are properly customized to reduce false positives and in case of API's to be able to recognize the endpoints and authenticate
- Findings are being pushed to the [vulnerability management program](../product-security/vulnerability-management-program.md)
- Severity/Priority is recalculated based on the asset's criticality/risk
- The DAST tool is integrated into the SDLC

## Metrics

*Metrics for this topic are included in [Vulnerability Management](../product-security/vulnerability-management-program.md)*

## Tools & Resources

- [Nuclei](https://github.com/projectdiscovery/nuclei) + [Nuclei Dast Templates](https://github.com/projectdiscovery/nuclei-templates/tree/main/dast) (Free)
- [Dasterdly](https://portswigger.net/burp/dastardly)  (Free)
- [ZAP Proxy](https://github.com/zaproxy/zaproxy) (Free)
- [RESTler](https://github.com/microsoft/restler-fuzzer) (Free)
- [Pentest Ground](https://pentest-ground.com/) Lists of vulnerable apps for tests (Free)

## Further Reading

- [What is wrong with the current state of DAST? Feedback from my conversations with AppSec engineers](https://escape.tech/blog/what-is-wrong-with-the-current-state-of-dast-feedback-from-my-conversations-with-appsec-engineers/)
- [Scaling Dynamic Application Security Testing (DAST)](https://msrc.microsoft.com/blog/2025/01/scaling-dynamic-application-security-testing-dast/)
