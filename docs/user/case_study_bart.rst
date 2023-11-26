ForensicVM Case Study - Bart the hacker
=======================================

.. _case_study:

Challenge Description
---------------------
This appendix details the ForensicVM Case Study and Challenge, which is designed to highlight the differences between the evidence collected by dead-box forensics and live-forensics in a virtualized environment. The data set was created with VirtualBox and features a Windows 11 Pro environment equipped with various local and cloud applications. The image was captured using the FTK Imager in Expert Witness Format (EWF).

- Virtualisation is required to extract vital evidence.
- Bypassing the 'Bart' password is necessary to access the applications.
- Existing passwords within the data set must remain unchanged to maintain the integrity of the challenge.
- The Bart windows password is simple, but the challenge encourages ethical hacking skills to bypass or decrypt it.

Steps to Solve the Challenge
----------------------------
The following steps provide a structured approach to tackle the ForensicVM challenge:

#. Utilise dead box forensics techniques in autopsy software to attempt full data retrieval from cloud applications and local applications. Document all findings.
#. Virtualize the forensic image using the autopsy ForensicVM plugin.
#. Attempt to identify and bypass the Bart password to gain access to the applications.
#. Run the ForensicVM
#. Without internet access, systematically extract information from each application cloud and local application. Document all findings.
#. Enable internet access and repeat the information extraction process, noting any differences.
#. Record any additional information obtained after establishing an Internet connection.
#. Identify and document information related to the two financial applications present in the environment.
#. Extract and analyse data related to cryptocurrency.
#. Create a comprehensive chain of custody for all investigative actions taken.
#. Conduct and document a memory dump and network traffic dump.
#. Capture all investigative actions via video and take screenshots for evidence support.
