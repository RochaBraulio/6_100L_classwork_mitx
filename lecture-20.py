# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def find_payment(loan, r, m):
    """Assumes loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))
    
class Mortgage(object):
    """Abstract class for building different kinds of mortgages' def _init_(self, loan, ann_rate, months):
    """Assumes: loan and ann_rate are floats, months an int Creates a new mortgage of size loan, duration months, and annual rate ann_rate"""
    self._loan loan
    self._rate= ann_rate/12 self._months = months
    self._paid [0.0]
    self._outstanding = [loan]
    self._payment = find_payment (loan, self._rate, months) self._legend = None #description of mortgage"""
    
    def make_payment (self):
    """Make a payment"""
    self._paid.append(self._payment)
    reduction = self._payment self._outstanding [-1]*self._rate self._outstanding.append(self._outstanding [-1] - reduction)

def get_total_paid (self):
    """Return the total amount paid so far"""
    return sum(self._paid)
    def _str_(self):
    return self._legend