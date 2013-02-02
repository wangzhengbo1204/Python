#-*- coding:utf-8 -*-
'''
Created on 2011-12-17

@author: GFTOwenWang
'''

import decimal

def func1():
    fmt = '{0:<20} {1:<20}'
    print fmt.format('Input', 'Output')
    print fmt.format('-' * 20, '-' * 20)
    
    # Integer
    print fmt.format(5, decimal.Decimal(5))
    
    # String
    print fmt.format('3.14', decimal.Decimal('3.14'))
    
    # Float
    print fmt.format(repr(0.1), decimal.Decimal(str(0.1)))
    
    # Float
    print fmt.format(repr(10000000000.93), decimal.Decimal(repr(10000000000.93)))
    
    # Float
    print fmt.format(repr(1000000000000.93), decimal.Decimal(repr(1000000000000.93)))
    
    print decimal.Decimal(repr(1000000000000.93)).ROUND_CEILING()
    
def func2():
    context = decimal.getcontext()
    
    ROUNDING_MODES = [ 
        'ROUND_CEILING', 
        'ROUND_DOWN',
        'ROUND_FLOOR', 
        'ROUND_HALF_DOWN', 
        'ROUND_HALF_EVEN',
        'ROUND_HALF_UP',
        'ROUND_UP',
        'ROUND_05UP',
        ]
    
    header_fmt = '{0:20} {1:^10} {2:^10} {3:^10}'
    
    print 'POSITIVES:'
    print
    
    print header_fmt.format(' ', '1/8 (1)', '1/8 (2)', '1/8 (3)')
    print header_fmt.format(' ', '-' * 10, '-' * 10, '-' * 10)
    for rounding_mode in ROUNDING_MODES:
        print '{0:20}'.format(rounding_mode),
        for precision in [ 1, 2, 3 ]:
            context.prec = precision
            context.rounding = getattr(decimal, rounding_mode)
            value = decimal.Decimal(1) / decimal.Decimal(8)
            print '{0:<10}'.format(value),
        print
    
    print
    print 'NEGATIVES:'
    
    print header_fmt.format(' ', '-1/8 (1)', '-1/8 (2)', '-1/8 (3)')
    print header_fmt.format(' ', '-' * 10, '-' * 10, '-' * 10)
    for rounding_mode in ROUNDING_MODES:
        print '{0:20}'.format(rounding_mode),
        for precision in [ 1, 2, 3 ]:
            context.prec = precision
            context.rounding = getattr(decimal, rounding_mode)
            value = decimal.Decimal(-1) / decimal.Decimal(8)
            print '{0:<10}'.format(value),
        print


def func3():
    with decimal.localcontext() as c:
        c.prec = 2
        print 'Local precision:', c.prec
        print '3.14 / 3 =', (decimal.Decimal('3.14') / 3)
        print '3.14 / 3 =', (decimal.Decimal('3.14') / 3)
    
    print
    print 'Default precision:', decimal.getcontext().prec
    print '1000000000000.93 =', (decimal.Decimal('1000000000000.93'))

if __name__ == '__main__':
    func3()
