#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a and b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    haList = [None for i in range(2)]  # 


    ha0 = halfAdder(a, b, s[0], s[1]) 
    ha1 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2] # 


    return instances()



@block
def adder2bits(x, y, soma, carry): # x e y sao vetores.
    carry0 = Signal(bool(0)) 
    h0 = halfAdder(x[0],y[0],soma[0],carry0) # ativam comb
    h1 = fullAdder(x[1],y[1],carry0, soma[1],carry)

    return instances()


@block
def adder(x, y, soma, carry):
    l = len(x)
    faList = [None for i in range(l)]
    carlist = [Signal(bool(0)) for i in range(l+1)]

    for i in range(0,l) :
        faList[i] = fullAdder(x[i], y[i], carlist[i-1], soma[i],carlist[i])

    @always_comb
    def comb():
        carry.next = carlist[l-1]

    return instances()


@block
def adderIntbv(x, y, soma, carry):
    @always_comb
    def comb():
        sum = x + y
        soma.next = sum
        if sum > x.max - 1:
            carry.next = 1
        else:
            carry.next = 0

    return comb
