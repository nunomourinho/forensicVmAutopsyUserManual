Running Autopsy Forensic VM Plugin
====================================

To efficiently use the Autopsy ForensicVM plugin, it's essential to initialize a new case within the :term:`:term:`Autopsy framework`` and then seamlessly integrate a new data source. Below, the comprehensive procedure is outlined:

1) **Add a New Case to Autopsy**
   
   Initiate the Autopsy application and from the wizard interface, choose the option to add a new case. This is the first step in creating a structured environment for your forensic analysis.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/autopsy_add_data_source_0001.jpg
      :alt: Add a New Case to Autopsy
      :align: center
      :width: 400px

      Add a New Case to Autopsy

   .. raw:: latex

      \FloatBarrier


2) **Fill in Case Name in** :term:`:term:`Case Information`` ******
   
   Once the case addition window pops up, provide a unique and descriptive name for your case. This helps in distinguishing it from other cases in the future.

   .. raw:: latex

      \FloatBarrier


   .. figure:: img/autopsy_add_data_source_0002.jpg
      :alt: Fill in Case Name in :term:`:term:`Case Information``
      :align: center
      :width: 600px

      Fill in Case Name in :term:`:term:`Case Information``

      .. raw:: latex

         \FloatBarrier


3) **Fill Optional Information**

   Here, you can include additional details about the case. While this is optional, it's recommended to fill in as much information as possible for thorough documentation.

   .. raw:: latex

      \FloatBarrier


   .. figure:: img/autopsy_add_data_source_0003.jpg
      :alt: Fill Optional Information
      :align: center
      :width: 600px

      Fill Optional Information

   .. raw:: latex

      \FloatBarrier



4) **Choose Host Options**
   
   Decide on the host configuration for this case. You can either:
   - Generate a new host using the data source parameters.
   - Specify a new host name manually.
   - Or, utilize an existing host from a previous case or configuration.

   .. raw:: latex

      \FloatBarrier


   .. figure:: img/autopsy_add_data_source_0004.jpg
      :alt: Choose Host Options
      :align: center
      :width: 600px

      Choose Host Options

   .. raw:: latex

      \FloatBarrier


5) **Select :term:`:term:`Data Source`` Type as ":term:`:term:`Disk Image or VM File``"**

   Choose the type of data source you're incorporating. For this procedure, select ":term:`:term:`Disk Image or VM File``", which allows Autopsy to process VM images and disk snapshots.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0005.jpg
      :alt: Select :term:`:term:`Data Source`` Type
      :align: center
      :width: 600px

      Select :term:`:term:`Data Source`` Type

   .. raw:: latex

      \FloatBarrier



6) **Browse and Choose Your** :term:`:term:`Forensic Image`` ******

   Navigate through your file system and pick the appropriate forensic image or VM file. Ensure that the chosen file is compatible and accessible.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0006.jpg
      :alt: Choose Your :term:`:term:`Forensic Image``
      :align: center
      :width: 600px

      Choose Your :term:`:term:`Forensic Image``

   .. raw:: latex

      \FloatBarrier



7) **Select Extra Parameters Like** :term:`:term:`Time Zone`` and :term:`:term:`Sector Size`` ******

   Fine-tune your forensic analysis by selecting the relevant time zone and determining the sector size. These parameters help in accurate data extraction and interpretation.

   .. raw:: latex

      \FloatBarrier


   .. figure:: img/autopsy_add_data_source_0007.jpg
      :alt: Select Extra Parameters
      :align: center
      :width: 600px

      Select Extra Parameters

   .. raw:: latex

      \FloatBarrier



8) **Configure the** :term:`:term:`Python`` Ingest Plugin to Run and Select the :term:`:term:`ForensicVM Client Plugin`` ******

   Activate the :term:`:term:`Python`` Ingest Plugin for automated data ingestion. Also, ensure to select the ForensicVM Client plugin, which is pivotal for the VM forensic analysis.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0008.jpg
      :alt: Configure the :term:`:term:`Python`` Ingest Plugin
      :align: center
      :width: 600px

      Configure the :term:`:term:`Python`` Ingest Plugin

   .. raw:: latex

      \FloatBarrier



9) **Monitor the :term:`:term:`Data Source`` Processing Progress**

   As the data gets processed, an intuitive progress bar displays the ongoing activities and the completion percentage. Keep an eye on this to gauge the processing speed and potential completion time.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0009.jpg
      :alt: :term:`:term:`Data Source`` Processing Progress
      :align: center
      :width: 600px

      :term:`:term:`Data Source`` Processing Progress

   .. raw:: latex

      \FloatBarrier



10) **Await the :term:`:term:`ForensicVM Loader``'s Initialization**

   The :term:`:term:`ForensicVM Loader`` will make a brief appearance. This indicates that the plugin is gearing up for execution. It will automatically close once the plugin is fully initialized.

   .. raw:: latex

      \FloatBarrier

   .. figure:: img/autopsy_add_data_source_0010.jpg
      :alt: :term:`:term:`ForensicVM Loader`` Initialization
      :align: center
      :width: 600px

      :term:`:term:`ForensicVM Loader`` Initialization

   .. raw:: latex

      \FloatBarrier



11) **Complete the Procedure and Minimize Autopsy Window**

   Click on the "Finish" button to round off the 'Add :term:`:term:`Data Source``' wizard. For better visibility and multitasking, it's advisable to minimize the main Autopsy window at this juncture.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0011.jpg
      :alt: Finish :term:`:term:`Data Source`` Wizard
      :align: center
      :width: 600px

      Finish :term:`:term:`Data Source`` Wizard

   .. raw:: latex

      \FloatBarrier



12) **Engage with the Autopsy ForensicVM Client** :term:`:term:`Plugin Interface`` ******

   Post the previous steps, the dedicated window for the Autopsy ForensicVM Client plugin will emerge. Here, you can conduct in-depth VM forensics using the myriad features offered by the plugin.

   .. raw:: latex

      \FloatBarrier



   .. figure:: img/autopsy_add_data_source_0012.jpg
      :alt: ForensicVM Client :term:`:term:`Plugin Interface``
      :align: center
      :width: 600px

      ForensicVM Client :term:`:term:`Plugin Interface``

   .. raw:: latex

      \FloatBarrier
