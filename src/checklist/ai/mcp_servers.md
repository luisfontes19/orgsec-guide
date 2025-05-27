# MCP Servers

The [MCP protocol](https://modelcontextprotocol.io/introduction) is a new communication protocol for AI agents that allows them to communicate with each other and with external systems. Unfortunately leveraging this protocol can lead to security issues, such as tool poisoning attacks.

Also MCP servers may introduce sensitive operations, like executing code or accessing sensitive data and with agents wrongly understanding your needs or hallucinating this can have serious consequences.

## Outcome

- [ ] Add an authentication layer if the servers are exposed
- [ ] Identify critical operations and add a confirmation step for them
- [ ] Display info of a tool being invoked
- [ ] Review MCP servers before deploying them

## Metrics

- [ ] [TBD]

## Tools & Resources

- [mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) (Free)
- [damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server) (Free)
- [Prompt Engineering Guide](https://www.promptingguide.ai/) (Free)
- [The Vulnerable MCP Project](https://vineethsai.github.io/vulnerablemcp/) (Free)

## Further Reading

- [Everything Wrong with MCP](https://blog.sshh.io/p/everything-wrong-with-mcp)
- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Securing the Model Context Protocol](https://block.github.io/goose/blog/2025/03/31/securing-mcp)
