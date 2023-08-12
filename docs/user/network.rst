Managing the Network Card to Capture and Analyse Network Traffic
=================================================================

By default, the forensicVM initiates with its network card disabled. This design choice is deliberate, to minimize the potential risks of activating a network card on a possibly compromised virtual forensic machine. Activating such a network card could jeopardize not only your individual computer but the broader network environment.

For many forensic investigations, an active network connection is unnecessary. When evidence is solely contained within a local device, it's recommended to keep the network card deactivated. This approach ensures the machine's safe operation and the security of your enterprise network or domain.

However, in certain situations, there may be a need to activate the network card. For instance, when the forensic virtual machine is deemed safe and requires an internet connection to retrieve cloud-based data—data sourced from cached cloud access credentials like those from OneDrive, Google Drive, Nextcloud, OwnCloud, etc. In such cases, the forensicVM's network card can be enabled. This card has an 
inbuilt firewall designed to block access to identified local networks while permitting internet connections. Additionally, every time the network card is toggled on or off, all inbound and outbound traffic is recorded. This leads to the creation of a Wireshark pcap file for each activation and deactivation event.

.. danger::

   It's paramount to treat the activation of the network card as a method of last    resort. Alternatively, consider using a remotely hosted forensicVM server. The integrity of the firewall isn't foolproof, meaning there's always a risk that malicious software might infiltrate your network. Furthermore, a compromised machine could ping back to an attacker, potentially revealing your external IP address and inadvertently notifying a malicious actor that they are under active investigation!

Enable the Network Card
------------------------

To activate the network card on the forensicVM, there are two methods available. The first method involves using the Autopsy ForensicVM client plugin interface, and the second requires directly interacting with the web screen interface through the network icon.

Enable network card using the Autopsy ForensicVM Client Plugin Interface
**************************************************************************

**Activate Network Card Button**

1. Start the forensicVM machine.
2. Navigate to the Network Panel within the interface.
3. Look for the "Enable network card" button and click on it.

.. figure:: img/network_0001.jpg
   :alt: Enabling the network card through the Autopsy ForensicVM Client interface
   :align: center

   Enabling the network card through the Autopsy ForensicVM Client interface

**Confirmation of Network Card Activation**

After clicking the button, a popup window will appear to confirm the successful 
activation of the network card.

.. figure:: img/network_0002.jpg
   :alt: Confirmation popup for network card activation
   :align: center

   Confirmation popup for network card activation

Enable Network Using the Web Screen Interface
************************************************

Activating the network card can also be achieved via the Web Screen Interface. This method allows users to manage network settings without diving into the main software interface. Here's how to enable the network card using the Web Screen Interface:

**Activating Network through Web Screen Interface Steps**

1. Initiate the **Panel Opener (1)** to reveal the available options.
2. Locate and click on the **network icon (2)** to access network settings.
3. Identify and click the red button labeled **Enable network (caution) (3)** to activate the network card.

.. figure:: img/network_0003.jpg
   :alt: Network Using the Web Screen Interface 
   :align: center

   Steps to activate the network through the Web Screen Interface 

**Acknowledgement of Successful Activation**

Once the network card is activated, an orange notification will pop up at the top of the screen. This message serves to confirm that the network card has been successfully activated.

.. figure:: img/network_0004.jpg
   :alt: Notification of Success
   :align: center

   Notification confirming successful activation of the network card

.. danger::

   Always proceed with caution when enabling the network, especially on systems that are meant for forensic investigations or are potentially compromised. It's vital to ensure systems and network security and to be aware of the risks involved.
