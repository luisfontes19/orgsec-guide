# AI Governance

Employees adopt AI tools without approval, uploading sensitive data to unmanaged systems. Without governance, organizations have no visibility into what AI is processing, no ability to respond to incidents, and no way to enforce data classification boundaries.

Beyond data leakage, AI introduces attack surfaces that traditional controls don't cover: prompt injection can cause AI agents to exfiltrate data or take unintended actions; malicious or compromised MCP servers can grant AI tools unauthorized access to internal systems; and AI-generated code or content can introduce vulnerabilities that bypass standard review processes.

Organizations need visibility, control, and a clear approval process before AI tools access company data or infrastructure.

## Outcome

- [ ] identify unauthorized AI tools in use
- [ ] Maintain a catalog of sanctioned tools with secure defaults and data-handling guidelines
- [ ] Capture enough telemetry to support incident response, including prompts, reponses, tool calls, etc
- [ ] Ability to detect and block malicious or unintended intent like prompt injection, sensitive command execution, malicious skills or MCPs, etc
- [ ] Ability to restrict AI usage per policy
- [ ] A defined intake for evaluating new requests

## Metrics

- [ ] Number of unauthorized AI tools discovered
- [ ] Number of AI tools formally reviewed and approved
- [ ] Coverage of AI traffic in proxy/DNS logging
- [ ] Time to detect unauthorized AI integrations

## Tools & Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/) (Free)
- [agentic-radar](https://github.com/splx-ai/agentic-radar/) - A security scanner for your LLM agentic workflows(Free)
- [Microsoft's agent-governance-toolking](https://github.com/microsoft/agent-governance-toolkit) (Free)
- [Meta's Llama Firewall](https://meta-llama.github.io/PurpleLlama/LlamaFirewall/) - The framework to detect and mitigate AI centric security risks (Free)
- [Promptfoo](https://www.promptfoo.dev/) (Free/Paid)
- [Geordie](https://www.geordie.ai/) (Paid)

## Further Reading

- [Prompt Engineering Guide](https://www.promptingguide.ai/) (Free)
