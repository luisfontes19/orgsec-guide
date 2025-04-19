# Multi Factor Authentication

Multi-Factor Authentication (MFA) is a security method that requires users to verify their identity using two or more factors before accessing a system. These factors can include something the user knows (like a password), something they have (such as a hardware token), or something they are (like a fingerprint).

MFA is essential for organizations as it provides an extra layer of defense against password-based attacks, such as phishing, brute force, or credential stuffing. Even if an attacker obtains a user’s password, they would still need the additional factor to gain access, significantly reducing the risk of unauthorized access.

Hardware tokens, like YubiKeys, offer one of the most secure forms of two-factor authentication (2FA). They are phishing-resistant because they use cryptographic methods to verify authentication requests, ensuring that credentials can only be sent to legitimate websites or services. This makes them a reliable choice for organizations seeking to strengthen their authentication processes and protect sensitive data from advanced threats.

## Outcome

- [ ] Enforce Multi-Factor Authentication (MFA) for business accounts, prioritizing the use of hardware tokens such as [Yubikeys](https://www.yubico.com/).
- [ ] Develop and document a robust process for MFA resets. Ensure it is manual and includes identity verification for employees.

## Metrics

- [ ] Percentage of users with MFA enabled
- [ ] Number of Logins/MFA requests failed

## Tools & Resources

- [Authy](https://authy.com/) (Free)
- [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en&co=GENIE.Platform%3DAndroid) (Free)
- [Yubikeys](https://www.yubico.com/) (Paid)
- [RSA Secure Id](https://www.rsa.com/products/securid/) (Paid)

## Further Reading

- [The (hardware) key to making phishing defense seamless with Cloudflare Zero Trust and Yubico](https://blog.cloudflare.com/making-phishing-defense-seamless-cloudflare-yubico/)
