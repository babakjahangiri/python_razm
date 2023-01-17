from enum import Enum
from product_inmemory_db import ProductInMemoryDb
from product_injson_db import ProductInJsonDb

class StorageType(Enum):
    IN_MEMORY = "m"
    IN_JSON = "j"
    
    def __init__(self, storage_type: str) -> None:
        self.storage_type = storage_type

    def get_db(self) -> (ProductInMemoryDb | ProductInJsonDb):
        if self.storage_type == StorageType.IN_MEMORY.value:
            return ProductInMemoryDb()
        elif self.storage_type == StorageType.IN_JSON.value:
            return ProductInJsonDb()
        else:
            raise Exception("Invalid storage type")
        
        
# test the code
if __name__ == "__main__":
    # test the Storage enum
    print(StorageType(1).db)
    storage = StorageType(2)
    print(storage.db)