#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from logging_setting.advanced_logger import file_handle


def run():
    # # advanced log
    # logger = logging.getLogger(__name__)
    # logger.addHandler(file_handle)
    # logger.setLevel(logging.DEBUG)
    # logger.info("advanced_logging")
    #
    # #basic log
    # logging.info('basic_logging')

    #config log
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.info("Run")
