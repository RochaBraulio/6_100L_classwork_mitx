#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 16:48:28 2025

@author: rocha
"""

from dateutil import parser

class Workout(object):
    """
    Object to record a workout
    """
    calories_hour = 200 #estimate of calories burned per unit of time
    
    
    def __init__(self, start, end, calories=None):
        self._start_time = parser.parse(start)
        self._end_time = parser.parse(end)
        self._calories = calories
        self._icon = '🥵'
        self._kind = 'Workout'
    def get_calories(self):
        if self._calories == None:
            return (Workout.calories_hour*
                    (self._end_time - self._start_time).
                    total_seconds()/3600
                    ) 
        else:
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
        
# ============================================================================ 
# For testing
# ============================================================================ 

start = '2025/09/24 15:35'
end = '2025/09/24 16:28'

w1 = Workout(start, end)
w2 = Workout(start, end, 137)

w3 = Workout('2021/01/1 3:30 PM', '2021/01/1 4:00 PM')
print(f'Total calories burned during w3 was {w3.get_calories()}\n')
w4 = Workout('2021/01/1 3:35 PM', '2021/01/1 4:00 PM', 300)
print(f'Total calories burned during w4 was {w4.get_calories()}\n')

 