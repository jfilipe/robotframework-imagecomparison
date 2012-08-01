import Image
import ImageChops
import math
import operator
import uuid
import tempfile
import os

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class ImageComparisonKeywords(object):
    def match_baseline_image(self, baseline_image):
        browser = BuiltIn().get_variable_value('${BROWSER}')
        clean_browser_name = self._clean_browser_name(browser)
        logger.debug("browser: %s" % browser)
        relative_baseline_image_path = '{0}/{1}/{2}.png'.format(self._baseline_path, clean_browser_name, baseline_image)
        baseline_image_path = os.path.abspath(relative_baseline_image_path)
        logger.debug("baseline_image_path: %s" % baseline_image_path)

        should_update_baseline = BuiltIn().get_variable_value('${UPDATE_BASELINE}')
        logger.debug("should_update_baseline: %s" % should_update_baseline)
        if should_update_baseline == 'True':
            logger.debug("updating baseline image: %s" % baseline_image_path)
            self._update_baseline_image(baseline_image_path)

        temp_image_path = '{0}/match-{1}.png'.format(tempfile.gettempdir(), uuid.uuid4())
        logger.debug("temp_image_path: %s" % temp_image_path)
        self._capture_fixed_dimension_page_screenshot(temp_image_path)

        self.compare_images(temp_image_path, baseline_image_path)

    def compare_images(self, im1, im2):
        """
        Calculate the exact difference between two images.
        """
        im1 = Image.open(im1)
        im2 = Image.open(im2)
        if ImageChops.difference(im1, im2).getbbox() is not None:
            raise AssertionError("Image: %s is different from baseline: %s" % (im1.filename, im2.filename))

    def calculate_rms_difference(self, im1, im2):
        """
        Calculate the root-mean-square difference between two images.
        If the images are exactly identical, the value is zero.
        """
        h = ImageChops.difference(im1, im2).histogram()
        # calculate rms
        return math.sqrt(reduce(operator.add, map(lambda h, i: h * (i ** 2), h, range(256))) / (float(im1.size[0]) * im1.size[1]))

    def _update_baseline_image(self, image_path):
        logger.debug('Updating baseline image: {0}'.format(image_path))
        self._capture_fixed_dimension_page_screenshot(image_path)

    def _capture_fixed_dimension_page_screenshot(self, filename):
        logger.debug("capturing fixed shot for: %s" % filename)
        self._set_window_size(1300, 500)
        self._driver.capture_page_screenshot(filename)
        self._driver.maximize_browser_window()

    def _clean_browser_name(self, dirty):
        supported_browsers = [
            'iexplore',
            'firefox',
            'googlechrome',
        ]
        for browser in supported_browsers:
            if browser in dirty.lower():
                return browser
        return 'unknown'

    def _set_window_size(self, width, height):
        self._driver._cache.current.set_window_size(width, height)

    def get_window_size(self):
        return self._driver._cache.current.get_window_size()
