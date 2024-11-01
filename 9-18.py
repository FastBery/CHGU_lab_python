class Note:
    def __init__(self, mood:str, date:str, note:str):
        if isinstance(mood, str) and isinstance(note, str) and isinstance(date, str):
            self.mood = mood
            self.date = date
            self.note = note
    
    def __str__(self):
        output = f'Mood: {self.mood}\nDate: {self.date}\nNote: {self.note}\n'
        return  output

class Diary:
    def __init__(self, note):
        if isinstance(note, list):
            if all(isinstance(x, Note) for x in note):
                self.note = note
        elif isinstance(note, Note):
            self.note = list(note)
        else:
            raise ValueError('must be Note')
        
    def __str__(self):
        if isinstance(self.note, list):
            output = ''
            for x in self.note:
                output += str(x) + '\n'
            return output
        return str(self.note)

    def add(self, note):
        if isinstance(note, list):
            for x in note:
                self.note.append(x)
        else:
            self.note.append(note)

    def __getitem__(self, n):
        if not isinstance(n, int):
            raise TypeError("Index must be integer")
        if 0 <= n <= len(self.array):
            return self.note[n]
        else:
            raise IndexError("Wrong index")

    def delete(self, n):
        if not isinstance(n, int):
            raise TypeError("Index must be integer")
        if 0 <= n <= len(self.note):
            return self.note.pop(n)
        else:
            raise IndexError("Wrong index")
        
    def update(self, n, note):
        self.note[n] = note

    def note_date(self, date):
        if isinstance(date, str):
            notes = Diary([])
            for x in self.note:
                if x.date == date:
                    notes.add(x)
            return notes
        else:
            raise ValueError('Wrong date')

    def note_mood(self, mood):
        if isinstance(mood, str):
            notes = Diary([])
            for x in self.note:
                if x.mood == mood:
                    notes.add(x)
            return notes
        else:
            raise ValueError('Wrong mood')





note = Note('norm', '1234', 'agsfoighks')
note2 = Note('ok', '560978', 'oykujkopuj')
print(note)
note3 = Note('(', '9398', 'jofgsjnvdbx')
# note.note_date('1234')
diary = Diary([note, note2])
diary.add(note3)
print(diary)
diary.delete(0)
print(diary)
notes = diary.note_mood('ok')
print(notes)
# print(diary)
