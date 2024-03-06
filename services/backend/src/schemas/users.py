from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

#UserInSchema = Criar Novos Usuario.
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

#UserOutSchema = Recuperar informações do Usuario para serem usadas fora do nosso aplicativo, para retornar aos usuários finais.
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

#UserDatabaseSchema = Recuperar informações do usuário para serem usadas em nosso aplicativo, para validar usuários.
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)