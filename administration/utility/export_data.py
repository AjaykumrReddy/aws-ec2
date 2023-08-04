import csv

def export_to_csv(queryset, fields,filename):
    print('======>',print(type(fields)))
    # filename = fields[0] + '.csv'
    print(filename)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(fields)
        
        # Write the data rows
        for obj in queryset:
            row = [getattr(obj, field) for field in fields]
            writer.writerow(row)
