Running Autopsy Forensic VM Plugin
====================================

To efficiently use the Autopsy ForensicVM plugin, it's essential to initialize a new case within the Autopsy framework and then seamlessly integrate a new data source. Below, the comprehensive procedure is outlined:

1) **Add a New Case to Autopsy**
   
   Initiate the Autopsy application and from the wizard interface, choose the option to add a new case. This is the first step in creating a structured environment for your forensic analysis.

   .. figure:: img/autopsy_add_data_source_0001.jpg
      :alt: Add a New Case to Autopsy
      :align: center

      Add a New Case to Autopsy

2) **Fill in Case Name in Case Information**
   
   Once the case addition window pops up, provide a unique and descriptive name for your case. This helps in distinguishing it from other cases in the future.

   .. figure:: img/autopsy_add_data_source_0002.jpg
      :alt: Fill in Case Name in Case Information
      :align: center

      Fill in Case Name in Case Information

3) **Fill Optional Information**

   Here, you can include additional details about the case. While this is optional, it's recommended to fill in as much information as possible for thorough documentation.

   .. figure:: img/autopsy_add_data_source_0003.jpg
      :alt: Fill Optional Information
      :align: center

      Fill Optional Information

4) **Choose Host Options**
   
   Decide on the host configuration for this case. You can either:
   - Generate a new host using the data source parameters.
   - Specify a new host name manually.
   - Or, utilize an existing host from a previous case or configuration.

   .. figure:: img/autopsy_add_data_source_0004.jpg
      :alt: Choose Host Options
      :align: center

      Choose Host Options

5) **Select Data Source Type as "Disk Image or VM File"**

   Choose the type of data source you're incorporating. For this procedure, select "Disk Image or VM File", which allows Autopsy to process VM images and disk snapshots.

   .. figure:: img/autopsy_add_data_source_0005.jpg
      :alt: Select Data Source Type
      :align: center

      Select Data Source Type

6) **Browse and Choose Your Forensic Image**

   Navigate through your file system and pick the appropriate forensic image or VM file. Ensure that the chosen file is compatible and accessible.

   .. figure:: img/autopsy_add_data_source_0006.jpg
      :alt: Choose Your Forensic Image
      :align: center

      Choose Your Forensic Image

7) **Select Extra Parameters Like Time Zone and Sector Size**

   Fine-tune your forensic analysis by selecting the relevant time zone and determining the sector size. These parameters help in accurate data extraction and interpretation.

   .. figure:: img/autopsy_add_data_source_0007.jpg
      :alt: Select Extra Parameters
      :align: center

      Select Extra Parameters

8) **Configure the Python Ingest Plugin to Run and Select the ForensicVM Client Plugin**

   Activate the Python Ingest Plugin for automated data ingestion. Also, ensure to select the ForensicVM Client plugin, which is pivotal for the VM forensic analysis.

   .. figure:: img/autopsy_add_data_source_0008.jpg
      :alt: Configure the Python Ingest Plugin
      :align: center

      Configure the Python Ingest Plugin

9) **Monitor the Data Source Processing Progress**

   As the data gets processed, an intuitive progress bar displays the ongoing activities and the completion percentage. Keep an eye on this to gauge the processing speed and potential completion time.

   .. figure:: img/autopsy_add_data_source_0009.jpg
      :alt: Data Source Processing Progress
      :align: center

      Data Source Processing Progress

10) **Await the ForensicVM Loader's Initialization**

   The ForensicVM Loader will make a brief appearance. This indicates that the plugin is gearing up for execution. It will automatically close once the plugin is fully initialized.

   .. figure:: img/autopsy_add_data_source_0010.jpg
      :alt: ForensicVM Loader Initialization
      :align: center

      ForensicVM Loader Initialization

11) **Complete the Procedure and Minimize Autopsy Window**

   Click on the "Finish" button to round off the 'Add Data Source' wizard. For better visibility and multitasking, it's advisable to minimize the main Autopsy window at this juncture.

   .. figure:: img/autopsy_add_data_source_0011.jpg
      :alt: Finish Data Source Wizard
      :align: center

      Finish Data Source Wizard

12) **Engage with the Autopsy ForensicVM Client Plugin Interface**

   Post the previous steps, the dedicated window for the Autopsy ForensicVM Client plugin will emerge. Here, you can conduct in-depth VM forensics using the myriad features offered by the plugin.

   .. figure:: img/autopsy_add_data_source_0012.jpg
      :alt: ForensicVM Client Plugin Interface
      :align: center

      ForensicVM Client Plugin Interface
