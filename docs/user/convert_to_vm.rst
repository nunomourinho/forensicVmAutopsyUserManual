Convert :term:`Forensic Image` to a Forensic Virtual Machine
=====================================================

When aiming to convert a local forensic image to a remote forensic virtual machine on a server, two primary methods are prevalent:

1. **:term:`Direct Copy to Server`**: This approach duplicates the forensic image, creating a new forensic virtual machine on the server. It grants comprehensive access and utility of the forensicVM, making it the ideal choice for collaborative remote investigations.
   
2. **:term:`Link Creation`**: In this method, a link is forged between the local forensic image and a new counterpart on the server. Although it's swifter (given that the image isn't transferred to the remote server), there are limitations. The conversion and previewing are quick, yet initiating the machine locally is mandatory. The investigator must resort to the Autopsy client plugin to start the machine, as the web interface is incompatible due to the dependency on the original forensic image.

**Steps for Both Methods**:

1. **Initiate SSH Connection**: An SSH link is established with the forensicVM server.

2. **Reverse Connection Establishment**: This connection triggers a reverse connection to a read-only samba CIFS share, often known as a Windows share. This maneuver enables the server to access the Windows share containing the forensic image.

3. **Initiate Conversion**: Here, the type of forensic image is identified, followed by the selection of an appropriate tool on the server to mount the image to a virtual raw device. This is especially vital when images span across multiple files.

   .. note:: 
      This tool selection process ensures that the appropriate software is utilized for optimal conversion.

4. **Snapshot Creation**: An initial forensic image snapshot is generated. Acting as a base snapshot, it retains the state tied to the forensic image's virtual raw. This facilitates the installation of drivers without altering the forensic image's state or information, preserving the sanctity of the evidence.

5. **Image Conversion**: The image undergoes a transformation into the :term:`qcow2` format - the favored format for KVM virtualization. It not only supports snapshots but also ensures the image only occupies the space used by the forensic image.

6. **Partition Detection**: The system identifies any partitions present within the image.

7. **Operating System Detection**: The OS inside each partition is discerned. If recognized, KVM-optimized virtual drivers get pre-installed, which will initiate upon the forensic virtual machine's first boot.

8. **:term:`Fallback Conversion`**: If the OS remains unidentified, the VM undergoes a full conversion without any driver installations. While this could potentially enable booting, post-conversion, manual scrutiny and possible KVM driver installations are essential.

9. **Partition Absence Handling**: In the event no partitions are identified, a virtual partition gets generated alongside a virtual boot device. This procedure aids in converting partition images into complete images. However, the user must invest additional effort to adapt this image for booting. They might need supplementary tools, like a virtual CD-ROM, to rectify and make the VM operational.

.. tip::
   It's crucial to regularly monitor the conversion process to ensure all steps are proceeding as expected and that any necessary adjustments can be made promptly.

Method 1: Copy the Local :term:`Forensic Image` to a New Forensic Virtual Machine on the Server
****************************************************************************************
**:term:`Direct Copy to Server`**: This approach duplicates the forensic image, creating a new forensic virtual machine on the server. It grants comprehensive access and utility of the forensicVM, making it the ideal choice for collaborative remote investigations.


**Conversion steps:**

1. **Begin the Conversion**:
   
   Initiate the conversion process by clicking on the button titled "Virtualize - a) Convert to VM". This action sets the process in motion.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0001.jpg
      :alt: Screenshot showcasing the "Virtualize - a) Convert to VM" button.
      :align: center
      :width: 600px

      "Virtualize - a) Convert to VM" button

   .. raw:: latex

      \FloatBarrier


2. **Popup Confirmation**:

   Upon clicking the conversion button, a popup alert appears. This alert will display the message: "The conversion will start in a command window. Please do not close it until the conversion is finished...". Click on "OK" to commence the conversion process.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0002.jpg
      :alt: Popup alert confirming the start of the conversion.
      :align: center

      Conversion :term:`Confirmation Popup`

   .. raw:: latex

      \FloatBarrier

3. **:term:`MS-DOS Command Window` Feedback**:

   A MS-DOS command window materializes post confirmation. This window is instrumental in detecting the image format, which will be visibly printed within. Ensure to keep an eye out for messages color-coded in green, indicating successful steps. However, should there be any errors, take note for future reference.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0003.jpg
      :alt: MS-DOS command window indicating the progress.
      :align: center
      :width: 600px

      :term:`MS-DOS Command Window` Progress Display

   .. raw:: latex

      \FloatBarrier

4. **Driver Installation and Conversion Completion**:

   During this phase, the system installs the required :term:`KVM drivers`. Various messages get displayed in this window. Here's a color code to understand them:

   - **Green**: Success messages.
   - **Blue**: Warnings.
   - **Magenta**: Special information messages.
   - **Red**: Error messages.

   The conversion progression is displayed as a percentage. 

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0004.jpg
      :alt: Conversion process display
      :align: center
      :width: 600px

      Conversion Progress Display

   .. raw:: latex

      \FloatBarrier


5. **Conversion completed**: 

   Once completed, a success message paired with the elapsed time is showcased, signaling the end of the conversion.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0005.jpg
      :alt: Conversion Completion Display
      :align: center
      :width: 600px

      Conversion Completion Display

   .. raw:: latex

      \FloatBarrier

