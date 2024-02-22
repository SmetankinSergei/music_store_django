class Session:
    def __init__(self):
        self.recipients_list = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None
        self.show_letters_list = []

    def save_mailing(self):
        pass

    def clear_session(self):
        self.recipients_list = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None
        self.show_letters_list = []


session = Session()
