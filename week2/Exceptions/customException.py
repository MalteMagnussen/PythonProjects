class NoOneValueError(ValueError):

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


value = 1
some_data = [2, 7, 8, 10, 'aha']
if value in some_data:
    print('Alright!')
else:
    raise NoOneValueError('Oh no, {} is not in {}!'.format(value, some_data))
