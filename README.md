To run an adhoc conversion from `data.json` to `data.xlsx`:
```
git clone https://github.com/cbugk/JsonToExcel
```

```
cd JsonToExcel/JsonToExcel/
# cp /path/to/data.json ./ # copy your json file beside convert_data.py
python3 ./convert_data.py
```

---

# JsonToExcel

**JsonToExcel is a package which converts complex, nested json to excel.**

Available at https://pypi.org/project/jsontoexcel

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

![alt text](https://github.com/akritianand/JsonToExcel/blob/master/JsonToExcel/SampleOutput.png "Output")

## FAQs

1. Use True/False instead of true/false in json input data.
2. Heading is only 1 line with each layer key appended to it.
