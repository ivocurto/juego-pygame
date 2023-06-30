import sqlite3
class Ranking:
    def __init__(self, player_name, score, lvl):
        self.database_name = "ranking_database.db"
        self.database_flag = False

        with sqlite3.connect(self.database_name) as conection:
            try:
                sentence = """
                            create table Ranking
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score int,
                            level int
                            )
                """
                conection.execute(sentence)
                try:
                    sentence = """
                                insert into Ranking(nombre, score, level) values(?,?,?)
                                """
                    conection.execute(sentence, (player_name, score, lvl))
                except:
                    pass
            except:
                sentence = """
                            insert into Ranking(nombre, score, level) values(?,?,?)
                            """
                conection.execute(sentence, (player_name, score, lvl))


    def show_top5_list(lvl):
        database_name = "ranking_database.db"

        with sqlite3.connect(database_name) as conection:
            try:
                sentence = "select * from Ranking WHERE level = ? order by score desc limit 5"
                cursor = conection.execute(sentence, (lvl,))
                top5 = []
                for fila in cursor:
                    dict = {"name": fila[1], "score": fila[2], "level": fila[3]}
                    top5.append(dict)
                return top5
            except:
                with open("log.txt", "a", encoding="utf-8") as file:
                    file.write(f"No hay ningun usuario en el top del nivel {lvl}\n")
