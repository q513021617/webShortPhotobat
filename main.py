import requests
from selenium import webdriver
import re
import chardet
import time
import pymysql
import Mysql_orm
chrome_driver_path = r"/opt/google/chrome/chromedriver"
import json
from urllib import parse
import generate_xml
from lxml import etree

def getindexhtmlPic_2(url,filename):
    html_url=url+"/index.html"
    picNmae=filename+".jpg"
    brower=webdriver.Chrome(chrome_driver_path)
    print(html_url)
    brower.get(html_url)
    brower.save_screenshot(picNmae)
    brower.close()

def getindexhtmlPic_1(pathString):
    for i in range(1,1187):
        fileurl=pathString+str(i)
        file_Name="H"+str(i)
        try:
            getindexhtmlPic_2(url=fileurl,filename=file_Name)
        except Exception as err:
            continue

def utf8_transfer(strs):
    ''''' 
    utf8编码转换 
    '''
    try:
        if isinstance(strs, str):
            strs = strs.encode('utf-8')
        elif chardet.detect(strs)['encoding'] == 'GB2312':
            strs = strs.decode("gb2312", 'ignore').encode('utf-8')
        elif chardet.detect(strs)['encoding'] == 'utf-8':
            strs = strs.decode('utf-8', 'ignore').encode('utf-8')
    except Exception as e:
        print('utf8_transfer error'+strs+e)
    return strs

def get_title(url,filename,num):
    ''''' 
    用re抽取网页Title 
    '''
    html_url=url+"/index.html"

    brower=webdriver.Chrome(chrome_driver_path)
    brower.get(html_url)
    time.sleep(1)
    Html=brower.page_source
    brower.close()
    #Html = utf8_transfer(Html)
    compile_rule = r'<title>.*</title>'
    title_list = re.findall(compile_rule, str(Html))

    if title_list == []:
        title = ''
    else:
        title = title_list[0][7:-8]

    #将文件编号和标题作为键值对
    #post_content(filename,title,num)
    #post_content_img(filename,title,num)


def post_content(file_name,title,num):
    post_author=1
    post_date=time.strftime("%Y-%m-%d %H:%M:%S")
    post_date_gmt=post_date
    post_content="<img src='http://htmlmuban.zhiyigo.cn/wp_files/"+file_name+".jpg' with='750px' height='750px'/></br>演示地址:</br><a href='http://htmlmuban.zhiyigo.cn/wp_files/"+file_Name+"/index.html'>http://htmlmuban.zhiyigo.cn/wp_files/"+file_Name+"/index.html</a></br>下载地址:</br><a href='http://htmlmuban.zhiyigo.cn/wp_files/"+file_Name+".zip'>http://htmlmuban.zhiyigo.cn/wp_files/"+file_Name+".zip</a></br><h5>注意：</h5></br>由于本站的架构不是特别稳定所以如果出现网页样式加载不完全时请多刷新几次！！</br>如果您可怜up主请按照二维码打赏站长</br>我们会做到更好！！</br>本站资源均采集自互联网，如果你觉得侵犯了您的创作权益请与我们联系"
    post_title="精美模板、响应式"+str(num)+title
    post_status="publish"
    comment_status="open"
    ping_status="open"
    post_name=parse.quote(post_title)
    post_modified=post_date
    post_modified_gmt=post_date
    post_parent=0
    guid="http://htmlmuban.zhiyigo.cn/?p="+str(10+num)
    menu_order=0
    post_type="post"
    comment_count=0
    post_minme_type=""
    print(file_name)

    to_mysql((10+num),post_author, post_date, post_date_gmt, post_content, post_title, post_status, comment_status, ping_status,
             post_name, post_modified, post_modified_gmt, post_parent,
             guid, menu_order, post_type, comment_count,post_minme_type)

def post_content_img(file_name,title,num):
    post_author=1
    post_date=time.strftime("%Y-%m-%d %H:%M:%S")
    post_date_gmt=post_date
    post_content=""
    post_title="精美模板、响应式"+str(num)+title
    post_status="inherit"
    comment_status="closed"
    ping_status="open"
    post_name=parse.quote(post_title)
    post_modified=post_date
    post_modified_gmt=post_date
    post_parent=(10+num)
    guid="http://htmlmuban.zhiyigo.cn/wp_files/H"+str(num)+".jpg"
    menu_order=0
    post_type="attachment"
    post_minme_type = "image/png"
    comment_count=0
    print(file_name)

    to_mysql((2000+num),post_author, post_date, post_date_gmt, post_content, post_title, post_status, comment_status, ping_status,
             post_name, post_modified, post_modified_gmt, post_parent,
             guid, menu_order, post_type, comment_count,post_minme_type)
    to_mysql_wp_postmeta(None,(2000+num),'_wp_attached_file',file_name+'.jpg')
    to_mysql_wp_postmeta(None, (2000+num), '_wp_attachment_metadata', 'a:5:{s:5:"width";i:230;s:6:"height";i:60;s:4:"file";s:27:"'+file_name+'.jpg";s:5:"sizes";a:0:{}s:10:"image_meta";a:12:{s:8:"aperture";s:1:"0";s:6:"credit";s:0:"";s:6:"camera";s:0:"";s:7:"caption";s:0:"";s:17:"created_timestamp";s:1:"0";s:9:"copyright";s:0:"";s:12:"focal_length";s:1:"0";s:3:"iso";s:1:"0";s:13:"shutter_speed";s:1:"0";s:5:"title";s:0:"";s:11:"orientation";s:1:"0";s:8:"keywords";a:0:{}}}')
    to_mysql_wp_postmeta(None, 10 + num, '_edit_last', '1')
    to_mysql_wp_postmeta(None, 10 + num, '_edit_lock', '1522833342:1')
    to_mysql_wp_postmeta(None, 10 + num, 'views', '0')
    to_mysql_wp_postmeta(None, 10 + num, '_thumbnail_id', 2000+num)

def to_mysql(id,post_author,post_date,post_date_gmt,post_content,post_title,post_status,comment_status,ping_status,post_name,post_modified,post_modified_gmt,post_parent,
    guid,menu_order,post_type,comment_count,post_minme_type):


    DB_item = Mysql_orm.wp_posts(id,post_author,post_date,post_date_gmt,post_content,post_title,post_status,comment_status,ping_status,post_name,post_modified,post_modified_gmt,post_parent,
    guid,menu_order,post_type,comment_count,post_minme_type)
    session=Mysql_orm.wp_posts.DBSession()
    session.add(DB_item)
    session.commit()
    session.close()

def to_mysql_wp_postmeta(meta_id,post_id,meta_key,meta_value):
    DB_item = Mysql_orm.wp_posts_meta(meta_id,post_id,meta_key,meta_value)
    session=Mysql_orm.wp_posts_meta.DBSession()
    session.add(DB_item)

    session.commit()
    session.close()

def name_change(id,title):

    session = Mysql_orm.wp_posts.DBSession()

    session.query(Mysql_orm.wp_posts).filter(Mysql_orm.wp_posts.ID == id).update({'post_name': title})
    session.commit()
    session.close()

if __name__ == '__main__':
    pathString = "https://htmlmuban.zhiyigo.cn/?p="
