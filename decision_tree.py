#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:23:21 2017

@author: evgeniy
"""


class NodeBase(object):    
    def __init__(self, value=None, label=None, parent=None, children=[]):
        self._children = children
        self._label = label
        self._parent = parent
        self._value = value
        
        for child in self._children:
            child._parent = self
      
    def __str__(self):
        return "id: %d, label: %s, value: %s, type: %s" % \
                (id(self), self._label, str(self._value), str(self.__class__))

    @property
    def get_value(self):
        return self._value
        
    def set_value(self, value):
        self._value = value

    @property
    def is_leaf(self):
        return len(self._children) == 0
        
    def compute_value(self):
        # recursion
        if self.is_leaf:
            assert(self._value is not None)
            return

        for child in self._children:
            child.compute_value()

        self._value = self.get_value_from_children()
            
    def update_parents(self):
        # the weights or some of the childrens's nodes 
        # can be edited - some new or removed or changed...
        node = self
        node._value = node.get_value_from_children
        while(node._parent is not None):
            node = node._parent
            node._value = node.get_value_from_children

    def get_value_from_children(self):
        return self.get_value

    @property
    def get_height(self):
        # recursion
        if self.is_leaf:
            return 1
        return 1 + max(child.get_height for child in self._children)

################################            
class DecisionNode(NodeBase):
    def __init__(self, value=None, label=None, 
                 parent=None, 
                 children=[], penalties=None):
        if penalties is None:
            if len(children) == 0:
                penalties = []
            else:
                penalties = [0.0]*len(children)

        assert len(children) == len(penalties), \
               "len(children)=%d, len(penalties)=%d"%(len(children),len(penalties))

        super(DecisionNode, self).__init__(value, label, parent, children)
        self._penalties = penalties
        
    def get_value_from_children(self):
        return max([(child.get_value - penalty) \
                    for child, penalty in zip(self._children, self._penalties)])


################################            
class ChanceNode(NodeBase):
    
    def __init__(self, value=None, label=None, parent=None, children=[], weights=[]):
        assert len(children) == len(weights), \
               "len(children)=%d, len(weights)=%d"%(len(children),len(weights))
        super(ChanceNode, self).__init__(value, label, parent, children)
        self._weights = weights    

    def get_value_from_children(self):
        return sum([(child.get_value * weight) \
                    for child, weight in zip(self._children, self._weights)])
        
################################