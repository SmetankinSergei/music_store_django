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
        self.mailing_start = None
        self.mailing_finish = None

    def clear_session(self):
        self.__init__()


session = Session()
