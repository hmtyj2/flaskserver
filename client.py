import dbModule


class ClientDb:
    def __init__(self):
        self.db_class = dbModule.Database()

    # INSERT
    def insert(self,t_name,title,contents):


        sql = "INSERT INTO "+t_name+" (title,contents) \
                    VALUES(%s,%s)"
        self.db_class.execute(sql,(title,contents))
        self.db_class.commit()

        return


    # SELECT
    def select_all(self,t_name):

        sql = "SELECT * \
                    FROM parsing_db.%s" % t_name
        row = self.db_class.executeAll(sql)

        return row  # list(dict1,dict2 ... dict n) 1dict = 1 column

    def select(self,t_name,col_name):

        sql = "SELECT "+col_name+" \
                    FROM parsing_db.%s" % t_name
        row = self.db_class.executeAll(sql)

        return row  # list(dict1,dict2 ... dict n) 1dict = 1 column

    # UPDATE
    def update(self,t_name,title,content):

        sql = "UPDATE parsing_Db.%s \
                    SET contents='%s' \
                    WHERE title='%s'" % (t_name,content,title)
        self.db_class.execute(sql)
        self.db_class.commit()

        sql = "SELECT title, contents \
                    FROM parsing_db.%s" % t_name
        row = self.db_class.executeAll(sql)
        print(row)

        return

    def createTable(self,t_name):

        sql = "CREATE TABLE %s (\
                    idx INT PRIMARY KEY AUTO_INCREMENT, \
                    title TEXT(3000),\
                    contents TEXT(3000))" % t_name


        self.db_class.execute(sql)
        self.db_class.commit()

        '''
        sql = "SELECT title, contents \
                    FROM parsing_db.%s" % t_name
        row = self.db_class.executeAll(sql)

        print(row)
        '''

        return
pass