===============================================
Computer Requirements to use the Autopsy Plugin
===============================================

To ensure that ForensicVM runs smoothly on your system, your computer and your server should meet or exceed the following requirements.


Computer Requirements
----------------------

Operating System
--------------------

ForensicVM was tested and supports the following operating systems:

- Windows 10 or later
- Autopsy 4.20 or later


Processor
--------------------

- A 64-bit multi-core processor is recommended for optimal performance.

Memory
--------------------

- A minimum of 16 GB RAM is required. From the oficial autopsy documentation website: "We recommend a minimum of 16GB of RAM. By default, Autopsy will use a maximum of 4GB of RAM (not including memory that the Solr text indexing server uses)."

Storage
--------------------

- A minimum of 300 mb of free disk space is needed for the ForensicVM plugin installation.
- Additional storage will be required for forensic images. The amount will depend on the size of the images you will be working with.
- The use of Nvme or SSD is not strictly necessary but recommend as it speeds up the aquisition processes.

Networking
--------------------

- A network connection is required for software updates and to access cloud-stored forensic images. Additionally, a robust internet connection with high upload speeds is necessary to expedite the virtualization process if there is a need to convert forensic images into forensic VMs.

Display
--------------------

- A display with a resolution of 1980x1080 or higher is recommended for the best experience. If possible use a two monitor setup; one for the Autopsy plugin, and the other for forensicVM server control.


Software Dependencies
--------------------

- Install Autopsy 4.20 or higher

Additional Notes
--------------------

.. IMPORTANT::
   ForensicVM plugin requires administrator or root privileges for installation and running certain high-privilege operations like creating readonly windows shares!


