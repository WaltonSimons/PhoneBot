import MySQLdb as mysql


class Database(object):
    """Interface to local mysql base with metods for easy extracting text messages
    from database.
    """

    def __init__(self, host, username, password, dbname):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname

        try:
            self.connector = mysql.connect(host, username, password, dbname)
            self.cursor = self.connector.cursor()
        except mysql.Error, e:
            print "Error {}: {}".format(e.args[0], e.args[1])

    def close_connection(self):
        self.connector.close()

    def get_inbox_sms(self):
        query = "SELECT * FROM inbox"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result

    def clear_inbox_table(self):
        query = "DELETE FROM inbox"
        self.cursor.execute(query)
