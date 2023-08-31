Glossary
=========

.. glossary::
   :sorted:

   1980x1080 resolution
      A specific pixel count for display screens. This resolution is recommended to ensure a clear and detailed view of the ForensicVM interface.

   64-bit multi-core processor
      A processor with multiple cores capable of handling 64-bit data chunks simultaneously. It's essential for ForensicVM to achieve optimal performance, especially during intricate tasks.

   7-zip
      A free and open-source file archiver, commonly used for compressing and decompressing files.

   Access the Project Repository
      The hosted project on GitHub where you can view, clone, or fork the ForensicVM Plugins repository.

   Accessing the WebShell
      Refers to the methods available for users to access the WebShell for remote administration.

   Add Linux Forensic Admin
      A plugin to create a new Linux user with ‘sudo’ permissions.

   Add Windows Forensic Admin
      A plugin that creates a new Windows admin user with specific credentials. The user belongs to the “Administrator” group.

   Additional Security Bypass Features
      Plugins designed to bypass other security measures apart from authentication.

   Adjusting Screen Scaling: Local Scaling
      Steps to optimize the viewing experience within the webscreen console.

   Advanced options
      A deeper layer of settings, usually accessed after selecting “Troubleshoot”, that offers more specific ways to address boot issues.

   Advanced options in the Automatic Repair boot screen
      An option in the boot screen that provides advanced repair capabilities when facing boot-related issues.

   Alerts
      Notifications triggered when certain parameters exceed predefined limits.

   API key
      A code passed in by computer programs to identify the calling program. It grants access to a service, in this case, the ForensicVM server.

   Authentication Bypass Features
      A suite of plugins designed specifically to bypass various authentication measures.

   Autopsy
      An open-source digital forensics platform designed for analyzing, managing, reporting, and conducting digital investigations. It is used for disk forensics, post-mortem analysis, and handling forensic data. The platform also provides a user interface to manage various functionalities, including the ForensicVM. ForensicVM requires compatibility with at least Autopsy version 4.20.

   Autopsy Case
      Displays Autopsy case details, including existing case tags and the generated unique UUID.

   Autopsy framework
      A subset of the Autopsy platform focused on tools and functionalities used for conducting investigations, such as analyzing disk images or VM files, and post-mortem analysis.

   Autopsy ForensicVM Client Plugin
      An extension for the Autopsy framework, this plugin facilitates interaction with the ForensicVM environment. Through this interface, forensic investigators can access and manage various functionalities, including snapshot, ISO, and tools management like WebShell and Netdata. It is also tailored for managing and analyzing virtual forensic machines.

   Autopsy ForensicVM Client Plugin: A Comprehensive Interface Guide
      A detailed guide describing the functionalities and operations of the Autopsy ForensicVM Client Plugin.

   Autopsy Tags
      Markers or labels within the Autopsy platform that aid in organizing and categorizing evidence. They are represented as directories or folders on the evidence disk.

   Autopsy Plugin
      Extensions or tools within the Autopsy platform designed to enhance its forensic investigation capabilities. These plugins extend the core functionality of the Autopsy platform. The ForensicVM Client Plugin is a notable example.

   Bare metal server
      A physical server dedicated to a single tenant or purpose.

   Base Snapshot
      Often referred to as the ‘first snapshot,’ this represents the initial state of a system or piece of evidence, functioning as an untouched reference point.

   Belkasoft Evidence Center
      A software solution that includes the ability to analyze computer memory.

   BIOS
      Basic Input/Output System, a software that is built into the PC, and is the first code run by a PC when powered on.

   BitLocker Drive
      A drive encryption feature integrated into the Microsoft Windows operating system. In the provided context, the entire encrypted BitLocker drive is showcased being transferred for forensic analysis.

   Blue Screen of Death
      A colloquial term for a Windows system crash.

   Boot Manager
      A software process that starts the operating system when the computer is powered on.

   Bootable Media
      Digital storage media, like an ISO, that contains a boot sector, allowing a computer to start up from it. It provides details about booting from an ISO or CD-ROM for specific forensic tasks.

   BOOTFIX: Disable Driver Enforcement
      A utility that addresses challenges related to driver signatures.

   Booting without signed drivers
      Refers to the potential issue of a machine not booting when certain drivers, such as virtio drivers, are unsigned or possess an invalid signature for a given operating system.

   Browse and Upload ISO
      The process to navigate the interface and upload essential ISO files to the ForensicVM environment.

   Browse ForensicVM
      Accessing and navigating the forensic virtual machine using interfaces like web browsers.

   Browsing Available Plugins
      A process to view, manage, and deploy available plugins for ForensicVM using the Autopsy ForensicVM Client.

   Bypass Windows Password
      A plugin that patches the “ntlmshared.dll” file, allowing for the bypass of Windows authentication.

   C2C (Command and Control) client
      A centralized computer that issues commands to a botnet (a group of private computers infected with malicious software) and receives reports back.

   Case
      A specific digital forensic investigation project in Autopsy that may contain one or more data sources.

   Case Information
      Metadata associated with a case, including its name and other optional details.

   Chain of Custody
      The chronological documentation or paper trail, showing the seizure, custody, control, transfer, analysis, and disposition of physical or electronic evidence.

   Client
      Provides a user-friendly interface for managing forensic images. It allows users to create, run, and decommission instances as per their needs.

   Cloud Services
      Platforms and applications that provide data and services over the internet, often requiring network access to retrieve data.

   Command Line Window
      A windowed interface for command-line interactions.

   Community Plugins Project
      An open initiative aiming to enhance ForensicVM functionalities through community contributions.

   Configuration File
      A file that stores settings and parameters that define how a software or system behaves, and contains various parameters for the forensic virtual machine, such as memory size, attached disks, UEFI boot options, and more.

   Confirmation Dialog
      A prompt or interface that seeks affirmation from a user for a potentially critical action.

   Confirmation Popup
      A user interface element that appears to ensure that the user wants to proceed with an action, in this case, the deletion of the ForensicVM.

   Connect with Other Tools
      Refers to Netdata’s integration capabilities, where it can relay alerts to other platforms such as Slack or Twilio.

   Contributing Code
      Steps to contribute developed plugins or improvements to existing ones.

   Control
      A UI element, such as a button, that provides management capabilities (e.g., “Start,” “Stop,” “Reset”) for the forensicVM.

   Control Bar icon
      An icon that reveals the tool panel in the ForensicVM’s web interface.

   Convert Forensic Image to VM
      Options that facilitate transforming the forensic image into a forensic virtual machine.

   CPU
      Central Processing Unit, a primary indicator of a server’s processing capability. Netdata provides insights into its utilization.

   Danger Zone
      A section within the ForensicVM client interface dedicated to critical or potentially irreversible operations, such as deleting snapshots.

   Data Extraction and Analysis
      Tools or functionalities that help to extract and analyze data from a forensic image.

   Data Overload
      A situation where the amount of captured data is so vast that it becomes challenging to identify essential and relevant information.

   Data Source
      An entity from which digital evidence is extracted. This can refer to a repository, location, specific input, or reference. In the context of Autopsy, it encompasses evidence such as disk images, VM files, or any origin of forensic data. It is used as a connection or reference to gather, analyze, and acquire evidence within the forensic tool.

   Data Source Processing Progress
      A visual representation, usually a progress bar, showing the ongoing processing of a data source.

   Deactivate
      The process or act of shutting down or turning off a virtual machine or forensicVM, making it inactive or non-operational.

   Debian 11 (Bullseye)
      A specific version of the Debian operating system, also known as Bullseye. Recommended for installing the ForensicVM server and supported by ForensicVM.

   DEBUG: Remote ssh to folder
      A feature that provides a direct remote connection to the forensicVM, facilitating the editing of configuration files or control over its state.

   Decoding Protocols
      The process of translating network data from a machine-based protocol into a format that is human-readable.

   Delete
      The action of permanently removing an item, in this context, an ISO file, from storage or memory.

   Delete ISO
      Instructions to remove unwanted ISO files.

   Delete VM Button
      A designated button within the ForensicVM interface or related software used to initiate the deletion process of the virtual machine.

   Digital Evidence
      Information stored or transmitted in binary form that might be relied upon in court.

   Direct Copy to Server
      A method that duplicates the forensic image, creating a new forensic virtual machine on the server.

   Disable driver signature enforcement
      A startup option that allows Windows to bypass driver signature checks during boot, potentially enabling problematic or unsigned drivers to load.

   Disable Network Card
      The action of turning off the network card to halt all network communications for the forensicVM.

   Disable Windows Defender and Firewall
      A plugin that disables both Windows Defender and the firewall.

   Disk Activity
      Indicates how actively a disk is being read or written to, monitored by Netdata.

   Disk Image or VM File
      A digital copy or replica of a physical disk, also known as a bit-by-bit copy, often used in digital forensics to preserve the state of a drive. In the context of ForensicVM, a forensic image is used as a source for virtualization. As a data source, it represents either a snapshot of a disk or a virtual machine image.

   Django
      A high-level Python web framework that promotes rapid development and pragmatic, clean design. Allows for rapid web development.

   Documentation and Chain of Custody
      A process to ensure that the evidence is genuine and reliable, maintained through a documented and unbroken sequence of possession or control.

   Download Progress
      An indicator that displays the current status of a download operation.

   Eject ISO / Web Eject CD-ROM
      Guidance on ejecting a mounted ISO file or CD-ROM.

   Elevate to root permissions
      The act of gaining elevated system access rights, commonly achieved using the “su” command in Unix-like systems.

   Evidence Collection
      The process of gathering evidence, often digital, to support investigations and potentially use in court.

   Evidence Disk
      A disk or drive that serves multiple functions. It contains all tags from Autopsy Software and is automatically generated during the conversion of a forensic image to a ForensicVM. The disk contains directories named after Autopsy tags and serves as a container for evidence related to each tag. Additionally, it is the specific storage area where collected forensic evidence is saved and is often labeled as "possible evidence".

   Evidence Preservation
      The safeguarding of the original state of evidence, reducing risks of contamination or alteration.

   evidence.vmdk disk
      A specific format of a virtual disk image used to store forensic evidence in the context of Autopsy and VMs.

   Executing Plugins
      The process of running plugins on the ForensicVM.

   Fallback Conversion
      A backup method of conversion for unidentified OS.

   Feature Suggestions and Plugin Requests
      A method to contribute ideas for new plugins, features, or improvements without coding them.

   Fiber Optics
      A type of high-speed internet connection.

   File Explorer
      A graphical user interface (GUI) component that lets users manage and view files. It is used to navigate and identify the evidence disk.

   Fine-Tuning ForensicVM
      The process of making adjustments to various configuration parameters of a ForensicVM. This is done via a configuration file that is generated when a forensic image is converted into a ForensicVM.

   Firewall
      A network security system or component that monitors and controls incoming and outgoing network traffic based on predetermined security policies. Designed to block unauthorized access, it allows only permitted communications to pass.

   Forensic Administrator User
      A user profile with elevated privileges, potentially created for the purpose of a forensic investigation, to ensure unrestricted access to required data.

   Forensic Analysis
      Using memory dumps in digital forensics to reconstruct events, recover data, and analyze user and system interactions.

   Forensic Image
      A digital representation, snapshot, or copy of a storage device or data from a device. It preserves both the structure and content and is used for the purpose of analysis and investigation in digital forensics. Crucial for digital forensic investigations.

   Forensic SSH Server Redirection
      A method used by ForensicVM to safely access Windows shared folders over the internet via a reverse SSH connection.

   Forensic Virtual Machine (VM)
      A digital environment replicated from a forensic image that serves as a snapshot of a system at a specific point in time.

   ForensicVM / forensicVM
      A specialized or comprehensive virtual machine environment tailored for forensic investigations. It operates on a hypervisor and is derived from a forensic image. The operating system is detected, and necessary drivers are installed to replicate the functionality of the original system. An initial snapshot is created to preserve the original state. The ForensicVM allows detailed examination within a safe and controlled environment, without risk to other systems or compromising the original data. It often has a network card disabled by default for security reasons and offers tools and functionalities essential for digital forensic investigations. Designed to assist forensic investigators in the virtualization, management, and analysis of forensic images, it’s essential to manage its operations correctly to preserve the integrity of the evidence.

   ForensicVM Client Plugin
      A specialized Autopsy plugin that forms one of the two primary components of the ForensicVM project. It is the main program interface running in Autopsy Software and is designed to assist in the processing, converting, and forensic analysis of virtual machines and forensic images. Tailored for managing and interacting with Forensic Virtual Machines (VM), it facilitates the analysis of VM images.

   ForensicVM Loader
      A component that is part of the ForensicVM toolset and plugin, responsible for initializing and setting up the forensic analysis environment for VM analysis.

   ForensicVM Main Screen
      The primary interface of the forensic virtual machine when accessed via the web.

   ForensicVM Main Web Interface or web page
      The primary interface of the ForensicVM, where users can navigate to various tools and features, including the WebShell and Netdata.

   ForensicVM Server Remote Web Screen/Console Control Interface
      A web-based interface designed for remote forensic investigators to collaborate and control the ForensicVM. It lets users interact with the forensicVM directly and provides an interactive console for access to the virtual screen of the remote ForensicVM. It serves as a display of the forensicVM as seen when accessed remotely, especially through web interfaces.

   ForensicVM Server
      The main backbone of the ForensicVM system, developed using Django and Python, it facilitates the functionalities of the ForensicVM.

   ForensicVM Webscreen Console Control Toolbar
      A detailed overview of the Control Toolbar in the ForensicVM Webscreen Console.

   ForensicVM.exe
      The setup file responsible for installing the AutopsyVM client plugin on a user’s system.

   FTK Imager
      A product by AccessData, used for capturing and analyzing memory dumps.

   Gigabit connection
      A network connection that offers speeds of up to 1 gigabit per second.

   GRR (Google Rapid Response)
      An incident response framework that includes memory analysis capabilities.

   Halt
      The act of temporarily pausing or stopping the operations of the forensicVM without fully shutting it down.

   Hash Dump File
      A file that contains hashed representations of data. In the context, it is identified as potential evidence.

   Hibernate File Management
      Tools or methods to manage or remove hibernation files.

   Hibernation
      A power-saving mode for computers. In Windows, when the system goes into hibernation, it saves the current state of the system (including open applications and documents) into the hibernation file and shuts down, allowing for a faster start-up later.

   Hypervisor
      A piece of software, firmware, or hardware that creates and manages virtual machines (VMs). Also known as a virtual machine monitor (VMM), it is responsible for the execution of virtualized forensic images, manages resources, and ensures isolation between different instances.

   Host
      In the context of Autopsy, refers to a machine or system from which data is being collected or investigated.

   Host configuration
      The settings that determine how the data source is treated or processed within a forensic analysis environment.

   HP ILO
      Integrated Lights-Out. A remote management tool used for server administration.

   ifconfig
      A system administration utility in Unix-like operating systems to configure, control, and query TCP/IP network interface parameters.

   Immediate Reboot
      A rapid restart of the forensicVM without fully shutting it down. This is especially useful in scenarios requiring quick troubleshooting, testing, or managing different VM states.

   Immutable Record
      Non-alterable and chronological documentation, especially in the form of a video, captures every action and finding during an investigation.

   Import
      The act of bringing data into a software platform (like Autopsy) from an external source.

   Import Evidence Disk
      A function or feature that allows users to introduce an evidence disk into the analysis environment.

   Ingest Modules
      Modules in Autopsy that perform data extraction, analysis, and organization tasks automatically for the investigator.

   Ingest Plugins
      Plugins or modules in forensic software that are used to process and analyze specific types of data or evidence.

   Insert ISO / Web Insert CD-ROM
      Procedure to virtually insert an ISO file or CD-ROM for access within the ForensicVM environment.

   Installation / Installation and Setup
      The process of setting up various components, such as Netdata on a system. For ForensicVM Server, Netdata comes pre-installed. It also involves the steps necessary to install and prepare ForensicVM for use.

   Interface
      The user-friendly platform of ForensicVM that presents various features and tools systematically.

   IP Conflict
      Occurs when two or more devices or components on the same local network claim to have the same IP address, leading to network malfunctions.

   ISO / ISO files
      ISO 9660, also known as ECMA-119, is a file system for optical disc media standardized by the International Organization for Standardization (ISO). It is an optical disc image containing the content from a CD, DVD, or Blu-ray Disc that can be used to reproduce the content of these media. In the context of forensic tools, ISO files are encapsulations of entire file systems used to house specialized forensic tools. (Reference: `ISO 9660 on Wikipedia <https://en.wikipedia.org/wiki/ISO_9660>`_)

   ISO Management
      The handling of ISO files, which are typically used for optical disk images.

   Kali Linux Forensic Tools
      A set of forensic tools provided by the Kali Linux distribution.

   KVM / Kernel-based Virtual Machine
      A virtualization infrastructure for the Linux kernel that allows the kernel to function as a hypervisor.

   KVM drivers
      Drivers optimized for KVM virtualization.

   Legal Compliance
      Adhering to standards and requirements established by legal authorities, ensuring the chain of custody is maintained.

   Legal Evidence
      In legal proceedings, memory dumps might provide evidence related to computer usage, unauthorized access, and intellectual property theft.

   Link Creation
      A method where a link is established between the local forensic image and a new VM on the server.

   Link Mode
      A specific mode in which a forensic image is linked, rather than copied, to the forensicVM.

   Linux Terminal
      A command-line interface in Linux-based operating systems for executing commands.

   List Remote ISO Files
      An overview of ISO files stored remotely on the ForensicVM server.

   List Remote Snapshots
      A feature that allows users to manually fetch and view the list of all snapshots associated with a ForensicVM from a remote server.

   Logical Files
      A type of data source in Autopsy representing non-physical files, often used for importing various types of digital data.

   Login Button
      A button clicked after entering username and password to gain access to the web interface.

   Magnet RAM Capture
      A free tool designed to capture physical RAM.

   Main Panel Overview
      A detailed breakdown of the main display area based on the selected tab option.

   Main Plugin Interface
      The primary user interface within a specific framework, such as Autopsy, from where the forensicVM can be initiated, managed, and controlled. It also offers options to shut down the forensicVM.

   Main Toolbar Overview
      A description of the primary toolbar on the Autopsy ForensicVM Client Plugin.

   Main Web Interface
      The primary browser-based interface for managing and interacting with the forensicVM.

   Media Control Modal Box
      An interface component used in the process of inserting or ejecting ISOs via the web interface.

   Media Control Modal Panel
      A specific part of the web screen interface that provides controls for media management.

   Media Management in ForensicVM
      The procedure to navigate, upload, select, insert, eject, delete, and boot from ISO files within ForensicVM.

   Media Panel
      An interface section within the Autopsy ForensicVM Client Plugin used to manage different media files, including ISOs.

   Media Panel Separator
      A component in the ForensicVM Client Plugin to access the Media Panel.

   Memory
      RAM (Random Access Memory) usage and availability, tracked by Netdata.

   Memory Dump
      A snapshot or the recorded state of the working memory (RAM) of a computer program or system at a specific time. Used in forensic analysis to review the state of the system and includes tools to engage with the active memory data of the forensic virtual machine.

   Meterpreter
      A type of payload in the Metasploit framework that provides an investigator with a command line interface to the targeted system. In the context, its deployment is considered as potential evidence.

   Modifying Memory Size
      The process of adjusting the ForensicVM’s memory size within the “Fine-Tuning” section of the Autopsy ForensicVM Client interface.

   MoonSols DumpIt
      A tool for creating memory dumps from Windows systems.

   MS-DOS Command Window
      A command-line interface available in older versions of Windows.

   Netdata
      A real-time health monitoring and performance troubleshooting tool for systems. It offers insights into server and application performance.

   Network
      Options to manage network settings and operations for the ForensicVM.

   Network Card
      A hardware component or a virtual representation that connects a computer to a network.

   Network Isolation
      A safety measure that eliminates the need for network connectivity to mitigate associated risks.

   Network Troubleshooter
      A built-in Windows tool designed to diagnose and fix common network issues.

   Notable Item Tag
      A label or marker in Autopsy, used to identify and categorize significant pieces of evidence or data points during forensic analysis.

   Notification Area
      A designated area on the interface for system notifications, warnings, and error messages.

   NVMe
      Non-Volatile Memory Express. A modern protocol developed for SSDs to exploit the full potential of high-speed PCI Express storage devices.

   Open ForensicVM
      An action or option to access and interact with the forensicVM’s main display, either through the Autopsy plugin or web interface. This can be initiated through various means such as a button within the Autopsy ForensicVM Client Plugin that allows users to launch the WebShell in their default browser.

   Output Console
      A console that captures all system messages and is instrumental for debugging.

   Panel Opener
      An interface element within the forensicVM used to reveal various options or configurations.

   Password Administration
      Tools or methods to reset forgotten passwords or generate new administrator accounts.

   Patch Accessibility
      A strategic patch enabling the invocation of a system-level cmd.exe prompt by pressing the shift key five times on the Windows login screen.

   pcap Directory
      The directory or folder where pcap files, often extracted from the pcap.zip, are stored for analysis.

   pcap.zip
      A compressed file containing Wireshark pcap files collected during the network card activity periods.

   Picture Analyser Plugin
      A plugin in Autopsy used to analyze and manage pictures or images.

   Plugin/Plugins
      Modular software components that add specific features to an existing computer program. Within the context of ForensicVM and Autopsy, the plugin architecture fosters community involvement and functionality expansion. They enhance or extend functionality and provide forensic investigators with capabilities to bypass protections in locked forensicVM machines. They may also help in functions such as creating new user credentials or resetting existing ones.

   Plugin Architecture
      A method by which external additions can be made to extend a software’s capabilities.

   Plugin Interface
      The user interface provided by a software plugin, such as the one in Autopsy for the forensicVM.

   Plugin Location
      The directory or file path where the AutopsyVM client plugin will be installed on your computer.

   Possible Evidence virtual drive
      A dedicated virtual drive within ForensicVM designed to store potential pieces of evidence without contaminating the original data.

   Power Off/Log Out Option
      An option in operating systems (like Ubuntu 22.10) that allows users to either shut down or log out of their accounts. Proper shutdown is recommended to ensure the integrity of collected evidence.

   Pre-plugin Execution Recommendation
      A cautionary advice to capture a snapshot of the machine’s state before initiating any plugin.

   Protective Shield
      The protection provided by ForensicVM’s virtual environment to the host system against potential threats.

   Python
      A high-level programming language known for its clear syntax and readability.

   Python Ingest Plugin
      A plugin in Autopsy used to automate the ingestion of data from a data source.

   Python Ingest Plugin
      A plugin in Autopsy used for data ingestion and is written in Python.

   qcow2
      A disk file format commonly used in QEMU, a free and open-source hardware virtualization solution.

   qcow2 format
      A popular disk image format used in KVM virtualization.

   QEMU
      An open-source machine emulator and virtualizer.

   QEMU
      Quick Emulator. An open-source hypervisor that performs hardware virtualization. ForensicVM uses QEMU to create a new forensic hypervisor server.

   QEMU Documentation
      The official documentation for QEMU, a software that provides hardware virtualization.

   RAID 10
      A type of RAID (Redundant Array of Independent Disks) configuration that combines mirroring and striping to protect data. It’s recommended for storing forensic images in ForensicVM.

   RAM
      Random Access Memory. It’s a type of computer memory used for temporary storage and quick access. ForensicVM requires a minimum of 16 GB RAM, but 32 GB or more is recommended for efficient virtualization of forensic images.

   RAM
      Random Access Memory. ForensicVM requires a minimum of 16 GB RAM for efficient operation. The Autopsy documentation suggests that the software can use up to 4GB of RAM, not including the additional memory the Solr text indexing server might use.

   readonly windows shares
      Network-shared folders in the Windows operating system that do not allow modifications to the shared files. The ForensicVM plugin may create such shares and therefore requires specific permissions.

   Real-time Look
      Refers to Netdata’s capability to update its insights every second.

   Recreate Evidence Disk
      An action that leads to the deletion and fresh generation of the evidence disk within the Autopsy environment.

   Redline
      A tool provided by FireEye offering advanced memory and file analysis capabilities.

   Rekall
      A memory forensics toolkit.

   Reset
      The act of immediately rebooting the forensicVM, similar to a hard restart. It brings the machine back to its initial or default state without shutting it down completely.

   Reset Button
      A user interface control designed to immediately reboot the forensicVM, bringing it to its default or initial state.

   Reset Windows 2003 or XP Activation
      A plugin that resets activation for Windows 2003 or XP.

   Reverse SSH connection
      A technique where an SSH connection is initiated from a remote machine to the user’s machine, essentially reversing the typical connection direction.

   Rollback
      The process of reverting the state of the ForensicVM to a previously taken snapshot.

   root privileges
      The highest level of access rights on a system, allowing full control over all functions and files.

   samba CIFS share
      A type of shared resource that can be accessed by other computers. Known as Windows share.

   Save As Dialog
      A prompt or interface in software applications that lets users specify the name and location of a file they wish to save.

   Save As Dialogue
      A dialog box in software that prompts the user to specify the location and name of a file before saving it.

   Save Screenshots Button
      A button in the interface that initiates the process of saving captured screenshots.

   Screenshot
      A digital image that captures the contents of a computer screen, often used for documentation, analysis, or reporting purposes.

   Screenshot Management
      Tools to capture and manage screenshots during forensic investigations.

   Secondary Toolbar Overview
      An overview of the secondary set of tools in the Autopsy ForensicVM Client Plugin.

   Sector size
      A fundamental unit of data storage on a disk, usually specified in bytes (e.g., 512 bytes).

   Sector Size
      The smallest addressable unit on a disk.

   Security Analysis
      In cybersecurity, it involves using memory dumps to uncover malware behavior, detect hidden processes, analyze injected codes, and assess user credentials.

   Select ISO / Web Select CD-ROM
      Instructions on choosing the appropriate ISO file or CD-ROM.

   Session Cookies
      Small pieces of data stored on a user’s computer during a browsing session, often containing information about user preferences or authentication status.

   Set Your Alarms
      A feature in Netdata that allows users to customize alert thresholds based on their needs.

   Setting the VM Date & Time
      A function that allows users to define the start date & time for the ForensicVM.

   shellinabox project
      An open-source project that enables users to access remote servers from a web browser using a web-based terminal emulator.

   Shut Down VM on the Web Interface
      The method of deactivating the forensicVM directly from the web-based interface.

   Shut Down VM on the Web Remote Screen
      The method of shutting down the forensicVM when accessing remotely via the web.

   Shutdown Button
      A button in the Autopsy Plugin used to power off the forensicVM.

   Shutdown Button
      A UI control present on various interfaces that, when pressed, initiates the process to shut down the forensicVM.

   Shutdown Button
      A user interface control designed to initiate the process to deactivate and shut down the forensicVM.

   Shutdown Icon
      A graphical representation or symbol indicating the control to shut down the forensicVM.

   Snapshot
      A saved state of a virtualized resource, such as a VM or forensic image.

   Snapshot Deletion Interface
      An interface or prompt within the ForensicVM client that facilitates the process of deleting a snapshot.

   Snapshot Management
      The control and management of VM snapshots.

   Snapshot Management
      A section or functionality within the ForensicVM or its client interface, where snapshots are created, viewed, and managed.

   Snapshots
      A feature in ForensicVM that captures and preserves the state of the system or evidence at a specific point in time.

   SSD
      Solid State Drive. A storage device that uses integrated circuit assemblies to store data persistently, typically using flash memory.

   SSD
      Solid State Drive. A faster type of storage device compared to traditional HDDs, beneficial for speeding up acquisition processes.

   SSH
      Secure Shell. A cryptographic network protocol used for secure data communication and server administration.

   SSH (Secure Shell)
      A cryptographic network protocol used for operating network services securely over an unsecured network.

   SSH Connection
      Secure Shell connection; a cryptographic network protocol for secure data communication.

   Start Button
      A button used to initiate the forensicVM.

   Startup Settings
      An option within the “Advanced options” which allows changing the behavior of Windows during startup.

   Stop Button
      A button in the Autopsy Plugin used to halt the forensicVM.

   Stop Button
      A user interface control designed to initiate the process to halt and stop the forensicVM.

   Tag
      A label or marker within Autopsy used to identify and categorize data points or items of interest during forensic analysis.

   Tagging
      The act of marking or labeling a specific item (like a screenshot) for identification, organization, or further analysis.

   Tagging
      The process of marking or labeling a piece of evidence or finding with a specific tag or label to easily categorize, search, or identify it later.

   Tampered Data
      Information that has been intentionally altered or falsified to mislead or deceive.

   Third-Party Tools
      Software or utilities that are not part of the original package or platform but can be integrated or used alongside it for additional functionalities.

   Time Zone
      A region that observes a uniform standard time for legal, commercial, and social purposes.

   Timestamps
      Digital records of specific times at which events occurred.

   Tools
      Additional utilities for forensic operations within the ForensicVM interface.

   Traffic Analysis
      The process of intercepting and examining messages to deduce information from patterns in communication, endpoints, and more.

   Transparency and Accountability
      The assurance that the forensic process is done ethically and without tampering, as demonstrated by a detailed log such as a video recording.

   Troubleshoot
      A selection available during boot-up that aids in diagnosing and fixing issues that prevent the system from starting.

   TTPs (Tactics, Techniques, and Procedures)
      Patterns of activities or methods associated with a specific threat actor or group of threat actors.

   Ubuntu 22.10
      A version of the Ubuntu operating system. Ubuntu is an open-source software platform that runs everywhere from the PC to the server and the cloud.

   UEFI
      Unified Extensible Firmware Interface, a specification for the software program that connects a computer’s firmware to its operating system.

   UEFI QEMU DVD-ROM
      A UEFI-compatible DVD-ROM virtual device provided by QEMU, a hosted virtual machine monitor.

   UUID (Universally Unique Identifier)
      A 128-bit number used to uniquely identify some object or entity on the Internet. In this context, it identifies the specific ForensicVM instance that was deleted.

   Video Recording Sound
      Refers to the audio component of a video recording. In the context provided, the current VM does not support audio capture, though it is recognized as an important feature for some investigations.

   Virtual CD-ROM Drive
      A simulated CD-ROM drive that can read ISO files as if they were physical discs.

   Virtual CD-ROM drive
      A software representation of a CD-ROM drive that allows the mounting and reading of ISO files as if they were physical discs.

   Virtualization
      The creation and management of virtualized instances of certain resources, in this context, forensic images.

   Virtualize Tab
      The main tab within the toolbar that provides access to core ForensicVM operations.

   VM
      Virtual machine - In computing, a virtual machine (VM) is the virtualization or emulation of a computer system. Virtual machines are based on computer architectures and provide the functionality of a physical computer. Their implementations may involve specialized hardware, software, or a combination of the two. Virtual machines differ and are organized by their function, shown here: System virtual machines (also called full virtualization VMs) provide a substitute for a real machine. They provide the functionality needed to execute entire operating systems. A hypervisor uses native execution to share and manage hardware, allowing for multiple environments that are isolated from one another yet exist on the same physical machine. Modern hypervisors use hardware-assisted virtualization, with virtualization-specific hardware features on the host CPUs providing assistance to hypervisors. (Reference: https://en.wikipedia.org/wiki/Virtual_machine)

   VM Control
      Options to manage the basic operations of the forensic virtual machine.

   VM File (Virtual Machine File)
      A file representing a virtual machine, which contains an OS, applications, and data, and can be executed on a hypervisor.

   VM Image
      A virtual disk image, which contains a virtual system’s disk data, used for creating replicas of or taking snapshots of original virtual disks.

   vmdk
      A disk file format used for virtual appliances developed for VMware products.

   Volatility
      An open-source memory forensics framework.

   Web Interface
      An interface accessible via a web browser where users can control the forensicVM.

   Web Interface
      The web-based platform from which users can manage and control the forensicVM. It offers different functionalities including shutting down the machine.

   Web Interface
      The web-based platform from which users can manage and control the forensicVM. It offers different functionalities including stopping the machine.

   Web Interface
      A web-based platform through which users can manage, control, and reset the forensicVM. It is accessible through a browser and might be preferable for remote operations or specific service interfaces.

   Web Interface URL
      The web address used to access the forensicVM’s browser-based interface.

   Web Remote Screen
      A specific section of the web interface tailored for remote access.

   Web Remote Screen (Shutdown)
      A method to shut down the forensicVM when accessed remotely, offering flexibility for those working from distant locations or specific service interfaces.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It can be accessed after logging in.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It can be accessed after logging in.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It provides options to reset the machine, among other functionalities.

   Web Screen Interface
      A web-based platform through which users can interact with and manage the forensicVM.

   Web Screen Interface
      An interface within the forensicVM that provides access to various settings including network configurations.

   Web Screen Interface
      An interface within the forensicVM that provides access to various settings including network configurations.

   Web Screen Interface
      A web-based interface that provides access to various functionalities, including the ability to eject and manage media within the ForensicVM.

   Webscreen Console Main Area
      A description of the main area in the ForensicVM Webscreen Console.

   WebShell
      A script that can be uploaded to a web server to enable remote administration of the machine.

   WebShell for Remote Administration
      A tool based on the shellinabox project adapted into a Django application that facilitates enhanced remote server administration, offering secure root access to the server.

   WebShell Interface
      The user interface that is presented upon accessing the WebShell, providing a direct and secure interaction with the server.

   What-If Analysis
      A series of hypothetical scenarios in forensic investigations, where investigators simulate actions to test different hypotheses.

   WinDbg
      Microsoft’s debugger used for debugging Windows applications and analyzing memory dumps.

   Windows 10 or later
      A version of the Microsoft Windows operating system. ForensicVM supports Windows 10 and its successors for running the Autopsy plugin.

   Windows Explorer
      The default file manager in Microsoft Windows operating systems that provides a graphical user interface for accessing the file system.

   Windows Share
      A feature in the Windows operating system that allows files and folders to be shared over a network.

   Wireshark
      A network packet analyzer. It captures network packets in real-time and displays them in human-readable format.

   Wireshark
      A network protocol analyzer tool, which captures and displays packets for detailed analysis.

   Wireshark pcap file
      A specific file format used to capture and store network packets for later analysis using tools like Wireshark.

   Wireshark pcap Files
      A specific file format used to capture and store network packets for later analysis using tools like Wireshark.

   Wireshark PCAP format
      A specific format used to capture and save network traffic.

   Wizard Interface
      A user-friendly interface in software that guides users through a process step by step.

   X-Ways Forensics
      A commercial forensic software with strong memory analysis features.

   ZIP File
      A file format that allows for lossless data compression. It can contain multiple files or folders compressed into a single file.

