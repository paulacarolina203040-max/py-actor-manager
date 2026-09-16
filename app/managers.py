import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            query = (
                f"INSERT INTO {self.table_name} "
                "(first_name, last_name) VALUES (?, ?);"
            )
            cursor.execute(query, (first_name, last_name))
            connection.commit()

    def all(self) -> list[Actor]:
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            query = (
                f"SELECT id, first_name, last_name "
                f"FROM {self.table_name};"
            )
            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                return []

            return [
                Actor(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2]
                )
                for row in rows
            ]

    def update(
        self,
        pk: int,
        new_first_name: str,
        new_last_name: str
    ) -> None:
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            query = (
                f"UPDATE {self.table_name} "
                "SET first_name = ?, last_name = ? "
                "WHERE id = ?;"
            )
            cursor.execute(
                query,
                (new_first_name, new_last_name, pk)
            )
            connection.commit()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            query = (
                f"DELETE FROM {self.table_name} "
                "WHERE id = ?;"
            )
            cursor.execute(query, (pk,))
            connection.commit()
