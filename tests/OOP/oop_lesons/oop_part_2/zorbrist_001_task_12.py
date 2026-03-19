class MessageArchive:
    def __init__(self):
        self.list_message = []

    def __len__(self):
        return len(self.list_message)

    def add_message(self, text):
        self.list_message.append(text)

    @property
    def last_message(self):
        return self.list_message[-1]


archive = MessageArchive()
archive.add_message("Привет!")
archive.add_message("Как дела?")
print(archive.last_message) # Как дела?
print(len(archive)) # 2