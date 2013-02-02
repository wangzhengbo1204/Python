# krbparse_test_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from compiled_krb import krbparse_test_plans

def name2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('a', 'b', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "krbparse_test.name2: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(2).match_data(context, context, x_1):
              raise AssertionError("krbparse_test.name2: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            with engine.prove(rule.rule_base.root_name, 'x', context,
                              (rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "krbparse_test.name2: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(6).match_data(context, context, x_2):
                  raise AssertionError("krbparse_test.name2: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def name3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('a', 'b', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is not None, \
              "krbparse_test.name3: expected plan from when clause 1"
            mark1 = context.mark(True)
            if not rule.pattern(2).match_data(context, context, x_1):
              raise AssertionError("krbparse_test.name3: plan match to $plan#1 failed in when clause 1")
            context.end_save_all_undo()
            with engine.prove(rule.rule_base.root_name, 'x', context,
                              (rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "krbparse_test.name3: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(6).match_data(context, context, x_2):
                  raise AssertionError("krbparse_test.name3: plan match to $foo_fn failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
                context.undo_to_mark(mark2)
            context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('krbparse_test')
  
  bc_rule.bc_rule('name2', This_rule_base, 'x',
                  name2, krbparse_test_plans.name2,
                  (pattern.pattern_literal(1),
                   contexts.variable('c'),
                   pattern.pattern_literal((1, 'b',)),
                   pattern.pattern_tuple((pattern.pattern_literal(1), pattern.pattern_literal('b'), contexts.variable('c'),), None),),
                  ('plan', 'd',),
                  (pattern.pattern_literal('x'),
                   contexts.variable('c'),
                   contexts.variable('plan#1'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal(3),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('name3', This_rule_base, 'x',
                  name3, krbparse_test_plans.name3,
                  (pattern.pattern_literal(1),
                   contexts.variable('c'),
                   pattern.pattern_literal((1, 'b',)),
                   pattern.pattern_tuple((pattern.pattern_literal(1), pattern.pattern_literal('b'), contexts.variable('c'),), None),),
                  ('d',),
                  (pattern.pattern_literal('x'),
                   contexts.variable('c'),
                   contexts.variable('plan#1'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal(3),
                   contexts.variable('foo_fn'),))


Krb_filename = '..\\pyke\\krb_compiler\\TEST\\krbparse_test.krb'
Krb_lineno_map = (
    ((17, 21), (12, 12)),
    ((23, 33), (14, 14)),
    ((34, 45), (17, 17)),
    ((60, 64), (24, 24)),
    ((66, 76), (26, 26)),
    ((77, 88), (29, 29)),
)
