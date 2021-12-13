import sys
from camilladsp_plot.validate_config import CamillaValidator
try:
    from matplotlib import pyplot as plt
    from camilladsp_plot.plot_pipeline import plot_pipeline
    #from camilladsp_plot.plot_filters import plot_filters, plot_all_filtersteps
except ImportError:
    plt = None

# Start by validating the config file
file_validator = CamillaValidator()
file_validator.validate_file(sys.argv[1])
errors = file_validator.get_errors()
warnings = file_validator.get_warnings()
config_with_defaults = file_validator.get_processed_config()

svgData = plot_pipeline(config_with_defaults, True)
open('pipeline.svg', 'wb').write(svgData.getvalue())
