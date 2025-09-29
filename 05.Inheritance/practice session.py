class Date(object):
    def get_date(self):
        return "2016-05-14"


class Time(Date):
    def get_time(self):
        return "07:00:00"


dt = Date()
tm = Time()

print('просто дата',dt.get_date())
print('просто время',tm.get_time())
print('просто дата и время через класс Time',tm.get_date() + ' ' + tm.get_time())

