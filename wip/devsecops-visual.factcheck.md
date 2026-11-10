# DevSecOps visual draft fact check

Checked: 10 November 2026

This draft uses a single vertical diagram to connect lifecycle phases, governance work and secure development activities. The diagram is described in `devsecops-visual.flow.txt`.

## Scope and verdict

The page is a high-level synthesis of the lifecycle descriptions supplied with the request. The governance risks are supported by public primary sources from NIST and OWASP. The phase descriptions and secure development activities reflect the supplied lifecycle outline. No external policy, regulatory interpretation or product capability is asserted.

## Interpretation by AI

The risk pills describe potential consequences of skipping the activity in the same lane. Governance covers ownership, decisions, oversight and evidence. Engineering covers technical safeguards and their effects. The labels and phase mapping are interpretation by AI. The cited passages establish the risk mechanism or the purpose of the control.

Verified 10 November 2026. All excerpts below match the linked primary sources. The data recovery example concerns media that should be sanitized at retirement.

### Engineering risks

| Phase | Risk pill | Verified excerpt and source |
|---|---|---|
| Plan | Sensitive data left out of scope | “protection requirements concerning confidentiality, integrity, availability, and authenticity of all data assets” [OWASP A06 · Requirements and Resource Management](https://top10.owasp.org/2025/A06_2025-Insecure_Design/#:~:text=protection%20requirements%20concerning%20confidentiality%2C%20integrity%2C%20availability%2C%20and%20authenticity%20of%20all%20data%20assets) |
| Design | Abuse paths left open | “Threat modeling is a structured activity for identifying, evaluating, and managing system threats, architectural design flaws, and recommended security mitigations.” [OWASP SAMM · Threat Modeling](https://owaspsamm.org/model/design/threat-assessment/stream-b/#:~:text=Threat%20modeling%20is%20a%20structured%20activity%20for%20identifying%2C%20evaluating%2C%20and%20managing%20system%20threats%2C%20architectural%20design%20flaws%2C%20and%20recommended%20security%20mitigations.) |
| Code | Credentials exposed in code | “The product contains hard-coded credentials, such as a password or cryptographic key.” [MITRE CWE-798 · Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html#:~:text=The%20product%20contains%20hard%2Dcoded%20credentials%2C%20such%20as%20a%20password%20or%20cryptographic%20key.) |
| Build | Build output tampered with | “An adversary introduces an unauthorized change to a build output through tampering of the build process” [SLSA 1.2 · Build Process Threats](https://slsa.dev/spec/v1.2/threats#:~:text=An%20adversary%20introduces%20an%20unauthorized%20change%20to%20a%20build%20output%20through%20tampering%20of%20the%20build%20process) |
| Test | Broken controls go unnoticed | “ensure that the implemented security controls operate as expected and satisfy the project’s stated security requirements” [OWASP SAMM · Requirements-driven Testing](https://owaspsamm.org/model/verification/requirements-driven-testing/#:~:text=ensure%20that%20the%20implemented%20security%20controls%20operate%20as%20expected%20and%20satisfy%20the%20project%E2%80%99s%20stated%20security%20requirements) |
| Release | A substituted artifact ships | “SLSA Build L2 covers tampering of the artifact or provenance after the build.” [SLSA 1.2 · Verifying Artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts#:~:text=SLSA%20Build%20L2%20covers%20tampering%20of%20the%20artifact%20or%20provenance%20after%20the%20build.) |
| Deploy | Insecure settings go live | “missing appropriate security hardening across any part of the application stack or improperly configured permissions on cloud services” [OWASP A02 · Security Misconfiguration](https://top10.owasp.org/2025/A02_2025-Security_Misconfiguration/#:~:text=missing%20appropriate%20security%20hardening%20across%20any%20part%20of%20the%20application%20stack%20or%20improperly%20configured%20permissions%20on%20cloud%20services) |
| Operate | Known flaws stay exploitable | “Help ensure that vulnerabilities are remediated in accordance with risk to reduce the window of opportunity for attackers.” [NIST SSDF 1.1 · RV.2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf#page=26) |
| Monitor | Attacks go undetected | “Without logging and monitoring, attacks and breaches cannot be detected” [OWASP A09 · Security Logging and Alerting Failures](https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/#:~:text=Without%20logging%20and%20monitoring%2C%20attacks%20and%20breaches%20cannot%20be%20detected) |
| Retire | Old credentials still work | “When secrets are no longer required or potentially compromised, you must securely revoke them to restrict access.” [OWASP · Secrets Revocation](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet#273-revocation) |
| Retire | Data remains recoverable | “Media sanitization refers to a process that renders access to target data on the media infeasible for a given level of effort.” [NIST SP 800-88 Rev. 2 · Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final#:~:text=Media%20sanitization%20refers%20to%20a%20process%20that%20renders%20access%20to%20target%20data%20on%20the%20media%20infeasible%20for%20a%20given%20level%20of%20effort.) |

### Governance risks

| Phase | Risk pill | Verified excerpt and source |
|---|---|---|
| Plan | No named risk owner | “Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced.” [NIST CSF 2.0 · GV.RR-02](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf#page=17) |
| Design | Risk response left undefined | “Strategic direction that describes appropriate risk response options is established and communicated.” [NIST CSF 2.0 · GV.RM-04](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf#page=17) |
| Code | Development starts without security requirements | “Identify and document all security requirements for organization-developed software to meet, and maintain the requirements over time.” [NIST SSDF 1.1 · PO.1.2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf#page=14) |
| Build | Security findings go untracked | “Record and track all security defects in a defined location.” [OWASP SAMM · Defect Tracking](https://owaspsamm.org/model/implementation/defect-management/stream-a/#:~:text=Record%20and%20track%20all%20security%20defects%20in%20a%20defined%20location.) |
| Test | Security sign-off lacks test evidence | “consider the passing of security tests as part of merge requirements before allowing new code to enter the main code base.” [OWASP SAMM · Control Verification](https://owaspsamm.org/model/verification/requirements-driven-testing/stream-a/#:~:text=consider%20the%20passing%20of%20security%20tests%20as%20part%20of%20merge%20requirements%20before%20allowing%20new%20code%20to%20enter%20the%20main%20code%20base.) |
| Release | Accepted risk lacks stakeholder review | “all relevant stakeholders have a solid understanding of the imposed risk.” [OWASP SAMM · Defect Tracking](https://owaspsamm.org/model/implementation/defect-management/stream-a/) |
| Deploy | Unapproved changes reach production | “Implement approved configuration-controlled changes to the system” [NIST SP 800-53 Rev. 5 · CM-3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf#page=125) |
| Operate | Open actions lose ownership at handover | “Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced.” [NIST CSF 2.0 · GV.RR-02](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf#page=17) |
| Monitor | Overdue fixes go unreported | “centrally monitor and regularly report on SLA breaches.” [OWASP SAMM · Defect Tracking](https://owaspsamm.org/model/implementation/defect-management/stream-a/#:~:text=centrally%20monitor%20and%20regularly%20report%20on%20SLA%20breaches.) |
| Retire | Retention obligations left unresolved | “You have retention requirements for data, and you destroy backups in a timely manner after the relevant retention period ends” [OWASP SAMM · Data Protection](https://owaspsamm.org/model/operations/operational-management/stream-a/#:~:text=You%20have%20retention%20requirements%20for%20data%2C%20and%20you%20destroy%20backups%20in%20a%20timely%20manner%20after%20the%20relevant%20retention%20period%20ends) |

The three-lane layout and the governance summaries are interpretation by AI. The retirement governance prompt is also interpretation by AI, based on the supplied lifecycle description. The page does not claim these are formal organizational requirements.

## Verification gaps

The case presentation is a supplied exercise brief. The in-app browser blocked access to the local HTML, so desktop and narrow viewport rendering, overflow, and console behavior remain unverified.
