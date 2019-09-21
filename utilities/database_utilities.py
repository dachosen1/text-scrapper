import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "create table words(word text not null constraint words_pk primary key, usage_count int default 1 not null)"
        cur.execute(ddl)
        ddl = "create unique index words_word_uindex on words (word)"
        cur.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check if word is in there
            sql = "select count(word) from words where word = '" + word + "' "
            cur.execute(sql)

            count= cur.fetchone()[0]

            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = ' + words'"

            else:
                sql = "insert into words(word) values ('"+ word + "')"

            cur.execute(sql)

        print("Database save complete!")

