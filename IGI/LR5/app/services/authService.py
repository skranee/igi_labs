from app.dbServices.auth_db_service import AuthDbService
from app.security.security import password_hash, password_verify


class AuthService:
    @staticmethod
    def login(email, password):
        print(email)
        user, role = AuthDbService.login(email)
        if password_verify(password, user.password) is False or user is None:
            return None, None
        if role != 'user' and user.isAdmin:
            role = 'admin'
        return user, role

    @staticmethod
    def sign_up(email, name, phone, password):
        return AuthDbService.sign_up(email, name, phone, password_hash(password))
