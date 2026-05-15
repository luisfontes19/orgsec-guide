# Risk Matrix

The [Checklist](./checklist.md) presents security controls grouped by **domain** (Product Security, Endpoint Security, DevSecOps, etc.). That view is useful for building teams, ownership, and roadmaps — but it does not answer the question every executive eventually asks: *"What are we actually defending against, and which controls reduce that specific risk?"*

This page provides that second lens: a **risk-based view** of the same controls.

## How to read this matrix

- **Risk** — A high-level adverse outcome the organization wants to avoid (e.g. *Supply Chain Attack*, *Account Takeover*). Risks are business-impact oriented.
- **Threat** — A concrete way the risk can materialize (e.g. *malicious dependency*, *phishing*). One risk usually has several threats. Threats are attacker- or scenario-oriented.
- **Controls** — The mitigations from the checklist that reduce the likelihood or impact of that threat. The same control may appear under several threats — defense in depth is intentional.

Controls are **not ranked** within a threat. Picking which ones to invest in first depends on your organization's maturity, industry, and existing posture (see [Using This Guide](../01-using-this-guide.md)).

> This matrix is intentionally non-exhaustive. It covers the most common risks faced by modern organizations and maps them to the controls described in this guide. Adapt it — add risks specific to your industry (PCI, HIPAA, critical infrastructure, etc.), remove what does not apply.

---

## Risk Summary

