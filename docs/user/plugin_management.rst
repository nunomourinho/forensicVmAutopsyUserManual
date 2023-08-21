Plugins - Security Bypass Utilities
=====================================

Plugins serve as a vital component of the forensicVM, offering an array of capabilities that can greatly assist forensic investigators. Often, forensic investigators encounter forensicVM machines that are locked or protected by certain security measures, making it difficult to access them. One common scenario is where the forensicVM is locked behind a user account, with the suspect not revealing the password. Plugins provide methods to bypass these protections.

Authentication Bypass Features
------------------------------

The suite of plugins specifically designed to bypass authentication includes:

- **Add Windows Forensic Admin**:
  
  - This plugin creates a new Windows admin user under the "Administrator" group. The credentials for this user are:

    - **Username**: forensicAdmin
    - **Password**: forensicAdmin
    
    The newly created user can also be used to reset the password for any local account.

- **Add Linux Forensic Admin**:

  - Creates a new Linux user with the following credentials:
    
    - **Username**: forensicAdmin
    - **Password**: forensicAdmin
    
    This user is granted 'sudo' permissions, allowing elevated access.

- **Patch Accessibility**:

  - A strategic patch that enables forensic administrators to invoke a system-level cmd.exe prompt. This can be triggered by pressing the shift key five times consecutively on the Windows login screen.

- **Bypass Windows Password**:

  - This plugin patches the "ntlmshared.dll" file, effectively allowing a bypass of Windows authentication. While the login screen will accept any password entered, it will still utilize the cached user password hash. This is particularly crucial when trying to access encrypted auto-mounted BitLocker files that depend on the original user's credentials for access.

Additional Security Bypass Features
-----------------------------------

Apart from authentication bypass, there are plugins designed to circumvent other security measures:

- **Disable Windows Defender and Firewall**:

  - Certain external security tools like NirSoft or Mimikatz necessitate the deactivation of antivirus programs. This plugin disables both Windows Defender and the firewall to accommodate such tools.

- **Reset Windows 2003 or XP Activation**:

  - This is required for instances where a forensic investigator needs to access machines that are awaiting activation, like Windows 2003 or XP. The plugin resets the activation to allow unobstructed login.

- **BOOTFIX: Disable Driver Enforcement**:

  - When working with older systems or in scenarios where you've converted a forensic image, you might encounter certain constraints related to driver signatures. The "Disable Driver Enforcement" utility addresses these challenges:

      - **Allow Unsigned Drivers**: By default, many operating systems, especially modern ones, enforce driver signing for security reasons. Disabling this enforcement lets you run unsigned drivers. This can be particularly handy for running drivers like `virtio` on older systems.

      - **Support for Programs Using Unsigned Drivers**: Some utilities or programs require the use of unsigned drivers. Disabling the driver enforcement provides flexibility to run these applications without any hitches.

      - **Blue Screen Issue Resolution**: After converting a forensic image, systems may sometimes experience the infamous 'Blue Screen of Death' (BSOD) due to driver issues. This tool can assist in resolving those problems by ensuring that all drivers, even the unsigned ones, can run without any enforcement barriers.

.. note::

   While these plugins provide powerful capabilities, they should be used responsibly and ethically. Misuse could lead to unintended consequences or legal issues.
