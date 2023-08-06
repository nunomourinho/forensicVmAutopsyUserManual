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

ForensicVM's interface is designed with usability in mind. It provides a clear view of the current state of your forensic images, including active instances, resource usage, and the status of any ongoing analysis tasks. It also provides easy access to ForensicVM's suite of analysis tools, making it simple to start investigating a forensic image.

Plugin Architecture
======================

ForensicVM supports a plugin architecture that allows developers from the community to extend its functionality. These plugins can interact with forensic images to perform tasks such as password reset, hibernation file removal, and data extraction. By allowing users to add new capabilities through plugins, ForensicVM becomes a versatile tool that can be customized to fit a variety of use cases.  
For more details, refer to the :ref:`plugin-documentation`.

.. toctree::
   :maxdepth: 1

   Plugin Architecture <plugin>


