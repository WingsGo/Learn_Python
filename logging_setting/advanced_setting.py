#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from logging_setting.advanced_logger import file_handle
from logging_setting.other_module import run


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handle)
    logger.setLevel(logging.DEBUG)
    logger.info("Start")
    run()
    logger.info("Stop")
