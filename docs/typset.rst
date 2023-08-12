=======
Typset
=======

The following typeset is used in this document, based on:
   1) https://docutils.sourceforge.io/docs/ref/rst/directives.html#topic
   2) https://sublime-and-sphinx-guide.readthedocs.io/en/latest/indices.html
   3) https://docutils.sourceforge.io/docs/user/rst/quickstart.html
   4) https://docutils.sourceforge.io/docs/user/rst/quickref.html

.. DANGER::
   Denotes actions that could result in serious harm or damage.

.. CAUTION::
   Signifies a potential hazard or cautionary advice.

.. ERROR::
   Marks an error in the system that needs rectification.

.. HINT::
   Highlights key information that requires special attention.

.. IMPORTANT::
   Something important to notice!

.. NOTE::
   Offers additional, auxiliary information that may be useful to the reader.

.. TIP::
   Presents a smart or strategic suggestion to achieve a task more effectively.

.. WARNING::
   Warns about a potential pitfall or danger that must be avoided.

.. admonition:: Additional Information

   Provides an extra piece of related, explanatory information.

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

"To Ma Own Beloved Lassie: A Poem on her 17th Birthday", by
Ewan McTeagle (for Lassie O'Shea):

    .. line-block::

        Lend us a couple of bob till Thursday.
        I'm absolutely skint.
        But I'm expecting a postal order and I can pay you back
            as soon as it comes.
        Love, Ewan.

.. parsed-literal::

   ( (title_, subtitle_?)?,
     decoration_?,
     (docinfo_, transition_?)?,
     `%structure.model;`_ )


.. code:: python

  def my_function():
      "just a test"
      print 8/2

.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

   .. container:: custom

   This paragraph might be rendered in a custom way.

.. header:: This space for rent.


.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.

I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around
.. _Python: https://www.python.org/

Copyright |copy| 2023, |ForensicVM (c)| |---|
all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign
.. |ForensicVM (c)| unicode:: ForensicVM U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

.. |date| date:: "%Y/%m/%d"
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/S6V66G2tVr8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

