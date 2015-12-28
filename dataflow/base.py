#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: base.py
# Author: Yuxin Wu <ppwwyyxx@gmail.com>

from abc import abstractmethod

__all__ = ['DataFlow']

class DataFlow(object):
    # TODO private impl
    @abstractmethod
    def get_data(self):
        """
        A generator to generate data as tuple.
        """

    @abstractmethod
    def size(self):
        """
        Size of this data flow.
        """

