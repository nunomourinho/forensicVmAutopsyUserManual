Recording Video from a Forensic Virtual Machine
===============================================

Recording video from a forensic virtual machine (VM) that was created from a forensic image is not just a technical procedure; it's a crucial part of preserving and analyzing digital evidence in a meticulous and traceable manner. Below are the reasons why this approach is essential:

**Immutable Record**

When a virtual machine is created from a forensic image, it's a snapshot of a system at a specific point in time. Recording a video of the interactions and findings within this VM provides an immutable and chronological record. It ensures that every action taken can be reviewed, analyzed, and presented, leaving no room for doubt or ambiguity.

**Transparency and Accountability**

The video serves as a transparent and detailed log of what was done during the investigation. This helps in maintaining the integrity of the process, proving that the examination was conducted ethically and without alteration of the original data. If questions arise later, the video can be referred back to, to demonstrate exactly what was done.

**Legal Compliance**

In legal scenarios, the chain of custody must be robust and without breaks. Video recordings from the forensic VM provide a visual and auditable trail that can be an integral part of court proceedings. They offer judges, lawyers, and juries a clear and understandable view of the digital evidence, often aiding in decisions.

**Training and Collaboration**

The videos are not only useful for the case at hand but can be utilized for training purposes. They offer a real-world insight into how a forensic examination is conducted, the tools used, and the methodologies followed. Furthermore, they facilitate collaboration between teams and experts, allowing them to review and discuss findings visually.

**Error Detection**

If mistakes are made during the investigation, video recordings enable forensic analysts to backtrack and understand where things went wrong. This can be vital for correcting errors and learning from them for future investigations.

**Enhancing Public Trust**

Lastly, the practice of recording video from forensic VMs can also contribute to enhancing public trust in digital forensic processes. It sends a strong signal that the work is conducted with utmost professionalism, thoroughness, and adherence to legal standards.


Record a video from the forensicVM
-----------------------------------

1. **Show the control bar on the forensicVM web screen web interface by clicking the arrow button.**
   
   .. figure:: img/webrecord_video_0001.jpg
      :alt: Show the control bar
      :align: center

      Show the control bar

2. **Press the video recording icon. This icon will open a modal box.**

   .. figure:: img/webrecord_video_0002.jpg
      :alt: Press the video recording icon
      :align: center

      Press the video recording icon

3. **Press the red "Record Video" button.**

   .. figure:: img/webrecord_video_0003.jpg
      :alt: Press "Record Video" button
      :align: center

      Press "Record Video" button

4. **The recording is in progress; it can be up to 3 hours of recording before the video stops. The "rec" animation on the top right will show that the recording is in progress on the server.**

   .. figure:: img/webrecord_video_0004.jpg
      :alt: Recording in progress
      :align: center

      Recording in progress

Stop the video recording
-------------------------

1. **To stop the recording, first press the record icon on the control bar.**

   .. figure:: img/webrecord_video_0005.jpg
      :alt: Stop recording
      :align: center

      Stop recording

2. **On the modal box, please press the "Stop recording button".**

   .. figure:: img/webrecord_video_0006.jpg
      :alt: Stop recording button
      :align: center

      Stop recording button

3. **You will see two notification messages. The first one says, "Sent stop video recording," to indicate that the video has stopped recording. The video has to be processed on the server to download. When the video is completed on the server, you will see a second notification message stating, "Video saved (Video recorder with the name videoNNNN.mp4)", where NNNN is the video number. Please note down this number.**

   .. figure:: img/webrecord_video_0007.jpg
      :alt: Notifications
      :align: center

      Notifications


Download video recording
-------------------------
1. **To download, please press the record video icon again on the control bar.**

   .. figure:: img/webrecord_video_0008.jpg
      :alt: Download icon
      :align: center

      Download icon

2. **Now, press the "Download" button. You should now wait until the download is ready. It will start download automatically, so please do not close the webpage. The video preparation time and the download time will directly depend on the video size.**

   .. figure:: img/webrecord_video_0009.jpg
      :alt: Press "Download" button
      :align: center

      Press "Download" button

3. **Download started message**

   .. figure:: img/webrecord_video_0010.jpg
      :alt: Download started message
      :align: center

      Download started message

4. **After the video is downloaded, in the web browser, please open the download folder where the video file is.**

   .. figure:: img/webrecord_video_0011.jpg
      :alt: Locate downloaded file
      :align: center

      Locate downloaded file

Import video recording for analysis in Autopsy Software
--------------------------------------------------------

1. **With the shift key pressed, press the right-click on the mouse over the video file. Then select the "Copy as path" option on the menu.**

   .. figure:: img/webrecord_video_0012.jpg
      :alt: Copy as path
      :align: center

      Copy as path

2. **Open Autopsy software. On the menu bar, please click the "Add Data Source" button.**

   .. figure:: img/webrecord_video_0013.jpg
      :alt: Open Autopsy
      :align: center

      Open Autopsy

3. **Select the host and click next.**

   .. figure:: img/webrecord_video_0014.jpg
      :alt: Select host
      :align: center

      Select host

4. **Select Logical Files and click next.**

   .. figure:: img/webrecord_video_0015.jpg
      :alt: Select Logical Files
      :align: center

      Select Logical Files

5. **Click Add to select the video.**

   .. figure:: img/webrecord_video_0016.jpg
      :alt: Click Add to select video
      :align: center

      Click Add to select video

6. **Paste the path in the "File name:" field and click the "Select" button.**

   .. figure:: img/webrecord_video_0017.jpg
      :alt: Select video
      :align: center

      Select video to import

7. **Click Next.**

   .. figure:: img/webrecord_video_0018.jpg
      :alt: Click Next
      :align: center

      Click Next

8. **Deselect all ingest plugins and click next.**

   .. figure:: img/webrecord_video_0019.jpg
      :alt: Deselect plugins
      :align: center

      Deselect plugins

9. **Click Finish.**

   .. figure:: img/webrecord_video_0020.jpg
      :alt: Click Finish
      :align: center

      Click Finish

10. **1. Select the video file, 2. With the mouse right-click, "Add a File Tag", 3. Select the tag that is relevant to the forensic investigation.**

   .. figure:: img/webrecord_video_0021.jpg
      :alt: Tagging video
      :align: center

      Tagging video


.. note:: **Video Recording Sound**
   The current version of the video recording feature within the forensic virtual machine does not include sound. It captures only the visual interactions and activities within the system. We recognize the importance of sound in some investigations, and we are actively working to add this capability in a forthcoming version of our software.

   In the meantime, if sound recording is a necessary component of your forensic analysis, we advise utilizing third-party tools specifically designed for video and audio capture. Please ensure that any third-party tool used complies with your legal and organizational requirements.

