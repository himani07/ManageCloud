from flask_sqlalchemy import SQLAlchemy


class DatabaseServer:
    """
        Class helps to formalize the database connection with database
        as singleton object
        """

    __instance = None

    def __init__(self):

        if DatabaseServer.__instance:
            raise Exception("DatabaseServer class is a singleton!")
        else:
            ########################################
            # SETTING SQL ALCHEMY INSTANCE
            DatabaseServer.__instance = SQLAlchemy()
            ########################################

    @staticmethod
    def get_instance():
        """
        Function help to get the database connection
        """
        if not DatabaseServer.__instance:
            DatabaseServer()
        return DatabaseServer.__instance



