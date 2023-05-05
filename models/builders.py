from .routine import Routine
from .timedate import Duration, Time, WEEKDAYS, WEEKENDS

def routine(**kwargs):
    args = {
        'name': kwargs.get('name')
    }
    args['start'] = Time.of(kwargs['start'])
    if kwargs.get('end'):
        args['end'] = Time.of(kwargs['end'])

    if kwargs.get('duration'):
        args['end'] = args['start'].plus(Duration.of(kwargs['duration']))

    if kwargs.get('sticky'):
        args['sticky'] = kwargs['sticky']

    if kwargs.get('sticky_for'):
        args['sticky_for'] = Duration.of(kwargs['sticky_for'])

    if kwargs.get('days'):
        args['days'] = kwargs['days']
    return Routine(**args)
        

def weekday(**kwargs):
    return routine(**kwargs, days=WEEKDAYS)

def weekend(**kwargs):
    return routine(**kwargs, days=WEEKENDS)

def daily(**kwargs):
    return routine(**kwargs)
