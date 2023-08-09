Convert Forensic Image to a Forensic Virtual Machine
=====================================================
There are two methods to convert a local forensic image to a remote forensic virtual machine on the server. The first method copys the forensic image to a new 
forensic virtual machine on the server. The second method creates a link between the local forensic image to a new forensic image on the server.
The first method allows the full functionality of the forensicVM and is the recommended method for remote colaboration. The second method is faster since
the image does not have to be copied to the remote server. It allows a rapid convertion and preview, but the machine has to be started localy by the 
investigator - it can only be started in the Autopsy client plugin. It cannot be started on the web interface, since it needs to be linked to the original 
forensic image.

Both methods to the following steps:
1. A ssh connection is made to the forensicVM server
2. This connection makes a reverse connection to a readonly samba cifs share - or windows share. This process makes possible to the server to connect to the windows share where the forensic image is present
3. The convertion process begins. The forensic image type is detected. The apropriated tool is choosen in the server to mount the forensic image to a virtual raw device, since that same images are spanned in multiple files
4. A first forensic image snapshot is created. This is the base snapshot that links the state to the forensic image virtual raw. It allows the instalation of drivers without changing the forensic image state or information - this maintains the evidence integrity
5. The image is converted to a qcow2 format. The qcow2 is the prefered format for kvm virtualization. It allows snapshots and the image only occupies the used forensic image space.
6. The partitions are detected.
7. The operating system inside each partition is detected. If it is a knowned operating system, kvm optimized virtual drivers are pré-installed. This drivers will be installed on the forensic virtual machine first boot
8. If the operating system was not detected, a complete vm conversion is made without installing any drivers. This makes the boot probable possible, but the resulting machine should be checked and possible optimized kvm drivers should be installed manually.
9. If no partions are detected, a virtual partion is created and a virtual boot device is created. This allows to convert partion images to full images. Extra work is needed by the user to adapt this image to make it bootable. In this case the user should use extra tools like virtual cdrom to try to make the vm work.


Method 1: Copy the local forensic image to a new forensic virtual machine on the server
****************************************************************************************

Method 2: Link the local forensic image to a new forensic virtual machine on the server
****************************************************************************************
