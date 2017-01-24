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