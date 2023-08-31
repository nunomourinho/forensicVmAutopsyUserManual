Plugins - Security Bypass Utilities
=====================================

Plugins serve as a vital component of the forensicVM, offering an array of capabilities that can greatly assist forensic investigators. Often, forensic investigators encounter forensicVM machines that are locked or protected by certain security measures, making it difficult to access them. One common scenario is where the forensicVM is locked behind a user account, with the suspect not revealing the password. Plugins provide methods to bypass these protections.

:term:`Authentication Bypass Features`
------------------------------

The suite of plugins specifically designed to bypass authentication includes:

- **:term:`Add Windows Forensic Admin`**:
  
  - This plugin creates a new Windows admin user under the "Administrator" group. The credentials for this user are:

    - **Username**: forensicAdmin
    - **Password**: forensicAdmin
    
    The newly created user can also be used to reset the password for any local account.

- **:term:`Add Linux Forensic Admin`**:

  - Creates a new Linux user with the following credentials:
    
    - **Username**: forensicAdmin
    - **Password**: forensicAdmin
    
    This user is granted 'sudo' permissions, allowing elevated access.

- **:term:`Patch Accessibility`**:

  - A strategic patch that enables forensic administrators to invoke a system-level cmd.exe prompt. This can be triggered by pressing the shift key five times consecutively on the Windows login screen.

- **:term:`Bypass Windows Password`**:

  - This plugin patches the "ntlmshared.dll" file, effectively allowing a bypass of Windows authentication. While the login screen will accept any password entered, it will still utilize the cached user password hash. This is particularly crucial when trying to access encrypted auto-mounted BitLocker files that depend on the original user's credentials for access.

:term:`Additional Security Bypass Features`
-----------------------------------

Apart from authentication bypass, there are plugins designed to circumvent other security measures:

- **Disable Windows Defender and :term:`Firewall`**:

  - Certain external security tools like NirSoft or Mimikatz necessitate the deactivation of antivirus programs. This plugin disables both Windows Defender and the firewall to accommodate such tools.

- **:term:`Reset Windows 2003 or XP Activation`**:

  - This is required for instances where a forensic investigator needs to access machines that are awaiting activation, like Windows 2003 or XP. The plugin resets the activation to allow unobstructed login.

- **:term:`BOOTFIX: Disable Driver Enforcement`**:

  - When working with older systems or in scenarios where you've converted a forensic image, you might encounter certain constraints related to driver signatures. The "Disable Driver Enforcement" utility addresses these challenges:

      - **Allow Unsigned Drivers**: By default, many operating systems, especially modern ones, enforce driver signing for security reasons. Disabling this enforcement lets you run unsigned drivers. This can be particularly handy for running drivers like `virtio` on older systems.

      - **Support for Programs Using Unsigned Drivers**: Some utilities or programs require the use of unsigned drivers. Disabling the driver enforcement provides flexibility to run these applications without any hitches.

      - **Blue Screen Issue Resolution**: After converting a forensic image, systems may sometimes experience the infamous ':term:`Blue Screen of Death`' (BSOD) due to driver issues. This tool can assist in resolving those problems by ensuring that all drivers, even the unsigned ones, can run without any enforcement barriers.

.. note::

   While these plugins provide powerful capabilities, they should be used responsibly and ethically. Misuse could lead to unintended consequences or legal issues.


:term:`Browsing Available Plugins`
---------------------------

Forensic investigations often require an adaptable approach, and the ability to extend functionality through plugins makes the ForensicVM tool particularly versatile. To stay updated with the latest available plugins or to review the catalog of installed plugins, the Autopsy ForensicVM Client provides an easy-to-use interface.

**Steps to List Available Plugins**

1. **Navigate to the 'Plugins' Tab**:
   Open the Autopsy ForensicVM Client and access the **Plugins** tab. This tab consolidates all plugin-related functionalities, making it easier to manage and deploy extensions.

