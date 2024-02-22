class Session:
    def __init__(self):
        self.recipients_list = []
        self.show_letters_list = []
        self.week_days = []
        self.months_days = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None

    def save_mailing(self):
        pass

    def mailing_done(self):
        pass

    def clear_session(self):
        self.recipients_list = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None
        self.show_letters_list = []


session = Session()
