import re
import csv
import yaml
import datetime
import ScanHandler as sh
import ScanStats as ss


def scan_urls():
    with open('urls.csv', 'r') as urls_file:
        for url in urls_file:
            url = re.sub(r"[\n\s]*", "", url)
            if check_last_update(url) is True:
                scan_resp = sh.request_scan(url)
                parameters_dict = sh.parse_response(scan_resp)
                scan_stats_obj = ss
                scan_stats_obj.stats_scan_data(scan_stats_obj, url, parameters_dict)
                write_to_csv(scan_stats_obj)
                last_update_dict(scan_stats_obj)
        urls_file.close()


def write_to_csv(parameters):
    list_of_scan_results = [parameters.url, parameters.risk, parameters.total_voting, parameters.category,
                            parameters.time]
    with open('url_scan_records.csv', 'a', newline='') as scan_records_file:
        writer = csv.writer(scan_records_file, dialect='excel')
        writer.writerow(list_of_scan_results)
        scan_records_file.close()


def check_last_update(url):
    with open('config.yml', 'r') as read_config:
        config_file = yaml.full_load(read_config)
        read_config.close()
    last_update = config_file['LAST_SCAN']['URL_LAST_SCAN'][url]
    if last_update is None:
        return True
    last_30_min = datetime.datetime.now() - datetime.timedelta(minutes=30)
    print(last_update, last_30_min)
    if last_update < last_30_min:
        return True
    return False


def last_update_dict(scan_stats_obj):
    with open('config.yml', 'r') as read_config:
        config_file = yaml.full_load(read_config)
        config_file['LAST_SCAN']['URL_LAST_SCAN'][scan_stats_obj.url] = scan_stats_obj.time
    with open('config.yml', 'w') as write_config:
        yaml.dump(config_file, write_config)

    read_config.close()
    write_config.close()


if __name__ == '__main__':
    scan_urls()

