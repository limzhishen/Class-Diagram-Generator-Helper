from typing import TextIO


class OutputRedirector:
    def __init__(self, textbox, stream: TextIO):
        self.textbox = textbox
        self.stream = stream

    def write(self, text: str):
        self.textbox.insert("end", text)
        
    def flush(self):
        pass
