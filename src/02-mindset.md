# The Security Team Mindset

Lets review how should be the right mindset of a security team so it can thrive and be a core and strong pillar of the organization.

## Security is an Enabling Teams

An enabling security team focuses on finding ways to allow business operations to proceed safely and efficiently, rather than simply blocking actions due to security concerns. This approach recognizes that the ultimate goal of security is not to stop progress but to manage and mitigate risks in a way that supports organizational goals.

A blocking security team often prioritizes absolute safety over flexibility, which can prevent business innovation, delay projects, and frustrate teams. While security is critical, a rigid, “no-by-default” approach can lead to inefficiencies and wasted resources as teams are forced to circumvent obstacles or abandon initiatives altogether.

An enabled security team, on the other hand, works collaboratively with the organization to strike a balance between security and business needs. Instead of denying requests outright, they assess risks and propose controlled, safer alternatives. For example, rather than rejecting a cloud migration due to concerns about sensitive data, an enabled team might recommend encryption, access controls, and monitoring to reduce the risk to an acceptable level. This not only keeps the business moving but also ensures risks are managed intelligently.

Ultimately, security is about reducing and managing risk, not eliminating it entirely, which is neither realistic nor cost-effective. Organizations must decide whether to accept the reduced risk associated with an enabled approach or face the potential of wasting time and resources on initiatives that are blocked entirely.

## Guardrails are better than Gates

To be true enablers of the business, a security team must provide guardrails: clear boundaries and tools that allow teams to work effectively without constantly worrying about security. These guardrails are designed to enable business operations to proceed securely while preventing hazardous or high-risk activities from occurring.

Guardrails are not about restricting innovation or controlling every aspect of work but about creating a safe zone where teams can operate freely and focus on their objectives. For example, security teams might define automated policies for cloud configurations, enforce secure coding practices, or deploy tools that ensure sensitive data is protected without requiring constant intervention. By proactively providing these boundaries and frameworks, the security team eliminates the need for employees to navigate complex security concerns on their own.

This approach ensures that employees can perform their tasks securely without inadvertently creating vulnerabilities or exposing the organization to unnecessary risks. At the same time, it prevents dangerous operations—such as deploying unapproved software or transferring unencrypted sensitive data by default, reducing the chance of a breach.

By delivering guardrails, security teams foster a collaborative relationship with the business. They empower teams to achieve their goals while maintaining a controlled, secure environment. This proactive and supportive model aligns security with business objectives, ensuring progress is achieved safely and efficiently.

## Demonstrate the value of the security team

One of the persistent challenges for security teams is clearly demonstrating their value to the business. A common, oversimplified answer to the question “What does the security team do?” is often: “We make sure we don’t get hacked.” While technically true, this response falls short when justifying a budget of X or explaining why a team of Y professionals is necessary.

To bridge this gap, security teams need to shift from being a black box to a transparent, data-driven function. They should actively communicate their goals, initiatives, and accomplishments through clear metrics and key performance indicators (KPIs).

By aligning security work with business impact, whether it’s enabling compliance, reducing risk exposure, or protecting revenue-generating systems, teams can make a stronger case for resources and staffing. This approach not only supports investment decisions but also elevates security as a strategic function within the organization, rather than a cost center or insurance policy.

For each initiative described in this guide there's a metrics section that can be used as a baseline to measure the success of the initiative as well as to communicate the value of the security team to the business. These metrics should be tailored to your organization’s specific context and goals, but they can serve as a starting point for demonstrating the impact of security efforts.

## Standardization is Key

Standardizing processes, workflows, and even code within an organization offers significant long-term benefits compared to a "free-for-all" approach, where developers have full independence to choose their preferred methods of working. While giving teams freedom may seem to foster creativity and speed in the short term, it often leads to inconsistencies, inefficiencies, and difficulties in scaling or securing operations as the organization grows.

By adopting a standardized approach, companies can create guardrails and implement effective security controls that are consistent across all teams. These guardrails ensure that everyone operates within a predefined secure framework, reducing the risk of vulnerabilities introduced by varying practices or tools. For example, standardized libraries, frameworks, and infrastructure templates make it easier to identify and fix security gaps while maintaining a high level of efficiency.

Standardization also fosters a consistent approach to problem-solving. When teams follow the same processes and use shared tools, it becomes easier to identify issues, debug problems, and implement solutions across the entire organization. This consistency ensures that improvements—whether they address security, performance, or usability—can be applied uniformly and quickly, avoiding the overhead of modifying multiple, disparate systems or workflows.

In contrast, a "free-for-all" approach often results in fragmentation, where each team or individual uses their own tools, frameworks, and coding practices. This can lead to knowledge silos, increased technical debt, and a patchwork of solutions that are harder to maintain, secure, and scale. It also complicates collaboration between teams and makes onboarding new employees more challenging.

