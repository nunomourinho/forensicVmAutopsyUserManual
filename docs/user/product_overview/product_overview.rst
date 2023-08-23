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
| Feature                                                                                                 | M     | W     | A     | AS    | E     |
+---------------------------------------------------------------------------------------------------------+-------+-------+-------+-------+-------+
| Convert Forensic Image to a Forensic Virtual Machine                                                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Method 1: Copy the Local Forensic Image to a New Forensic Virtual Machine on the Server               | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Method 2: Link the Local Forensic Image to a New Forensic Virtual Machine on the Server               | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Gather Evidence Using the Evidence Disk                                                                 | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Evidence Disk Creation                                                                               | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Collecting Evidence: A Step-by-Step Guide                                                             | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Recreate Evidence Disk                                                                               | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Import Possible Evidence Disk into Autopsy                                                            | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Deletion of ForensicVM at Investigation Conclusion                                                     | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Fine-Tuning ForensicVM                                                                                 | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Media Management in ForensicVM: Leveraging ISOs for Enhanced Forensic Investigations                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Uploading an ISO to the ForensicVM Server                                                            | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   List Remote ISO Files                                                                                | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Insert ISO / Web Insert CD-ROM                                                                       | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Run programs and utilities from ISO                                                                  | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Bootable Media                                                                                       | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Making, Downloading, and Analyzing a Memory Dump (memory_dump_vm)                                       | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg |
|   Making and download a Memory Dump                                                                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Importing and Analyzing a Memory Dump in Autopsy                                                     | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg |
| Netdata on ForensicVM Server                                                                           | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Managing the Network Card to Capture and Analyse Network Traffic                                       | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Enable the Network Card                                                                              | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Reseting the Operating System Network Card                                                           | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Disable the Network Card                                                                             | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Download Wireshark pcap Files                                                                        | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Open or Browse the Forensic Virtual Machine (VM)                                                       | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Plugins - Security Bypass Utilities                                                                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Browsing Available Plugins                                                                           | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Executing Plugins                                                                                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Resetting the Virtual Machine (VM)                                                                     | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Making and importing Screenshots                                                                       | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Making screenshots                                                                                   | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Downloading Screenshots as a ZIP File                                                                | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Importing Screenshots to Autopsy Software                                                            | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg |
| Shutting Down the Virtual Machine (VM)                                                                 | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Snapshots in ForensicVM: A Crucial Asset for Investigators                                             | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Create a new snapshot                                                                                | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   List Remote Snapshots                                                                                | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Select and Rollback a Snapshot                                                                       | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
|   Delete a Snapshot                                                                                    | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Starting the Virtual Machine (VM)                                                                      | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Stopping the Virtual Machine (VM)                                                                      | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| Recording Video from a Forensic Virtual Machine                                                        | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| WebShell for Remote Administration                                                                     | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
| DEBUG: Remote ssh to folder                                                                            | .. image:: img/missing.jpg | .. image:: img/missing.jpg | .. image:: img/check.jpg | .. image:: img/missing.jpg | .. image:: img/missing.jpg |
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



