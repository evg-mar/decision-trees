#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:50:12 2017

@author: evgeniy
"""
from decision_tree import ChanceNode, DecisionNode, NodeBase
        

#####################
researchGoodMarket = DecisionNode(value=None, label='Market Favorable', parent=None,
           children = [NodeBase(800.0, 'Invest', parent=None),
                      NodeBase(0.0, 'Not Invest', parent=None)],
           penalties = [300.0, 0.0])

researchBadMarket = DecisionNode(value=None, label='Market Unfavorable', parent=None,
           children = [NodeBase(100.0, 'Invest', parent=None),
                      NodeBase(0.0, 'Not Invest', parent=None)],
           penalties = [300.0, 0.0])
######
do_MktResearch = ChanceNode(value=None, label="Do Mkt Research", parent=None,
                           children = [researchGoodMarket, researchBadMarket],
                           weights = [0.4, 0.6])
####################
do_InvestChance = ChanceNode(value=None, label='Invest choice', parent=None,
           children = [NodeBase(800.0, 'Market Favorable', parent=None),
                      NodeBase(100.0, 'Market Unfavorable', parent=None)],
           weights = [0.4, 0.6])

doNot_InvestChance = ChanceNode(value=None, label='Invest choice', parent=None,
           children = [NodeBase(0.0, 'Market Favorable', parent=None),
                      NodeBase(0.0, 'Market Unfavorable', parent=None)],
           weights = [0.4, 0.6])
#######
doNot_MktResearch = DecisionNode(value=None, label="No Mkt Research", parent=None,
                            children = [do_InvestChance, doNot_InvestChance],
                            penalties = [300.0, 0.0])
#####################

rootDecision = DecisionNode(value=None, label="Do/Not Mkt Research", parent=None,
                            children = [do_MktResearch, doNot_MktResearch],
                            penalties = [50.0, 0.0])


print("compute expected value of the root")

rootDecision.compute_value()

print(rootDecision.get_value)


