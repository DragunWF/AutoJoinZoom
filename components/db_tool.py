import sqlite3
import os
from .time_getter import TimeGetter
from .utils import Utils


class DatabaseTool:
    def __init__(self):
        dirname = Utils.get_dirname()
        root = os.path.abspath(os.path.join(os.path.dirname(dirname), ".."))
        self.__path = f"{root}\\sql\\db.sqlite3"

        self.__meeting_names = []
        self.__fill_meeting_names()

    def __format_meeting_name(self, name: str) -> str:
        return "_".join(name.lower().split(" "))

    def __detect_plural(word, times) -> str:
        return f"{word}s" if times > 1 else word

    def __get_date_and_hour(self) -> tuple:
        return Utils.get_date_string()[0], Utils.format_hour(TimeGetter.get_hour())

    def __fill_meeting_names(self):
        with sqlite3.connect(self.__path) as db:
            data = db.execute("SELECT name FROM meetings").fetchall()
            self.__meeting_names = [i[0] for i in data]

    def __insert_meeting_with_validation(self, meeting_name: str):
        name = self.__format_meeting_name(meeting_name)
        if not name in self.__meeting_names:
            with sqlite3.connect(self.__path) as db:
                db.execute(f'INSERT INTO meetings (name) VALUES ("{name}")')
                db.commit()
        self.__fill_meeting_names()

    def insert_meeting_join_record(self, meeting_name: str):
        self.__insert_meeting_with_validation(meeting_name)
        name = self.__format_meeting_name(meeting_name)
        meeting_id = self.__meeting_names.index(name) + 1

        date, hour = self.__get_date_and_hour()
        with sqlite3.connect(self.__path) as db:
            db.execute("INSERT INTO meeting_joins (meeting_id, date_joined, hour_joined) " +
                       f'VALUES ({meeting_id}, "{date}", "{hour}")')
            db.commit()

    def insert_program_opened_record(self):
        date, hour = self.__get_date_and_hour()
        with sqlite3.connect(self.__path) as db:
            db.execute("INSERT INTO times_program_opened (date_opened, hour_opened) " +
                       f'VALUES ("{date}", "{hour}")')
            db.commit()

    def display_stats(self):
        meeting_joins, program_opened = None, None
        with sqlite3.connect(self.__path) as db:
            data = db.execute("SELECT * FROM software_stats").fetchall()
            meeting_joins, program_opened = data[0][1], data[0][0]

        times_string = self.__detect_plural("time", program_opened)
        if meeting_joins:
            meeting_string = f"{meeting_joins} {self.__detect_plural('meeting', meeting_joins)}"
        else:
            meeting_string = "no meetings yet"
        Utils.colored_print(f"You have opened this automation bot {program_opened} {times_string} " +
                            f"and have used this bot to join {meeting_string}!", color="cyan")
