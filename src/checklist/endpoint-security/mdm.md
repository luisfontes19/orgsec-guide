# Mobile Device Management (MDM)

Mobile Device Management (MDM) solutions enable organizations to manage and secure mobile devices such as smartphones, tablets, and laptops. These solutions provide a centralized platform for deploying applications, enforcing security policies, and monitoring device compliance. However, MDMs often fall short of meeting all the requirements for managing devices comprehensively. Beyond applying configurations and restrictions, it is crucial to empower users to manage their devices and install necessary applications, especially for developers and engineers who require specific tools and libraries for their work.

For instance, many MDM solutions lack native capabilities to block applications on macOS. Tools like [Santa](https://github.com/northpolesec/santa), originally developed by Google, can address this gap by allowing or blocking application and file access. To enhance Santa's functionality, backends such as [Zentral](https://github.com/zentralopensource/zentral) or Airbnb's [Rudolph](https://github.com/airbnb/rudolph) can be used to configure Santa and analyze application usage. This approach helps organizations avoid inadvertently disrupting workflows when enabling lockdown modes.

Ultimately, it is essential to consider the impact of MDM solutions on both users and the organization. Providing mechanisms for users to manage their devices effectively ensures a balance between security and usability.

## Outcome

- [ ] MDM is installed by default in all devices provided to employees
- [ ] The MDM is configured with secure defaults and restrictions according to the organization's needs
  - [ ] Enable disk encryption
  - [ ] Standard applications per role are defined if needed
  - [ ] Enforce updates
  - [ ] Force device lock when inactive
  - [ ] SSH Keys are password protected
  - [ ] Enforce EDR
  - [ ] Disable remote logins
  - [ ] User has no admin permissions
- [ ] There's a defined process to quarantine devices
- [ ] Alerts are monitored and acted upon
- [ ] There's a self serve way for users to gain admin access to the devices so they manage it as needed
- [ ] Applications usage is restricted
- [ ] There's a way for users to install applications for their needs, based on a pre-approved list

## Metrics

- [ ] Number/Percentage of devices under MDM
- [ ] Number of detected occurrences
  - [ ] Percentage of False Positives
- [ ] Number of confirmed occurrences
- [ ] Devices not compliant with defined policies

## Tools & Resources

- [Jamf](https://www.jamf.com/) (Paid)
- [Kandji](https://www.kandji.io/) (Paid)
- [JumpCloud](https://jumpcloud.com/) (Paid)
- [ScaleFusion](https://scalefusion.com/mobile-device-management) (Paid)
- [IMazing Profile Editor](https://imazing.com/profile-editor) - GUI tool to help generating MacOS profiles (Free)
- [Santa](https://github.com/northpolesec/santa) - A tool to allow or block applications and files access for macOS (Free)
- [Munki](https://www.munki.org/munki/) - A tool to manage software installation and updates for macOS (Free)
- [Gorilla](https://github.com/1dustindavis/gorilla) - Similar to Munki, for Windows (Free)
- [Fleet](https://github.com/fleetdm/fleet) MDM (Free)
- [Elevate24](https://github.com/Jigsaw24/Elevate24) - Tool to require temporary admin access for MacOS (Free/Paid)
- [Manage Engine's Endpoint Central](https://www.manageengine.com/products/desktop-central/) (Multi platform MDM) (Paid)
- [Zentral](https://github.com/zentralopensource/zentral) Allows you to control Santa, Munk & osquery(Free/Paid)
- [Rudolph](https://github.com/airbnb/rudolph) A Santa backend (Free)
- [Nudge](https://github.com/macadmins/nudge) - A tool for encouraging the installation of macOS security updates (free)
- [osquery](https://www.osquery.io/) Tool to query OS for interesting data (Free)

## Further Reading

- [Designing for security and usability: Figma's modern endpoint strategy](https://www.figma.com/blog/figmas-modern-endpoint-strategy)
- [We scaled Santa, an open-source binary authorization tool, across all Figmates’ laptops to boost endpoint security while keeping workflows seamless. Here’s how we tackled the challenges and ensured a smooth rollout.](https://www.figma.com/blog/rolling-out-santa-without-freezing-productivity)
