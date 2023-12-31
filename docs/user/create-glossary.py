import re

def fix_rst_term_line(line):
    # This pattern captures three groups: (1) The text before :term:, (2) the term itself, (3) the text after :term:
    pattern = r"(\*\*.*?)(\:term\:\`.*?\`)(.*?\*\*)"
    
    while re.search(pattern, line):
        match = re.search(pattern, line)
        before_term, term, after_term = match.groups()
        
        # Cases where the text before :term: is not empty and the text after :term: is not empty
        if before_term != '**' and after_term != '**':
            new_text = f"{before_term.strip()}** {term} **{after_term.strip()}"
        
        # Cases where only the text before :term: is not empty
        elif before_term != '**':
            new_text = f"{before_term.strip()}** {term}"
        
        # Cases where only the text after :term: is not empty
        elif after_term != '**':
            new_text = f"{term} **{after_term.strip()}"
        
        # Cases where both the text before and after :term: are empty
        else:
            new_text = f"{term}"
        
        # Replace the old text with the new text
        old_text = f"{before_term}{term}{after_term}"
        line = line.replace(old_text, new_text)
    
    return line


def generate_replacement(term):
    return f":term:`{term}`"

terms = [
    'SSD',
    'vmdk',
    'UEFI',
    'QEMU',
    'NVMe',
    'BIOS',
    'qcow2',
    '7-zip',
    'WinDbg',
    'Rekall',
    'Python',
    'HP ILO',
    'Django',
    'Tagging',
    'Redline',
    'RAID 10',
    'Netdata',
    'API key',
    'pcap.zip',
    'ZIP File',
    'VM Image',
    'Firewall',
    'Time Zone',
    'Volatility',
    'VM Control',
    'Timestamps',
    'Hypervisor',
    'FTK Imager',
    'Sector Size',
    'Meterpreter',
    'Memory Dump',
    'KVM drivers',
    'Data Source',
    'Ubuntu 22.10',
    'Network Card',
    'Fiber Optics',
    'Boot Manager',
    'Autopsy Tags',
    'Autopsy Case',
    'Windows Share',
    'Tampered Data',
    'Logical Files',
    'Link Creation',
    'File Explorer',
    'Evidence Disk',
    'Disk Activity',
    'Data Overload',
    'Base Snapshot',
    'pcap Directory',
    'Wireshark pcap',
    'Real-time Look',
    'Output Console',
    'Linux Terminal',
    'Legal Evidence',
    'Ingest Plugins',
    'Ingest Modules',
    'ISO Management',
    'Hash Dump File',
    'ForensicVM.exe',
    'Forensic Image',
    'Cloud Services',
    'Bootable Media',
    'Autopsy Plugin',
    'Set Your Alarms',
    'Session Cookies',
    'Root privileges',
    'Plugin Location',
    'MoonSols DumpIt',
    'BitLocker Drive',
    'X-Ways Forensics',
    'Wizard Interface',
    'Windows Explorer',
    'What-If Analysis',
    'Traffic Analysis',
    'Startup Settings',
    'Samba CIFS share',
    'Plugin Interface',
    'Notable Item Tag',
    'Legal Compliance',
    'Immutable Record',
    'Immediate Reboot',
    'Digital Evidence',
    'Control Bar icon',
    'Chain of Custody',
    'Case Information',
    'UEFI QEMU DVD-ROM',
    'Third-Party Tools',
    'Security Analysis',
    'Protective Shield',
    'Notification Area',
    'Network Isolation',
    'ForensicVM Server',
    'ForensicVM Loader',
    'Forensic Analysis',
    'Executing Plugins',
    'Download Progress',
    'Contributing Code',
    'Browse ForensicVM',
    'Bare metal server',
    'Autopsy framework',
    'evidence.vmdk disk',
    'WebShell Interface',
    'Main Web Interface',
    'Magnet RAM Capture',
    'Host configuration',
    'Gigabit connection',
    'Decoding Protocols',
    'Confirmation Popup',
    'Configuration File',
    'Windows 10 or later',
    'Snapshot Management',
    'Shellinabox project',
    'Plugin Architecture',
    'Patch Accessibility',
    'Main Panel Overview',
    'Fallback Conversion',
    'Evidence Collection',
    'Confirmation Dialog',
    'Command Line Window',
    'Web Screen Interface',
    'Virtual CD-ROM Drive',
    'Import Evidence Disk',
    'Disable Network Card',
    'Debian 11 (Bullseye)',
    'Blue Screen of Death',
    '1980x1080 resolution',
    'Screenshot Management',
    'Modifying Memory Size',
    'Media Panel Separator',
    'Main Toolbar Overview',
    'Main Plugin Interface',
    'MS-DOS Command Window',
    'List Remote Snapshots',
    'List Remote ISO Files',
    'Evidence Preservation',
    'Disk Image or VM File',
    'Direct Copy to Server',
    'Browse and Upload ISO',
    'Reverse SSH connection',
    'Recreate Evidence Disk',
    'Network Troubleshooter',
    'ForensicVM Main Screen',
    'Fine-Tuning ForensicVM',
    'Accessing the WebShell',
    'Readonly windows shares',
    'Picture Analyser Plugin',
    'Password Administration',
    'Media Control Modal Box',
    'ForensicVM / forensicVM',
    'Bypass Windows Password',
    'Power Off/Log Out Option',
    'ForensicVM Client Plugin',
    'Connect with Other Tools',
    'Add Linux Forensic Admin',
    'Media Control Modal Panel',
    'Kali Linux Forensic Tools',
    'Hibernate File Management',
    'Community Plugins Project',
    'Belkasoft Evidence Center',
    'Setting the VM Date & Time',
    'Browsing Available Plugins',
    'Add Windows Forensic Admin',
    'Webscreen Console Main Area',
    'Web Remote Screen Interface',
    'Snapshot Deletion Interface',
    'GRR (Google Rapid Response)',
    'Forensic Administrator User',
    'Elevate to root permissions',
    'DEBUG: Remote ssh to folder',
    '64-bit multi-core processor',
    'Eject ISO / Web Eject CD-ROM',
    'Data Extraction and Analysis',
    'Convert Forensic Image to VM',
    'Forensic Virtual Machine (VM)',
    'Access the Project Repository',
    'VM File (Virtual Machine File)',
    'Media Management in ForensicVM',
    'Insert ISO / Web Insert CD-ROM',
    'Booting without signed drivers',
    'Authentication Bypass Features',
    'Transparency and Accountability',
    'Possible Evidence virtual drive',
    'Forensic SSH Server Redirection',
    'Data Source Processing Progress',
    'C2C (Command and Control) client',
    'Autopsy ForensicVM Client Plugin',
    'WebShell for Remote Administration',
    'KVM / Kernel-based Virtual Machine',
    'Documentation and Chain of Custody',
    'Reset Windows 2003 or XP Activation',
    'Pre-plugin Execution Recommendation',
    'BOOTFIX: Disable Driver Enforcement',
    'Additional Security Bypass Features',
    'UUID (Universally Unique Identifier)',
    'Disable driver signature enforcement',
    'Installation / Installation and Setup',
    'Disable Windows Defender and Firewall',
    'Feature Suggestions and Plugin Requests',
    'Adjusting Screen Scaling: Local Scaling',
    'ForensicVM Main Web Interface or web page',
    'TTPs (Tactics, Techniques, and Procedures)',
    'ForensicVM Webscreen Console Control Toolbar',
    'Web Remote Screen / Web Remote Screen (Shutdown)',
    'Advanced options in the Automatic Repair boot screen',
    'ForensicVM Server Remote Web Screen/Console Control Interface',
    'Autopsy ForensicVM Client Plugin: A Comprehensive Interface Guide',
]

excluded_file = "glossary.rst"

import os

total_files = 0
processed_files = 0

for file_name in os.listdir("."):
    if file_name.endswith(".rst") and file_name != excluded_file:
        total_files += 1

print(f"Total files to process: {total_files}\n")

for file_name in os.listdir("."):
    if file_name.endswith(".rst") and file_name != excluded_file:
        print(f"Processing {file_name}...")

        for term in terms:
            #print(term)
            temp_file = f"{file_name}.temp"
            with open(file_name, "r") as input_file, open(temp_file, "w") as output_file:
                for line in input_file:                    
                    line = line.replace(term, generate_replacement(term))
                    #fixed_line = fix_rst_term_line(line)
                    output_file.write(line)

            os.remove(file_name)
            os.rename(temp_file, file_name)

        processed_files += 1
        print(f"{file_name} processed. ({processed_files}/{total_files})")

print("\nReplacements completed in specified files.")