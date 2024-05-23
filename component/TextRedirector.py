class OutputRedirector:
    def __init__(self, textbox, stream):
        self.textbox = textbox
        self.stream = stream

    def write(self, text):
        self.textbox.insert("end", text)
        
    def flush(self):
        pass