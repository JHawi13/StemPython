profile={}
def register():
    Username=input("enter username:")
    Email=input("Enter Email:")
    password=input("Enter password")

    profile["username"]=Username
    profile["email"]=Email
    profile["Password"]=password
def get_profile ():
    print(profile)
register()
get_profile()

def change_username():
    new_name=input("Enter your new username")
    profile["username"]=new_name
change_username()
get_profile()