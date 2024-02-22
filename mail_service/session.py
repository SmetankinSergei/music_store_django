class Session:
    def __init__(self):
        self.recipients_list = []
        self.letter = None
        self.mailing = None

    def save_mailing(self):
        pass

    def clear_session(self):
        self.recipients_list = []
        self.letter = None
        self.mailing = None


session = Session()
