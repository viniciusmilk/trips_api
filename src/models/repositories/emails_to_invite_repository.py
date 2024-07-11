from typing import Dict, Tuple, List
from sqlite3 import Connection

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, email_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute('''
                       INSERT INTO emails_to_invite
                       (id, email, trip_id)
                       VALUES (?, ?, ?)''',
                       (email_infos['id'], email_infos['email'], email_infos['trip_id']))
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute('SELECT * FROM emails_to_invite WHERE trip_id = ?', (trip_id,))
        emails = cursor.fetchall()
        return emails
    