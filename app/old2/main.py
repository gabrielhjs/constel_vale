from app.views import view_login
from app.objects import User

if __name__ == "__main__":
    user = User()
    view_login(user)
