# Web Application Firewall (WAF), Distributed Denial of Service (DDoS) and Bot Protection

Configuring a Web Application Firewall (WAF) demands significant time and effort, yet it's a critical measure for reducing noise and fortifying the security posture of organizational applications.

While basic WAF features address common threats like SQL injection and Denial of Service (DoS) attacks, they often fall short in mitigating automated traffic, particularly from scanners. A strategic approach involves identifying patterns in scanners' behavior to effectively block unwanted traffic while allowing legitimate requests to pass through.

For instance, understanding the structure of backend applications enables the creation of rules tailored to specific patterns. Consider an API endpoint identified by the `/api/`` prefix; implementing a rule to block requests lacking this prefix can significantly reduce unwanted requests. Additionally, setting thresholds for blocked requests and implementing temporary IP bans can deter malicious actors.

Web scanners frequently target well-known paths such as `.git`, `.env`, and `.well-known`. If these paths are not utilized by the backend, rules can be established to block requests to these paths or even blacklist the corresponding IPs. The objective is to proactively identify and block common scanner patterns to safeguard the integrity of backend systems.

Furthermore, for APIs requiring authentication, rules can be configured to enforce token inclusion in relevant headers. This ensures that requests without a proper authentication header/cookie is not allowed, minimizing the risk of unwanted requests from scanners and enhancing overall security posture.

## Outcome

- [ ] Implement a WAF in front of web applications
- [ ] The WAF is configured to block known attacks
- [ ] There are rate limiting rules in place
- [ ] Sensitive endpoints (like login) have additional rate limiting protections
- [ ] WebsScrapping is detected and blocked
- [ ] There's a DDoS Protection in place
- [ ] The WAF is capable of detecting and block common attack patterns
- [ ] Rule changes are monitored and audited
- [ ] Captchas are presented to users when bot activity is suspected
- [ ] Security headers are injected by the WAF

## Metrics

- [ ] Number of requests blocked
- [ ] Percentage of traffic served
- [ ] Endpoints/Servers with the most blocked requests
- [ ] Bot verification requests
- [ ] Scans/Attacks detected and blocked

## Tools & Resources

- [CloudFlare](https://www.cloudflare.com/) (Paid)
- [AWS WAF](https://aws.amazon.com/waf/) (Paid)
- [Akamai](https://www.akamai.com/) (Paid)
- [Imperva](https://www.imperva.com/) (Paid)
- [DataDome](https://datadome.co/) (Paid)
- [Awesome Waf](https://github.com/0xInfection/Awesome-WAF) (Free)

## Further Reading

- [When WAFs Go Awry: Common Detection & Evasion Techniques for Web Application Firewalls](https://www.mdsec.co.uk/2024/10/when-wafs-go-awry-common-detection-evasion-techniques-for-web-application-firewalls)
