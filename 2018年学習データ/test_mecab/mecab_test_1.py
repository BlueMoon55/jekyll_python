# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:25:10 2018

@author: t6014250
"""

from negima import MorphemeMerger
mm = MorphemeMerger()
mm.set_rule_from_csv('noun.csv')

words, _ = mm.get_rule_pattern('約5000人が国立競技場に駆けつけた')
print(words)