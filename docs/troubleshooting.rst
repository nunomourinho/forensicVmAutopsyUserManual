Troubleshooting
===============

Booting without signed drivers
------------------------------

If your machine cannot boot due to the virtio drivers installed during the automatic driver installation in the virtualization phase being unsigned or having an invalid signature for your operating system, the machine may enter a recovery boot loop. To address this issue, follow these steps:

- **1. Advanced options in the Automatic Repair boot screen**:
  Press the "Advanced options" button.

  .. figure:: user/img/troubleshoot_0001.jpg
     :name: advanced-options
     :alt: Advanced options in the Automatic Repair boot screen
     :width: 600

     Advanced options in the Automatic Repair boot screen

- **2. Troubleshoot**:
  Select the "Troubleshoot" option.

  .. figure:: user/img/troubleshoot_0002.jpg
     :name: troubleshoot
     :alt: Troubleshoot option
     :width: 300

     Troubleshoot option

- **3. Advanced options**:
  Choose the "Advanced options".

  .. figure:: user/img/troubleshoot_0003.jpg
     :name: advanced-options-selection
     :alt: Choosing Advanced options
     :width: 300

     Choosing Advanced options

- **4. Startup Settings**:
  Within the Advanced options, select the "Startup Settings" to change Windows startup behavior.

  .. figure:: user/img/troubleshoot_0004.jpg
     :name: startup-settings
     :alt: Startup Settings option
     :width: 500

     Startup Settings option

- **5. Restart**:
  Press the "Restart" button and await the system restart.

  .. figure:: user/img/troubleshoot_0005.jpg
     :name: restart-option
     :alt: Restart option
     :width: 500

     Restart option

- **6. Press F7**:
  Once the system restarts, press the **F7** key to choose "Disable driver signature enforcement".

  .. figure:: user/img/troubleshoot_0006.jpg
     :name: disable-driver-signature-enforcement
     :alt: Pressing F7 for Disable driver signature enforcement
     :width: 300

     Pressing F7 for Disable driver signature enforcement

- **7. Windows normal boot**:
  Your Windows should now boot normally.

  .. figure:: user/img/troubleshoot_0007.jpg
     :name: windows-normal-boot
     :alt: Windows booting normally
     :width: 600

     Windows booting normally

.. note::

   This behavior has been observed in older Windows versions, such as Windows 8.1. Mismatches or odd dates in the driver certificate can lead to this issue.
 
