"""Configure tests."""

# Standard library imports
import os
import sys

# Third party imports
# n/a

# Local application imports
# n/a

# Allow local application imports from the project directory
project_path = os.path.join(
    os.path.dirname(__file__),  # /tests
    "..",  # /
)

if project_path not in sys.path:

    sys.path.append(project_path)

