=====================
Product Overview
=====================

ForensicVM is a powerful tool in digital forensics. It simplifies the investigation process by allowing the virtualization and management of forensic images. 

ForensicVM Architecture
==========================

ForensicVM is composed of two main components:

- **The Client**: The client provides a user-friendly interface for managing forensic images, allowing users to create, run, and decommission instances as needed. It supports a variety of forensic image formats, ensuring compatibility with a wide range of existing tools and workflows.

- **The Hypervisor**: The hypervisor is responsible for the execution of the virtualized forensic images. It manages resources and isolation between instances, ensuring that each virtual machine runs effectively and securely.

Understanding the Interface
==============================

ForensicVM's interface is designed with usability in mind. It provides a clear view of the current state of your forensic images, including active instances, and the status of any ongoing analysis tasks. It also provides easy access to ForensicVM's suite of analysis tools, making it simple to start investigating a forensic image.

+---------------------------------------------------------------------------------------------------------+-------+-------+-------+-------+-------+
| Feature                                                                                                 |   M   |   W   |   A   |  AS   |   E   |
+---------------------------------------------------------------------------------------------------------+-------+-------+-------+-------+-------+
| ::ref:`Convert Forensic Image to a Forensic Virtual Machine`                                            |   -   |   -   |   X   |   -   |   -   |
|   Method 1: Copy the Local Forensic Image to a New Forensic Virtual Machine on the Server               |   -   |   -   |   X   |   -   |   -   |
|   Method 2: Link the Local Forensic Image to a New Forensic Virtual Machine on the Server               |   -   |   -   |   X   |   -   |   -   |
| Gather Evidence Using the Evidence Disk                                                                 |   -   |   -   |   X   |   -   |   -   |
|   Evidence Disk Creation                                                                                |   -   |   -   |   X   |   -   |   -   |
|   Collecting Evidence: A Step-by-Step Guide                                                             |   -   |   X   |   -   |   -   |   -   |
|   Recreate Evidence Disk                                                                                |   -   |   -   |   X   |   -   |   -   |
|   Import Possible Evidence Disk into Autopsy                                                            |   -   |   -   |   X   |   -   |   -   |
| Deletion of ForensicVM at Investigation Conclusion                                                      |   -   |   -   |   X   |   -   |   -   |
| Fine-Tuning ForensicVM                                                                                  |   -   |   -   |   X   |   -   |   -   |
| Media Management in ForensicVM: Leveraging ISOs for Enhanced Forensic Investigations                    |   -   |   -   |   X   |   -   |   -   |
|   Uploading an ISO to the ForensicVM Server                                                             |   -   |   -   |   X   |   -   |   -   |
|   List Remote ISO Files                                                                                 |   -   |   X   |   X   |   -   |   -   |
|   Insert ISO / Web Insert CD-ROM                                                                        |   -   |   X   |   X   |   -   |   -   |
|   Run programs and utilities from ISO                                                                   |   -   |   X   |   -   |   -   |   -   |
|   Bootable Media                                                                                        |   -   |   X   |   -   |   -   |   -   |
| Making, Downloading, and Analyzing a Memory Dump (memory_dump_vm)                                       |   -   |   -   |   X   |   X   |   X   |
|   Making and download a Memory Dump                                                                     |   -   |   -   |   X   |   -   |   -   |
|   Importing and Analyzing a Memory Dump in Autopsy                                                      |   -   |   -   |   -   |   X   |   X   |
| Netdata on ForensicVM Server                                                                            |   X   |   -   |   X   |   -   |   -   |
| Managing the Network Card to Capture and Analyse Network Traffic                                        |   -   |   X   |   X   |   -   |   -   |
|   Enable the Network Card                                                                               |   -   |   X   |   X   |   -   |   -   |
|   Reseting the Operating System Network Card                                                            |   -   |   X   |   -   |   -   |   -   |
|   Disable the Network Card                                                                              |   -   |   X   |   X   |   -   |   -   |
|   Download Wireshark pcap Files                                                                         |   -   |   -   |   X   |   -   |   -   |
| Open or Browse the Forensic Virtual Machine (VM)                                                        |   X   |   X   |   X   |   -   |   -   |
| Plugins - Security Bypass Utilities                                                                     |   -   |   -   |   X   |   -   |   -   |
|   Browsing Available Plugins                                                                            |   -   |   -   |   X   |   -   |   -   |
|   Executing Plugins                                                                                     |   -   |   -   |   X   |   -   |   -   |
| Resetting the Virtual Machine (VM)                                                                      |   X   |   X   |   X   |   -   |   -   |
| Making and importing Screenshots                                                                        |   -   |   X   |   X   |   -   |   -   |
|   Making screenshots                                                                                    |   -   |   X   |   X   |   -   |   -   |
|   Downloading Screenshots as a ZIP File                                                                 |   -   |   -   |   X   |   -   |   -   |
|   Importing Screenshots to Autopsy Software                                                             |   -   |   -   |   -   |   X   |   -   |
| Shutting Down the Virtual Machine (VM)                                                                  |   X   |   X   |   X   |   -   |   -   |
| Snapshots in ForensicVM: A Crucial Asset for Investigators                                              |   -   |   -   |   X   |   -   |   -   |
|   Create a new snapshot                                                                                 |   -   |   -   |   X   |   -   |   -   |
|   List Remote Snapshots                                                                                 |   -   |   -   |   X   |   -   |   -   |
|   Select and Rollback a Snapshot                                                                        |   -   |   -   |   X   |   -   |   -   |
|   Delete a Snapshot                                                                                     |   -   |   -   |   X   |   -   |   -   |
| Starting the Virtual Machine (VM)                                                                       |   X   |   X   |   X   |   -   |   -   |
| Stopping the Virtual Machine (VM)                                                                       |   X   |   X   |   X   |   -   |   -   |
| Recording Video from a Forensic Virtual Machine                                                         |   -   |   X   |   -   |   -   |   -   |
| WebShell for Remote Administration                                                                      |   X   |   -   |   X   |   -   |   -   |
| DEBUG: Remote ssh to folder                                                                             |   -   |   -   |   X   |   -   |   -   |
+---------------------------------------------------------------------------------------------------------+-------+-------+-------+-------+-------+



Plugin Architecture
======================

One of the key features of ForensicVM is its plugin architecture, which enables the community to extend its functionality and interact with forensic images in innovative ways. This open architecture fosters the development of new software that can interact with forensic images, providing flexibility and promoting active community involvement.

Through the plugin architecture, developers can create tools to perform a variety of tasks, including but not limited to:

- **Password Administration**: Reset forgotten passwords or generate new administrator accounts to gain access to the systems encapsulated in the forensic image.
- **Hibernate File Management**: Remove hibernation files to remove state of the system at the time of hibernation.
- **Data Extraction and Analysis**: Extract and analyze data from a forensic image to uncover evidence or gain insights into the operation of the system.

By contributing plugins to the community, developers can help to improve ForensicVM, enriching it with new features and capabilities. Moreover, by utilizing the plugins developed by the community, users can tailor ForensicVM to their specific needs, creating a more versatile and powerful forensic analysis environment.

You can contribute at: https://github.com/nunomourinho/forensicVM-Plugins



