# JsonToExcel

**JsonToExcel is a package which converts complex, nested json to excel.**

To install dependencies

`pip install -r requirements.txt`

### Initialisiation:
  To create an excel file with given name.
  
  `<workbook instance> =json2excel(<filename in quotes>)`
  
### Create workesheet:
  To create a sheet in the above excel workbook.
  
  `<worksheet instance> = createSheet(<sheetname in quotes>, <json data>)`
  
### Close workbook:
  `<workbook instance>.closeWorkbook()`
  
## Example
  Json data:
  
  ```json
  [
   {
        "name": "John",
        "age": 22,
        "subjects": [
            {
                "maths": {
                    "marks": 87,
                    "project": "submitted"
                }
            },
            {
                "science": {
                    "marks": 91,
                    "project": "submitted"
                }
            },
            {
                "english": {
                    "marks": 81,
                    "project": "not submitted"
                }
            }
        ],
        "graduated": True
    },
    {
        "name": "Mary",
        "age": 21,
        "subjects": [
            {
                "marks": 80,
                "project": "not submitted"
            },
            {
                "marks": 97,
                "project": "submitted"
            },
            {
                "marks": 88,
                "project": "submitted"
            }
        ],
        "graduated": True
    },
    {
        "name": "Matt",
        "age": 22,
        "subjects": [
            {
                "marks": 69,
                "project": "not submitted"
            },
            {
                "marks": 73,
                "project": "submitted"
            },
            {
                "marks": 75,
                "project": "not submitted"
            }
        ],
        "graduated": False
    }
]
```

Output

