Virtual Introspection
=========================

Virtual introspection allows the user to access the internal state of a forensicVM. Throuth the use of virtual introspection one can access process state, the process running, the command line that is presently executed, files in memory, handles, the operative system state. 
We achive the virtual introspection using the qemu hability to make memmory snapshots that are analísed througth volatility 3.

Presently the virtual introspection only works on windows operating systems.

The first step to execute virtual introspection is to run the forensicVM until the operating system boots completly. Then you press the Virtual Introspect button on the forensicVM webclient screen:

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0001.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me


After pressing the virtual introspection button, a progress window appears. This progress will automaticaly open the results when the introspection process was completed.

.. raw:: latex

   \FloatBarrier   

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0002.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   
 
The ForensicVM introspection is composed  by seven tabs:
1) Process Tree
2) Command Line Arguments
3) Enviroment Variables
4) Possible malware injection processes
5) Network connections
6) Network services
7) Possible user password hash


1) Process tree: The list of processes that are currently running in the system. Even if the forensicVM is locket on the login screen we can see what are the currently running processes.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0003.jpg
   :alt: <change me>
   :align: center
   :width: 500

      Change me

.. raw:: latex

   \FloatBarrier   

2) Command line arguments: The commands that are or were running and the arguments.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0004.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   

3) Enviroment Variables: The enviroment variables looaded by eache running process

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0005.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   


4) Possible malware ingestion processes: Processes that were injected or run with special priviledges. They could indicate malware injection techniques, but they can also be false positives. Addition attention is needed.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0006.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   

5) Netscan results: List of network open connections. Can be a posible indicator of compromise. For instance, is a address is listed at virustotal.com urls or in https://sitereview.symantec.com it could indicate a connection to a C2C site.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0007.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   

6) Netstat: Running network services. Could indicate compromise if an unknow system is opening ports on the local forensicVM.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0008.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   

7) Possible user password hash: Lists the password hash in memory. This hashes when used in an external site, like crackstation.com could be used to find the user password, facilitating the task of retriving addicional cached evidence in the forensicVM by the forensic investigator.

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0009.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   

Example of the Bart Simpson hash beeing decoded to the original password "bart".

.. raw:: latex

   \FloatBarrier

.. figure:: img/vi-0010.jpg
   :alt: <change me>
   :align: center
   :width: 500

   Change me

.. raw:: latex

   \FloatBarrier   
