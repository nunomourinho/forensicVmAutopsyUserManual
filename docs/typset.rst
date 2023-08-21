========
Typset
========

.. raw::

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

.. raw::

   .. DANGER::
      Denotes actions that could result in serious harm or damage.

.. CAUTION::
   Signifies a potential hazard or cautionary advice.

.. raw::

   .. CAUTION::
      Signifies a potential hazard or cautionary advice.

.. ERROR::
   Marks an error in the system that needs rectification.

.. raw::

   .. ERROR::
      Marks an error in the system that needs rectification.

.. HINT::
   Highlights key information that requires special attention.

.. raw::

   .. HINT::
      Highlights key information that requires special attention.

.. IMPORTANT::
   Something important to notice!

.. raw::

   .. IMPORTANT::
      Something important to notice!

.. NOTE::
   Offers additional, auxiliary information that may be useful to the reader.

.. raw::

   .. NOTE::
      Offers additional, auxiliary information that may be useful to the reader.

.. TIP::
   Presents a smart or strategic suggestion to achieve a task more effectively.

.. raw::

   .. TIP::
      Presents a smart or strategic suggestion to achieve a task more effectively.

.. WARNING::
   Warns about a potential pitfall or danger that must be avoided.

.. raw::

   .. WARNING::
      Warns about a potential pitfall or danger that must be avoided.

.. admonition:: Additional Information

   Provides an extra piece of related, explanatory information.

.. raw::

   .. admonition:: Additional Information

      Provides an extra piece of related, explanatory information.

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

.. raw::

   .. topic:: Topic Title

      Subsequent indented lines comprise
      the body of the topic, and are
      interpreted as body elements.

.. sidebar:: Optional Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

.. raw::

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

.. raw::

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

.. raw::

   .. parsed-literal::

      ( (title_, subtitle_?)?,
        decoration_?,
        (docinfo_, transition_?)?,
        `%structure.model;`_ )

.. code:: python

  def my_function():
      "just a test"
      print 8/2

.. raw::

   .. code:: python

     def my_function():
         "just a test"
         print 8/2

.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

.. raw::

   .. math::

     α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

.. raw::

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

.. raw::

   .. compound::

      The 'rm' command is very dangerous.  If you are logged
      in as root and enter ::

          cd /
          rm -rf *

      you will erase the entire contents of your file system.

      .. container:: custom

      This paragraph might be rendered in a custom way.

.. header:: This space for rent.

.. raw::

   .. header:: This space for rent.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/S6V66G2tVr8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

