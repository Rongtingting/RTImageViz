"""ImageRTk: A toolkit for image-based spatial analysis and modeling.
"""

from .version import __version__
from time import gmtime, strftime
print (f'(Running RTImageViz {__version__})')
print (strftime("%Y-%m-%d %H:%M:%S", gmtime()))

# set simplified alias
from . import preprocessing as pp
from . import plot as pl
from . import data
from . import utils