class AppRepository():
    def __init__(self):
        self.records = []
    
    def save(self, record: dict) -> None:
        self.records.append(record)
        
    def get_all(self) -> list[dict]:
        return self.records
        
    def get(self, id: int) -> dict:
        return self.records[id]