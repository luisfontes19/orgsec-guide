# Secure Defaults

Organizations are increasingly adopting a proactive approach, shifting from reactive measures to prevention strategies. This shift is evident in the [shift left](https://www.sonarsource.com/learn/shift-left/) paradigm. By providing developers with secure defaults, such as project repositories with pre-configured settings or standardized code templates, security principles can be seamlessly integrated into projects without additional effort. This approach not only reduces the risk of vulnerabilities but also ensures that security is ingrained into the project from its inception.

A similar trend is observed in infrastructure management, with the rise of Infrastructure as Code (IaC). By offering secure defaults for provisioning infrastructure, organizations can mitigate the risk of misconfigurations, vulnerabilities, and human errors.

Netflix popularized the term of the Paved Road, which empowers teams with autonomy while equipping them with secure defaults. This approach allows teams to work on their projects independently while saving time by leveraging established security configurations. The ultimate goal of secure defaults is to provide teams with a secure foundation upon which they can innovate and create freely. This balance between security and flexibility fosters a culture of empowerment and encourages innovation within organizations.

## Outcome

- [ ] Repository templates are available for developers to use as secure defaults
- [ ] [Devcontainers](https://containers.dev/) are provided by default in the repository templates
- [ ] Secure container images are provided for deployments and development
- [ ] Infra configurations are done (through code) with secure defaults
- [ ] A security library is included by default in projects for developers to use in their code
- [ ] Monitor for projects not using or bypassing the provided secure options
- [ ] Provide a self service way for developers to request new resources for a project

## Metrics

- [ ] Number of repositories using the secure defaults
- [ ] Number of container images using the secure defaults
- [ ] Number of vulnerabilities found in the secure default templates
- [ ] Percentage of projects using secure defaults

## Tools & Resources

- [Awesome Secure Defaults](https://github.com/tldrsec/awesome-secure-defaults) (Free)
- [OWASP Proactive Controls](https://owasp.org/www-project-proactive-controls/) (Free)

## Further Reading

- [Docker Security Best Practices: A Complete Guide](https://anchore.com/blog/docker-security-best-practices-a-complete-guide/#securing-images-1)
- [The Show Must Go On: Securing Netflix Studios At Scale](https://netflixtechblog.com/the-show-must-go-on-securing-netflix-studios-at-scale-19b801c86479)
- [Business of Secure Defaults](https://tldrsec.com/p/business-of-secure-defaults)
