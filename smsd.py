import gammu.smsd
import thread


class smsd(object):
    """Starts gammu in another thread so the bot can interpret incoming sms"""

    def __init__(self, configpath):
        self.sms = gammu.smsd.SMSD(configpath)
        self.thread = None

    def start(self):
        self.thread = thread.start_new_thread(self.sms.MainLoop, ())

    def stop(self):
        self.sms.Shutdown()

    def inject_sms(self, phonenumber, message):
        smsinfo = {
                'Class': -1,
                'Unicode': True,
                'Entries':  [
                    {
                        'ID': 'ConcatenatedTextLong',
                        'Buffer': message
                    }
                ]}

        encoded = gammu.encode(smsinfo)

        for message in encoded:
            message['SMSC'] = {'Location': 1}
            message['Number'] = phonenumber

        self.sms.InjectSMS(encoded)