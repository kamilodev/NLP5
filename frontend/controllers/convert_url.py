import re


def convert_gsheets_url(u):
    try:
        worksheet_id = u.split("#gid=")[1]
    except:
        worksheet_id = None
        u = re.findall("https://docs.google.com/spreadsheets/d/.*?/", u)[0]
        u += "export"
        u += "?format=csv"
        if worksheet_id:
            u += "&gid={}".format(worksheet_id)
        return u
