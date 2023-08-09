Convert Forensic Image to a Forensic Virtual Machine
=====================================================

When aiming to convert a local forensic image to a remote forensic virtual machine on a server, two primary methods are prevalent:

1. **Direct Copy to Server**: This approach duplicates the forensic image, creating a new forensic virtual machine on the server. It grants comprehensive access and utility of the forensicVM, making it the ideal choice for collaborative remote investigations.
   
2. **Link Creation**: In this method, a link is forged between the local forensic image and a new counterpart on the server. Although it's swifter (given that the image isn't transferred to the remote server), there are limitations. The conversion and previewing are quick, yet initiating the machine locally is mandatory. The investigator must resort to the Autopsy client plugin to start the machine, as the web interface is incompatible due to the dependency on the original forensic image.

**Steps for Both Methods**:

1. **Initiate SSH Connection**: An SSH link is established with the forensicVM server.

2. **Reverse Connection Establishment**: This connection triggers a reverse connection to a read-only samba CIFS share, often known as a Windows share. This maneuver enables the server to access the Windows share containing the forensic image.

3. **Initiate Conversion**: Here, the type of forensic image is identified, followed by the selection of an appropriate tool on the server to mount the image to a virtual raw device. This is especially vital when images span across multiple files.

   .. note:: 
      This tool selection process ensures that the appropriate software is utilized for optimal conversion.

4. **Snapshot Creation**: An initial forensic image snapshot is generated. Acting as a base snapshot, it retains the state tied to the forensic image's virtual raw. This facilitates the installation of drivers without altering the forensic image's state or information, preserving the sanctity of the evidence.

5. **Image Conversion**: The image undergoes a transformation into the qcow2 format - the favored format for KVM virtualization. It not only supports snapshots but also ensures the image only occupies the space used by the forensic image.

6. **Partition Detection**: The system identifies any partitions present within the image.

7. **Operating System Detection**: The OS inside each partition is discerned. If recognized, KVM-optimized virtual drivers get pre-installed, which will initiate upon the forensic virtual machine's first boot.

8. **Fallback Conversion**: If the OS remains unidentified, the VM undergoes a full conversion without any driver installations. While this could potentially enable booting, post-conversion, manual scrutiny and possible KVM driver installations are essential.

9. **Partition Absence Handling**: In the event no partitions are identified, a virtual partition gets generated alongside a virtual boot device. This procedure aids in converting partition images into complete images. However, the user must invest additional effort to adapt this image for booting. They might need supplementary tools, like a virtual CD-ROM, to rectify and make the VM operational.

.. tip::
   It's crucial to regularly monitor the conversion process to ensure all steps are proceeding as expected and that any necessary adjustments can be made promptly.

Method 1: Copy the Local Forensic Image to a New Forensic Virtual Machine on the Server
****************************************************************************************
**Direct Copy to Server**: This approach duplicates the forensic image, creating a new forensic virtual machine on the server. It grants comprehensive access and utility of the forensicVM, making it the ideal choice for collaborative remote investigations.


**Conversion steps:**

1. **Begin the Conversion**:
   
   Initiate the conversion process by clicking on the button titled "Virtualize - a) Convert to VM". This action sets the process in motion.

   .. figure:: img/virtualize_convert_0001.jpg
      :alt: Screenshot showcasing the "Virtualize - a) Convert to VM" button.
      :align: center

      "Virtualize - a) Convert to VM" button


2. **Popup Confirmation**:

   Upon clicking the conversion button, a popup alert appears. This alert will display the message: "The conversion will start in a command window. Please do not close it until the conversion is finished...". Click on "OK" to commence the conversion process.

   .. figure:: img/virtualize_convert_0002.jpg
      :alt: Popup alert confirming the start of the conversion.
      :align: center

      Conversion Confirmation Popup


3. **MS-DOS Command Window Feedback**:

   A MS-DOS command window materializes post confirmation. This window is instrumental in detecting the image format, which will be visibly printed within. Ensure to keep an eye out for messages color-coded in green, indicating successful steps. However, should there be any errors, take note for future reference.

   .. figure:: img/virtualize_convert_0003.jpg
      :alt: MS-DOS command window indicating the progress.
      :align: center

      MS-DOS Command Window Progress Display


4. **Driver Installation and Conversion Completion**:

   During this phase, the system installs the required KVM drivers. Various messages get displayed in this window. Here's a color code to understand them:

   - **Green**: Success messages.
   - **Blue**: Warnings.
   - **Magenta**: Special information messages.
   - **Red**: Error messages.

   The conversion progression is displayed as a percentage. Once completed, a success message paired with the elapsed time is showcased, signaling the end of the conversion.

   .. figure:: img/virtualize_convert_0004.jpg
      :alt: Final stages of the conversion process.
      :align: center

      Conversion Completion Display

Method 2: Link the local forensic image to a new forensic virtual machine on the server
****************************************************************************************
**Link Creation**: In this method, a link is forged between the local forensic image and a new counterpart on the server. Although it's swifter (given that the image isn't transferred to the remote server), there are limitations. The conversion and previewing are quick, yet initiating the machine locally is mandatory. The investigator must resort to the Autopsy client plugin to start the machine, as the web interface is incompatible due to the dependency on the original forensic image.

**Conversion steps:**

   .. figure:: img/2-virtualize_link_0001.jpg
      :alt: Change
      :align: center

      Change

   .. figure:: img/2-virtualize_link_0002.jpg
      :alt: Change
      :align: center

      Change


   .. figure:: img/2-virtualize_link_0003.jpg
      :alt: Change
      :align: center

      Change


   .. figure:: img/2-virtualize_link_0004.jpg
      :alt: Change
      :align: center

      Change


   .. figure:: img/2-virtualize_link_0005.jpg
      :alt: Change
      :align: center

      Change


   .. figure:: img/2-virtualize_link_0006.jpg
      :alt: Change
      :align: center

      Change
