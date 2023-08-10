Starting the Virtual Machine (VM)
==================================

Three ways to start the forensicVM
***********************************

There are three different ways to start the forensic virtual machine (forensicVM). These methods provide flexibility depending on your access level and location within the system interface:

1) Start ForensicVM in the Main Plugin Interface
-------------------------------------------------

To initiate the forensicVM from the main plugin interface, follow these simple steps:

   a) Locate the start button on the main interface as depicted in the figure below.

   .. figure:: img/start_vm_0001.jpg
      :alt: Start VM on the main interface
      :align: center

      Start VM on the main interface

   b) Press the start button to activate the virtual machine.

2) Start ForensicVM after Logging in to the Web Interface
---------------------------------------------------------

To start the forensicVM through the web interface after login, you need to:

   a) Open the login main page.

   b) Enter your username and password, and then click on the login button.

   .. figure:: img/start_vm_0002.jpg
      :alt: Login on the main web interface
      :align: center

      Login on the main web interface

   c) Once logged in, locate the start button for the selected forensicVM you wish to initiate.

   d) Press the start button to activate the virtual machine.

   .. figure:: img/start_vm_0003.jpg
      :alt: Start VM on the main web interface
      :align: center

      Start VM on the main web interface

3) Start ForensicVM on the Web Remote Screen
---------------------------------------------

Another option to start the forensicVM is from the web remote screen. This method may be preferred if you are working remotely or through a particular service interface:

   a) Navigate to the web remote screen.

   b) Locate the start button, as shown in the figure below.

   .. figure:: img/start_vm_0004.jpg
      :alt: Start VM on web remote screen
      :align: center

      Start VM on the web remote screen

   c) Press the start button to initiate the virtual machine.

These three methods ensure that you can initiate the forensicVM from various points in the system. 


Special case: Starting the forensicVM in link mode
***************************************************

**Precautions and considerations**:

When a forensic image is converted to a forensic virtual machine using the option "Virtualize b) Link to VM", it can on be started using the Autopsy Plugin. Some precautions must be taken to assure that a smooth virtual machine operation:

   ... Warning:: 
      1) Only start a linked the forensicVM using the Autopsy Plugin. Do not try to use the forensicVM web interface. It will not work.
      2) Use a stable internet connection, like fiber óptics. Connection failure will result in machine disk timeouts and possibily virtual machine blue screen of death.
      3) Do not close the command line window. This window needs to be open all times. Shutdown or stop the forensicVM using the "Stop" or "Shutdown" Autopsy Plugin buttons. Only this assures that there will be no problems resulting of zoombie mount points to your computer.

**Steps to start and stop or shutdown**:

1) Start ForensicVM in the Main Plugin Interface
   
   Press "Start" button to start the vm:

   .. figure:: img/start_vm_0001.jpg
      :alt: Change
      :align: center

      Change

   A popup message will appear indicating that the machine was started in "snap" or link mode:

   .. figure:: img/start_vm_0005.jpg
      :alt: Change
      :align: center

      Change

   A command line window will open. Minimize this window. DO NOT CLOSE IT! If you want to close the machine, please follow the steps bellow to ether stop or shutdown the forensicVM safely. 

   .. figure:: img/start_vm_0006.jpg
      :alt: Change
      :align: center

      Change

   Press the "Open ForensicVM" to open the web screen interface. This will allow you to interact with the machine:

   .. figure:: img/start_vm_0007.jpg
      :alt: Change
      :align: center

      Change

   The machine will open in the web interface. Now you can interact with the system normally.

   .. figure:: img/start_vm_0008.jpg
      :alt: Change
      :align: center

      Change

   The safe and only way to shutdown or stop the machine is to use the Autopsy Plugin buttons "shutdown" or "stop" 


   .. figure:: img/start_vm_0009.jpg
      :alt: Change
      :align: center

      Change



