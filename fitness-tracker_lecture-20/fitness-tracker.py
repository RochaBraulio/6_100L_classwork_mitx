#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:48:28 2025

@author: rocha
"""

class Workout(object):
    """
    Object to record a workout
    """
    def __init__(self, start, end, calories):
        self._start_time = start
        self._end_time = end
        self._calories = calories
        self._icon = '🥵'
        self._kind = 'Workout'
    def get_calories(self):
        return self._calories
    def get_start_time(self):
        return self._start_time
    def get_end_time(self):
        return self._end_time
    def set_calories(self, calories):
        self._calories = calories
    def set_start_time(self, start):
        self._start_time = start
    def set_end_time(self, end):
        self._end_time = end