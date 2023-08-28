Starting the Virtual Machine (VM)
==================================

Three ways to start the forensicVM
***********************************

There are three different ways to start the forensic virtual machine (forensicVM). These methods provide flexibility depending on your access level and location within the system interface:

1) Start ForensicVM in the Main Plugin Interface
-------------------------------------------------

To initiate the forensicVM from the main plugin interface, follow these simple steps:

   a) Locate the start button on the main interface as depicted in the figure below.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0001.jpg
      :alt: Start VM on the main interface
      :align: center
      :width: 500

      Start VM on the main interface

   .. raw:: latex

      \FloatBarrier

   b) Press the start button to activate the virtual machine.

2) Start ForensicVM after Logging in to the Web Interface
---------------------------------------------------------

To start the forensicVM through the web interface after login, you need to:

   a) Open the login main page.

   b) Enter your username and password, and then click on the login button.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0002.jpg
      :alt: Login on the main web interface
      :align: center
      :width: 500

      Login on the main web interface

   .. raw:: latex

      \FloatBarrier

   c) Once logged in, locate the start button for the selected forensicVM you wish to initiate.

   d) Press the start button to activate the virtual machine.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0003.jpg
      :alt: Start VM on the main web interface
      :align: center
      :width: 500

      Start VM on the main web interface

   .. raw:: latex

      \FloatBarrier

3) Start ForensicVM on the Web Remote Screen
---------------------------------------------

Another option to start the forensicVM is from the web remote screen. This method may be preferred if you are working remotely or through a particular service interface:

   a) Navigate to the web remote screen.

   b) Locate the start button, as shown in the figure below.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0004.jpg
      :alt: Start VM on web remote screen
      :align: center
      :width: 500

      Start VM on the web remote screen

   .. raw:: latex

      \FloatBarrier

   c) Press the start button to initiate the virtual machine.

These three methods ensure that you can initiate the forensicVM from various points in the system. 

Special Case: Starting the ForensicVM in Link Mode
***************************************************

**Precautions and Considerations**:

When a forensic image is converted to a forensic virtual machine using the "Virtualize b) Link to VM" option, it can only be started via the Autopsy Plugin. Ensure that you adhere to the following precautions to guarantee a smooth operation of the virtual machine:

.. warning::
   
   1. Only initiate the linked forensicVM through the Autopsy Plugin. Avoid using the forensicVM web interface—it will be ineffective.
   2. Utilize a reliable internet connection, such as fiber optics. Any connection disruptions could lead to machine disk timeouts, and potentially the virtual machine encountering a "blue screen of death."
   3. Maintain the command line window in an open state. This window must remain open at all times. To power off or stop the forensicVM, use the "Stop" or "Shutdown" options in the Autopsy Plugin. This method ensures the prevention of lingering mount points on your computer, which could cause issues.

**Steps to Start, Stop, or Shutdown**:

1. **Activate ForensicVM in the Main Plugin Interface**:
   
   To initiate the VM, click the "Start" button.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0001.jpg
      :alt: Screenshot of the "Start" button in the main plugin interface.
      :align: center
      :width: 500

      The "Start" button in the main plugin interface.

   .. raw:: latex

      \FloatBarrier

   Following this action, a popup will inform you that the machine has launched in "snap" or link mode.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0005.jpg
      :alt: Popup indicating the machine's "snap" or link mode status.
      :align: center

      Machine's launch mode notification.

   .. raw:: latex

      \FloatBarrier

   Next, a command line window will manifest. While you should minimize it, it's crucial not to close it. If you need to shut down the machine, kindly adhere to the subsequent steps to safely halt or power off the forensicVM.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0006.jpg
      :alt: Command line window showing machine's process.
      :align: center
      :width: 500

      Command line window – important not to close.

   .. raw:: latex

      \FloatBarrier

   To interact with the machine through its graphical interface, hit the "Open ForensicVM" option.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0007.jpg
      :alt: "Open ForensicVM" button for graphical interaction.
      :align: center
      :width: 500

      "Open ForensicVM" button.

   .. raw:: latex

      \FloatBarrier

   This action will lead to the machine's manifestation within a web interface, allowing you to seamlessly interact with the system.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0008.jpg
      :alt: Web interface of the forensicVM.
      :align: center
      :width: 500

      ForensicVM web interface.

   .. raw:: latex

      \FloatBarrier

   It's imperative to note that the solitary and secure method to halt or power off the machine is by utilizing the "Shutdown" or "Stop" buttons available in the Autopsy Plugin.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/start_vm_0009.jpg
      :alt: Autopsy Plugin buttons for shutting down or stopping the machine.
      :align: center
      :width: 500

      Autopsy Plugin's control buttons.

   .. raw:: latex

      \FloatBarrier
