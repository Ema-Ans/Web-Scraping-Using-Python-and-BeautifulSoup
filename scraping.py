
#to request the data from the web servers
import requests as r
#works with a parser, to extract data from HTML 
from bs4 import BeautifulSoup as bs


def make_Link(group_name):
    link = "https://attack.mitre.org" + group_name + "/"
    return link

def get_techniques(t_table):
    if (t_table == None):
        print("NONE")
    else:
        tableValues = []
        for x in t_table.find_all('tr')[1:]:
        #we don't convert it to sets, to get rid of the duplicates
        #because in this case, we care about the order for zipping in the end
            td_tags = list(x.find_all('a'))
            td_val = [y for y in td_tags]
            tableValues.append(td_val)

        nameList = []
        #from that raw html list, we extract the names i.e., texts only for each group
        for elem in tableValues:
            my_val = [y.text for y in elem]
            nameList.append(list(my_val))
        #contains [[<a href="/software/S0012">PoisonIvy</a, <a href="/groups/G0018"> G0018 </a>,..] ...] for each row
        #for each of the elem in html list, we extract its link
        url_List = []
        for elem in tableValues:
            my_urls = [x.get('href') for x in elem]
            url_List.append(list(my_urls))
        final = list(zip(nameList, url_List))
        techniques_List = []
        for elem in final:
            techniques = elem[0]
            links = elem[1]
            temp  = []
            for i in range(len(links)):
                if links[i][:11] == "/techniques":
                    temp.append((techniques[i], links[i]))
            techniques_List.append(temp)

        return techniques_List
    
def get_softwares(my_table):
    if my_table == None:
        print("NONE")
    else:
        tableValues = []
        for elem in my_table.find_all('tr')[1:]:
            #we dont convert it to sets, because we care about the order
            td_tags = list(elem.find_all('a'))
            td_val = [y for y in td_tags]
            tableValues.append(td_val)
            #contains [[<a href="/software/S0012">PoisonIvy</a, <a href="/groups/G0018"> G0018 </a>,..] ...] for each row

        nameList = []
        #from that raw html list, we extract the names i.e., texts only for each group
        for elem in tableValues:
            my_val = [y.text for y in elem]
            nameList.append(list(my_val))

        #for each of the elem in html list, we extract its link
        url_List = []
        for elem in tableValues:
            my_urls = [x.get('href') for x in elem]
            url_List.append(list(my_urls))
        #zip these two:
        final = list(zip(nameList, url_List))
        software_List = []
        for elem in final:
            techniques = elem[0]
            links = elem[1]
            temp  = []
            for i in range(len(links)):
                if links[i][:9] == "/software":
                    temp.append((techniques[i], links[i]))
        software_List.append(temp)
        return software_List       
