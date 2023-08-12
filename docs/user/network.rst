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

To activate the network card on the forensicVM, there are two methods available. 
The first method involves using the Autopsy ForensicVM client plugin interface, 
and the second requires directly interacting with the system through the network 
icon.

Using the Autopsy ForensicVM Client Plugin Interface
******************************************************

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

.. danger::

   Activating the network card carries certain risks, especially on a forensic virtual machine that may be examining potentially compromised data or systems. Always ensure you're aware of the risks before enabling network access.
