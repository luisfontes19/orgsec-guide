# Shadow AI

Shadow AI represents one of the most pervasive and underestimated security risks facing modern organizations. Employees routinely adopt AI tools and services without IT approval or security review, driven by the immediate productivity benefits these systems offer. From ChatGPT and Claude for content creation to specialized AI coding assistants, design tools, and workflow automation platforms, workers are integrating AI into their daily tasks without considering the security implications. This organic adoption creates a sprawling ecosystem of unsanctioned AI integrations that operate outside organizational visibility and control.

The security risks are multifaceted and severe. When employees use external AI services, they often upload sensitive company data, proprietary code, confidential documents, and customer information to systems that may store, process, or train on this data without adequate protections. Many AI platforms retain conversation history, create persistent accounts linked to corporate email addresses, and lack enterprise-grade security controls. Even more concerning, some AI services explicitly state in their terms that user inputs may be used for model training, essentially turning confidential business information into publicly accessible knowledge.

The challenge extends beyond data leakage to operational security risks. Employees may use AI tools to generate code that contains vulnerabilities, create documents with embedded security flaws, or automate processes that bypass established security controls. Without proper oversight, these AI-generated outputs can introduce risks into production systems, compliance workflows, and customer interactions. Additionally, many shadow AI tools require broad permissions, persistent authentication tokens, or integration with existing business systems, creating potential backdoors and privilege escalation paths for attackers.

Organizations must establish comprehensive shadow AI discovery and governance programs to regain visibility and control. This requires proactive identification of unauthorized AI usage combined with pragmatic policies that balance security with productivity needs.

## Outcome

- [ ] Identify Shadow AI Apps
  - [ ] Cross-reference user web browsing and network traffic analysis with known AI tool domains and services
  - [ ] Cross-check installed applications on user laptops and workstations against known AI tools and services
  - [ ] Cross-reference authorized applications in SSO systems with comprehensive lists of AI platforms and integrations
  - [ ] Conduct user surveys and self-reporting initiatives to identify AI tool usage patterns across the organization
- [ ] Process to Review New AI Tools
  - [ ] Establish a formal AI tool evaluation process that assesses security posture, data handling practices, and compliance requirements
  - [ ] Understand the business impact and use cases for each requested AI tool to determine if organizational benefits justify security risks
  - [ ] Provide secure defaults and configuration guidelines for approved AI tools, including data handling restrictions and access controls
- [ ] Shadow AI Governance
  - [ ] Create an AI tool registry that catalogs all authorized and discovered unauthorized AI services within the organization
  - [ ] Implement technical controls that can detect, alert on, or restrict access to high-risk AI platforms
  - [ ] Establish clear policies regarding acceptable AI use, data classification restrictions, and approval processes for new tools
  - [ ] Provide alternative sanctioned AI tools that meet business needs while maintaining security standards and organizational control
  - [ ] Identify Agentic tools that can work with [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) servers and review possible MCP servers usage

## Metrics

- [ ] Number of unauthorized AI tools discovered across the organization
- [ ] Percentage of employees using unauthorized AI services based on surveys and technical detection
- [ ] Number of AI tools formally reviewed and approved through the evaluation process
- [ ] Time to detect and remediate unauthorized AI integrations
- [ ] Employee satisfaction with sanctioned AI alternatives compared to shadow tools

## Tools & Resources

## Further Reading

- [Prompt Engineering Guide](https://www.promptingguide.ai/) (Free)
