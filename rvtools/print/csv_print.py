""" Module responsible to save the content as csv file """
import csv


def csv_print(module_name, server_list):
    """
    Def which will receive the server list and then will
    populate all fields from header as the content.

    Note. All fields will be populated automatically, then according to
    the module which will call csv_print, the # of fields will be updated
    automatically.
    """

    print("Inside Print definition")

    with open(module_name, 'w', newline='') as f:
        fieldnames = server_list[0].keys()
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()

        for each_line in server_list:
            csv_data_fields = {}
            for each_field in fieldnames:
                csv_data_fields[each_field] = each_line[each_field]
            thewriter.writerow(csv_data_fields)
