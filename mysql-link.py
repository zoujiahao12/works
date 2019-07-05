import pymysql
import random
import requests
import re
import os

def main():

    url = "http://sports.sina.com.cn/nba/"
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    resp = requests.get(url, headers=header)
    data = resp.content.decode("utf-8")

    pattern = re.compile("""<a href="(.*)" target="_blank">(.*)</a>""")
    ret = pattern.findall(data)
    lst = []
    db = pymysql.connect("172.17.0.2", "root", "abc123456", "zjh", charset='utf8')
    cursor = db.cursor()
    insert_stmt = (
        "INSERT INTO links(url,title)"
        "VALUES (%s,%s)"
    )
    for i in ret:
        x = (i[0], i[-1])
        lst.append(x)
        try:
            cursor.execute(insert_stmt,x)
            db.commit()
        except:
            print
            "insert error"
            db.rollback()
    # nst = []
    # for i in lst:
    #     print (i[0])
    #     print (i[1])
    #     print ("""
    #
    #     """)

        html = """<html>
        <head>
          <title>this is my world</title>
            <meta name = "keyword" content = "">
            <meta name = "description" content ="nuibi"> 

        </head>

        <body>
        <h3>from Sina</h3>
        <ul>
        """
        for i in lst:
            html += """<li><a target="_blank" href="""
            html += i[0]
            html += """">"""
            html += i[1]
            html += """</a>"""
    with open("a.html", "w", encoding="utf-8") as f:
        f.write(html)


    #
    # for i in lst:
    #     link=i[0]
    #     name=i[1]
    #     data = (link,name)
    db.close()



if __name__ == "__main__":
    main()