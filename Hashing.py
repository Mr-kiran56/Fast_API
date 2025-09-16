from passlib.context import CryptContext



pas_bct=CryptContext(schemes=['bcrypt'],deprecated="auto")


class Hash:
    def hash_pass(password):
        return pas_bct.hash(password)
    def hash_verify(password,original_password):
        return pas_bct.verify(password,original_password)
    
