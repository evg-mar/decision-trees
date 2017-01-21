#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:50:12 2017

@author: evgeniy
"""
from decision_tree import ChanceNode, NodeBase
        
chance01 = ChanceNode(value=None, label='Market Favorable', parent=None,
           children = [NodeBase(3200, 'TV Promotion', parent=None),
                      NodeBase(800, 'No TV Promotion', parent=None)],
           weights= [0.1, 0.9])

chance02 = ChanceNode(value=None, label='Market Unfavorable', parent=None,
           children = [NodeBase(400, 'TV Promotion', parent=None),
                      NodeBase(100, 'No TV Promotion', parent=None)],
           weights= [0.01, 0.99])

root_chance = ChanceNode(value=None, label="Root", parent=None,
                         children = [chance01, chance02],
                         weights = [0.4, 0.6])

print("compute expected value of the root")

root_chance.compute_value()

print(root_chance.get_value)
