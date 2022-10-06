from email_out import send_email
from ifconfig import ifconfig_get
import csv
import json
import os

def convert_bytes(byt):
    output = str(byt, 'UTF-8')
    return output

def write_csv(row):
    f = open('store_adr', 'w')
    writer = csv.writer(f)
    writer.writerow([row])
    f.close()

def read_csv_csv():
    with open('store_adr', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines != []:
                return lines

if __name__ == '__main__':
    csv_file_name = 'store_adr'
    # Get Current IP
    current_ip = convert_bytes(ifconfig_get())

    if os.path.exists(csv_file_name):
        # Get last recorded IP
        last_ip = read_csv_csv()[0]

        # If change detected
        if current_ip != last_ip:
            # Set email message
            message = f"""Subject:Raspberry Pi External Change Detected\n
            Detail:{last_ip} -> {current_ip}"""

            # Write new ip to csv file store
            write_csv(current_ip)
            
            # read in json config for smtp details
            with open('config.json') as f:
                data = json.load(f)
            # Convert json dict into vars
            gmail_user, gmail_pwd, to, msg_from = data['mail_user'], data['mail_pw'], data['mail_to'], data['mail_from']
            # Send email detailing change
            send_email(gmail_user,gmail_pwd,msg_from,to,message)
    else:
        # If no file, then write a new one
        write_csv(current_ip)