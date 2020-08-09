import csv
import os
import operator


# task 5.1a)
def preview_csv(file_name, num):
    if not os.path.isfile(file_name):
        print('ERROR: "{0}" file not found'.format(file_name))
        exit()
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        res_list = []
        for element in reader:
            if element["municipality"] not in res_list and len(res_list) <= num-1:
                res_list.append(element["municipality"])
            if len(res_list) == num:
                break
    return res_list


print(preview_csv('./vehicles.csv', 10))
print(preview_csv('./vehicles.csv',5))


# task 5.1b)
def satisfies_conditions(row, vehicle_type=None, from_year=None, to_year=None, years=None):
    if vehicle_type is not None and from_year is not None and to_year is not None:
        if row["vehicle_type"] == vehicle_type:
                if int(row["year"]) >= from_year and int(row["year"]) <= to_year:
                    return True
    elif vehicle_type is not None and years is not None:
        if row["vehicle_type"] == vehicle_type:
            if int(row["year"]) == years:
                return True
    elif vehicle_type is None and from_year is not None and to_year is not None:
        if int(row["year"]) >= from_year and int(row["year"]) <= to_year:
            return True
    elif vehicle_type is None and years is not None:
        if int(row["year"]) == years:
            return True
    else:
        return False


def municipalities_most_vehicles(file_name, limit=10, vehicle_type=None, from_year=None, to_year=None, years=None):
    filtered_municipalities = {}
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for element in reader:
            if satisfies_conditions(element, vehicle_type, from_year, to_year, years) == True:
                    if element["municipality"] in filtered_municipalities:
                        filtered_municipalities[element["municipality"]] += int(element["count"])
                    else:
                        filtered_municipalities[element["municipality"]] = int(element["count"])
            result = sorted(filtered_municipalities.items(), key=operator.itemgetter(1))
            result = result[-limit:]
            result = result[::-1]
    return result


print(municipalities_most_vehicles('./vehicles.csv', limit=10, years=1993))
print(municipalities_most_vehicles('./vehicles.csv', vehicle_type="car", limit=5, years=1994))
print(municipalities_most_vehicles('./vehicles.csv', limit=5, from_year=1997, to_year=1999))