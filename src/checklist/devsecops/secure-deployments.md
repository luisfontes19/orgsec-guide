# Secure Deployments

[TBD]

## Outcome

- [ ] Infrastructure deployments are reproducible and automated
  - [ ] IaC is used for infrastructure provisioning
  - [ ] State files are stored securely and encrypted
- [ ] Any secret or sensitive data is not hardcoded in deployment scripts or IaC files
- [ ] OIDC or short-lived credentials are used for authentication in deployment pipelines
- [ ] Deployment pipelines have least privilege access to resources they manage
- [ ] Approval processes are in place for deployments to sensitive environments (e.g., production)
- [ ] Deployment pipelines are monitored and logged for auditing purposes

## Metrics

- [ ] [TBD]

## Tools & Resources

- [OpenPolicyAgent](https://www.openpolicyagent.org/) (Free)

## Further Reading

- [FacetController: How we made infrastructure changes at Lyft simple](https://eng.lyft.com/facetcontroller-how-we-made-infrastructure-changes-at-lyft-simple-dab49f5b27c7)
- [CI/CD SECRETS EXTRACTION, TIPS AND TRICKS](https://www.synacktiv.com/en/publications/cicd-secrets-extraction-tips-and-tricks)
- [Poisoned Pipeline Execution Attacks](https://bishopfox.com/blog/poisoned-pipeline-attack-execution-a-look-at-ci-cd-environments)
- [Continuous Deployment at Lyft](https://eng.lyft.com/continuous-deployment-at-lyft-9b457314771a)
- [Monocle: How Chime creates a proactive security & engineering culture (Part 1)](https://medium.com/life-at-chime/monocle-how-chime-creates-a-proactive-security-engineering-culture-part-1-dedd3846127f)
- [Shifting left at enterprise scale: how we manage Cloudflare with Infrastructure as Code](https://blog.cloudflare.com/shift-left-enterprise-scale/)
