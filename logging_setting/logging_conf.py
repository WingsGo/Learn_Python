#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import logging.config
from logging_setting.other_module import run

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    logger.info("Start")
    run()
    logger.info("Stop")