2. **Refresh the Plugin List**:
   To get the most recent list of plugins, simply click on the **List Remote Plugins** button. This action fetches and displays all available plugins from the remote repository, ensuring you're working with the latest toolset.

    .. raw:: latex

       \FloatBarrier

    .. figure:: img/list_plugins_0001.jpg
       :alt: Interface displaying the 'List Remote Plugins' button for updating and viewing available plugins.
       :align: center
       :width: 500

       Browsing and refreshing the available plugins

    .. raw:: latex

       \FloatBarrier

:term:`Executing Plugins`
------------------

The capability to execute plugins enhances the versatility of the ForensicVM, allowing for specialized tasks and bypassing certain security measures. However, prior to running any plugin, precautions are necessary to ensure the integrity of the investigation and to minimize potential issues.

.. important::
   
   **:term:`Pre-plugin Execution Recommendation`**: 
   Before initiating any plugin, it is imperative to capture the current state of the machine using a snapshot. This provision safeguards against any unintended or adverse actions by the plugin, facilitating a revert to the original state if necessary. Start the machine, create a snapshot, and then proceed to shut down the ForensicVM.

**Procedure to Execute a Plugin:**


1. **Ensure ForensicVM is Stopped**:
   Before running any plugins, verify in the VM control area that the forensic virtual machine is in a stopped state.

2. **Select the Desired Plugin**:
   Navigate to the plugin management area and designate the specific plugin you intend to run.

3. **Execute the Selected Plugin**:
   Initiate the plugin execution by pressing the **Run Selected Plugin** button.

4. **Review the Plugin Output**:
   Post execution, it's vital to inspect the results and logs. These can be found within the **:term:`Output Console`** tab.

    .. raw:: latex

       \FloatBarrier

    .. figure:: img/run_plugin_0001.jpg
       :alt: Running a plugin
       :align: center
       :width: 500

       Running a plugin

    .. raw:: latex

       \FloatBarrier

.. warning::

   For the integrity of the process, always ensure a complete shutdown of the ForensicVM before executing any plugins. In the context of Windows, pressing the shift key while initiating the shutdown ensures the machine isn't placed in hibernation and undergoes a full shutdown. This step is crucial as hibernation can interfere with the functionality of certain plugins and the snapshot reverting process.

Join the :term:`Community Plugins Project` and Shape ForensicVM's Future!
------------------------------------------------------------------

The **:term:`Community Plugins Project`** for AutoPsy ForensicVM is an open initiative aimed at driving innovation and enhancing the functionalities of the ForensicVM tool. As a community-driven platform, we invite individuals from all backgrounds to contribute. Whether you're a seasoned developer, a forensic investigator with a penchant for coding, or a user with an innovative idea, your input can make a difference!

Here's how you can get involved:

:term:`Access the Project Repository`
*******************************

The entire project is hosted on GitHub. You can view, clone, or fork the repository by visiting:

`ForensicVM Plugins on GitHub <https://github.com/nunomourinho/forensicVM-Plugins>`_

:term:`Contributing Code`
******************

If you've developed a new plugin or made improvements to existing ones, follow these steps to contribute:

1. **Fork the Project**: Fork the main repository to create a personal copy you can work on.
2. **Commit Your Changes**: Make your changes, ensuring they adhere to the project's coding standards and best practices.
3. **Suggest a Merge**: Once ready, submit a pull request. Our team will review your code, and if it meets our quality standards, it will be merged into the next release.

:term:`Feature Suggestions and Plugin Requests`
*****************************************

If you have ideas for new plugins, features, or improvements, but aren't looking to code them yourself, you can still contribute:

1. **Open an Issue**: Navigate to the `Issues section <https://github.com/nunomourinho/forensicVM-Plugins/issues>`_ on our GitHub page.
2. **Describe Your Idea**: Provide as much detail as possible. This helps in understanding and potentially implementing your suggestion.
3. **Engage with the Community**: Once your issue is posted, community members might join the discussion, providing feedback, insights, or offering to develop your idea.

.. note::

   Collaboration is the backbone of open-source projects. By sharing ideas, providing feedback, or contributing code, you're not just enhancing a tool; you're building a community.
