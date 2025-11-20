from tabulate import tabulate

def parse_log_line(line: str) -> dict:
    date,time,level,*message=line.split()
    return {'date':date,'time':time,'level':level,'message':' '.join(message)}

def load_logs(file_path: str) -> list:
    list_of_logs=[]

    with open(file_path,'r') as file:
        for line in file.readlines():
            list_of_logs.append(parse_log_line(line))

    return list_of_logs
        

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x['level']==level.upper(),logs))

def count_logs_by_level(logs: list) -> dict:
    set_levels={log['level'] for log in logs}
    logs_map={}

    for level in set_levels:
        logs_map[level]= len(filter_logs_by_level(logs,level))

    return logs_map

def display_log_counts(counts: dict):
    print(tabulate(list(counts.items()), headers=['Рівень логування', 'Кількість'], tablefmt='orgtbl'))



from pathlib import Path
if __name__=='__main__':
    current_dir=Path(__file__).parent
    
    dict_of_logs=count_logs_by_level(load_logs(current_dir/'logs.txt'))
    display_log_counts(dict_of_logs)



