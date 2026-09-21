import csv

class DataPipeline:
    #Initialize
    def __init__(self, source, destination):
        self.source= source
        self.destination= destination
    
    #Extract the data
    def extract_data(self):
        print(f"Extracting data from {self.source}")
        data = []

        with open(self.source,newline="", encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for raw in reader:
                data.append(raw)

        return data
    
    #transform the data
    def transform_data(self, data):
        print("Transforming data")
        cleaned_data=[]

        for row in data:
            if row["amount"] not in [None, "", "NULL"]:
                row["amount"] = float(row["amount"])
                cleaned_data.append(row)
        
        return cleaned_data
    
    #Load the data to destination
    def load_data(self, data):
        print(f"loading{len(data)} records to {self.destination}")
        
        if not data:
            print("No data to write.")
            return
        
        with open(self.destination, 'w', newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    #Orchestrate Flow
    def run(self):
        data = self.extract_data()
        data = self.transform_data(data)
        self.load_data(data)

pipeline = DataPipeline("data/raw/dirty_orders.csv","data/cleaned/cleaned_orders.csv")
pipeline.run()