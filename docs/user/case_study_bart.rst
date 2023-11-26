ForensicVM Case Study - Bart the hacker
=======================================

.. _case_study:

Challenge Description
---------------------
This appendix details the ForensicVM Case Study and Challenge, which is designed to highlight the differences between the evidence collected by dead-box forensics and live-forensics in a virtualized environment. The data set was created with VirtualBox and features a Windows 11 Pro environment equipped with various local and cloud applications. The image was captured using the FTK Imager in Expert Witness Format (EWF).

- Virtualisation is required to extract vital evidence.
- Bypassing the 'Bart' password is necessary to access the applications.
- Existing passwords within the data set must remain unchanged to maintain the integrity of the challenge.
- The Bart windows password is simple, but the challenge encourages ethical hacking skills to bypass or decrypt it.

Steps to Solve the Challenge
----------------------------
The following steps provide a structured approach to tackle the ForensicVM challenge:

#. Utilise dead box forensics techniques in autopsy software to attempt full data retrieval from cloud applications and local applications. Document all findings.
#. Virtualize the forensic image using the autopsy ForensicVM plugin.
#. Attempt to identify and bypass the Bart password to gain access to the applications.
#. Run the ForensicVM
#. Without internet access, systematically extract information from each application cloud and local application. Document all findings.
#. Enable internet access and repeat the information extraction process, noting any differences.
#. Record any additional information obtained after establishing an Internet connection.
#. Identify and document information related to the two financial applications present in the environment.
#. Extract and analyse data related to cryptocurrency.
#. Create a comprehensive chain of custody for all investigative actions taken.
#. Conduct and document a memory dump and network traffic dump.
#. Capture all investigative actions via video and take screenshots for evidence support.

.. _further_information:

For further information, refer to the ForensicVM Autopsy Plugin User Manual available at:

`ForensicVM Autopsy Plugin User Manual <https://forensicvm-autopsy-plugin-user-manual.readthedocs.io/en/latest/>`_

The complete dataset can be accessed via the following links:

* `Google Drive Dataset <https://drive.google.com/drive/folders/1ecGvwAToAfSRmCDmtVesrEhP7uMFh2M6>`
* `Zenodo Dataset <https://zenodo.org/doi/10.5281/zenodo.10070981>`
* `NIST CFReDS Dataset <https://cfreds.nist.gov/all/NunoMourinho%2FEstigBeja/BartthehackerForensicVMshowcase2023>`

Challenge Solution
==================

Dead box forensics
------------------

The resolution of the digital forensic challenge began with the establishment of a new case within the forensic autopsy software. The initial phase involved the creation of a case as captured in Figure~\ref{fig:autopsy_001}.

.. _FloatBarrier:

.. figure:: apendices/img/autopsy_0001.jpg
   :width: 50%
   :align: center
   :alt: Creation of a New Case

   Creation of a New Case
   :label: fig:autopsy_001

Subsequently, the case details were entered as demonstrated in Figure~\ref{fig:autopsy_0002}, ensuring that all pertinent information was correctly documented.

.. figure:: apendices/img/autopsy_0002.jpg
   :width: 50%
   :align: center
   :alt: Entering Case Information

   Entering Case Information
   :label: fig:autopsy_0002

Optional case information was also provided to provide additional context and metadata for the investigation, as shown in Figure~\ref{fig:autopsy_0003}.

.. figure:: apendices/img/autopsy_0003.jpg
   :width: 50%
   :align: center
   :alt: Providing Optional Case Information

   Providing Optional Case Information
   :label: fig:autopsy_0003

To facilitate analysis, host information was generated as shown in Figure~\ref{fig:autopsy_0004}, which helps align the investigative environment with the specifics of the case.

.. figure:: apendices/img/autopsy_0004.jpg
   :width: 50%
   :align: center
   :alt: Generating Host Information

   Generating Host Information
   :label: fig:autopsy_0004

The subsequent step was to select the disk image or VM file that contained the forensic evidence, ensuring that the correct data source was incorporated into the investigation (Figure~\ref{fig:autopsy_0005}).

.. figure:: apendices/img/autopsy_0005.jpg
   :width: 50%
   :align: center
   :alt: Disk Image or VM File Selection

   Disk Image or VM File Selection
   :label: fig:autopsy_0005

