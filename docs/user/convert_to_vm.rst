Convert Forensic Image to a Forensic Virtual Machine
=====================================================
There are two methods to convert a local forensic image to a remote forensic virtual machine on the server. The first method copys the fonsic image to a new 
forensic virtual machine on the server. The second method creates a link between the local forensic image to a new forensic image on the server.
The first method allows the full functionality of the forensicVM and is the recommended method for remote colaboration. The second method is faster since
the image does not have to be copied to the remote server. It allows a rapid convertion and preview, but the machine has to be started localy by the 
investigator - it can only be started in the Autopsy client plugin. It cannot be started on the web interface, since it needs to be linked to the original 
forensic image.


Method 1: Copy the local forensic image to a new forensic virtual machine on the server
****************************************************************************************

Method 2: Link the local forensic image to a new forensic virtual machine on the server
****************************************************************************************
