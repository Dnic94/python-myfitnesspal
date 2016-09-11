import datetime


class Note(unicode):
    def __new__(cls, note_data):
        self = super(Note, cls).__new__(cls, note_data['body'])
        self._note_data = note_data
        return self

    @property
    def type(self):
        return self._note_data.get('type', None)

    @property
    def date(self):
        return datetime.datetime.strptime(
            self._note_data.get('date'),
            '%Y-%m-%d',
        ).date()

    def as_dict(self):
        return self._note_data
