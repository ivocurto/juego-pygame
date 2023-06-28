import sqlite3
class Ranking:
    def __init__(self, player_name, score, lvl):
        match lvl:
            case 1:
                database_name = "ranking_database.db"
            case 2:
                database_name = "ranking_database2.db"
            case 3:
                database_name = "ranking_database3.db"

        with sqlite3.connect(database_name) as conection:
            try:
                sentence = """
                            create table Ranking
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            score int
                            )
                """
                conection.execute(sentence)
                sentence = """
                            insert into Ranking(nombre, score) values(?,?)
                            """
                conection.execute(sentence, (player_name, score))
            except:
                sentence = """
                            insert into Ranking(nombre, score) values(?,?)
                            """
                conection.execute(sentence, (player_name, score))


    def show_top5_list(lvl):
        match lvl:
            case 1:
                database_name = "ranking_database.db"
            case 2:
                database_name = "ranking_database2.db"
            case 3:
                database_name = "ranking_database3.db"

        with sqlite3.connect(database_name) as conection:
            try:
                sentence = "select * from Ranking order by score desc limit 5"
                cursor = conection.execute(sentence)
                top5 = []
                for fila in cursor:
                    dict = {"name": fila[1], "score": fila[2]}
                    top5.append(dict)
                return top5
            except:
                print(f"Error, no hay ningun usuario en el top o no existe la base de datos del nivel {lvl}")

