import motor.motor_asyncio

MONGODB_URL = 'mongodb://localhost:27017/'


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database name

database = client.python_db