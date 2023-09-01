# Configuration file for the Sphinx documentation builder.
import sys
import os
# -- Project information

project = 'ForensicVM'
copyright = '2023, Nuno Mourinho'
author = 'Eng. Nuno Mourinho, Eng. Mario Candeias, Dr. Rogério Bravo'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',    
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',	
    'sphinx.ext.autosectionlabel',
    #'sphinx.ext.numfig',
    #'sphinx_autodoc_typehints',
    #'sphinxcontrib.autodocsumm',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_theme_options = {
    # Other options...
    'authors': [
        'Eng. Nuno Mourinho',
        'Eng. Mario Candeias',
        'Dr. Rogério Matos Bravo',
    ],
}

latex_elements = {
    'preamble': r'''
    \usepackage{placeins}
    '''
}

latex_additional_files = ["cover.jpg"]

latex_elements = {
  'preamble': r'''
    \usepackage{graphicx}
    \newcommand{\coverpage}{
      \begin{titlepage}
        \IfFileExists{cover.jpg}{
          \newgeometry{margin=1cm}
             \includegraphics[width=\textwidth]{cover.jpg}
           \restoregeometry
        }{
          \textbf{Cover Image Not Found}
        }
      \end{titlepage}
      \clearpage
      \newpage\null\newpage
    }
  ''',
}

latex_engine = 'pdflatex'
latex_elements = {
    'preamble': r'''
        % Preamble
    ''',
    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering
            \vspace*{40mm} %%% * is used to give space from top
            \IfFileExists{cover.jpg}{
              \includegraphics[width=\textwidth]{cover.jpg}
            }{
              \textbf{Cover Image Not Found}
            }
            \newpage
        \end{titlepage}
        \clearpage
        \pagenumbering{arabic}
    '''
}

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
numfig = True
