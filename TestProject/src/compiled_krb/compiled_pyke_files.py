# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'pyke\\krb_compiler\\compiler.krb'):
           [1323166115.7590001, 'compiler_bc.py'],
         ('', '', 'pyke\\krb_compiler\\TEST\\krbparse_test.krb'):
           [1323166115.7720001, 'krbparse_test_fc.py', 'krbparse_test_plans.py', 'krbparse_test_bc.py'],
         ('', '', 'pyke\\krb_compiler\\TEST\\kfbparse_test.kfb'):
           [1323166115.8429999, 'kfbparse_test.fbc'],
        },
        compiler_version)

