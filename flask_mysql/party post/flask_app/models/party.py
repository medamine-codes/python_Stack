from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
class Party :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.location = data['location']
        self.date = data['date']
        self.all_ages = data['all_ages']
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#     # Queries
    @classmethod
    def create_party(cls,data):
        query = """
        INSERT INTO parties (user_id , title, location, date, all_ages,description ) 
        VALUES (%(user_id)s,%(title)s,%(location)s,%(date)s,%(all_ages)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM parties 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all = []
        for row in results:
            all.append(cls(row))
        return all
    @classmethod
    def get_by_id(cls,data):
        query = """
        SELECT * FROM parties WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_user_parties(cls,data):
        query="""
        SELECT * FROM parties WHERE user_id = %(user_id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results , "*"*25)
        if(results):
            parties = []
            for row in results:
                parties.append(cls(row))
            return parties
        print("===========================================================")
        return None
    @classmethod
    def update_party(cls,data):
        query="""
        UPDATE parties SET
        title=%(title)s,location=%(location)s,date=%(date)s,all_ages=%(all_ages)s,description=%(description)s
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def cancel_party(cls,data):
        query="""
        DELETE FROM parties WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)


    
    # * VALIDATIONS 
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])< 2:
            flash("Title must be at least 3 ")
            is_valid = False
        if len(data['location'])< 2:
            flash("location is required !!!!!!!")
            is_valid = False
        if data['date']== "":
            flash("date is required !!!!!!!")
            is_valid = False
        if len(data['description'])< 9:
            flash("description is required !!!!!!!")
            is_valid = False
        print(data)
        return is_valid

