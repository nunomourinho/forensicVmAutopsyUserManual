=====================
Installation and Setup
=====================
This section will guide you through the steps necessary to install and set up ForensicVM on your system.

AutopsyVM Client Plugin Installation
####################################

Introduction
************

The AutopsyVM client plugin is a valuable addition to Autopsy, enhancing its functionality for digital forensics. Follow the steps below to install the plugin.

Step 1: Download ForensicVM.exe Setup File
******************************************

Download the latest version of the ForensicVM.exe setup file from the [AutopsyForensicVM GitHub Releases](https://github.com/nunomourinho/AutopsyForensicVM/releases) page. Navigate to the "Assets" section and download the setup file.

Step 2: Run the ForensicVM.exe Setup
************************************

Run the ForensicVM.exe setup file to begin the installation process. The setup consists of four steps:

1. Welcome Screen: Displays an introduction to the installation process.
2. Component Installation: Proceed with the default settings. Do not make any changes.
3. Plugin Location: Specify the location where the AutopsyVM client plugin will be installed. Typically, this does not require any changes.
4. Install: Click the "Install" button to start the installation process.

Step 3: Complete the Installation
*********************************

Follow the on-screen instructions to complete the installation. Once the installation is finished, you can proceed with using the AutopsyVM client plugin in Autopsy.

Step 4: Verify the Installation
*******************************

To verify the successful installation of the AutopsyVM client plugin, open Autopsy and check if the plugin is available and functional.

Screenshots
***********

Here are the screenshots that illustrate the installation process:

.. raw:: latex

   \FloatBarrier

.. figure:: img/0001.JPG
   :alt: Welcome Screen
   :align: center

   Welcome Screen

.. raw:: latex

   \FloatBarrier

.. raw:: latex

   \FloatBarrier

.. figure:: img/0002.JPG
   :alt: Component Installation
   :align: center

   Component Installation

.. raw:: latex

   \FloatBarrier

.. raw:: latex

   \FloatBarrier

.. figure:: img/0003.JPG
   :alt: Plugin Location
   :align: center

   Plugin Location

.. raw:: latex

   \FloatBarrier

.. raw:: latex

   \FloatBarrier

.. figure:: img/0004.JPG
   :alt: Finish Screen
   :align: center

   Finish Screen

.. raw:: latex

   \FloatBarrier




Initial Setup
##############
After successfully installing ForensicVM one needs to configure the AutopsyVM plugin. The initial configuration is composed of the following steps:

Step 1: In Autopsy: Add a new data source to Autopsy. This new data source is the forensic image that we need to convert to a forensicVM
*****************************************************************************************************************************************
 #. Add datasource
 #. Specify a new hostname
 #. Next

 .. raw:: latex

    \FloatBarrier

 .. figure:: img/setup_0001.jpg
    :alt: Add data source
    :align: center
    :width: 500

    Add a new data source to Autopsy

Step 2: Select your Disk Image
******************************
 #. Select the option disk image or VM FIle
 #. Next

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0002.jpg
   :alt: Disk Image
   :align: center
   :width: 500

   Disk Image

.. raw:: latex

   \FloatBarrier

Step 3: Select your forensic image
***********************************
 #. Browse for your forensic image, select it
 #. Click Next


.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0003.jpg
   :alt: Forensic Image Selection
   :align: center
   :width: 500

   Forensic Image Selection

.. raw:: latex

   \FloatBarrier

Step 4: Run the ForensicVM client plugin
****************************************
 #. Deselect all other plugins
 #. Select the forensicVM Client plugin
 #. Click next

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0004.jpg
   :alt: Select data source
   :align: center
   :width: 500

   Select Datasource

.. raw:: latex

   \FloatBarrier

Step 5: Open your forensicVM Server web address in the admin. Ex: https://<ip-or-web>:port/admin
*************************************************************************************************
 #. Enter user and password
 #. Click the login button

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0005.jpg
   :alt: Configure inject
   :align: center

   Configure inject - Select ForensicVM Client plugin

.. raw:: latex

   \FloatBarrier

Step 6: Add  a new user
************************
 #. Enter user, password and password confirmation dialogues
 #. Click SAVE

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0006.jpg
   :alt: Add user
   :align: center
   :width: 500

   Add user

.. raw:: latex

   \FloatBarrier

Step 7: Add  a new api key to the user
***************************************
 #. Click the add button on the api keys
 #. Select the user
 #. Click the plus sign


.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0007.jpg
   :alt: Add API key to user
   :align: center
   :width: 500

   Add API key to user

.. raw:: latex

   \FloatBarrier

Step 8: Copy the user API key
******************************
 #. Select the newly created API key
 #. Press CTRL + C or copy it using the right mouse button and select copy

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0008.jpg
   :alt: Copy user api key
   :align: center
   :width: 500

   Copy user API key

.. raw:: latex

   \FloatBarrier

Step 9: Paste the user API key
*******************************
 #. Put the mouse on the Forensic API field
 #. Press CTRL + V or paste it using the right mouse button and select paste

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0009.jpg
   :alt: Past user API key
   :align: center
   :width: 500

   Paste the user API key

.. raw:: latex

   \FloatBarrier


Step 10: Fill and test the Forensic VM Server configuration
************************************************************
 #. Put the mouse on the Forensic VM server address. Fill in the information with your server address
 #. Click the Test Server Connection to test if API and server address are correct

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0010.jpg
   :alt: Fill and test forensic VM
   :align: center
   :width: 500

   Fill and test forensic VM Server Configuration

.. raw:: latex

   \FloatBarrier

Step 11: Forensic VM Server configuration test success
*******************************************************
 #. If all pieces of information are correct and if the server is online you should see a connected successfully dialog box.
 #. If there are any problems, you should see a red error dialogue. Please check and correct the field values.

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0011.jpg
   :alt: Forensic VM Server Connection test
   :align: center
   :width: 500

   Forensic VM server connection test

.. raw:: latex

   \FloatBarrier

Step 12: Configure Windows Share over Forensic SSH Server Redirection
**********************************************************************
 The way that forensicVM Server access the forensic images is by making a reverse ssh connection to your computer and accessing a local share via the internet. The reverse ssh connection is in need to make a safe Windows share access. You should configure now the forensicVM server SSH address and port number:
 #. Please fill in the SSH Server Address and port number.
 #. Press the button to copy the ssh key to the server

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0012.jpg
   :alt: Configure and copy SSH key to the server
   :align: center
   :width: 500

   Configure and copy the ssh key to the server

.. raw:: latex

   \FloatBarrier

Step 13: Windows Share over Forensic SSH copy ssh key status
*************************************************************
 #. If the configuration is correct you should see a dialog stating that a Public key added to authorized keys
 #. If not, you should see an error dialogue or a dialogue stating that the ssh public key is already present on the remote server

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0013.jpg
   :alt: Copy ssh key status
   :align: center
   :width: 500

   Copy ssh key status

.. raw:: latex

   \FloatBarrier


Step 14: Testing Windows Share over Forensic SSH Server Redirection
********************************************************************
 #. Click the Test Ssh connection button
 #. If the configuration is correct you should see a dialog stating that the connection was successful
 #. If not, you should see an error dialogue


.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0014.jpg
   :alt: Test Windows share over ssh
   :align: center
   :width: 500

   Test windows share over ssh

.. raw:: latex

   \FloatBarrier

Step 15: Configure windows share over ssh
******************************************
 #. Press the Autofill info button to autofill the Windows share information with the Share login and local and the remote path to share. This info is extracted from the forensic image's current path.

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0015.jpg
   :alt: Configure windows share over ssh
   :align: center
   :width: 500

   Configure windows share over ssh

.. raw:: latex

   \FloatBarrier

Step 16: Configure the share login and the share password
**********************************************************
 #. The share login and share password is a Windows local user and is password. It does not need to be an Administrator account. It can be a regular user. It also does not need to exist, since it is created if it does not exist when the user presses the create share button.

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0016.jpg
   :alt: Configure the share login and the Share password
   :align: center
   :width: 500

   Share login and the share password configuration

.. raw:: latex

   \FloatBarrier

Step 17: Create Share Button
*****************************
 #. After filling in the share login and password please press the create share button.

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0017.jpg
   :alt: Create a share button
   :align: center
   :width: 500

   Create share button

.. raw:: latex

   \FloatBarrier


Step 18: Create a share Dialog
*******************************
 #. After pressing the create share button a command window will open. This will try to create the local user with the defined password. 

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0018.jpg
   :alt: Create share command window
   :align: center
   :width: 500

   Create a share command window

.. raw:: latex

   \FloatBarrier

Step 19: Testing the forensicVM image Windows share over ssh
*************************************************************
 #. Press Test Windows share button to test if it is possible to connect to the Windows share from the server using a reverse ssh connection. If all is ok you will be presented with a Windows alert stating that the connection was successful

.. raw:: latex

   \FloatBarrier

.. figure:: img/setup_0019.jpg
   :alt: Testing the forensicVM image Windows share over ssh
   :align: center
   :width: 500

   Testing the forensicVM image Windows share over ssh

.. raw:: latex

   \FloatBarrier

.. CAUTION::
   Ensure to use a secure Windows username and password for your share. Although this share is protected over the internet by your SSH private key, on the Windows network, your username and password could be a potential vulnerability. We recommend a dedicated, strong username and password for your share, which can be reused for multiple forensic image shares if necessary.

.. NOTE::
   Please configure your firewall to allow local access to your Windows shares. You can restrict the Windows share to be accessible only by your own computer. If needed, please seek assistance from your system administrator to perform this task.
   
