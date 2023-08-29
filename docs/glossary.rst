Glossary
=========

.. glossary::

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

