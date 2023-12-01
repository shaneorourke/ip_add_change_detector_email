from email_out import send_email
from ifconfig import ifconfig_get
import csv
import json
import os
import requests

def convert_bytes(byt):
    output = str(byt, 'UTF-8')
    print(f'convert_bytes:in:{byt}:out:{output}')
    return output

def write_csv(filename,row):
    f = open(f'/home/shanepi/git/ip_add_change_detector_email/{filename}', 'w')
    writer = csv.writer(f)
    writer.writerow([row])
    f.close()
    print(f'write_csv:in:{filename}|{row}:out:null')

def read_csv_csv(filename):
    with open(f'/home/shanepi/git/ip_add_change_detector_email/{filename}', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines != []:
                return lines
    print(f'read_csv_csv:in:{filename}:out:{lines}')

def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address

if __name__ == '__main__':
    csv_file_name = 'store_adr'
    # Get Current IP
    #current_ip = convert_bytes(ifconfig_get())
    current_ip = get_ip_address()
    print(f'current_ip:out:{current_ip}')

    if os.path.exists(csv_file_name):
        # Get last recorded IP
        last_ip = read_csv_csv(csv_file_name)[0]
        print(f'last_ip:out:{last_ip}')

        # If change detected
        if current_ip != last_ip:
            # Set email message
            message = f"""Subject:Raspberry Pi External Change Detected\n
            Detail:{last_ip} -> {current_ip}"""
            print(f'message:out:{message}')
            # Write new ip to csv file store
            write_csv(csv_file_name,current_ip)
            
            # read in json config for smtp details
            with open('config.json') as f:
                data = json.load(f)
                print(f'data:out:{data}')
            # Convert json dict into vars
            gmail_user, gmail_pwd, to, msg_from = data['mail_user'], data['mail_pw'], data['mail_to'], data['mail_from']
            # Send email detailing change
            send_email(gmail_user,gmail_pwd,msg_from,to,message)
            print(f'send_email:in:{gmail_user},{gmail_pwd},{msg_from},{to},{message}')
    else:
        # If no file, then write a new one
        write_csv(csv_file_name,current_ip)
