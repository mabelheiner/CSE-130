import json

def main():
    book = {
        "author": "Marissa Meyer",
        "year_published": 2021,
        "title": "Supernova",
        "series_details": ["Renegades", "Archenemies", "Supernova"]
    }
    
    text = json.dumps(book)    
    with open("example.json", "w") as file:
        file.write(text)
        
    with open("example.json", "r") as file:
        book = file.read()
        data2 = json.loads(book)
        
    print(book)
    print(data2)
        
    
    
if __name__ == "__main__":
    main()