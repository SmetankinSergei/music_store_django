class Session:
    def __init__(self):
        self.recipients_list = []
        self.show_letters_list = []
        self.week_days = []
        self.months_days = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None
        self.mailing_time = None

    def save_mailing(self):
        pass

    def mailing_done(self):
        pass

    def clear_session(self):
        self.recipients_list = []
        self.show_letters_list = []
        self.week_days = []
        self.months_days = []
        self.letter = None
        self.mailing = None
        self.mailing_type = None
        self.mailing_time = None


session = Session()
