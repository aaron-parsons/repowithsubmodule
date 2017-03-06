'''
some utils for the test
'''

import inspect

def get_test_data_path(fname):
    path = inspect.stack()[0][1].split('repoNoData')[0]+'repo4data/test_data/%s'
    return path % fname