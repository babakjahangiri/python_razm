import motor.motor_asyncio

MONGODB_URL = 'mongodb://localhost'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.python_db