6. **Success Conversion Popup**:

   Once the image conversion completes, a success popup will appear confirming the conversion's successful completion.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0006.jpg
      :alt: Success Conversion Popup
      :align: center

      Screenshot of the success conversion popup.

   .. raw:: latex

      \FloatBarrier

7. **ForensicVM First Boot**:

   To boot up the machine for the first time, click the "Start" button available in the Autopsy ForensicVM Plugin.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0007.jpg
      :alt: "Start" Button on the Autopsy ForensicVM Plugin
      :align: center
      :width: 600px

      Screenshot of the "Start" button on the Autopsy ForensicVM Plugin.

   .. raw:: latex

      \FloatBarrier

8. **Informational Popup - Machine Started**:

   Post clicking the "Start" button, an informational popup will appear to inform you about the machine's status.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0008.jpg
      :alt: Informational Popup on Machine Start
      :align: center

      Screenshot of the informational popup after machine start.

   .. raw:: latex

      \FloatBarrier

9. **Opening the ForensicVM**:

   To access the ForensicVM's web screen interface, click the "Open ForensicVM" button. This interface will allow you to interact directly with the forensicVM.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0009.jpg
      :alt: "Open ForensicVM" Button
      :align: center
      :width: 600px

      Screenshot of the "Open ForensicVM" button.

   .. raw:: latex

      \FloatBarrier

10. **ForensicVM :term:`Web Screen Interface`**:

   Once inside the web screen interface, click the prominent "Connect / Start" button to establish a connection with the forensicVM and view its virtual screen monitor.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0010.jpg
      :alt: ForensicVM's "Connect / Start" Button
      :align: center
      :width: 600px

      Screenshot of the ForensicVM's "Connect / Start" button.

   .. raw:: latex

      \FloatBarrier

11. **Interact with the ForensicVM**:

   With the connection established, you can now freely interact with the forensicVM.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/virtualize_convert_0011.jpg
      :alt: ForensicVM Interaction Interface
      :align: center
      :width: 600px

      Screenshot showcasing the ForensicVM's interactive interface.

   .. raw:: latex

      \FloatBarrier

Method 2: Link the Local :term:`Forensic Image` to a New Forensic Virtual Machine on the Server
****************************************************************************************

**:term:`Link Creation`**:

In this method, a link is forged between the local forensic image and a new counterpart on the server. This approach is faster because it doesn't involve transferring the entire image to the remote server. However, there are some limitations. The conversion process and preview are swift, but starting the machine locally is a requirement. The investigator needs to use the Autopsy client plugin to initiate the machine since the web interface cannot be used due to its dependency on the original forensic image.

**Conversion Steps**:

1. **Begin the Conversion**:
   
   Start the conversion by clicking on the button labeled "Virtualize - b) Link to VM".

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0001.jpg
      :alt: Screenshot showcasing the "Virtualize - b) Link to VM" button.
      :align: center
      :width: 600px

      "Virtualize - b) Link to VM" button

   .. raw:: latex

      \FloatBarrier

2. **Popup Confirmation**:
   
   After activating the conversion, a popup will emerge. It will instruct: "The conversion will commence in a command window. Please refrain from shutting it until the process concludes." Press "OK" to proceed.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0002.jpg
      :alt: A popup dialog confirming the start of the linking process.
      :align: center

      Linking :term:`Confirmation Popup`

   .. raw:: latex

      \FloatBarrier

3. **:term:`MS-DOS Command Window` Feedback**:

   The MS-DOS command window will surface, and the software will identify the image format, displaying it within the window. Successful actions are highlighted in green. However, be vigilant and record any errors that arise.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0003.jpg
      :alt: MS-DOS command window displaying the progress.
      :align: center
      :width: 600px

      :term:`MS-DOS Command Window` Feedback

   .. raw:: latex

      \FloatBarrier

4. **Driver Installation Phase**:

   This step focuses on the installation of required :term:`KVM drivers`. The messages in this phase are color-coded:
   
   - **Green**: Success indicators.
   - **Blue**: Warnings.
   - **Magenta**: Special informational messages.

   The linking process's progression is represented in percentage terms.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0004.jpg
      :alt: Phase indicating KVM driver installations and progress.
      :align: center
      :width: 600px

      Driver Installation and Progress Display

   .. raw:: latex

      \FloatBarrier

5. **Conclusion of Conversion**:

   Upon the conversion's culmination, a success notification will display the elapsed time. Ensure to press any key to close the window.
   
   .. WARNING:: 

      Avoid manually shutting this window. Such an action could leave a Linux mount unsealed, leading to potential complications in the future.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0005.jpg
      :alt: Window showcasing the successful completion of the linking process.
      :align: center
      :width: 600px

      Conversion Completed Notification

   .. raw:: latex

      \FloatBarrier

6. **Success Notification**:

   A concluding popup emerges, affirming that the forensic image was successfully linked to the VM. Click "OK" to exit this dialog.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/2-virtualize_link_0006.jpg
      :alt: Popup displaying the successful linking of the forensic image to the VM.
      :align: center

      Successful Linking Notification


   .. raw:: latex

      \FloatBarrier
