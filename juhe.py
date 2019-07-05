import pymysql
import random
import requests
import re
import os

def main():

    url1 = "http://sports.sina.com.cn/nba/"
    url2 = "https://sports.163.com/nba/"
    url3 = "https://nba.hupu.com/"
    url4 = "http://sports.sohu.com/s/nba"

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }

    resp1 = requests.get(url1, headers=header)
    resp2 = requests.get(url2, headers=header)
    resp3 = requests.get(url3, headers=header)
    resp4 = requests.get(url4, headers=header)

    data1 = resp1.content.decode("utf-8")
    data2 = resp2.content.decode("gbk")
    data3 = resp3.content.decode("utf-8")
    data4 = resp4.content.decode("UTF-8")

    pattern1 = re.compile("""<a href="(.*)" target="_blank">(.*)</a>""")
    ret1 = pattern1.findall(data1)
    lst1 = []
    pattern2 = re.compile("""<a href="https://(.*).html">(.*)</a>""")
    ret2 = pattern2.findall(data2)
    lst2 = []
    pattern3 = re.compile("""<a target="_blank" href="(.*)">(.*)</a>""")
    ret3 = pattern3.findall(data3)
    lst3 = []
    pattern4 = re.compile("""<a href="(.*)" target="_blank">(.*)</a>""")
    ret4 = pattern4.findall(data4)
    lst4 = []


    db1 = pymysql.connect("172.17.0.2", "root", "abc123456", "zjh", charset='utf8')
    db2 = pymysql.connect("172.17.0.2", "root", "abc123456", "zjh", charset='gbk')
    db3 = pymysql.connect("172.17.0.2", "root", "abc123456", "zjh", charset='utf8')
    db4 = pymysql.connect("172.17.0.2", "root", "abc123456", "zjh", charset='utf8')
    cursor1 = db1.cursor()
    cursor2 = db2.cursor()
    cursor3 = db3.cursor()
    cursor4 = db4.cursor()


    insert_stmt1 = (
        "INSERT INTO sina(url,title)"
        "VALUES (%s,%s)"
    )
    insert_stmt2 = (
        "INSERT INTO wangyi(url,title)"
        "VALUES (%s,%s)"
    )
    insert_stmt3 = (
        "INSERT INTO hupu(url,title)"
        "VALUES (%s,%s)"
    )
    insert_stmt4 = (
        "INSERT INTO souhu(url,title)"
        "VALUES (%s,%s)"
    )


    for i in ret1:
        x1 = (i[0], i[-1])
        lst1.append(x1)
        try:
            cursor1.execute(insert_stmt1,x1)
            db1.commit()
        except:
            print
            "insert error"
            db1.rollback()
    for i in ret2:
        x2 = (i[0], i[-1])
        lst2.append(x2)
        try:
            cursor2.execute(insert_stmt2, x2)
            db2.commit()
        except:
            print
            "insert error"
            db2.rollback()
    for i in ret3:
        x3 = (i[0], i[-1])
        lst3.append(x3)
        try:
            cursor3.execute(insert_stmt3, x3)
            db3.commit()
        except:
            print
            "insert error"
            db3.rollback()
    for i in ret4:
        x4 = (i[0], i[-1])
        lst4.append(x4)
        try:
            cursor4.execute(insert_stmt4, x4)
            db4.commit()
        except:
            print
            "insert error"
            db4.rollback()
    # nst = []
    # for i in lst:
    #     print (i[0])
    #     print (i[1])
    #     print ("""
    #
    #     """)

    html1 = """<html>
        <head>
            <title>this is NBA news</title>
            <meta name = "keyword" content = "">
            <meta name = "description" content ="nuibi"> 
        </head>

        <body>
        <h2>from Sina</h2>
        <ul>
        """
    for i in lst1:
        html1 += """<li><a target="_blank" href="""
        html1 += i[0]
        html1 += """">"""
        html1 += i[1]
        html1 += """</a>"""


    html2 = """<html>
        <head>
            <title>this is NBA news</title>
            <meta name = "keyword" content = "">
            <meta name = "description" content ="nuibi"> 

        </head>

        <body>
       
        <h2>from 163</h2>
        <ul>
        """
    for i in lst2:
        html2 += """<li><a href="""
        html2 += """https://"""
        html2 += i[0]
        html2 += """.html"""
        html2 += """">"""
        html2 += i[1]
        html2 += """</a>"""




    html3 = """<html>
        <head>
            <title>this is NBA news</title>
            <meta name = "keyword" content = "">
            <meta name = "description" content ="nuibi"> 
        </head>

        <body>
        <h2>from Hupu</h2>
        <ul>
        """
    for i in lst3:
        html3 += """<li><a target="_blank" href="""
        html3 += i[0]
        html3 += """">"""
        html3 += i[1]
        html3 += """</a>"""






    html4 = """<html>
        <head>
            <title>this is NBA news</title>
            <meta name = "keyword" content = "">
            <meta name = "description" content ="nuibi"> 
        </head>

        <body>
        <h2>from Souhu</h2>
        <ul>
        """
    for i in lst4:
        html4 += """<li><a href="""
        html4 += i[0]
        html4 += """" target="_blank" >"""
        html4 += i[1]
        html4 += """</a>"""


    with open("a.html", "w", encoding="utf-8") as f:

         f.write(html1)
         f.write(html3)
         f.write(html2)
         f.write(html4)


    #with open("a.html", "w", encoding="utf-8") as f:






    #
    # for i in lst:
    #     link=i[0]
    #     name=i[1]
    #     data = (link,name)
    db1.close()
    db2.close()
    db3.close()
    db4.close()



if __name__ == "__main__":
    main()