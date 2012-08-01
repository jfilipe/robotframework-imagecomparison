from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from keywords import ImageComparisonKeywords

__version__ = '0.1'


class ImageComparisonLibrary(ImageComparisonKeywords):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, baseline_path):
        self._driver = BuiltIn().get_library_instance('Selenium2Library')
        logger.debug('setting baseline_path to: %s' % baseline_path)
        self._baseline_path = baseline_path
