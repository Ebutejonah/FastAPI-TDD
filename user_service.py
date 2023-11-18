class UserService:
    def get_users_from_db(self):
        return [
            {"username":"Ade"}, 
            {"username":"Bola"}
        ]
    
user_service = UserService()