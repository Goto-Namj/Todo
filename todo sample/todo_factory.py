from todo import Todo
import time


class TodoFactoryInterface(object):
    def make_todo(self, name, date):
        raise NotImplementedError


class TodoFactory(TodoFactoryInterface):
    def make_todo(self, name, date="default", important=2):
        if self.check_date(date):
            date = self.convert_date(date)
            important = self.conver_important(important)
            todo = Todo(name, date, important)
            return todo
        raise PastDateError

    def check_date(self, date):
        if date == "default":
            return True
        if self.is_past_date(date):
            return False
        return True

    def date_to_int(self, date):
        result = date[:4]+date[5:7]+date[8:10]
        return int(result)

    def convert_date(self, date):
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if date == "default":
            return now_date
        return date

    def is_past_date(self, date):
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        int_date = self.date_to_int(date)
        int_now_date = self.date_to_int(now_date)
        if int_date < int_now_date:
            return True
        return False


class PastDateError(Exception):
    pass