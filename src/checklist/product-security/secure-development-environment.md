# Secure Development Environment

Modern software development faces an unprecedented array of security threats targeting developers and their environments. The traditional approach of developing directly on workstation machines creates numerous attack vectors that sophisticated threat actors actively exploit.

Supply chain attacks have emerged as one of the most dangerous categories of threats facing developers today. Attackers routinely inject malicious code into popular open-source libraries and packages, knowing that developers will unknowingly integrate these compromised dependencies into their applications. High-profile incidents like the [event-stream](https://es-incident.github.io/paper.html) npm package compromise, and the [colors.js](https://www.revenera.com/blog/software-composition-analysis/the-story-behind-colors-js-and-faker-js/) sabotage demonstrate how a single malicious package can impact thousands of downstream applications. These attacks are particularly insidious because they leverage the trust developers place in package repositories and the automated nature of dependency management tools.

Beyond compromised packages, developers face increasingly sophisticated social engineering attacks. Fake technical interviews have become a common tactic where attackers pose as recruiters from reputable companies, asking candidates to run "coding challenges" or "assessment tools" that are actually malware designed to steal credentials, code, or establish persistence on the victim's development machine. Similarly, malicious IDE extensions and plugins represent another attack vector, as these tools often request broad permissions to access files, network resources, and system functions under the guise of developer productivity features.

Developers often accumulate dozens of tools across their development workflow, each representing a potential entry point for attackers. Git repositories can be compromised to inject malicious commits, development containers can be backdoored, and even legitimate development tools can be weaponized through supply chain compromises of their own dependencies.

A prevention option lies in implementing dedicated, secure development environments that isolate development activities from the host system and other sensitive resources. Technologies like Dev Containers, Docker development environments, and cloud-based development environments provide strong isolation boundaries that can contain potential compromises. These environments can be configured with minimal necessary permissions, regularly rebuilt from trusted base images, and monitored for suspicious activity. By treating development environments as ephemeral and potentially hostile, organizations can significantly reduce the blast radius of successful attacks while maintaining developer productivity and workflow flexibility.

## Outcome

- [ ] Isolated environments are used for development, like [DevContainers](https://containers.dev/)
- [ ] Installed packages are monitored for vulnerabilities and supply chain risks
- [ ] Development tools like IDEs, extensions and AI tools are standardized and vetted for security risks
- [ ] Developers are trained to recognize social engineering attacks targeting development environments
- [ ] SSH keys are protected with hardware security modules (HSMs) or equivalent solutions
- [ ] Secure package manager settings like delayed dependency updates are enforced in all projects
- [ ] [EDR](../endpoint-security/endpoint-detection-response.md) solutions are deployed on developer workstations
- [ ] Ensure production secrets are never stored or used in development environments
- [ ] [Invisible characters](https://www.promptfoo.dev/blog/invisible-unicode-threats/) are detected in source code and dependencies to prevent supply chain attacks

## Metrics

- [ ] [TBD]

## Tools & Resources

- [Aikido Safechain](https://github.com/AikidoSec/safe-chain) - Hooks into NPM/PyPI register calls to analyze and block malicious packages being installed (Free)
- [Wiz's SDLC Infrastructure Threat Framework](https://wiz-sec-public.github.io/SITF/) (Free)

## Further Reading

- [IDEsaster: A Novel Vulnerability Class in AI IDEs](https://maccarita.com/posts/idesaster/)
- [New DPRK Contagious Interview Campaign: “Fake Font” Uses Malicious VSCode Fonts](https://opensourcemalware.com/blog/contagious-code-fake-font)
- [VSCode MDM Policies](https://code.visualstudio.com/docs/enterprise/overview)
- [pnpm's New setting for delayed dependency updates](https://pnpm.io/blog/releases/10.16#new-setting-for-delayed-dependency-updates)
- [Trojan Source - Invisible Source Code Vulnerabilities](https://trojansource.codes/)
- [Proof-of-concept for an 'invisible' JavaScript payload](https://github.com/lambdacasserole/zero-width-js)
