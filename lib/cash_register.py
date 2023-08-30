#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, ones, twos, fives, tens, twenties):
    self._ones = ones
    self._twos = twos
    self._fives = fives
    self._tens = tens
    self._twenties = twenties
 
  def __str__(self):
    return "CashRegister = {0} {1} {2} {3} {4}".format(self._ones, self._twos, self._fives, self._tens, self._twenties)
  
  def get_total(self):
    return self._ones + self._twos * 2 + self._fives * 5 + self._tens * 10 + self._twenties * 20
     
  
  def apply_discount (self, discount):
    if discount > 0:
      return self.get_total() * (1 - discount/100)
    else:
      return self.get_total()
    
  def void_last_transaction(self):
    self._total -= self._last_transaction
    self._last_transaction = 0