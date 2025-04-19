# Threat Modeling

The primary goal of threat modeling is to proactively identify potential threats to a system before they can be exploited. These threats may stem from a variety of sources, including the system’s architecture, for example race conditions in asynchronous microservice calls, or dependencies on third-party services that could be compromised and leveraged in an attack.

To structure and deepen the analysis, combining methodologies such as the [STRIDE model](https://en.wikipedia.org/wiki/STRIDE_model) and [Attack Trees](https://en.wikipedia.org/wiki/Attack_tree) can be highly effective. Together, these tools help break down complex systems into manageable components, guiding participants through a structured and comprehensive thought process during threat modeling sessions.

A key element of successful threat modeling is the involvement of developers and other relevant system stakeholders. These individuals possess deep knowledge of how systems are built and operate, making them essential contributors to identifying realistic threat scenarios. As organizations mature, the goal should be for development teams to take ownership of the threat modeling process. Achieving this level of maturity, however, requires consistent support, training, and well-defined processes led by the security team.

Creating the right environment is just as important as applying the right methodologies. People are more likely to contribute meaningful insights when they feel safe to speak openly. That’s why it’s essential to foster a relaxed, blame-free atmosphere where all participants understand that their input is valued and that there are no wrong answers. When contributors feel supported rather than scrutinized, they’re more likely to surface known issues or flag concerns that might otherwise go unspoken.

Once these discussions take place, it’s the responsibility of the security team to document the insights, validate the risks, and guide the implementation of mitigations or safety measures. By tapping into the collective knowledge of those who design, build, and maintain the system—and doing so in an inclusive and collaborative way—threat modeling becomes not only more accurate but also more impactful.

## Outcome

- [ ] Theres a documented process of how to do threat modeling
- [ ] Threat models are integrated into the SDLC and done on a regular basis
- [ ] Discovered threats are reported into the [vulnerability management program](./vulnerability-management-program.md)

## Metrics

- [ ] Number of threat models done
- [ ] Percentage of projects covered with Threat Model
- [ ] Number of threats per project
- [ ] Average reported threats for projects
- [ ] Total reported threats
- [ ] Percentage of open/closed threats
- [ ] Average mean time to resolution
- [ ] Average mean time to resolution per project

## Tools & Resources

- [AWS Threat Composer](https://awslabs.github.io/threat-composer) (Free)
- [ThreatDragon](https://www.threatdragon.com/) (Free)
- [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool) (Free)
- [Gram](https://github.com/klarna-incubator/gram/) (Free)
- [ThreatGPT](https://github.com/mrwadams/stride-gpt) (Free)
- [Miro](https://miro.com/) (Free/Paid)

## Further Reading

- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/)
- [OWASP's Software Assurance Maturity Model](https://owaspsamm.org/model/design/threat-assessment/)
- [Threat Modeling of Threat Modeling](https://threat-modeling.net/threat-modeling-of-threat-modeling/)
- [Maturing Your Threat Modeling Skills](https://www.youtube.com/watch?v=2zxYPwpPVis)
- [How to Approach Threat Modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
- [OWASP's Threat Modeling Playbook](https://github.com/OWASP/threat-modeling-playbook)
