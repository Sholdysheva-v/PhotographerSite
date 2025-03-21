from datetime import datetime

class DateOrder:
    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')
