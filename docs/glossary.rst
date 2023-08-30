Glossary
=========

.. glossary::
   :sorted:

   forensicVM
      A specialized virtual machine that operates on a hypervisor and is utilized in digital forensic investigations. It is created through the conversion of a forensic image into a virtual machine format. The operating system is detected, and necessary drivers are installed to replicate the functionality of the original system. An initial snapshot is created to preserve the original state. The forensicVM simulates the original computer or server within a safe and controlled environment, allowing detailed examination without risk to other systems.

   ISO
      ISO 9660 (also known as ECMA-119) is a file system for optical disc media. The file system is an international standard available from the International Organization for Standardization (ISO). Since the specification is available for anybody to purchase, implementations have been written for many operating systems (Reference: https://en.wikipedia.org/wiki/ISO_9660)

   VM
      Virtual machine - In computing, a virtual machine (VM) is the virtualization or emulation of a computer system. Virtual machines are based on computer architectures and provide the functionality of a physical computer. Their implementations may involve specialized hardware, software, or a combination of the two. Virtual machines differ and are organized by their function, shown here:
         System virtual machines (also called full virtualization VMs) provide a substitute for a real machine. They provide the functionality needed to execute entire operating systems. A hypervisor uses native execution to share and manage hardware, allowing for multiple environments that are isolated from one another yet exist on the same physical machine. Modern hypervisors use hardware-assisted virtualization, with virtualization-specific hardware features on the host CPUs providing assistance to hypervisors. (Reference: https://en.wikipedia.org/wiki/Virtual_machine)

   Virtualization
      The creation and management of virtualized instances of certain resources, in this context, forensic images.

   Snapshot
      A saved state of a virtualized resource, such as a VM or forensic image.

   Forensic Image
      A digital representation of data from a device, used for analysis in digital forensics.

   Hypervisor
      A piece of software, firmware, or hardware that creates and manages VMs.

   QEMU
      An open-source machine emulator and virtualizer.

   KVM (Kernel-based Virtual Machine)
      A virtualization module in the Linux kernel that allows the kernel to function as a hypervisor.

   Plugin Architecture
      A method by which external additions can be made to extend a software's capabilities.

   Evidence Disk
      A disk containing all tags from Autopsy Software.

   Network Card
      A hardware component that connects a computer to a network.

   Wireshark PCAP format
      A specific format used to capture and save network traffic.

   Memory Dump
      The recorded state of the working memory of a computer program at a specific time.

   ISO Management
      The handling of ISO files, which are typically used for optical disk images.

   Snapshot Management
      The control and management of VM snapshots.

   C2C (Command and Control) client
      A centralized computer that issues commands to a botnet (a group of private computers infected with malicious software) and receives reports back.

   TTPs (Tactics, Techniques, and Procedures)
      Patterns of activities or methods associated with a specific threat actor or group of threat actors.

   Autopsy ForensicVM plugin
      A specific plugin for the Autopsy framework that aids in the forensic analysis of VMs.

   Autopsy framework
      A platform used for conducting digital investigations, such as for analyzing disk images or VM files.

   Data source
      Specific input or evidence, such as a disk image or VM file, which will be analyzed within the forensic tool.

   Host configuration
      The settings that determine how the data source is treated or processed within a forensic analysis environment.

   Disk Image or VM File
      A type of data source that represents either a snapshot of a disk or a virtual machine image.

   Forensic image
      A digital copy of a device's storage, used for the purpose of forensic investigation.

   Sector size
      A fundamental unit of data storage on a disk, usually specified in bytes (e.g., 512 bytes).

   Python Ingest Plugin
      A plugin in Autopsy used to automate the ingestion of data from a data source.

   ForensicVM Client plugin
      A specialized tool within the Autopsy ForensicVM plugin suite that aids in the forensic analysis of virtual machines.

   ForensicVM Loader
      Part of the ForensicVM toolset that initializes the forensic analysis environment for VM analysis.

   ForensicVM
      A comprehensive project designed to assist forensic investigators in the virtualization of forensic images.

   ForensicVM client
      An Autopsy plugin, forming one of the two primary components of the ForensicVM project.

   Autopsy
      A platform or tool used for digital forensics investigations.

   ForensicVM server
      The main backbone of the ForensicVM system, developed using Django and Python, it facilitates the functionalities of the ForensicVM.

   Django
      A high-level Python web framework, promoting rapid development and pragmatic, clean design.

   Python
      A high-level programming language known for its clear syntax and readability.

   Debian 11
      A specific version of the Debian operating system. Recommended for installing the ForensicVM server.

   Bare metal server
      A physical server dedicated to a single tenant or purpose.

   Hypervisor
      A virtual machine monitor or VMM that creates and runs virtual machines.

   Debian 11 (Bullseye)
      An operating system release that ForensicVM supports.

   64-bit multi-core processor
      A type of processor with multiple cores that can process 64-bit data chunks simultaneously. It's recommended for ForensicVM to ensure optimal performance, especially for complex tasks.

   RAM
      Random Access Memory. It's a type of computer memory used for temporary storage and quick access. ForensicVM requires a minimum of 16 GB RAM, but 32 GB or more is recommended for efficient virtualization of forensic images.

   NVMe
      Non-Volatile Memory Express. A protocol developed for SSDs to exploit the full potential of high-speed PCI Express storage devices.

   SSD
      Solid State Drive. A storage device that uses integrated circuit assemblies to store data persistently, typically using flash memory.

   RAID 10
      A type of RAID (Redundant Array of Independent Disks) configuration that combines mirroring and striping to protect data. It's recommended for storing forensic images in ForensicVM.

   Gigabit connection
      A network connection that offers speeds of up to 1 gigabit per second.

   SSH
      Secure Shell. A cryptographic network protocol used for secure data communication and server administration.

   HP ILO
      Integrated Lights-Out. A remote management tool used for server administration.

   QEMU
      Quick Emulator. An open-source hypervisor that performs hardware virtualization. ForensicVM uses QEMU to create a new forensic hypervisor server.

   root privileges
      The highest level of access rights on a system, allowing full control over all functions and files.

   Windows 10 or later
      A version of the Microsoft Windows operating system. ForensicVM supports Windows 10 and its successors for running the Autopsy plugin.

   Autopsy 4.20 or later
      A version of the digital forensics platform and graphical interface. ForensicVM requires at least version 4.20 for compatibility.

   64-bit multi-core processor
      A type of processor with multiple cores that can process 64-bit data chunks simultaneously, ensuring optimal performance for ForensicVM.

   RAM
      Random Access Memory. ForensicVM requires a minimum of 16 GB RAM for efficient operation. The Autopsy documentation suggests that the software can use up to 4GB of RAM, not including the additional memory the Solr text indexing server might use.

   Nvme
      Non-Volatile Memory Express. A modern protocol developed for SSDs to take advantage of high-speed PCI Express storage devices.

   SSD
      Solid State Drive. A faster type of storage device compared to traditional HDDs, beneficial for speeding up acquisition processes.

   1980x1080 resolution
      A specific pixel count for display screens. This resolution is recommended to ensure a clear and detailed view of the ForensicVM interface.

   Autopsy 4.20
      A specific version of the digital forensics software that is necessary for compatibility with the ForensicVM plugin.

   readonly windows shares
      Network-shared folders in the Windows operating system that do not allow modifications to the shared files. The ForensicVM plugin may create such shares and therefore requires specific permissions.

   AutopsyVM client plugin
      A software extension for the Autopsy digital forensics platform, which enables advanced functionalities specifically for ForensicVM.

   ForensicVM.exe
      The setup file responsible for installing the AutopsyVM client plugin on a user's system.

   Plugin Location
      The directory or file path where the AutopsyVM client plugin will be installed on your computer.

   Data source
      A reference or connection to data that Autopsy uses to gather evidence, such as forensic images.

   Disk Image
      A digital copy or replica of a physical disk. In the context of ForensicVM, a forensic image is used as a source for virtualization.

   forensicVM Client plugin
      The component of ForensicVM that is integrated within Autopsy to assist in processing and converting forensic images.

   API key
      A code passed in by computer programs to identify the calling program. It grants access to a service, in this case, the ForensicVM server.

   SSH (Secure Shell)
      A cryptographic network protocol used for operating network services securely over an unsecured network.

   Windows Share
      A feature in the Windows operating system that allows files and folders to be shared over a network.

   Forensic SSH Server Redirection
      A method used by ForensicVM to safely access Windows shared folders over the internet via a reverse SSH connection.

   Reverse SSH connection
      A technique where an SSH connection is initiated from a remote machine to the user's machine, essentially reversing the typical connection direction.

   Firewall
      A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security policies.

   Getting Started
      The initial section to acquaint yourself with the basics of ForensicVM.

   ForensicVM
      A forensic virtual machine used to convert forensic images for detailed analysis.

   Autopsy Software
      The software in which the ForensicVM Client Plugin runs.

   Installation and Setup
      Steps necessary to install and prepare ForensicVM for use.

   ForensicVM Client Plugin
      The main program interface of ForensicVM that runs in Autopsy Software.

   Autopsy ForensicVM Client Plugin: A Comprehensive Interface Guide
      A detailed guide describing the Autopsy ForensicVM Client Plugin's functionalities and operations.

   Main Toolbar Overview
      A description of the primary toolbar on the Autopsy ForensicVM Client Plugin.

   Virtualize Tab
      The main tab within the toolbar that provides access to core ForensicVM operations.

   Autopsy Case
      Displays Autopsy case details, including existing case tags and the generated unique UUID.

   Output Console
      A console that captures all system messages and is instrumental for debugging.

   Secondary Toolbar Overview
      An overview of the secondary set of tools in the Autopsy ForensicVM Client Plugin.

   Main Panel Overview
      A detailed breakdown of the main display area based on the selected tab option.

   Notification Area
      A designated area on the interface for system notifications, warnings, and error messages.

   Convert Forensic Image to VM
      Options that facilitate transforming the forensic image into a forensic virtual machine.

   VM Control
      Options to manage the basic operations of the forensic virtual machine.

   Screenshot Management
      Tools to capture and manage screenshots during forensic investigations.

   Memory Dump
      Tools to engage with the active memory data of the forensic virtual machine.

   Tools
      Additional utilities for forensic operations within the ForensicVM interface.

   Network
      Options to manage network settings and operations for the ForensicVM.

   ForensicVM Webscreen Console
      An interactive console providing access to the virtual screen of the remote ForensicVM.

   Webscreen Console Main Area
      A description of the main area in the ForensicVM Webscreen Console.

   ForensicVM Webscreen Console Control Toolbar
      A detailed overview of the Control Toolbar in the ForensicVM Webscreen Console.

   Adjusting Screen Scaling: Local Scaling
      Steps to optimize the viewing experience within the webscreen console.

   ForensicVM Server Web Control Interface
      A web interface designed for remote forensic investigators to collaborate and control the ForensicVM.

   ForensicVM
      A tool designed to simplify the digital forensics investigation process by allowing the virtualization and management of forensic images.

   Client
      Provides a user-friendly interface for managing forensic images. It allows users to create, run, and decommission instances as per their needs.

   Hypervisor
      Responsible for the execution of virtualized forensic images. Manages resources and ensures isolation between different instances.

   Forensic Image
      A digital snapshot or copy of a storage device, preserving both the structure and content. It's crucial for digital forensic investigations.

   Interface
      The user-friendly platform of ForensicVM that presents various features and tools systematically.

   Autopsy Interface
      The interface from which features tailored to aid forensic analysts can be accessed.

   Plugin
      Extensions that provide specific functionalities to ForensicVM. The plugin architecture fosters community involvement and functionality expansion.

   Memory Dump
      A snapshot of the content of computer memory. Used in forensic analysis to review the state of the system at a particular time.

   Netdata
      A tool for real-time health monitoring and performance troubleshooting for systems.

   Wireshark
      A network packet analyzer. It captures network packets in real-time and displays them in human-readable format.

   WebShell
      A script that can be uploaded to a web server to enable remote administration of the machine.

   Password Administration
      Tools or methods to reset forgotten passwords or generate new administrator accounts.

   Hibernate File Management
      Tools or methods to manage or remove hibernation files.

   Data Extraction and Analysis
      Tools or functionalities that help to extract and analyze data from a forensic image.

   Autopsy
      An open-source digital forensics platform used for conducting digital investigations.

   Autopsy ForensicVM plugin
      A plugin designed to enhance the capabilities of Autopsy by allowing users to process and analyze virtual machine images.

   Wizard Interface
      A user-friendly interface in software that guides users through a process step by step.

   Case
      A specific digital forensic investigation project in Autopsy that may contain one or more data sources.

   Case Information
      Metadata associated with a case, including its name and other optional details.

   Host
      In the context of Autopsy, refers to a machine or system from which data is being collected or investigated.

   Data Source
      An entity from which digital evidence is extracted. In this context, it refers specifically to disk images or virtual machine files.

   Disk Image
      A bit-by-bit copy of a physical disk, often used in digital forensics to preserve the state of a drive.

   VM File (Virtual Machine File)
      A file representing a virtual machine, which contains an OS, applications, and data, and can be executed on a hypervisor.

   Forensic Image
      A digital snapshot or copy of a storage device, preserving both the structure and content.

   Time Zone
      A region that observes a uniform standard time for legal, commercial, and social purposes.

   Sector Size
      The smallest addressable unit on a disk.

   Python Ingest Plugin
      A plugin in Autopsy used for data ingestion and is written in Python.

   ForensicVM Client Plugin
      The specific plugin in Autopsy that facilitates the analysis of VM images.

   Data Source Processing Progress
      A visual representation, usually a progress bar, showing the ongoing processing of a data source.

   ForensicVM Loader
      A component of the ForensicVM plugin responsible for initializing and setting up the environment for VM analysis.

   Autopsy ForensicVM Plugin
      A tool used for VM forensic analysis and integration within the Autopsy framework.

   Direct Copy to Server
      A method that duplicates the forensic image, creating a new forensic virtual machine on the server. 

   Link Creation
      A method where a link is established between the local forensic image and a new VM on the server.

   forensicVM
      Forensic Virtual Machine created for investigations.

   SSH Connection
      Secure Shell connection; a cryptographic network protocol for secure data communication.

   samba CIFS share
      A type of shared resource that can be accessed by other computers. Known as Windows share.

   qcow2 format
      A popular disk image format used in KVM virtualization.

   KVM
      Kernel-based Virtual Machine, a virtualization infrastructure for the Linux kernel.

   Fallback Conversion
      A backup method of conversion for unidentified OS.

   MS-DOS Command Window
      A command-line interface available in older versions of Windows.

   KVM drivers
      Drivers optimized for KVM virtualization.

   ForensicVM Web Screen Interface
      A web-based interface that lets users interact with the forensicVM directly.

   Autopsy ForensicVM Plugin
      A tool or extension used for forensic investigations within the Autopsy framework.

   Autopsy Plugin
      A tool or extension used for forensic investigations.

   Blue Screen of Death
      A colloquial term for a Windows system crash.

   Command Line Window
      A windowed interface for command-line interactions.

   Direct Copy to Server
      A method that duplicates the forensic image, creating a new forensic virtual machine on the server.

   Fiber Optics
      A type of high-speed internet connection.

   ForensicVM
      Forensic virtual machine.

   Link Mode
      A specific mode in which a forensic image is linked, rather than copied, to the forensicVM.

   Login Button
      A button clicked after entering username and password to gain access to the web interface.

   Main Plugin Interface
      A location from where the forensicVM can be initiated.

   Open ForensicVM
      An option/button to interact with the forensicVM's graphical interface.

   Shutdown Button
      A button in the Autopsy Plugin used to power off the forensicVM.

   Start Button
      A button used to initiate the forensicVM.

   Stop Button
      A button in the Autopsy Plugin used to halt the forensicVM.

   Web Interface
      An interface accessible via a web browser where users can control the forensicVM.

   Web Remote Screen
      A specific section of the web interface tailored for remote access.

   Autopsy Plugin Interface
      The UI within the Autopsy framework that provides options to manage the forensicVM.

   Browse ForensicVM
      Accessing and navigating the forensic virtual machine using interfaces like web browsers.

   Control
      A UI element, such as a button, that provides management capabilities (e.g., "Start," "Stop," "Reset") for the forensicVM.

   Forensic Image
      A digital snapshot or representation of data, often used for forensic investigations.

   ForensicVM Main Screen
      The primary interface of the forensic virtual machine when accessed via the web.

   ForensicVM Remote Screen Interface
      A display of the forensicVM as seen when accessed remotely, especially through web interfaces.

   Main Web Interface
      The primary browser-based interface for managing and interacting with the forensicVM.

   Open ForensicVM
      An action or option to access the forensicVM's main display, either through the Autopsy plugin or web interface.

   Open ForensicVM on the Main Interface
      The process or action of accessing the forensicVM directly through the Autopsy plugin interface.

   Plugin Interface
      The user interface provided by a software plugin, such as the one in Autopsy for the forensicVM.

   Web Interface URL
      The web address used to access the forensicVM's browser-based interface.

   Deactivate
      The process of shutting down or turning off a virtual machine, making it inactive.

   Main Plugin Interface (Shutdown)
      The primary UI within the Autopsy framework that offers options to shut down the forensicVM.

   Shutdown Button
      A UI control present on various interfaces that, when pressed, initiates the process to shut down the forensicVM.

   Shutdown Icon
      A graphical representation or symbol indicating the control to shut down the forensicVM.

   Shut Down VM on the Web Interface
      The method of deactivating the forensicVM directly from the web-based interface.

   Shut Down VM on the Web Remote Screen
      The method of shutting down the forensicVM when accessing remotely via the web.

   Web Remote Screen (Shutdown)
      A method to shut down the forensicVM when accessed remotely, offering flexibility for those working from distant locations or specific service interfaces.

   forensicVM
      A specialized virtual machine tailored for forensic purposes.

   Main Plugin Interface
      The primary user interface within a specific framework, in this context, used for managing the forensicVM.

   Shutdown Button
      A user interface control designed to initiate the process to deactivate and shut down the forensicVM.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It can be accessed after logging in.

   Web Interface
      The web-based platform from which users can manage and control the forensicVM. It offers different functionalities including shutting down the machine.

   Deactivate
      The act of turning off or shutting down the forensicVM, making it non-operational.

   Stop Button
      A user interface control designed to initiate the process to halt and stop the forensicVM.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It can be accessed after logging in.

   Web Interface
      The web-based platform from which users can manage and control the forensicVM. It offers different functionalities including stopping the machine.

   Halt
      The act of temporarily pausing or stopping the operations of the forensicVM without fully shutting it down.

   Reset
      The act of immediately rebooting the forensicVM, similar to a hard restart. It brings the machine back to its initial or default state without shutting it down completely.

   Main Plugin Interface
      The primary user interface within a specific framework, used for managing and controlling the forensicVM.

   Reset Button
      A user interface control designed to immediately reboot the forensicVM, bringing it to its default or initial state.

   Web Remote Screen Interface
      A web-based interface allowing users to remotely control and manage the forensicVM. It provides options to reset the machine, among other functionalities.

   Web Interface
      A web-based platform through which users can manage, control, and reset the forensicVM. It is accessible through a browser and might be preferable for remote operations or specific service interfaces.

   Immediate Reboot
      A rapid restart of the forensicVM without fully shutting it down. This is especially useful in scenarios requiring quick troubleshooting, testing, or managing different VM states.

   forensicVM
      A specialized virtual machine tailored for forensic purposes.

   Autopsy
      A digital forensics platform used for analyzing, managing, and reporting digital evidence.

   Screenshot
      A digital image that captures the contents of a computer screen, often used for documentation, analysis, or reporting purposes.

   Web Screen Interface
      A web-based platform through which users can interact with and manage the forensicVM.

   ZIP File
      A file format that allows for lossless data compression. It can contain multiple files or folders compressed into a single file.

   Save Screenshots Button
      A button in the interface that initiates the process of saving captured screenshots.

   Save As Dialogue
      A dialog box in software that prompts the user to specify the location and name of a file before saving it.

   Download Progress
      An indicator that displays the current status of a download operation.

   Logical Files
      A type of data source in Autopsy representing non-physical files, often used for importing various types of digital data.

   Picture Analyser Plugin
      A plugin in Autopsy used to analyze and manage pictures or images.

   Tagging
      The act of marking or labeling a specific item (like a screenshot) for identification, organization, or further analysis.

   Import
      The act of bringing data into a software platform (like Autopsy) from an external source.
    Memory Dump
        Refers to the process of capturing the content of a computer’s memory (RAM) at a specific moment in time.

    Security Analysis
        In cybersecurity, it involves using memory dumps to uncover malware behavior, detect hidden processes, analyze injected codes, and assess user credentials.

    Forensic Analysis
        Using memory dumps in digital forensics to reconstruct events, recover data, and analyze user and system interactions.

    Legal Evidence
        In legal proceedings, memory dumps might provide evidence related to computer usage, unauthorized access, and intellectual property theft.

    Autopsy
        A digital forensics platform used to conduct disk forensics and post-mortem analysis.

    Volatility
        An open-source memory forensics framework.

    Rekall
        A memory forensics toolkit.

    WinDbg
        Microsoft’s debugger used for debugging Windows applications and analyzing memory dumps.

    Magnet RAM Capture
        A free tool designed to capture physical RAM.

    FTK Imager
        A product by AccessData, used for capturing and analyzing memory dumps.

    MoonSols DumpIt
        A tool for creating memory dumps from Windows systems.

    Redline
        A tool provided by FireEye offering advanced memory and file analysis capabilities.

    GRR (Google Rapid Response)
        An incident response framework that includes memory analysis capabilities.

    Belkasoft Evidence Center
        A software solution that includes the ability to analyze computer memory.

    X-Ways Forensics
        A commercial forensic software with strong memory analysis features.

    Forensic Virtual Machine (VM)
        A digital environment replicated from a forensic image that serves as a snapshot of a system at a specific point in time.

    Immutable Record
        A non-alterable and chronological documentation, especially in the form of a video, that captures every action and finding during an investigation.

    Transparency and Accountability
        The assurance that the forensic process is done ethically and without tampering, as demonstrated by a detailed log such as a video recording.

    Legal Compliance
        Adhering to standards and requirements established by legal authorities, ensuring the chain of custody is maintained.

    Chain of Custody
        The chronological documentation or paper trail, showing the seizure, custody, control, transfer, analysis, and disposition of physical or electronic evidence.

    Autopsy Software
        A digital forensics platform utilized for disk forensics and post-mortem analysis.

    Video Recording Sound
        Refers to the audio component of a video recording. In the context provided, the current VM does not support audio capture, though it is recognized as an important feature for some investigations.

    Ingest Plugins
        Plugins or modules in forensic software that are used to process and analyze specific types of data or evidence.

    Tagging
        The process of marking or labeling a piece of evidence or finding with a specific tag or label to easily categorize, search, or identify it later.

    Third-Party Tools
        Software or utilities that are not part of the original package or platform but can be integrated or used alongside it for additional functionalities.

    Evidence Disk
        An automatically generated drive that appears during the conversion of a forensic image to a ForensicVM. It contains directories named after Autopsy tags and serves as a container for evidence related to each tag.

    ForensicVM
        A virtual machine environment tailored for forensic analysis. It is derived from a forensic image and is used for systematic investigations without compromising the original data.

    Autopsy Tags
        Markers or labels within the Autopsy forensic software that aid in categorizing and organizing evidence. They are reflected as directories in the evidence disk.

    Plugin
        Software components that add specific features to an existing computer program. Within the context, plugins in Autopsy can help in functions such as creating new user credentials or resetting existing ones.

    Forensic Administrator User
        A user profile with elevated privileges, potentially created for the purpose of a forensic investigation, to ensure unrestricted access to required data.

    BitLocker Drive
        A drive encryption feature integrated into the Microsoft Windows operating system. In the provided context, the entire encrypted BitLocker drive is showcased being transferred for forensic analysis.

    Ubuntu 22.10
        A version of the Ubuntu operating system. Ubuntu is an open-source software platform that runs everywhere from the PC to the server and the cloud.

    Evidence Disk
        The specific drive or storage area where collected forensic evidence is saved. It is often labeled as “possible evidence”.

    File Explorer
        A graphical user interface (GUI) component that lets users manage and view files. It is used to navigate and identify the evidence disk.

    Autopsy Tags
        Markers or labels within the Autopsy forensic software that help in organizing evidence into specific categories. These tags are represented as folders on the evidence disk.

    Hash Dump File
        A file that contains hashed representations of data. In the context, it is identified as potential evidence.

    Meterpreter
        A type of payload in the Metasploit framework that provides an investigator with a command line interface to the targeted system. In the context, its deployment is considered as potential evidence.

    ForensicVM
        A virtual machine environment tailored for forensic investigations. It's essential to manage its operations correctly to preserve the integrity of the evidence.

    Power Off/Log Out Option
        An option in operating systems (like Ubuntu 22.10) that allows users to either shut down or log out of their accounts. Proper shutdown is recommended to ensure the integrity of collected evidence.

    Autopsy
        A digital forensics platform used for analyzing and managing forensic data.

    qcow2
        A disk file format commonly used in QEMU, a free and open-source hardware virtualization solution.

    vmdk
        A disk file format used for virtual appliances developed for VMware products.

    Autopsy ForensicVM plugin
        A plugin within the Autopsy platform tailored to manage and interact with a Forensic Virtual Machine (VM).

    forensicVM
        A virtual machine specifically designed or purposed for forensic investigations.

    Import Evidence Disk
        A function or feature that allows users to introduce an evidence disk into the analysis environment.

    Windows Explorer
        The default file manager in Microsoft Windows operating systems that provides a graphical user interface for accessing the file system.

    Save As Dialog
        A prompt or interface in software applications that lets users specify the name and location of a file they wish to save.

    Data Source
        Refers to a repository or a location from which data is acquired. In the context of Autopsy, it refers to the origin or source of forensic evidence.

    VM Image
        A virtual disk image, which contains a virtual system's disk data, used for creating replicas of or taking snapshots of original virtual disks.

    Plugins
        Modular software components that add specific abilities to a larger software application. In the Autopsy context, they're used to enhance or extend functionality.

    Notable Item Tag
        A label or marker in Autopsy, used to identify and categorize significant pieces of evidence or data points during forensic analysis.

    Autopsy
        A digital forensics platform designed for analyzing and managing forensic data.

    Tag
        A label or marker within Autopsy used to identify and categorize data points or items of interest during forensic analysis.

    Ingest Modules
        Modules in Autopsy that perform data extraction, analysis, and organization tasks automatically for the investigator.

    ForensicVM Client Plugin
        A specific plugin within Autopsy tailored for managing and interacting with a Forensic Virtual Machine (VM).

    forensicVM
        A virtual machine purposed for forensic investigations.

    hibernation
        A power-saving mode for computers. In Windows, when the system goes into hibernation, it saves the current state of the system (including open applications and documents) into the hibernation file and shuts down, allowing for a faster start-up later.

    evidence.vmdk disk
        A specific format of a virtual disk image used to store forensic evidence in the context of Autopsy and VMs.

    Recreate Evidence Disk
        An action that leads to the deletion and fresh generation of the evidence disk within the Autopsy environment.

    Confirmation Dialog
        A prompt or interface that seeks affirmation from a user for a potentially critical action.

    ForensicVM
        A virtual machine purposed for forensic investigations.

    Delete VM Button
        A designated button within the ForensicVM interface or related software used to initiate the deletion process of the virtual machine.

    Confirmation Popup
        A user interface element that appears to ensure that the user wants to proceed with an action, in this case, the deletion of the ForensicVM. 

    UUID (Universally Unique Identifier)
        A 128-bit number used to uniquely identify some object or entity on the Internet. In this context, it identifies the specific ForensicVM instance that was deleted.

   forensicVM
        A specialized virtual machine tailored for forensic investigations, often having a network card disabled by default for security reasons.

   Network Card
        A hardware component or a virtual representation that allows computers to connect to a network.

   Firewall
        A system or component designed to block unauthorized access, allowing only permitted communications to pass.

   Wireshark pcap file
        A specific file format used to capture and store network packets for later analysis using tools like Wireshark.

   Autopsy ForensicVM Client Plugin Interface
        A specific interface within the forensic investigation software, Autopsy, tailored for managing virtual forensic machines.

   Web Screen Interface
        An interface within the forensicVM that provides access to various settings including network configurations.

   Panel Opener
        An interface element that reveals various options within the forensicVM.

   Network Troubleshooter
        A built-in Windows tool designed to diagnose and fix common network issues.

   IP Conflict
        Occurs when two or more devices or components on the same local network claim to have the same IP address, leading to network malfunctions.

   Linux Terminal
        A command-line interface in Linux-based operating systems for executing commands.

   ifconfig
        A system administration utility in Unix-like operating systems to configure, control, and query TCP/IP network interface parameters.

   Cloud Services
        Platforms and applications that provide data and services over the internet, often requiring network access to retrieve data.

   Session Cookies
        Small pieces of data stored on a user's computer during a browsing session, often containing information about user preferences or authentication status.

   Disable Network Card
      The action of turning off the network card to halt all network communications for the forensicVM.

   Web Screen Interface
      An interface within the forensicVM that provides access to various settings including network configurations.

   Panel Opener
      An interface element within the forensicVM, used to reveal more options or configurations.

   Wireshark pcap Files
      A specific file format used to capture and store network packets for later analysis using tools like Wireshark.

   pcap.zip
      A compressed file containing Wireshark pcap files collected during the network card activity periods.

   7-zip
      A free and open-source file archiver, commonly used for compressing and decompressing files.

   Wireshark
      A network protocol analyzer tool, which captures and displays packets for detailed analysis.

   Traffic Analysis
      The process of intercepting and examining messages to deduce information from patterns in communication, endpoints, and more.

   Evidence Collection
      The process of gathering evidence, often digital, to support investigations and potentially use in court.

   Timestamps
      Digital records of specific times at which events occurred.

   Decoding Protocols
      The process of translating network data from a machine-based protocol into a format that is human-readable.

   Data Overload
      A situation where the amount of captured data is so vast that it becomes challenging to identify essential and relevant information.

   Tampered Data
      Information that has been intentionally altered or falsified to mislead or deceive.

   pcap Directory
      The directory or folder where pcap files, often extracted from the pcap.zip, are stored for analysis.

   Media Management in ForensicVM
      The procedure to navigate, upload, select, insert, eject, delete, and boot from ISO files within ForensicVM.
   
   ISO files
      Encapsulations of entire file systems used to house specialized forensic tools.
   
   Network Isolation
      A safety measure that eliminates the need for network connectivity to mitigate associated risks.
   
   Protective Shield
      The protection provided by ForensicVM’s virtual environment to the host system against potential threats.
   
   Evidence Preservation
      The safeguarding of the original state of evidence, reducing risks of contamination or alteration.
   
   Browse and Upload ISO
      The process to navigate the interface and upload essential ISO files to the ForensicVM environment.
   
   Select ISO / Web Select CD-ROM
      Instructions on choosing the appropriate ISO file or CD-ROM.
   
   List Remote ISO Files
      An overview of ISO files stored remotely on the ForensicVM server.
   
   Insert ISO / Web Insert CD-ROM
      Procedure to virtually insert an ISO file or CD-ROM for access within the ForensicVM environment.
   
   Eject ISO / Web Eject CD-ROM
      Guidance on ejecting a mounted ISO file or CD-ROM.
   
   Delete ISO
      Instructions to remove unwanted ISO files.
   
   Bootable Media
      Details about booting from an ISO or CD-ROM for specific forensic tasks.
   
   Autopsy ForensicVM Client Plugin
      A plugin in ForensicVM used for various operations, including ISO management.
   
   Media Panel
      An interface section in the Autopsy VM used to manage ISO files.
   
   Media Panel Separator
      A component in the ForensicVM Client Plugin to access the Media Panel.
   
   Media Control Modal Box
      An interface component used in the process of inserting or ejecting ISOs via the web interface.
   
   Control Bar icon
      An icon that reveals the tool panel in the ForensicVM's web interface.
   ISO
      An optical disc image containing the content from a CD, DVD, or Blu-ray Disc.

   Virtual CD-ROM Drive
      A simulated CD-ROM drive that can read ISO files as if they were physical discs.

   Possible Evidence virtual drive
      A dedicated virtual drive within ForensicVM designed to store potential pieces of evidence without contaminating the original data.

   Bootable Media
      Digital storage media, like an ISO, that contains a boot sector, allowing a computer to start up from it.

   BIOS
      Basic Input/Output System, a software that is built into the PC, and is the first code run by a PC when powered on.

   UEFI
      Unified Extensible Firmware Interface, a specification for the software program that connects a computer's firmware to its operating system.

   Boot Manager
      A software process that starts the operating system when the computer is powered on.

   UEFI QEMU DVD-ROM
      A UEFI-compatible DVD-ROM virtual device provided by QEMU, a hosted virtual machine monitor.

   ForensicVM
      A virtualized environment tailored for forensic investigations.

   Kali Linux Forensic Tools
      A set of forensic tools provided by the Kali Linux distribution.

   ISO
      An optical disc image that can be used to reproduce the content of a CD or DVD.

   Virtual CD-ROM drive
      A software representation of a CD-ROM drive that allows the mounting and reading of ISO files as if they were physical discs.

   Autopsy ForensicVM Client Plugin
      A software plugin for the Autopsy forensics platform that facilitates interaction with the ForensicVM environment.

   Web Screen Interface
      A web-based interface that provides access to various functionalities, including the ability to eject and manage media within the ForensicVM.

   Media Control Modal Panel
      A specific part of the web screen interface that provides controls for media management.

   Delete
      The action of permanently removing an item, in this context, an ISO file, from storage or memory.

   Media Panel
      A section within the Autopsy ForensicVM Client Plugin interface that allows users to manage different media files, including ISOs.

   Snapshots
      A feature in ForensicVM that captures and preserves the state of the system or evidence at a specific point in time. 

   Base Snapshot
      Often referred to as the 'first snapshot,' this represents the initial state of a system or piece of evidence, functioning as an untouched reference point.

   Digital Evidence
      Information stored or transmitted in binary form that might be relied upon in court.

   What-If Analysis
      A series of hypothetical scenarios in forensic investigations, where investigators simulate actions to test different hypotheses.

   Documentation and Chain of Custody
      A process to ensure that the evidence is genuine and reliable, maintained through a documented and unbroken sequence of possession or control.

   ForensicVM
      A virtual machine that offers tools and functionalities essential for digital forensic investigations.

   Autopsy ForensicVM Client
      The interface or platform from which forensic investigators access and manage the ForensicVM functionalities, including snapshot management.

   Snapshot Management
      A section or functionality within the ForensicVM or its client interface, where snapshots are created, viewed, and managed.

   List Remote Snapshots
      A feature that allows users to manually fetch and view the list of all snapshots associated with a ForensicVM from a remote server.

   Rollback
      The process of reverting the state of the ForensicVM to a previously taken snapshot.

   Danger Zone
      A section within the ForensicVM client interface dedicated to critical or potentially irreversible operations, such as deleting snapshots.

   Snapshot Deletion Interface
      An interface or prompt within the ForensicVM client that facilitates the process of deleting a snapshot.

   Plugins
      Serve as a vital component of the forensicVM, enabling forensic investigators with capabilities to bypass protections in locked forensicVM machines.

   Authentication Bypass Features
      A suite of plugins designed specifically to bypass various authentication measures.

   Add Windows Forensic Admin
      A plugin that creates a new Windows admin user with specific credentials. The user belongs to the “Administrator” group.

   Add Linux Forensic Admin
      A plugin to create a new Linux user with 'sudo' permissions.

   Patch Accessibility
      A strategic patch enabling the invocation of a system-level cmd.exe prompt by pressing the shift key five times on the Windows login screen.

   Bypass Windows Password
      A plugin that patches the “ntlmshared.dll” file, allowing for the bypass of Windows authentication.

   Additional Security Bypass Features
      Plugins designed to bypass other security measures apart from authentication.

   Disable Windows Defender and Firewall
      A plugin that disables both Windows Defender and the firewall.

   Reset Windows 2003 or XP Activation
      A plugin that resets activation for Windows 2003 or XP.

   BOOTFIX: Disable Driver Enforcement
      A utility that addresses challenges related to driver signatures.

   Browsing Available Plugins
      A process to view, manage, and deploy available plugins for ForensicVM using the Autopsy ForensicVM Client.

   Executing Plugins
      The process of running plugins on the ForensicVM.

   Pre-plugin Execution Recommendation
      A cautionary advice to capture a snapshot of the machine's state before initiating any plugin.

   Community Plugins Project
      An open initiative aiming to enhance ForensicVM functionalities through community contributions.

   Access the Project Repository
      The hosted project on GitHub where you can view, clone, or fork the ForensicVM Plugins repository.

   Contributing Code
      Steps to contribute developed plugins or improvements to existing ones.

   Feature Suggestions and Plugin Requests
      A method to contribute ideas for new plugins, features, or improvements without coding them.

   Fine-Tuning ForensicVM
      The process of making adjustments to various configuration parameters of a ForensicVM. This is done via a configuration file that is generated when a forensic image is converted into a ForensicVM.

   Configuration File
      A file that contains various parameters for the forensic virtual machine, such as memory size, attached disks, UEFI boot options, and more.

   Autopsy ForensicVM Client interface
      The software interface where users can adjust various parameters of the ForensicVM.

   Modifying Memory Size
      The process of adjusting the ForensicVM’s memory size within the “Fine-Tuning” section of the Autopsy ForensicVM Client interface.

   Setting the VM Date & Time
      A function that allows users to define the start date & time for the ForensicVM.

   WebShell for Remote Administration
      A tool based on the shellinabox project adapted into a Django application that facilitates enhanced remote server administration, offering secure root access to the server.

   shellinabox project
      An open-source project that enables users to access remote servers from a web browser using a web-based terminal emulator.

   Django application
      A web framework written in Python that allows for rapid web development.

   Accessing the WebShell
      Refers to the methods available for users to access the WebShell for remote administration.

   Autopsy ForensicVM Client Plugin
      A plugin interface through which one can access various tools, including the WebShell.

   Open ForensicVM WebShell button
      A button within the Autopsy ForensicVM Client Plugin that allows users to launch the WebShell in their default browser.

   ForensicVM Main Web Interface
      The primary interface of the ForensicVM, where users can navigate to various tools and features, including the WebShell.

   WebShell Interface
      The user interface that is presented upon accessing the WebShell, providing a direct and secure interaction with the server.

   Netdata
      A real-time monitoring tool that offers insights into server and application performance.

   Real-time Look
      Refers to Netdata's capability to update its insights every second.

   Alerts
      Notifications triggered when certain parameters exceed predefined limits.

   Easy-to-Read Charts
      Graphical representations provided by Netdata to display various metrics in a comprehensible manner.

   Installation
      The process of setting up Netdata on a system. For ForensicVM Server, Netdata comes pre-installed.

   Autopsy ForensicVM Client Plugin
      A plugin interface in ForensicVM from which users can access various tools, including Netdata.

   ForensicVM main web page
      The primary interface of the ForensicVM, through which users can navigate to different tools and features, including Netdata.

   CPU
      Central Processing Unit, a primary indicator of a server's processing capability. Netdata provides insights into its utilization.

   Memory
      RAM (Random Access Memory) usage and availability, tracked by Netdata.

   Disk Activity
      Indicates how actively a disk is being read or written to, monitored by Netdata.

   Network
      Pertains to data transmission rates and network activity.

   Set Your Alarms
      A feature in Netdata that allows users to customize alert thresholds based on their needs.

   Connect with Other Tools
      Refers to Netdata's integration capabilities, where it can relay alerts to other platforms such as Slack or Twilio.

   Booting without signed drivers
      Refers to the potential issue of a machine not booting when certain drivers, such as virtio drivers, are unsigned or possess an invalid signature for a given operating system.

   Advanced options in the Automatic Repair boot screen
      An option in the boot screen that provides advanced repair capabilities when facing boot-related issues.

   Troubleshoot
      A selection available during boot-up that aids in diagnosing and fixing issues that prevent the system from starting.

   Advanced options
      A deeper layer of settings, usually accessed after selecting "Troubleshoot", that offers more specific ways to address boot issues.

   Startup Settings
      An option within the "Advanced options" which allows changing the behavior of Windows during startup.

   Disable driver signature enforcement
      A startup option that allows Windows to bypass driver signature checks during boot, potentially enabling problematic or unsigned drivers to load.

   DEBUG: Remote ssh to folder
      A feature that provides a direct remote connection to the forensicVM, facilitating the editing of configuration files or control over its state.

   Autopsy ForensicVM Client Plugin
      A software interface that aids in accessing and controlling the forensicVM.

   Elevate to root permissions
      The act of gaining elevated system access rights, commonly achieved using the "su" command in Unix-like systems.

   Configuration file
      A file that stores settings and parameters that define how a software or system behaves.

   QEMU Documentation
      The official documentation for QEMU, a software that provides hardware virtualization.
