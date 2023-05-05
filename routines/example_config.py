from models.builders import daily, weekday, weekend


routines = [
    weekday(start='09:00am', duration='1h', name='Wake Up', sticky=True),
    weekend(start='10:00am', duration='1h', name='Wake Up', sticky=True),
    weekday(start='12:15pm', duration='30m', name='Lunch', sticky_for='1h'),
    weekend(start='11:30am', end='1pm', name='Lunch'),
    weekday(start='5:30pm', end='7pm', name='Dinner'),
]

options = {
    'switchover_time': '06:00am'
}