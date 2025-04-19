# Invariants Monitoring

When developing and configuring systems or tools, it's common to rely on *invariants*, assumptions that are expected to remain consistently true. These are often treated as absolute truths, and as a result, exceptions or deviations may not be adequately considered or handled.

For instance, consider the assumption that "all connections are established over HTTPS". This ensures encrypted and secure communication. But what if, due to a misconfiguration or unforeseen issue, a connection is made using plain HTTP? Without proper monitoring, such an exception might go unnoticed, creating a security gap.

Another example involves access control. Imagine a highly sensitive code repository where access is intentionally restricted to a specific group of users. If additional users are mistakenly granted access because they were added to all repositories this may pose a significant risk and may take time to be detected. The assumption that "only authorized users have access" is violated, and the consequences could be severe.

To address these scenarios, it's essential to **actively monitor invariants**. By setting up alerting mechanisms for deviations from expected behaviors such as non-HTTPS traffic or unexpected permission changes, an organization can quickly detect and respond to issues that violate core security assumptions. This approach enhances resilience by acknowledging that even trusted configurations can fail and that continuous validation is key to maintaining security.

## Outcome

- [ ] Theres a comprehensive list of expected invariants
- [ ] Invariants are monitored for changes
- [ ] There's a process in place to quickly identify and react to the unexpected variations

## Metrics

- [ ] Number of detected variations due to requirements change
- [ ] Number of detected unexpected variations
- [ ] Number of total detected variations

## Tools & Resources

- [TBD](http://example.com) (Free)

## Further Reading

- [Secure by Design at Google](https://research.google/pubs/secure-by-design-at-google/)
