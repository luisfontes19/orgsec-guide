# Single Sign On

An SSO solution provides an easy way to manage employees' permissions to the organization systems. It serves a single account for the user to manage. This translates into the user only needing to know one password to manage multiple systems.

Although this can be seen as a single point of failure, in case an attacker compromises the SSO account, the advantages overcome the disadvantages. For example, on an account compromised, until understanding how the account was compromised it should be considered that all user's accounts were compromised, and if no SSO is place, an IT administrator would have to go to all systems, disabling the user's accounts. Having a single account can make it easy to act and contain the incident. Also, for the user having a single account is easy to enforce a strong password policy that they can remember and its less probable the use of insecure ways for saving or remembering the password.

## Outcome

- [ ] Have an SSO implemented to manage employee accounts
- [ ] SSO accounts are disabled in the off-boarding process of an employee
- [ ] Tools used by the company are configured to use SSO
- [ ] If the tools allow disable any account usage outside of the organization SSO
- [ ] Have properly documented the tools that do not support SSO, if any, and include them in the off-boarding process
- [ ] SSO sessions expire in a short period of time (20h for example)
- [ ] Groups are created and assigned to users, as a way to control their permissions in a system.
- [ ] Permissions to applications is controlled with SSO groups, and integrated into the [Permission Request](access-management.md) process

## Metrics

- [ ] Percentage of tools configured with SSO

## Tools & Resources

- [Google SSO](https://support.google.com/a/answer/60224?hl=en) (Paid)
- [Auth0](https://auth0.com/features/single-sign-on) (Paid)
- [Okta](https://www.okta.com/customer-identity/single-sign-on/) (Paid)

## Further Reading

- [TBD](http://example.com)