The timezone configuration is critical for accurate timestamp analysis; therefore, the forensic image path was established and the timezone was adjusted to Europe/Lisbon as part of the configuration process (Figure~\ref{fig:autopsy_0006}).

.. figure:: apendices/img/autopsy_0006.jpg
   :width: 50%
   :align: center
   :alt: Configuring the Forensic Image Path and Timezone

   Configuring the Forensic Image Path and Timezone
   :label: fig:autopsy_0006

For initial data processing, ingest plugins were selected, specifically 'Recent Activity' and 'Picture Analyser', to extract relevant user activities and image-related evidence (Figure~\ref{fig:autopsy_0007}).

.. figure:: apendices/img/autopsy_0007.jpg
   :width: 50%
   :align: center
   :alt: Selection of Initial Ingest Plugins

   Selection of Initial Ingest Plugins
   :label: fig:autopsy_0007

The investigator then waited for the completion of the addition of the data source, monitoring the progress to ensure successful incorporation into the case (Figure~\ref{fig:autopsy_0008}).

.. figure:: apendices/img/autopsy_0008.jpg
   :width: 50%
   :align: center
   :alt: Monitoring Data Source Addition

   Monitoring Data Source Addition
   :label: fig:autopsy_0008

Upon successful addition of the data source, as confirmed by the software, the evidence was ready for a thorough examination (Figure~\ref{fig:autopsy_0009}).

.. figure:: apendices/img/autopsy_0009.jpg
   :width: 50%
   :align: center
   :alt: Confirmation of Data Source Addition

   Confirmation of Data Source Addition
   :label: fig:autopsy_0009

Exploration within the "Os accounts" section yielded security answers that were potential avenues for password bypass efforts, with all answers being "\textbf{bart}", which could provide a breakthrough in the case (Figure~\ref{fig:autopsy_0010}).

.. figure:: apendices/img/autopsy_0010.jpg
   :width: 50%
   :align: center
   :alt: OS Accounts and Security Answers

   OS Accounts and Security Answers
   :label: fig:autopsy_0010

In the process of forensic analysis, the discovery of the password '\textbf{Lisa@Springfield}' via the Autofill feature in the Autopsy Web form represents a pivotal development. This password is a critical piece of evidence for the case, as it could potentially grant access to restricted areas that may contain further information or clues. The uncovering of this password, as displayed in Figure~\ref{fig:autopsy_0011}, underscores the importance of thorough examination of digital artefacts which may hold vital information within a forensic investigation.

.. figure:: apendices/img/autopsy_0011.jpg
   :width: 50%
   :align: center
   :alt: Discovery of a Password via Web Form Autofill

   Discovery of a Password via Web Form Autofill
   :label: fig:autopsy_0011

Moreover, the identification of specific applications such as Eraser 6.2.0.2993, which is designed for secure file deletion, and HomeBank 5.7.1, a personal finance application, can offer valuable insights into the suspect's actions and intents. As depicted in Figure~\ref{fig:autopsy_0012}, the presence of these applications may suggest attempts to conceal activities or manage finances in a way that is pertinent to the investigation.

.. figure:: apendices/img/autopsy_0012.jpg
   :width: 50%
   :align: center
   :alt: Applications Identification

   Applications Identification
   :label: fig:autopsy_0012

.. _FloatBarrier:

.. figure:: apendices/img/autopsy_0012.jpg
   :width: 50%
   :align: center
   :alt: Applications of Interest Including Secure File Deletion and Personal Finance Management Tools

   Applications of Interest Including Secure File Deletion and Personal Finance Management Tools
   :label: fig:autopsy_0012

The further discovery of Money Manager Ex v.1.6.4, another financial management tool, as indicated in Figure~\ref{fig:autopsy_0013}, reinforces the financial angle of the user's activity profile. This could be integral to constructing a narrative regarding the suspect's financial dealings or motivations.

.. figure:: apendices/img/autopsy_0013.jpg
   :width: 50%
   :align: center
   :alt: Additional Financial Application Money Manager Ex Indicating In-Depth Financial Activities

   Additional Financial Application Money Manager Ex Indicating In-Depth Financial Activities
   :label: fig:autopsy_0013

