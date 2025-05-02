# Threat Detection & Response (TDR)

Threat Detection and Response (TDR) is a critical aspect of any cybersecurity strategy, enabling organizations to quickly identify and respond to threats before they cause significant damage. A key component of TDR is a SIEM (Security Information and Event Management) system, which aggregates and correlates logs from across the organization’s IT environment. SIEM platforms provide centralized visibility, alerting, and forensic capabilities, empowering security teams to monitor, investigate, and respond to incidents effectively.

However, SIEMs can be resource-intensive. They require significant effort to deploy, tune, and maintain—including custom rule development, log source onboarding, and alert management. For organizations with limited internal security resources, this overhead can pose a major challenge.

In such cases, a Managed Detection and Response (MDR) service may be a more practical solution. MDR providers deliver 24/7 threat monitoring and response capabilities, reducing the operational burden on internal teams. Although MDR services often come with reduced visibility and control compared to an in-house SIEM, they offer a high level of expertise and rapid threat response out of the box.

Ultimately, the choice between SIEM and MDR should be based on the organization’s risk profile, available resources, and desired level of control.

## Outcome

- [ ] Playbooks are created to guide incident response for various threat types.
- [ ] A platform is in place to enable threat detection and response.
- [ ] SLAs are defined for detection and response timelines.
- [ ] Alerts from the platform are actively monitored and addressed.
- [ ] Detection rules are continuously tuned to improve alert accuracy and reduce false positives.
- [ ] Regular simulation attacks are conducted to test and improve detection and response processes.
- [ ] Analysts have access to sufficient data and context to investigate alerts efficiently.
- [ ] A formal post-mortem process is followed after each significant incident.

## Metrics

- [ ] Number of detections generated
- [ ] Number of false positives
- [ ] Number of simulated attacks conducted
- [ ] Number of false negatives
- [ ] Mean time to respond to an alert
- [ ] Mean time to resolve an incident
- [ ] SLAs breached

## Tools & Resources

- [OpenBAS](https://filigran.io/) - Adversary Simulations (Free/Paid)
- [Stratus RedTeam](https://github.com/DataDog/stratus-red-team) - Adversary Simulations for the cloud (Free)
- [Grimoire](https://github.com/dataDog/grimoire) - Tool to generate audit trails for common attacks (Free)
- [Threat Hunt Book by Predefender](https://huntbook.predefender.com/) (Free)
- [PurpleLab](https://github.com/Krook9d/PurpleLab?) (Free)
- [Wazuh](https://wazuh.com/) - XDR (Free/Paid)
- [TheHive](https://strangebee.com/) - Incident Response Tool (Free/Paid)
- [RedCanary](https://redcanary.com/) - MDR (Paid)
- [ArticWolf](https://arcticwolf.com/) - MDR (Paid)
- [Panther](https://panther.com/) - SIEM (Paid)
- [REx](https://rulexplorer.io/) - Detection Rule explorer (Free)
- [Elastic's Detection Rules](https://github.com/elastic/detection-rules/tree/main) (Free)

## Further Reading

- [Shorten your detection engineering feedback loops with Grimoire](https://securitylabs.datadoghq.com/articles/announcing-grimoire/)
- [Automatic Response: the Iron Dome!](https://www.linkedin.com/pulse/automatic-response-iron-dome-jorge-o-higgins-sfakf)
- [Delegate Security Remediation to Employees to employees](https://mayakaczorowski.com/blogs/slacksecops)
