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

The Forensic Virtual Machine offers a plethora of features tailored to aid forensic analysts during their investigations. These features are systematically organized and can be accessed from various zones of the Autopsy interface. Each zone provides specific tools and functionalities, ensuring a seamless and comprehensive analysis experience. 

In the table below, the distribution of features across the different zones of the interface is highlighted. This is to help users quickly identify where to locate and how to use each feature, maximizing efficiency and precision in their forensic operations.

.. list-table:: Features and Location
   :widths: 40 5 5 5 5 5
   :header-rows: 1

   * - Feature
     - M
     - W
     - A
     - AS
     - E
   * - :ref:`Convert Forensic Image to a Forensic Virtual Machine`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Method 1: Copy the Local Forensic Image to a New Forensic Virtual Machine on the Server`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Method 2: Link the Local Forensic Image to a New Forensic Virtual Machine on the Server`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Gather Evidence Using the Evidence Disk`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Evidence Disk Creation`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Collecting Evidence: A Step-by-Step Guide`
     - .
     - ✅
     - .
     - .
     - .
   * - :ref:`Recreate Evidence Disk`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Import Possible Evidence Disk into Autopsy`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Deletion of ForensicVM at Investigation Conclusion`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Fine-Tuning ForensicVM`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Media Management in ForensicVM: Leveraging ISOs for Enhanced Forensic Investigations`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Uploading an ISO to the ForensicVM Server`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`List Remote ISO Files`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Insert ISO / Web Insert CD-ROM`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Run programs and utilities from ISO`
     - .
     - ✅
     - .
     - .
     - .
   * - :ref:`Bootable Media`
     - .
     - ✅
     - .
     - .
     - .
   * - :ref:`Making, Downloading, and Analyzing a Memory Dump (memory_dump_vm)`
     - .
     - .
     - ✅
     - ✅
     - ✅
   * - :ref:`Making and download a Memory Dump`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Importing and Analyzing a Memory Dump in Autopsy`
     - .
     - .
     - .
     - ✅
     - ✅
   * - :ref:`Netdata on ForensicVM Server`
     - ✅
     - .
     - ✅
     - .
     - .
   * - :ref:`Managing the Network Card to Capture and Analyse Network Traffic`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Enable the Network Card`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Reseting the Operating System Network Card`
     - .
     - ✅
     - .
     - .
     - .
   * - :ref:`Disable the Network Card`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Download Wireshark pcap Files`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Open or Browse the Forensic Virtual Machine (VM)`
     - ✅
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Plugins - Security Bypass Utilities`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Browsing Available Plugins`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Executing Plugins`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Resetting the Virtual Machine (VM)`
     - ✅
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Making and importing Screenshots`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Making screenshots`
     - .
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Downloading Screenshots as a ZIP File`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Importing Screenshots to Autopsy Software`
     - .
     - .
     - .
     - ✅
     - .
   * - :ref:`Shutting Down the Virtual Machine (VM)`
     - ✅
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Snapshots in ForensicVM: A Crucial Asset for Investigators`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Create a new snapshot`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`List Remote Snapshots`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Select and Rollback a Snapshot`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Delete a Snapshot`
     - .
     - .
     - ✅
     - .
     - .
   * - :ref:`Starting the Virtual Machine (VM)`
     - ✅
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Stopping the Virtual Machine (VM)`
     - ✅
     - ✅
     - ✅
     - .
     - .
   * - :ref:`Recording Video from a Forensic Virtual Machine`
     - .
     - ✅
     - .
     - .
     - .
   * - :ref:`WebShell for Remote Administration`
     - ✅
     - .
     - ✅
     - .
     - .
   * - :ref:`DEBUG: Remote ssh to folder`
     - .
     - .
     - ✅
     - .
     - .

.. note::
   - M = ForensicVM Main Web Interface
   - W = ForensicVM Web Remote Screen
   - A = ForensicVM Autopsy Client Plugin Interface
   - AS = Basis Technology Autopsy Software
   - E = External Software: Volatility, wireshark, etc...

Plugin Architecture
======================

One of the key features of ForensicVM is its plugin architecture, which enables the community to extend its functionality and interact with forensic images in innovative ways. This open architecture fosters the development of new software that can interact with forensic images, providing flexibility and promoting active community involvement.

Through the plugin architecture, developers can create tools to perform a variety of tasks, including but not limited to:

- **Password Administration**: Reset forgotten passwords or generate new administrator accounts to gain access to the systems encapsulated in the forensic image.
- **Hibernate File Management**: Remove hibernation files to remove state of the system at the time of hibernation.
- **Data Extraction and Analysis**: Extract and analyze data from a forensic image to uncover evidence or gain insights into the operation of the system.

By contributing plugins to the community, developers can help to improve ForensicVM, enriching it with new features and capabilities. Moreover, by utilizing the plugins developed by the community, users can tailor ForensicVM to their specific needs, creating a more versatile and powerful forensic analysis environment.

You can contribute at: https://github.com/nunomourinho/forensicVM-Plugins



