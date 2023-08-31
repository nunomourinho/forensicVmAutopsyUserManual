:term:`Netdata` on :term:`ForensicVM Server`
============================

Introduction
------------

:term:`Netdata` is a tool that helps watch over servers and apps in real-time. With :term:`ForensicVM Server`, :term:`Netdata` shows how the server is doing and makes sure everything runs smoothly.

Key Points
----------

- :term:`Real-time Look`: :term:`Netdata` updates every second, helping catch issues fast.

- **Sees Everything**: It checks everything - like how the CPU is used, memory use, disk activity, and how the network is doing.

- **Alerts**: Get warnings if something goes beyond normal levels.

- **Easy-to-Read Charts**: A simple dashboard shows all the info in clear charts.

How to Start with :term:`Netdata` on :term:`ForensicVM Server`
----------------------------------------------

**Installation**:

:term:`Netdata` is already installed on :term:`ForensicVM Server`.

**How to Use the** :term:`Netdata` **Dashboard**:

You can open it from the Autopsy :term:`ForensicVM Client Plugin`:

.. raw:: latex

   \FloatBarrier

.. figure:: img/netdata_0001.jpg
   :alt: Opening :term:`Netdata` through Autopsy
   :align: center
   :width: 500

   Opening :term:`Netdata` through Autopsy

.. raw:: latex

   \FloatBarrier

Or, use the ForensicVM main web page:

.. raw:: latex

   \FloatBarrier

.. figure:: img/netdata_0002.jpg
   :alt: Opening :term:`Netdata` from the main page
   :align: center
   :width: 500

   Opening :term:`Netdata` from the main page

.. raw:: latex

   \FloatBarrier

How :term:`Netdata` Helps with :term:`ForensicVM Server`
----------------------------------------

Example of what you see:

.. raw:: latex

   \FloatBarrier

.. figure:: img/netdata_0003.jpg
   :alt: :term:`Netdata` Dashboard view
   :align: center
   :width: 500

   :term:`Netdata` Dashboard view

.. raw:: latex

   \FloatBarrier

- **CPU**: See how much CPU is being used. If it's too much, maybe add more resources.

- **Memory**: Make sure there's enough RAM for all the tasks.

- :term:`Disk Activity`: Make sure the disk isn’t too busy. If it is, tasks might slow down.

- **Network**: Keep an eye on data coming in and out, especially with big files.

- **Alerts**: Set warnings for important things, like if RAM use is very high.

Making :term:`Netdata` Work for You
---------------------------

- :term:`Set Your Alarms`: Set warnings for things that matter to you.

- **Your Dashboard**: Make a dashboard that shows what's important for your tasks.

- :term:`Connect with Other Tools`: :term:`Netdata` can send alerts to places like Slack, Twilio, or email.


:term:`Netdata` is a great helper for those using :term:`ForensicVM Server`. It watches over things and makes sure all is good. For admins, it's a must-have tool.

.. note::

   To learn more about :term:`Netdata`, visit the [:term:`Netdata` website](https://learn.netdata.cloud/).
