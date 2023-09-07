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
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_logo = '_static/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

latex_additional_files = ["cover.jpg", "backcover.jpg"]

latex_engine = 'pdflatex'

latex_elements = {
    'preamble': r'''
        \usepackage{graphicx}
        \usepackage{placeins}
        \usepackage[absolute]{textpos}
        \setlength{\TPHorizModule}{1cm}
        \setlength{\TPVertModule}{1cm}
        \usepackage{etoolbox}
    ''',
    'maketitle': r'''
        \begin{titlepage}
            \thispagestyle{empty}
            \begin{textblock}{20}(0,0)
                \IfFileExists{cover.jpg}{
                  \includegraphics[width=\paperwidth,height=\paperheight]{cover.jpg}
                }{
                  \textbf{Cover Image Not Found}
                }
            \end{textblock}
        \end{titlepage}
        \clearpage
        \newpage\null\thispagestyle{empty}\clearpage
        \newpage\null\thispagestyle{empty}\clearpage
        \newpage\null\thispagestyle{empty}\clearpage
        \pagenumbering{arabic}
        \AtEndDocument{
            \clearpage
            \newpage\null\thispagestyle{empty}\clearpage
            \newpage\null\thispagestyle{empty}\clearpage
            \begin{textblock}{20}(0,0)
                \IfFileExists{backcover.jpg}{
                  \includegraphics[width=\paperwidth,height=\paperheight]{backcover.jpg}
                  \textbf{2023}
                }{
                  \textbf{Back Cover Image Not Found}
                }
            \end{textblock}
        }
    '''
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
numfig = True
