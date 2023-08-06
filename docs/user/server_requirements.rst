=============================
ForensicVM Server Requirements
==============================

To ensure that ForensicVM operates efficiently on your system, our server must meet or exceed the following requirements:

Server Requirements
###################

**Operating System**
********************

ForensicVM has been tested and supports the following operating systems:

- Debian 11 (Bullseye)

**Processor**
********************

- A 64-bit multi-core processor is recommended for optimal performance. This will facilitate smoother operation, particularly when managing complex tasks.

**Memory**
********************

- A minimum of 16 GB RAM is required. However, 16 GB or more is recommended to handle the simultaneous virtualization of forensic images. This ensures that multiple tasks can be performed concurrently without a loss in performance.

**Storage**
********************

- A minimum of 2 GB of free disk space is needed for the ForensicVM installation itself.
- Additional storage will be required for forensic images. The amount will depend on the size of the images you will be working with. At least 1 TB of disk space, configured in RAID 10, is recommended.
- The use of NVMe or SSD is not strictly necessary but is recommended, as it can significantly speed up the virtualization process.

.. IMPORTANT::
   Remember to account for the extra space needed for virtual :term:`ISO` CD-ROM or DVD with your own tools. These might require additional storage depending on your specific requirements.

**Networking**
********************

- A network connection is necessary, with at least a gigabit connection recommended. The conversion of forensic images to a virtual machine, the downloading of Wireshark files, videos, or evidence disks all exert significant pressure on the network. Therefore, utilizing a reliable internet service hosting with robust upload and download rates is crucial.

**Display**
********************

- No specific display requirements exist for the server. You only need SSH access or HP ILO or similar for server administration.

**Software Dependencies**
**************************

- The installation will handle dependencies automatically. A dedicated server with Debian Bullseye as bare metal is necessary. Dedicated hardware with virtualization support is essential. The installation will create a new forensic hypervisor server based on QEMU.

Additional Notes
********************

.. IMPORTANT::
   ForensicVM requires root privileges for installation and to execute specific high-privilege operations, such as converting forensic images to virtual machines, managing the ForensicVM lifecycle, and controlling various security and administrative functions within the system. These elevated permissions are essential in allowing the software to interact with core system components, manipulate disk images securely, and handle complex virtualization tasks. 


