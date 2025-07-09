# Secrets Management

Applications usually require multiple secrets to work, either API tokens, password, private keys or others. Saving these secrets in the code or config files means that anybody with access to the code can see and steal them as well as when the application is compromised. On top of that it makes rotating the secrets more complicated as it requires a release update of the application.

For some time secrets have been recommended to be stored in environment variables which raise other issues, like ending having these secrets exposed in docker files, or object definitions in cloud providers.

The safer way to manage secrets is by implementing a secret management platform with restricted RBAC controls.

## Outcome

- [ ] Secrets are obtained from a Secrets Management platform, and loaded directly into memory
- [ ] No secrets hardcoded in applications
- [ ] No secrets in config files
- [ ] No secrets in environment variables
- [ ] Access to secrets is controlled with restricted ACL's and monitored
- [ ] If developers need programmatic access SaaS services provide a safe interface to avoid sharing secrets.

## Metrics

- [ ] Number of secrets stored in the Secrets Management platform
- [ ] Top projects with more secrets stored
- [ ] Top secrets with more permissions granted
- [ ] Number of unauthorized access to secrets

## Tools & Resources

- [Infisical](https://github.com/Infisical/infisical) - Secrets Manager Tool (Free)
- [HCP Vault](https://www.hashicorp.com/products/vault) - Secrets Manager Tool (Paid)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) - Secrets Manager Tool (Paid)
- [How to Rotate](https://howtorotate.com/) - Guides on how to rotate secrets in common services (Free)

## Further Reading

- [What is a Secrets Manager?](https://www.doppler.com/blog/what-is-a-secrets-manager)
- [Environment Variables Don’t Keep Secrets](https://developer.cyberark.com/blog/environment-variables-dont-keep-secrets-best-practices-for-plugging-application-credential-leaks/)
- [5 best practices for secrets management](https://www.hashicorp.com/resources/5-best-practices-for-secrets-management)
- [Building Uber’s Multi-Cloud Secrets Management Platform to Enhance Security](https://www.uber.com/en-AU/blog/building-ubers-multi-cloud-secrets-management-platform/)
