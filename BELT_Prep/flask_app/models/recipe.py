from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
class Recipe :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_cooked = data['date_cooked']
        self.under_30mins = data['under_30mins']
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#     # Queries
    @classmethod
    def create_recipe(cls,data):
        query = """
        INSERT INTO recipes (user_id , name, description, instruction, date_cooked,under_30mins ) 
        VALUES (%(user_id)s,%(name)s,%(description)s,%(instruction)s,%(date_cooked)s,%(under_30mins)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all = []
        for row in results:
            all.append(cls(row))
        return all
    @classmethod
    def get_by_id(cls,data):
        query = """
        SELECT * FROM recipes WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    # @classmethod
    # def get_user_recipes(cls,data):
    #     query="""
    #     SELECT * FROM recipes WHERE user_id = %(user_id)s ;
    #     """
    #     results = connectToMySQL(DATABASE).query_db(query,data)
    #     print(results , "*"*25)
    #     if(results):
    #         parties = []
    #         for row in results:
    #             parties.append(cls(row))
    #         return parties
    #     print("===========================================================")
    #     return None
    @classmethod
    def update_recipe(cls,data):
        query="""
        UPDATE recipes SET
        name=%(name)s,description=%(description)s,instruction=%(instruction)s,date_cooked=%(date_cooked)s,under_30mins=%(under_30mins)s
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def cancel_recipe(cls,data):
        query="""
        DELETE FROM recipes WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)


    
    # * VALIDATIONS 
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("Nme must be at least 3 ")
            is_valid = False
        if len(data['description'])< 10:
            flash("Description is required !!!!!!!")
            is_valid = False
        if len(data['instruction'])< 10:
            flash("Instructions are required !!!!!!!")
            is_valid = False
        if data['date_cooked']== "":
            flash("Date cooked/Made is required !!!!!!!")
            is_valid = False
        print(data)
        return is_valid