Standardization doesn’t mean stifling innovation, it actually creates a foundation for it to thrive. When processes and tools are standardized, innovations can still emerge organically within teams, but they are easier to evaluate, refine, and adopt organization-wide if they prove beneficial. This ensures that great ideas don’t remain siloed but instead contribute to improving the overall standard for everyone. Additionally, standards aren’t static; they evolve as needs change. It’s up to everyone in the organization to collaborate and decide what the standards look like, ensuring they remain relevant, efficient, and inclusive of new approaches or technologies. This way, innovation is not just possible but becomes a structured and scalable part of how the company operates.

## Provide Good Experience

User experience (UX)—or developer experience (DevX), in the case of engineering teams is critical to the success of a security team. Security initiatives should never be built in isolation; they must be designed with the end user in mind, ensuring they integrate seamlessly into workflows and enhance productivity rather than hinder it.

The starting point for any security initiative should be to understand what “good” looks like for the relevant end users. This means engaging directly with users, whether business users, employees, developers, or business leaders to understand their needs, challenges, and the ways they work. By prioritizing this understanding, security teams can craft solutions that not only meet compliance or risk management goals but also add tangible value to the people using them.

For example, instead of introducing a cumbersome authentication process that frustrates users, a security team might implement single sign-on (SSO) with adaptive MFA, providing both security and ease of use. For developers, providing pre-approved secure templates for infrastructure or code can streamline workflows while embedding security into their processes without additional effort.

When security aligns with user needs, adoption increases, bypasses decreases, and teams work more effectively. A solution designed without user experience in mind might achieve technical security goals but risks being ignored, circumvented, or creating friction that leads to inefficiency. By starting with the user and building backwards, security teams can deliver solutions that are not only secure but also enable business and technical success.

## Building vs Buying

Most security teams lack engineers skilled in software development beyond basic scripting. This leads to increased costs and challenges that are hard to overcome. As a result, teams often purchase multiple tools with low or negative cost/benefit ratio. These tools tend to be limited, forcing teams to adapt their workflows to the tool rather than the other way around. Over time, they fail to scale, creating unnecessary burdens for security teams.

This doesn’t mean teams should avoid buying solutions altogether. However, they should first define the problem, understand their business needs, and assess whether a solution truly fits. Too often, teams buy vulnerability management tools without sufficient control over scanners, leading to excessive false positives and data duplication across multiple systems. Poor integrations with the SDLC further complicate the process, creating inconsistency and extra maintenance work.

A security team capable of software development can bridge gaps between open-source and commercial tools, tailoring solutions to their needs.

Before engaging with vendors, teams should ask:
"What problem are we solving?"
"What are the requirements, or what do we need the tool to do?"
"How should it integrate with our existing tools and processes?"

Only then should they seek a tool that meets these criteria. If no suitable solution exists or is unattainable, developing an in-house tool may be the best approach. At the end the goal is to have an effective process that brings value to the organization with low maintenance costs.

For a deeper dive into this issue, check out the article  [Security is a Pricing Problem](https://securityis.substack.com/p/security-is-a-pricing-problem)" that does a great job explaining this issue.

## Keep Learning

In the ever-evolving landscape of cybersecurity, it is essential for members of a security team to continually update their knowledge and skills. Tools, attack techniques, and vulnerabilities evolve at a breakneck pace, rendering knowledge acquired even a year ago potentially outdated. Staying static in this field is bad, as it risks leaving the organization exposed to emerging threats and missing opportunities to implement cutting-edge defenses.

To stay ahead, security professionals must actively seek out new information and learning opportunities. This includes reading industry news, participating in training sessions, attending webinars, or even listening to podcasts that focus on the latest trends and challenges in cybersecurity. Engaging with the wider security community is equally important — fostering knowledge transfer sessions with peers, joining professional forums, and understanding how other companies address similar challenges can provide fresh perspectives and practical insights.

This constant pursuit of learning not only sharpens technical skills but also broadens strategic understanding, enabling security teams to better anticipate threats and adopt innovative solutions. Encouraging a culture of continuous improvement and knowledge sharing within the team ensures everyone remains current and prepared to adapt to the fast-changing threat landscape, ultimately strengthening the organization’s overall security posture.

## Incremental Rollouts

Incremental rollouts are a smarter approach when introducing new solutions or features. By starting with a small group of users, you can gather valuable feedback and identify potential issues early. This allows for improvements and adjustments to be made before scaling up, ensuring a smoother experience for the broader user base and even the security team.

From a security perspective, this approach prevents the team from being overwhelmed with alerts, complaints, or unexpected challenges immediately after implementation. Addressing issues in smaller, manageable increments helps build confidence in the solution and reduces the overall workload.

Once the initial rollout is refined and proves successful, expanding to other teams or users becomes more straightforward. This step-by-step process creates a replicable success story, avoids unnecessary disruptions, and ensures the solution is well-received across the organization. Compared to rolling out to everyone at once and then scrambling to fix widespread issues, incremental rollouts are more efficient and effective.
