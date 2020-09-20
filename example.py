from jsontoexcel import json2excel
import json

workbook=json2excel("haha")

data = json.dumps([
    {
        "employee_id": [
            123,
            123
        ],
        "employee_name": [
            "Akriti",
            "Akriti"
        ],
        "source": "Mumbai",
        "mines": "Diamond",
        "rr_no": 1,
        "rake_loading_date": "2020-09-03T00:00:00.000Z",
        "rake_unloading_date": "2020-09-08T00:00:00.000Z",
        "sample_collection_date": "2020-09-16T00:00:00.000Z",
        "rake_no": 1,
        "is_disputed": "false",
        "samples": [
            {
                "id": 1,
                "billed_grade": "G-12",
                "total_quantity": 23,
                "loading_end_ash": 3,
                "loading_end_vm": 4,
                "loading_end_gcv_cimfer": 3,
                "loading_end_gcv_npgc": 2,
                "loading_end_equilibrated_moisture": 3,
                "loading_end_total_moisture": 2,
                "loading_end_could_be_disputed": "false",
                "loading_end_disputed_lab": "null",
                "loading_end_disputed_by_cimfer": "false",
                "unloading_end_equilibrated_basis_equilibrated_moisture": 3,
                "unloading_end_equilibrated_basis_vm": 4,
                "unloading_end_equilibrated_basis_ash": 4,
                "unloading_end_equilibrated_basis_gcv_cimfer": 2,
                "unloading_end_equilibrated_basis_gcv_npgc": 2,
                "unloading_end_total_moisture_basis_total_moisture": 3,
                "unloading_end_total_moisture_basis_ash": 4.123711340206185,
                "unloading_end_total_moisture_basis_vm": 4.123711340206185,
                "unloading_end_total_moisture_basis_gcv": 2.0618556701030926,
                "unloading_end_could_be_disputed": "false",
                "unloading_end_disputed_lab": "null"
            },
            {
                "id": 2,
                "billed_grade": "Washery Grade II",
                "total_quantity": 34,
                "loading_end_ash": 32,
                "loading_end_vm": 2,
                "loading_end_gcv_cimfer": 3,
                "loading_end_gcv_npgc": 3,
                "loading_end_equilibrated_moisture": 322,
                "loading_end_total_moisture": 4,
                "loading_end_could_be_disputed": "false",
                "loading_end_disputed_lab": "null",
                "loading_end_disputed_by_cimfer": "false",
                "unloading_end_equilibrated_basis_equilibrated_moisture": 2,
                "unloading_end_equilibrated_basis_vm": 3,
                "unloading_end_equilibrated_basis_ash": 3,
                "unloading_end_equilibrated_basis_gcv_cimfer": 34,
                "unloading_end_equilibrated_basis_gcv_npgc": 2,
                "unloading_end_total_moisture_basis_total_moisture": 6,
                "unloading_end_total_moisture_basis_ash": 2.877551020408163,
                "unloading_end_total_moisture_basis_vm": 2.877551020408163,
                "unloading_end_total_moisture_basis_gcv": 32.61224489795918,
                "unloading_end_could_be_disputed": "false",
                "unloading_end_disputed_lab": "null"
            }
        ]
    }
])


workbook.createSheet("a", data)
workbook.closeWorkbook()
