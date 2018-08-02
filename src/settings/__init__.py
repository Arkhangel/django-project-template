from .default import *

# Set local_settings if exists
try:
    from .local import *
except ImportError:
    pass
