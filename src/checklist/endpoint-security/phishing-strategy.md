# Phishing Strategy

One of the most common ways organizations are compromised today is through social engineering, where attackers exploit human behavior rather than technical vulnerabilities. A prevalent form of this is phishing, where users are tricked into clicking malicious links or downloading harmful attachments, often disguised as legitimate communications.

To defend against such attacks, it’s critical to create and maintain effective phishing filter rules. These rules must be continuously updated and fine-tuned to address evolving threats. The nature of an organization’s business significantly influences how these filters should be configured. For example, a cryptocurrency company might frequently receive legitimate emails containing bitcoin addresses or references to BTC, which could otherwise trigger false positives. On the other hand, the same content might be considered suspicious in a company that develops authentication systems.

Artificial Intelligence (AI) can significantly enhance phishing detection capabilities. AI-based tools can analyze email content, sender behavior, and contextual signals to identify subtle signs of phishing attempts that traditional rule-based systems may overlook.

A growing tactic used by attackers is the inclusion of QR codes in phishing emails. These codes often embed malicious URLs in a way that bypasses conventional security filters. Organizations should incorporate detection measures for such techniques as part of their broader phishing defense strategy.

Running phishing simulations is an effective way to assess both the effectiveness of email filters and employee awareness. These exercises help identify potential weaknesses and serve as training opportunities. However, it's important to maintain a balance—conducting simulations too frequently or harshly can lead to employee fatigue, frustration, or fear.

When users fail a phishing simulation, the response should be educational, not punitive. Providing constructive feedback, guidance, and supportive training helps reinforce secure behavior and fosters a culture of continuous learning. This approach not only improves individual awareness but also strengthens the organization’s overall security posture without damaging morale.

## Outcome

- [ ] Create rules to filter phishing based on the organization's needs and business model
- [ ] Implement a flow for users to report suspicious or phishing emails
- [ ] Have a layer of automation trying to triage and filter the reports
- [ ] Run phishing simulations to test the effectiveness of the filters and the users' awareness
- [ ] Scan attachments and links in emails for potential phishing attempts
  - [ ] Automatically flag suspicious attachment extensions (e.g., `.exe`, `.bat`, `.vbs`)

## Metrics

- [ ] Number of phishing emails triaged/confirmed automatically
- [ ] Number of phishing emails that bypassed the filters
- [ ] Number of phishing emails that were not detected by the filters but were reported by users
- [ ] Number of phishing emails that got users engaging with them
- [ ] Number of emails wrongly flagged as phishing
- [ ] Number of emails flagged by users as phishing that were not phishing
- [ ] Number of phishing simulationsa and how many users clicked on them

## Tools & Resources

- [Jigsaw | Phishing Quiz](https://phishingquiz.withgoogle.com/) (Free)
- [Sublime Security](https://sublime.security/) (Free/Paid)
- [GoPhish](https://getgophish.com/) (Free)
- [Hoxhunt](https://www.hoxhunt.com/phishing-training) (Paid)

## Further Reading

- [Automatic Response: the Iron Dome!](https://www.linkedin.com/pulse/automatic-response-iron-dome-jorge-o-higgins-sfakf)
