# krbparse_test_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def name1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('a', 'b', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('c', 'd',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('krbparse_test')
  
  fc_rule.fc_rule('name1', This_rule_base, name1,
    (('a', 'b',
      (pattern.pattern_literal('x'),
       contexts.variable('b'),),
      False),),
    (contexts.variable('b'),))


Krb_filename = '..\\pyke\\krb_compiler\\TEST\\krbparse_test.krb'
Krb_lineno_map = (
    ((13, 17), (7, 7)),
    ((18, 19), (9, 9)),
)