| # | Risk | Threats covered |
|---|------|-----------------|
| 1 | [Supply Chain Attack](#1-supply-chain-attack) | Malicious dependency · Compromised vendor · Compromised container image · Compromised build pipeline |
| 2 | [Account Takeover & Credential Compromise](#2-account-takeover--credential-compromise) | Phishing · Credential stuffing & brute force · Leaked secrets & credentials · Session hijacking |
| 3 | [Application Vulnerability Exploitation](#3-application-vulnerability-exploitation) | Code-level vulnerabilities · Vulnerable dependencies · Zero-day & unknown vulnerabilities · Insecure defaults |
| 4 | [Data Breach & Data Leakage](#4-data-breach--data-leakage) | Unauthorized data access · Endpoint exfiltration · Misconfiguration exposure · Shadow IT/AI exposure |
| 5 | [Infrastructure & Cloud Compromise](#5-infrastructure--cloud-compromise) | Cloud misconfiguration · Public-facing service attacks · Lateral movement |
| 6 | [Endpoint Compromise](#6-endpoint-compromise) | Malware & ransomware · Lost or stolen device · Unmanaged software |
| 7 | [Insider Threat](#7-insider-threat) | Malicious insider · Negligent insider |
| 8 | [SCM, CI/CD & Developer Environment Compromise](#8-scm-cicd--developer-environment-compromise) | Compromised source code platform · Malicious pipeline changes · Compromised developer workstation |
| 9 | [AI Based Attacks](#9-ai-based-attacks) | Shadow AI usage · Compromised or misbehaving AI agents |
| 10 | [Brand & Reputation Attack](#10-brand--reputation-attack) | Brand impersonation · Uncontrolled vulnerability disclosure |
| 11 | [Operational Disruption](#11-operational-disruption) | Ransomware impact · System outage · Poor incident handling |
| 12 | [Compliance & Regulatory Failure](#12-compliance--regulatory-failure) | Regulatory non-compliance · Audit failure |

---

## 1. Supply Chain Attack

Modern software is assembled, not written. The vast majority of code running in production comes from third parties — open-source libraries, container base images, SaaS vendors, build tools. A compromise anywhere upstream of you propagates into your systems. Supply chain attacks are particularly dangerous because they bypass perimeter controls: the malicious code arrives through a trusted channel.

### Threat: Malicious or compromised library / dependency

An attacker publishes a malicious package, takes over an abandoned package, or compromises a maintainer account. Your build pulls it in and executes it.

Controls:

- [SCA Scans](./devsecops/sca-scans.md)
- [SBOMs](./devsecops/sboms.md)
- [Supply Chain Management](./product-security/supply-chain.md)
- [Secure Development Environment](./product-security/secure-development-environment.md)
- [Vulnerability Management Program](./product-security/vulnerability-management-program.md)

### Threat: Compromised third-party vendor

A SaaS provider or critical vendor is breached and the blast radius reaches your data, your customers, or your infrastructure.

Controls:

- [Vendor Onboarding](./grc/vendor-onboarding.md)
- [Security Questionnaires](./grc/security-questionnaires.md)
- [Supply Chain Management](./product-security/supply-chain.md)
- [Systems Criticality](./grc/systems-criticality.md)

### Threat: Compromised container base image

Public registries host images that may contain vulnerabilities, backdoors, or outdated components. Pulling them directly into production extends your trust boundary.

Controls:

- [Container Scanning](./devsecops/container-scanning.md)
- [Hardened Containers](./infra/hardened-containers.md)
- [SBOMs](./devsecops/sboms.md)

### Threat: Compromised build pipeline

The build itself is part of the supply chain. Tampered build tools, plugins or runners can inject code that never appears in your source repository.

Controls:

- [Secure Deployments](./devsecops/secure-deployments.md)
- [Secure the SCM Platform](./devsecops/secure-the-scm-platform.md)
- [SBOMs](./devsecops/sboms.md)

---

## 2. Account Takeover & Credential Compromise

Identity is the new perimeter. Most modern breaches do not start with an exploit — they start with valid credentials used by the wrong person. Once an attacker has a working identity, every downstream control has to assume that identity is legitimate.

### Threat: Phishing

The most common entry vector. An attacker tricks an employee into entering credentials on a fake page or approving an MFA prompt.

Controls:

- [Phishing Prevention](./endpoint-security/phishing-prevention.md)
- [MFA](./identity-access-management/mfa.md)
- [SSO](./identity-access-management/sso.md)
- [Security Training](./grc/security-training.md)
- [Brand Protection](./opsec/brand-protection.md)

### Threat: Credential stuffing & brute force

Attackers replay credentials leaked from other breaches, or systematically guess weak passwords against your login surfaces.

Controls:

- [MFA](./identity-access-management/mfa.md)
- [Password Manager](./identity-access-management/password-manager.md)
- [SSO](./identity-access-management/sso.md)
- [WAF, DDoS & Bot Protection](./infra/waf.md)

### Threat: Leaked secrets and credentials

API keys, tokens, or service credentials end up in source code, logs, screenshots, or public repositories.

Controls:

- [Secrets Management](./product-security/secrets-management.md)
- [Secret Scans](./devsecops/secrets-scans.md)
- [Password Manager](./identity-access-management/password-manager.md)
- [Secure the SCM Platform](./devsecops/secure-the-scm-platform.md)

### Threat: Session hijacking and token theft

A valid session token is stolen from a workstation, browser, or intercepted in transit, allowing the attacker to bypass authentication entirely.

Controls:

- [EDR](./endpoint-security/endpoint-detection-response.md)
- [MDM](./endpoint-security/mdm.md)
- [SIEM & Threat Detection and Response](./soc/tdr.md)
- [Access Management](./identity-access-management/access-management.md)

---

## 3. Application Vulnerability Exploitation

Code your team writes is the most direct attack surface you have. Even mature programs ship vulnerable code — the goal is to detect it early, reduce how much of it reaches production, and shrink the time to fix what slips through.

### Threat: Code-level vulnerabilities (injection, XSS, auth flaws, business logic)

Bugs in the application itself that allow attackers to bypass intended behavior — read other users' data, escalate privileges, run code.

Controls:

- [SAST Scans](./devsecops/sast-scans.md)
- [DAST Scans](./devsecops/dast-scans.md)
- [Secure Coding Training](./product-security/secure-coding-training.md)
- [Code Review Process](./product-security/code-review-process.md)
- [Threat Modeling](./product-security/threat-modeling.md)
- [Pentests](./product-security/pentests.md)
- [Vulnerability Management Program](./product-security/vulnerability-management-program.md)
- [Security Champions](./product-security/security-champions.md)

### Threat: Vulnerable third-party dependencies

A known CVE exists in a library you depend on and an exploit is published before you patch.

Controls:

- [SCA Scans](./devsecops/sca-scans.md)
- [SBOMs](./devsecops/sboms.md)
- [Vulnerability Management Program](./product-security/vulnerability-management-program.md)

### Threat: Zero-day and unknown vulnerabilities

A vulnerability exists in your code or stack that no scanner knows about yet. You will not find it with automated tooling alone.

Controls:

- [Responsible Vulnerability Disclosure](./product-security/responsible-vulnerability-disclosure.md)
- [Pentests](./product-security/pentests.md)
- [Red Teaming Exercises](./opsec/red-teaming.md)
- [Threat Modeling](./product-security/threat-modeling.md)
- [Invariants Monitoring](./opsec/invariants.md)

### Threat: Insecure defaults

A feature ships configured in a way that is convenient but unsafe — public buckets, permissive CORS, debug endpoints enabled.

Controls:

- [Secure Defaults](./product-security/secure-defaults.md)
- [Secure Guardrails](./infra/secure-guardrails.md)
- [Threat Modeling](./product-security/threat-modeling.md)

---

## 4. Data Breach & Data Leakage

Data is what most attackers actually want and what regulators care about most. Leakage doesn't require a sophisticated attacker — a misconfigured bucket, a wrong sharing setting, or an employee using an unsanctioned tool is enough.

### Threat: Unauthorized data access

A user or service accesses data they should not be able to see, either due to broken authorization, over-permissioned accounts, or stolen credentials.

Controls:

- [Access Management](./identity-access-management/access-management.md)
- [MFA](./identity-access-management/mfa.md)
- [SSO](./identity-access-management/sso.md)
- [SIEM & Threat Detection and Response](./soc/tdr.md)
- [Invariants Monitoring](./opsec/invariants.md)

### Threat: Exfiltration through the endpoint

Data leaves the company through a corporate laptop — copied to USB, uploaded to personal cloud storage, shared in a chat tool, or emailed externally.

Controls:

- [MDM](./endpoint-security/mdm.md)
- [EDR](./endpoint-security/endpoint-detection-response.md)
- [Shadow Apps](./endpoint-security/shadow-apps.md)

### Threat: Misconfiguration exposure

Cloud resource is unintentionally exposed to the internet — open S3 bucket, public database, permissive IAM policy.

Controls:

- [Secure Resource Provisioning](./infra/secure-resource-provisioning.md)
- [Secure Guardrails](./infra/secure-guardrails.md)
- [Infrastructure Scanning & Monitoring](./infra/infrastructure-scanning.md)
- [Secure Defaults](./product-security/secure-defaults.md)

### Threat: Shadow IT / Shadow AI exposure

Employees paste sensitive data into unsanctioned SaaS apps or AI tools, where it ends up in third-party logs or training data.

Controls:

- [Shadow Apps](./endpoint-security/shadow-apps.md)
- [Shadow AI](./ai/shadow-ai.md)
- [Security Training](./grc/security-training.md)
- [Policies](./grc/policies.md)

---

## 5. Infrastructure & Cloud Compromise

Cloud accounts are the new datacenter — and they have a much larger and more dynamic configuration surface. A single mis-scoped IAM role can be the difference between a contained incident and a full takeover.

### Threat: Cloud misconfiguration

Resources are provisioned in an insecure way — overly broad IAM, missing encryption, no network restrictions.

Controls:

- [Secure Resource Provisioning](./infra/secure-resource-provisioning.md)
- [Secure Guardrails](./infra/secure-guardrails.md)
- [Infrastructure Scanning & Monitoring](./infra/infrastructure-scanning.md)

### Threat: Attacks on public-facing services

DDoS, bot traffic, scraping, application-layer abuse against internet-facing endpoints.

Controls:

- [WAF, DDoS & Bot Protection](./infra/waf.md)
- [Infrastructure Scanning & Monitoring](./infra/infrastructure-scanning.md)
- [SIEM & Threat Detection and Response](./soc/tdr.md)

### Threat: Lateral movement after initial foothold

An attacker who lands on one host or one account pivots through the environment to reach high-value systems.

Controls:

- [Access Management](./identity-access-management/access-management.md)
- [Hardened Containers](./infra/hardened-containers.md)
- [EDR](./endpoint-security/endpoint-detection-response.md)
- [SIEM & Threat Detection and Response](./soc/tdr.md)
- [Invariants Monitoring](./opsec/invariants.md)

---

## 6. Endpoint Compromise

Employee laptops and phones are the front line. They run untrusted content (websites, attachments, third-party apps) and they hold credentials, source code, and customer data. A compromised endpoint is often the first step in a larger intrusion.

### Threat: Malware & ransomware

A device is infected via a malicious download, attachment, or drive-by; the attacker gains persistence and access to whatever the user can reach.

Controls:

- [EDR](./endpoint-security/endpoint-detection-response.md)
- [MDM](./endpoint-security/mdm.md)
- [Security Training](./grc/security-training.md)
- [Phishing Prevention](./endpoint-security/phishing-prevention.md)

### Threat: Lost or stolen device

A laptop or phone is lost, stolen, or sold without being properly wiped — exposing whatever data and credentials were on it.

Controls:

- [MDM](./endpoint-security/mdm.md)
- [Access Management](./identity-access-management/access-management.md)
- [Password Manager](./identity-access-management/password-manager.md)

### Threat: Unmanaged or unsanctioned software on endpoints

Employees install software the security team has not vetted — risky browser extensions, pirated tools, AI assistants with broad permissions.

Controls:

- [Shadow Apps](./endpoint-security/shadow-apps.md)
- [Shadow AI](./ai/shadow-ai.md)
- [MDM](./endpoint-security/mdm.md)
- [Policies](./grc/policies.md)

---

## 7. Insider Threat

Not every attacker is external. Insiders already have credentials, context, and trust — which makes them simultaneously the hardest threat to detect and the easiest to overlook.

### Threat: Malicious insider

A current or former employee deliberately abuses their access to steal data, sabotage systems, or sell credentials.

Controls:

- [Access Management](./identity-access-management/access-management.md)
- [SSO](./identity-access-management/sso.md)
- [SIEM & Threat Detection and Response](./soc/tdr.md)
- [Invariants Monitoring](./opsec/invariants.md)
- [Asset Inventory](./grc/asset-inventory.md)

### Threat: Negligent insider

An employee causes a security incident through carelessness, not malice — clicking a phishing link, mishandling data, misconfiguring a resource.

Controls:

- [Security Training](./grc/security-training.md)
- [Secure Coding Training](./product-security/secure-coding-training.md)
- [Secure Defaults](./product-security/secure-defaults.md)
- [Secure Guardrails](./infra/secure-guardrails.md)
- [MDM](./endpoint-security/mdm.md)

---

## 8. SCM, CI/CD & Developer Environment Compromise

The path from a developer's keyboard to production is itself a high-value target. Compromise anywhere along it — IDE, repo, build, deploy — and the attacker reaches production without ever touching production.

### Threat: Compromised source code management platform

GitHub / GitLab / similar is compromised through stolen tokens, OAuth app abuse, or a malicious member with elevated rights.

Controls:

- [Secure the SCM Platform](./devsecops/secure-the-scm-platform.md)
- [MFA](./identity-access-management/mfa.md)
- [SSO](./identity-access-management/sso.md)
- [Access Management](./identity-access-management/access-management.md)

### Threat: Malicious pipeline changes

A pull request, a workflow file, or a self-hosted runner is used to inject malicious behavior into builds and deployments.

Controls:

- [Secure Deployments](./devsecops/secure-deployments.md)
- [Code Review Process](./product-security/code-review-process.md)
- [Secret Scans](./devsecops/secrets-scans.md)
- [Secure the SCM Platform](./devsecops/secure-the-scm-platform.md)

### Threat: Compromised developer workstation

A developer's machine is compromised — giving the attacker access to source code, signing keys, cloud credentials, and the ability to push code.

Controls:

- [Secure Development Environment](./product-security/secure-development-environment.md)
- [EDR](./endpoint-security/endpoint-detection-response.md)
- [MDM](./endpoint-security/mdm.md)
- [Secrets Management](./product-security/secrets-management.md)

---

## 9. AI Based Attacks

AI introduces a new class of risk that does not map cleanly onto existing controls. Models reason over untrusted input, agents take actions on behalf of users, and sensitive data flows into systems the security team often does not own.

### Threat: Shadow AI usage

Employees use AI tools the organization has not approved — pasting source code, customer data, or strategic plans into systems that may log, retain, or train on it.

Controls:

- [Shadow AI](./ai/shadow-ai.md)
- [Security Training](./grc/security-training.md)
- [Policies](./grc/policies.md)
- [Shadow Apps](./endpoint-security/shadow-apps.md)

### Threat: Compromised or misbehaving AI agents

An autonomous agent is manipulated through prompt injection, given excessive permissions, or behaves unpredictably — taking actions the user did not intend.

Controls:

- [AI Agents](./ai/agents.md)
- [Access Management](./identity-access-management/access-management.md)
- [Invariants Monitoring](./opsec/invariants.md)
- [Threat Modeling](./product-security/threat-modeling.md)

---

## 10. Brand & Reputation Attack

Not every attack targets your infrastructure. Some target your customers, your name, or your stock price — and your security team is still the one expected to respond.

### Threat: Brand impersonation

Phishing domains, fake social media accounts, fraudulent apps, or counterfeit websites trick customers into handing over credentials or money.

Controls:

- [Brand Protection](./opsec/brand-protection.md)
- [Cyber Threat Intelligence](./soc/cti.md)
- [Phishing Prevention](./endpoint-security/phishing-prevention.md)

### Threat: Uncontrolled vulnerability disclosure

A researcher (or attacker) discloses a vulnerability publicly without a coordinated process, putting customers and the company's reputation at risk.

Controls:

- [Responsible Vulnerability Disclosure](./product-security/responsible-vulnerability-disclosure.md)
- [Incident Management](./grc/incident-management.md)
- [Policies](./grc/policies.md)

---

## 11. Operational Disruption

Confidentiality gets the headlines, but availability gets the pager. An outage — caused by an attack or a self-inflicted change — has direct business cost, and how the organization handles it shapes both customer trust and regulatory exposure.

### Threat: Ransomware impact on operations

Beyond data loss, ransomware halts the business: systems are encrypted, customer-facing services go down, and recovery becomes a multi-week project.

Controls:

- [EDR](./endpoint-security/endpoint-detection-response.md)
- [MDM](./endpoint-security/mdm.md)
- [Incident Management](./grc/incident-management.md)
- [Tabletop Exercises & Simulations](./grc/tabletop-simulations.md)

### Threat: System outage

A critical service becomes unavailable due to attack, dependency failure, or operational error.

Controls:

- [Systems Criticality](./grc/systems-criticality.md)
- [SLAs/OLAs Definition](./grc/sla-ola.md)
- [Asset Inventory](./grc/asset-inventory.md)
- [Incident Management](./grc/incident-management.md)

### Threat: Poor incident handling

The incident itself is recoverable, but slow response, miscommunication, or missing runbooks make it dramatically worse.

Controls:

- [Incident Management](./grc/incident-management.md)
- [Tabletop Exercises & Simulations](./grc/tabletop-simulations.md)
- [Security Champions](./product-security/security-champions.md)
- [Policies](./grc/policies.md)

---

## 12. Compliance & Regulatory Failure

Regulatory failure is rarely the result of a single missing control — it is the result of not being able to *show* a control. The risk is as much about evidence and documentation as it is about technology.

### Threat: Regulatory non-compliance

The organization is found in violation of a regulation it is subject to (GDPR, PCI, SOC 2, HIPAA, DORA, etc.).

Controls:

- [Compliance And Certifications](./grc/compliance-certifications.md)
- [Policies](./grc/policies.md)
- [Security Training](./grc/security-training.md)
- [Vendor Onboarding](./grc/vendor-onboarding.md)

### Threat: Audit failure

A scheduled audit fails — not necessarily because controls don't exist, but because evidence cannot be produced.

Controls:

- [Asset Inventory](./grc/asset-inventory.md)
- [Policies](./grc/policies.md)
- [Compliance And Certifications](./grc/compliance-certifications.md)
- [Security Questionnaires](./grc/security-questionnaires.md)
