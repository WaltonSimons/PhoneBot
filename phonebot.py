import database
import smsd

class Bot(object):

    def __init__(self):
        self.sms = smsd.smsd('config/gammu-smsdrc-sql')
        self.db = database.Database('', '', '', '')
        self.smslist = []

        self.plugins = []

    def load_new_messages(self):
        raw_sms = self.db.get_inbox_sms()

        for message in raw_sms:
            self.smslist.append({'Number' : message[3], 'Text' : message[2]})

    def process_messages(self):
        for sms in self.smslist:
            for p in self.plugins:
                p.message(sms)
