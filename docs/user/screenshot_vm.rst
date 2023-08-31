Making and importing Screenshots
================================

Making screenshots
*******************

It is often necessary to take screenshots of the forensic virtual machine (forensicVM) for documentation, analysis, or reporting purposes. There are two primary ways to capture a screenshot, depending on your location within the system interface:

1) Capture Screenshot in the Main :term:`Autopsy Plugin` Interface
----------------------------------------------------------

To take a screenshot of the forensicVM from the main Autopsy plugin interface, please press the Screenshot button on the screenshot panel:

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0001.jpg
      :alt: Screenshot VM on the main Autopsy plugin interface
      :align: center
      :width: 500

      Screenshot VM on the main Autopsy plugin interface

   .. raw:: latex

      \FloatBarrier

2) Capture Screenshot in the :term:`Web Screen Interface`
-------------------------------------------------

Capturing a screenshot from the web screen interface is similarly straightforward:

   a) Navigate to the web interface where the forensicVM is displayed. Expand the tools panel.

   b) Locate the screenshot icon or use the appropriate key command within the web interface.

   c) Press the camera icon to take a screenshot.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0002.jpg
      :alt: Screenshot VM on the web screen interface
      :align: center
      :width: 500

      Screenshot VM on the web screen interface

   .. raw:: latex

      \FloatBarrier

These methods enable you to capture visual records of the forensicVM from different points within the system, providing flexibility for various operational needs.

Downloading Screenshots as a :term:`ZIP File`
*************************************

After capturing the necessary screenshots of the forensic virtual machine (forensicVM), you can download them all as a ZIP file. This process is done in four steps:

1) Press the Save Screenshots Button
------------------------------------

   a) Navigate to the screenshots panel within the plugin interface.

   b) Locate and press the "Save Screenshots" button.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0003.jpg
      :alt: Save screenshots button on the plugin interface
      :align: center
      :width: 500

      Save screenshots button on the plugin interface

   .. raw:: latex

      \FloatBarrier
     
2) Save As Dialogue with Default Path
-------------------------------------

   a) You will be presented with a "Save As" dialog box.

   b) The default path for saving will be the forensic image path inside the Autopsy case path.

   c) Confirm the save location and proceed.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0004.jpg
      :alt: Save As dialog with default path
      :align: center
      :width: 500

      Save As dialog with default path

   .. raw:: latex

      \FloatBarrier


3) :term:`Download Progress` and Success Alert
--------------------------------------

   a) A download progress bar will appear, showing the status of the download.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0005_1.jpg
      :alt: Download progress
      :align: center

      Download progress

   .. raw:: latex

      \FloatBarrier

   b) Once the download is complete, an alert box will appear, saying that the screenshots were successfully downloaded.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0005.jpg
      :alt: Success alert
      :align: center

      Success alert

   .. raw:: latex

      \FloatBarrier

4) Open Windows Path with Screenshots.zip
-----------------------------------------

   a) The Windows path where the `screenshots.zip` file is saved will be opened in :term:`Windows Explorer`.

   b) You can then access the ZIP file containing all the screenshots.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0006.jpg
      :alt: Windows path with screenshots.zip
      :align: center
      :width: 500

      Windows path with screenshots.zip

   .. raw:: latex

      \FloatBarrier

These steps ensure an efficient and organized process for downloading the captured screenshots of the forensicVM, making it convenient for further use or analysis.

Importing Screenshots to Autopsy Software
******************************************

1) Unzip Your Screenshots with Your Favorite ZIP Program (e.g., 7-Zip)
-----------------------------------------------------------------------
   Start by extracting the ZIP file containing your screenshots. Using a tool like 7-Zip, right-click the ZIP file and choose the extraction option.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0007.jpg
      :alt: Unzip screenshots using 7-Zip
      :align: center
      :width: 500

      Unzip screenshots using 7-Zip

   .. raw:: latex

      \FloatBarrier

2) Copy Screenshot Path in Explorer
-----------------------------------
   Navigate to the folder where the screenshots were extracted and copy the full path from the address bar in Explorer.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0008.jpg
      :alt: Copy screenshot path in Explorer
      :align: center
      :width: 500

      Copy screenshot path in Explorer

   .. raw:: latex

      \FloatBarrier

3) Add a New :term:`Data Source`
------------------------
   Open Autopsy and initiate the process of adding a new data source by selecting the relevant option in the interface.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0009.jpg
      :alt: Add a new data source
      :align: center
      :width: 500

      Add a new data source

   .. raw:: latex

      \FloatBarrier

4) Select the Host for Which You Have to Import the Screenshots
---------------------------------------------------------------
   Choose the appropriate host for which you want to import the screenshots.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0010.jpg
      :alt: Select the host
      :align: center
      :width: 500

      Select the host

   .. raw:: latex

      \FloatBarrier

5) Select :term:`Logical Files` as the :term:`Data Source`
------------------------------------------
   Select ":term:`Logical Files`" as the type of data source for importing the screenshots.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0011.jpg
      :alt: Select :term:`Logical Files` as the data source
      :align: center
      :width: 500

      Select :term:`Logical Files` as the data source

   .. raw:: latex

      \FloatBarrier