Lastly, the opening of a financial database named example.xhb from the HomeBank files, as shown in Figure~\ref{fig:autopsy_0014}, further corroborates the financial dimension of the investigation. This particular file may contain transaction records, budgets, or other financial data which could be analysed to provide a clearer understanding of the suspect's financial behaviour or potential illicit activities.

.. figure:: apendices/img/autopsy_0014.jpg
   :width: 50%
   :align: center
   :alt: Opened Financial Database example.xhb Revealing Recent User Activities with Financial Data

   Opened Financial Database example.xhb Revealing Recent User Activities with Financial Data
   :label: fig:autopsy_0014

The discovery of the example.xhb database in XML format, as depicted in Figure~\ref{fig:autopsy_0015}, adds a layer of complexity due to the proprietary structure of the file. This could imply that special attention must be paid to decipher the data structure to interpret the financial information contained within. The proprietary nature of the format might necessitate the use of specific tools or methods to extract and analyse the data accurately.

.. figure:: apendices/img/autopsy_0015.jpg
   :width: 50%
   :align: center
   :alt: Proprietary XML Structure of the example.xhb Database

   Proprietary XML Structure of the example.xhb Database
   :label: fig:autopsy_0015

The identification of cloud applications in the forensic investigation is critical as it may provide insight into data that is not stored locally on the device. The accounts discovered through the Autopsy software, including GitHub, live.com, discord.com, and evernote.com, extend the potential for finding evidence to the cloud. The presence of these services as shown in Figure~\ref{fig:autopsy_0016}, suggests a broad range of user activity, from software development and project management to personal communication and note-taking, which could be relevant to the case.

.. figure:: apendices/img/autopsy_0016.jpg
   :width: 50%
   :align: center
   :alt: Overview of Cloud Applications Uncovered in Autopsy

   Overview of Cloud Applications Uncovered in Autopsy
   :label: fig:autopsy_0016

Tagging folders related to financial applications within Autopsy helps in organising evidence and highlights the importance of financial data in the investigation. As illustrated in Figure~\ref{fig:autopsy_0017}, tagging these folders ensures that relevant information is easily accessible and distinguishable from other unrelated data, facilitating a more efficient investigation process.

.. figure:: apendices/img/autopsy_0017.jpg
   :width: 50%
   :align: center
   :alt: Tagging of Folders Pertaining to Financial Applications

   Tagging of Folders Pertaining to Financial Applications
   :label: fig:autopsy_0017

The creation of an Autopsy HTML report is a critical step for documenting the investigation, offering a comprehensive and accessible format for presenting the findings. The series of figures, from Figure~\ref{fig:autopsy_0018} to Figure~\ref{fig:autopsy_0022}, encapsulate various aspects of the report, from the general overview to specific details regarding data sources and tagged items.

.. figure:: apendices/img/autopsy_0018.jpg
   :width: 50%
   :align: center
   :alt: Snapshot of the Autopsy HTML Report Interface

   Snapshot of the Autopsy HTML Report Interface
   :label: fig:autopsy_0018

.. figure:: apendices/img/autopsy_0019.jpg
   :width: 50%
   :align: center
   :alt: Detailing the Data Source 'bart.E01' within the HTML Report

   Detailing the Data Source 'bart.E01' within the HTML Report
   :label: fig:autopsy_0019

.. figure:: apendices/img/autopsy_0020.jpg
   :width: 50%
   :align: center
   :alt: Autopsy HTML Report Showing Tagged Items and Analysis Results

   Autopsy HTML Report Showing Tagged Items and Analysis Results
   :label: fig:autopsy_0020

.. figure:: apendices/img/autopsy_0021.jpg
   :width: 50%
   :align: center
   :alt: Compilation of All Results in the Autopsy HTML Report

   Compilation of All Results in the Autopsy HTML Report
   :label: fig:autopsy_0021

.. figure:: apendices/img/autopsy_0022.jpg
   :width: 50%
   :align: center
   :alt: Report Detailing Found Cloud Applications and Associated Usernames

   Report Detailing Found Cloud Applications and Associated Usernames
   :label: fig:autopsy_0022

Local applications and those identified as relevant through tagging were systematically documented within the Autopsy report as well. This incorporation of tagged local and cloud applications allows for a more comprehensive review of the software environment of the system under investigation (Figure~\ref{fig:autopsy_0023}).

