# krbparse_test_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def name2(context, a, b, c):
  line1
  line2 (context['d']) end2
  some (context['plan'])(stuff) \
                  and more stuff fail here
  a (context['plan']) b

def name3(context):
  line1
  line2 (context['d']) end2


Krb_filename = '..\\pyke\\krb_compiler\\TEST\\krbparse_test.krb'