6) Click the Button "Add" to Add a New Logical :term:`Data Source` Folder
----------------------------------------------------------------
   Click the "Add" button to create a new folder for the logical data source where the screenshots are stored.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0012.jpg
      :alt: Click "Add" button
      :align: center
      :width: 500

      Click "Add" button

   .. raw:: latex

      \FloatBarrier

7) Paste the Path of the Screenshots and Press "Select"
------------------------------------------------------
   Paste the previously copied path of the screenshots into the designated field and press the "Select" button.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0013.jpg
      :alt: Paste the path and press "Select"
      :align: center
      :width: 500

      Paste the path and press "Select"

   .. raw:: latex

      \FloatBarrier

8) Press "Next"
---------------
   Press the "Next" button to proceed to the following step of the configuration.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0014.jpg
      :alt: Press "Next"
      :align: center
      :width: 500

      Press "Next"

   .. raw:: latex

      \FloatBarrier

9) Deselect All Plugins. Select the Ingest Plugin "Picture Analyser." Press "Next"
---------------------------------------------------------------------------------
   Deselect any unnecessary plugins and select only the "Picture Analyser" plugin, then press "Next."

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0015.jpg
      :alt: Select "Picture Analyser" plugin
      :align: center
      :width: 500

      Select "Picture Analyser" plugin

   .. raw:: latex

      \FloatBarrier

10) Press "Finish"
------------------
   Press the "Finish" button to complete the configuration and begin the import process.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0016.jpg
      :alt: Press "Finish"
      :align: center
      :width: 500

      Press "Finish"

   .. raw:: latex

      \FloatBarrier

11) Browse into the Imported LogicalFileSet Inside the :term:`Data Source`. Right-click the Mouse
----------------------------------------------------------------------------------------
   Browse the imported LogicalFileSet inside the data source, and right-click on the specific file you want to view.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0017.jpg
      :alt: Browse into LogicalFileSet
      :align: center
      :width: 500

      Browse into LogicalFileSet

   .. raw:: latex

      \FloatBarrier

12) Select "Open in External Viewer" or Press CTRL+E
----------------------------------------------------
   Select the "Open in External Viewer" option from the context menu, or simply press CTRL+E on your keyboard.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0018.jpg
      :alt: Open in External Viewer
      :align: center
      :width: 500

      Open in External Viewer

   .. raw:: latex

      \FloatBarrier

13) The Image is Displayed
--------------------------
   The selected image is now displayed, allowing you to view and analyze it as needed.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/screenshot_vm_0019.jpg
      :alt: Image displayed
      :align: center
      :width: 500

      Image displayed

   .. raw:: latex

      \FloatBarrier

This step-by-step guide helps you efficiently import the screenshots from the forensic virtual machine into Autopsy software for in-depth analysis, enabling a streamlined workflow and enhancing your investigation process.

.. note:: **Importance of :term:`Tagging` Screenshots for Evidence**
   :class: attention

   :term:`Tagging` screenshots in Autopsy forensic software is a pivotal step in digital investigations. It allows forensic professionals to systematically identify, analyze, and report on crucial visual information. Tagged screenshots can be included in final reports, where they may be presented as potential evidence in legal proceedings. The process ensures the integrity of visual data and contributes significantly to building a solid case.

In the realm of digital forensics, Autopsy forensic software plays a crucial role in analyzing and managing evidence. A key feature of this powerful tool is its ability to handle screenshots, which are often vital in investigations.

**:term:`Tagging` Relevant Screenshots**: With Autopsy, investigators can sift through various images and screenshots collected during the forensic analysis. If certain images are identified as potentially relevant to a case, they can be tagged for further scrutiny. This tagging function is more than a mere organizational tool; it's a systematic way to highlight essential visual information that may prove crucial in understanding the digital activities related to a case.

**How to Tag**: Simply right-click on the desired screenshot and select the "Tag" option. You may create custom tags or use predefined ones, adding notes or comments as necessary. This flexibility ensures that you can organize your screenshots in a way that suits your specific investigative needs.

**Inclusion in the Final Report**: Tagged screenshots are not merely an intermediate step in the investigation. They often form an integral part of the final report. When compiling your findings, all tagged screenshot photos can be automatically included as potential evidence. They are presented in a well-organized manner, often alongside corresponding notes or observations made during the analysis phase.

**How to Include in Report**: Typically, there's an option to include tagged items in the report generation process. Make sure to select this option to have all tagged screenshots appear in the final document.
Presenting as Evidence: The end report, including the tagged screenshots, can be used in legal proceedings as possible evidence. The organized and systematic way in which these images are handled, analyzed, and reported in Autopsy ensures their integrity and admissibility in a court of law.

In conclusion, the ability to tag relevant screenshots in Autopsy forensic software is not merely a feature but an essential process that enables precise analysis, reporting, and legal utilization of visual data. It allows forensic professionals to efficiently identify and focus on critical visual information, contributing to a more comprehensive and convincing presentation of evidence in any given case.
