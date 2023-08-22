# Welcome to ForensicVM Documentation!

Github User Manual project site status: [![Documentation Status](https://readthedocs.org/projects/forensicvm-autopsy-plugin-user-manual/badge/?version=latest)](https://forensicvm-autopsy-plugin-user-manual.readthedocs.io/en/latest/?badge=latest) [![DOI](https://zenodo.org/badge/675339901.svg)](https://zenodo.org/badge/latestdoi/675339901)


![ForensicVM Logo](docs/ForensicVM.jpg)

**ForensicVM** is a comprehensive project designed to assist forensic investigators in the virtualization of forensic images. By utilizing advanced technologies and tools, ForensicVM simplifies the process of analyzing and examining digital evidence in a virtualized environment.

The project consists of two essential components: the ForensicVM client, which is an Autopsy plugin, and the ForensicVM server. These components work seamlessly together to provide a powerful and efficient forensic virtualization solution.

The ForensicVM server, developed using Django and Python, serves as the backbone of the system. It is recommended to install the server on Debian 11, which in turn should be set up on a dedicated bare metal server. This configuration ensures optimal performance and stability for your forensic investigations.

> **Note:** Installing the ForensicVM server on a hypervisor is not recommended. The ForensicVM server itself acts as the hypervisor, and running it within a nested setup may result in unpredictable behavior and performance issues. To maintain the integrity and reliability of your forensic analysis, it is advised to adhere to the recommended server installation setup.

To get started with ForensicVM, your first step is to install the server. For detailed instructions, please refer to the Installation section, where you'll find step-by-step guidance on setting up the server environment correctly.

Once the server is up and running, you can explore the various capabilities and features of ForensicVM by diving into the Usage Section. This section provides comprehensive information on how to make the most out of the project, including tips, best practices, and real-world scenarios.

I would like to emphasize that ForensicVM is an actively developed project. We're continuously working on enhancing its capabilities, improving performance, and adding new features. Stay tuned for updates and exciting developments as we strive to deliver the most effective and reliable forensic virtualization solution available.

Thank you for choosing ForensicVM. We are confident that it will greatly streamline your forensic investigations and contribute to the success of your work.

[![DOI](https://zenodo.org/badge/675339901.svg)](https://zenodo.org/badge/latestdoi/675339901)


## 📖 Citation

Reference to cite if you use AutopsyForensicVM in a paper:
```
@misc{Mourinho_forensicVmAutopsyUserManual_2023,
doi = {10.5281/ZENODO.8274587},
url = {https://zenodo.org/record/8274587},
author = {Mourinho, Nuno},
language = {en},
title = {nunomourinho/forensicVmAutopsyUserManual: v1.0.0},
publisher = {Zenodo},
year = {2023},
copyright = {European Union Public License 1.2}
}

@software{Mourinho_AutopsyForensicVM_2023,
author = {Mourinho, Nuno},
doi = {10.5281/zenodo.8153316},
month = {07},
title = {{Autopsy ForensicVM Client}},
url = {https://github.com/nunomourinho/AutopsyForensicVM},
year = {2023}
}
