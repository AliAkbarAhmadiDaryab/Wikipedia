import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import re
def download_provinces():
    url = 'https://en.wikipedia.org/wiki/Provinces_of_Afghanistan'
    html = urllib.request.urlopen(url)
    soup = bs(html, 'html.parser')
    soup = soup('table')
    provinces = []
    for i,table in enumerate(soup):
        if i == 2:
            prov_table = table('tr')
            for tr in prov_table:
                links = tr.find_all('a')
                links = list(links)
                if (len(links)>1):
                    text =(links[0].get_text().lower())
                    if not re.search('[0-9]+',text):
                        provinces.append(text)
    return provinces


def get_provinces_list():
    return download_provinces()

def write_provinces(file_name, text,method = 'n'):
    if method == 'n':
        provinces_list = download_provinces()
    else:
        provinces_list = text
    with open(file_name,'a') as write_file:
        if method == 'n':
            for pro in provinces_list:
                write_file.write(pro)
                write_file.write('\n')
        else:
            write_file.write(provinces_list.lower())
            write_file.write('\n')

#write_provinces()



def read_files (file_name):
    with open(file_name, 'r') as read_file:
        prov = (read_file.readlines())
    return prov



def download_districts():
    url = 'https://en.wikipedia.org/wiki/Districts_of_Afghanistan'
    html = urllib.request.urlopen(url)
    soup = bs(html, 'html.parser')
    return soup


def check_province(provinces,text):
    for province in provinces:
        if re.search(r'\b{0}\b'.format(province), text):
            return province
    return 'none'



def get_ditrict_province():
    soup = download_districts()
    soup = soup.body
    soup = soup('ul')
    for i,s in enumerate(soup):
        links_prov = s.find_all('ul')
        for i,link in enumerate(links_prov):
            if len(links_prov) > 0:
                link = link.get_text()
                write_provinces('provinces_new_list.txt', link, method='d')

        if i>20 and i<= len(soup)-25:
            links_list = s.find_all('a')

            if (len(links_list)>0):
                for link in links_list:
                    text = link.get_text().lower()
                    text = text
                    write_provinces('districts.txt',text, method='d')
                write_provinces('districts.txt', '\n', method='d')
#get_ditrict_province()

def get_province_list(file_name_prov_new, file_name_prov_old):
    provinces_orderd = read_files(file_name_prov_new)
    province_temp = read_files(file_name_prov_old)
    province_list = []
    ordered_provinces = []
    for prov in province_temp:
        province_list.append(prov.strip())

    for province in provinces_orderd:
        province = province.strip()
        if province:
            out_province = check_province(province_list,province)
            ordered_provinces.append(out_province)

    return ordered_provinces





def get_district_list(file_name):
    district_list = read_files(file_name)
    district_temp =[]
    ordered_districts = []
    for dist in district_list:
        if dist and dist.strip():
            dist = dist.strip()
            district_temp.append(dist)
        else:
            ordered_districts.append(district_temp)
            district_temp = []

    return ordered_districts



def get_prov_dist_dict(file_prov_new, file_prov_old, file_dist):
    district_list = get_district_list(file_dist)
    provinces_list= get_province_list(file_prov_new, file_prov_old)
    output_dict ={}
    for i,province in enumerate(provinces_list):
        output_dict[province] = district_list[i]

    return output_dict, provinces_list, district_list


prov_dict_list, prov_list, dist_list =get_prov_dist_dict('provinces_new_list.txt','province.txt','districts.txt')

def get_check_province(text):
    text = text.split()
    for item in text:
        if item in prov_list:
            return item
