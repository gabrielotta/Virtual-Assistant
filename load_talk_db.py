import sqlite3

class Data():
    def __init__(self):
        self.connection = sqlite3.connect('talks.db')
        self.cursor = self.connection.cursor()

    def get_response(self, context):
        self.cursor.execute("select response from responses where context = '{}'".format(context))
        return self.cursor.fetchall()

    def get_context(self, command_text):
        self.cursor.execute("select context from responses where command = '{}'".format(command_text))
        return self.cursor.fetchone()[0]

    def get_commands(self):
        self.cursor.execute('select command from responses')
        return self.cursor.fetchall()

    def finish_basic_learn(self, command, context, response):
        try:
            self.cursor.execute('insert into responses (command, context, response) values (?, ?, ?)', (command, context, response))
            self.connection.commit()
            return ""
        except sqlite3.IntegrityError:
            return "Isso eu já aprendi. Vamos do começo?"

    ### todo: ---> metodos para "aprendizado", onde inserimos novas informações nas tabelas
