#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from logging_setting.other_module import run


logging.basicConfig(level=logging.DEBUG, filename='basic.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - [line:%(lineno)d]',
                    datefmt='[%Y-%m-%d %H:%M:%S]')

if __name__ == '__main__':
    logging.info("Start")
    run()
    logging.info("Stop")
