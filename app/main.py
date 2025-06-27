from app.utils.load_env import env

print(env.get_env_variable("DATABASE_URL"))
