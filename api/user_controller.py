
from api.models import user_list


class User_controller:

    def add_user(self, user):
        new_user = {
            "userId":user.userId,
            "username":user.username,
            "email":user.email,
            "password":user.password,
          
        }
        
        user_list.get("users").append(new_user)

        return user_list
    
    def delete_user(self,userId):
        user_list.remove(userId)

        return  user_list

    def get_user_by_userId(self,userId):
        for user in user_list.get("users"):# get access to list of users using the key
            if user.get("userId") == userId:
                return user


    def get_users(self):
        return user_list
