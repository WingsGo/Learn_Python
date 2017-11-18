#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


file_handle = logging.FileHandler('advanced_logging.log', mode='a')
file_format = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s - [line:%(lineno)d]',
                                datefmt='[%Y-%m-%d %H:%M:%S]')
file_handle.setFormatter(file_format)
