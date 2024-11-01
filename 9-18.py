class Note:
    def __init__(self, mood:str, date:str, note:str):
        if isinstance(mood, str) and isinstance(note, str) and isinstance(date, str):
            self.mood = mood
            self.date = date
            self.note = note
    
    def __str__(self):
        output = f'Mood: {self.mood}\nDate: {self.date}\nNote: {self.note}'
        return  output

class Diary:
    def __init__(self, note):
        if isinstance(note, list):
            if all(isinstance(x, Note) for x in note):
                self.note = note
        elif isinstance(note, Note):
            self.note = note
        else:
            raise ValueError('must be Note')
        
    def __str__(self):
        if isinstance(self.note, list):
            output = ''
            return (output+=str(x) for x in self.note)
        return str(self.note)

    def add(self):
        self.note

note = Note('norm', '1234', 'agsfoighks')
note2 = Note('ok', '560978', 'oykujkopuj')
print(note)

diary = Diary([note, note2])
print(diary)
