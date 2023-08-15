=====================
Getting Started
=====================

.. warning::

   Author: Please update this! Make an program overview with screenshots with legends that show every function in a infographic

This section provides an overview of the initial steps to start using ForensicVM.

Installing ForensicVM
=========================

Before you can use ForensicVM, you must first install the software on your system. To do this, follow the steps outlined in the :ref:`Installation and Setup`.

Navigating the Interface
============================

Your first step is run the ForensicVM Client Plugin in Autopsy Software. The main interface will open. You manage this by reight clicking the datasource and choosing "Run Ingest Modules". After this it will open the main the Forensic Client Plugin main program interface.

.. figure:: img/infographics_0000.jpg
   :name: Change-me
   :alt: Change-me

   Change-me

Autopsy ForensicVM Client Plugin: A Comprehensive Interface Guide
------------------------------------------------------------------

The Autopsy ForensicVM Client Plugin serves as a pivotal hub for forensic analysts. This interface is designed for interactive engagement with forensic images, subsequently allowing users to transform these images into a forensic virtual machine (ForensicVM). Here's a breakdown of its primary functionalities:

Main Toolbar Overview (1)
===========================

1. **Configuration**:
    
    - Prior to exploring the main functionalities, it's paramount to configure the plugin's settings. This preliminary setup is generally executed during the :ref:`Installation and Setup`.

2. **Virtualize Tab**:
    
    This tab houses the primary operations. Specifically, users can:

    - **Control the ForensicVM**: Start, Stop, Shutdown, Reset, or Delete.
    - **Manage Media**: Organize manage media relevant to forensic analysis.
    - **Manage Plugins**: Run individual plugins.
    - **Handle Snapshots**: Capture and revert the ForensicVM to various states.
    - **Capture Screenshots**: Record specific instances or frames within the ForensicVM.
    - **Memory Management**: Generate and retrieve memory dumps, vital for observing real-time operations within the ForensicVM.
    - **Virtual Evidence Disk Management**: Import and regenerate the virtual evidence disk, accumulating all potential pieces of evidence.
    - **Network Management**: Toggle network cards on or off, and capture pcap (packet capture) files for granular network investigations.
    - **ForensicVM Customization**: Modify the starting date/time, reallocate memory, among other settings.
    - **Performance Analysis**: Employ Netdata for comprehensive metric analysis of the ForensicVM's operations.
    - **Troubleshooting**: Secure an SSH connection to the ForensicVM machine, connecting directly to its remote directory. Additionally, avail an equivalent webshell for an internet-based SSH interaction with the server.

3. **Autopsy Case**:
    
    - This tab displays the Autopsy case details, including the extant case tags (utilized for case folder creation) and the generated UUID. This UUID is unique and becomes the name for the foundational directory of the forensic virtual machine.

4. **Output Console**:
    
    - This console captures all system messages. It's a valuable tool for debugging or ascertaining the final state of operations.

5. **About**:

    - Contains copyright details pertaining to the ForensicVM Client.

Secondary Toolbar Overview (2)
===============================

1. **Media Management**:

    This tab gives access to the auxiliar virtualization functions:

    - **Media** - Manage media. Upload ISO files to the server, insert, eject and delete media.
    - **Plugins** - Select and run a plugin. Add new forensic administrators, bypass password, reset activation, bypass security protections to investigate user profiles.
    - **Snapshots** - Capture and revert the ForensicVM to various states.
    - **Finetuning** - Change memory size and set initial run date.

.. figure:: img/infographics_0001.jpg
   :name: Change-me
   :alt: Change-me

   Change-me


.. figure:: img/infographics_0002.jpg
   :name: Change-me
   :alt: Change-me

   Change-me

.. figure:: img/infographics_0003.jpg
   :name: Change-me
   :alt: Change-me

   Change-me

.. figure:: img/infographics_0004.jpg
   :name: Change-me
   :alt: Change-me

   Change-me

Next Steps
============

After familiarizing yourself with ForensicVM, you may want to explore more advanced topic. Refer to the respective sections in this documentation for more information.
