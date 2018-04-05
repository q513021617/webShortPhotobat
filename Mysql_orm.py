from sqlalchemy import Column,String,create_engine,BIGINT,DateTime,TEXT,INT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
Base =declarative_base()

class wp_posts(Base):
    __tablename__='wp_posts'

    #结构
    ID=Column(BIGINT,primary_key=True)
    # bigint
    post_author = Column(BIGINT)
    # datetime
    post_date = Column(DateTime(20))
    # datetime
    post_date_gmt = Column(DateTime(20))
    # longtext
    post_content = Column(TEXT(800))
    # text
    post_title = Column(TEXT(20))
    # text
    post_status = Column(TEXT(20))
    # varchar
    comment_status = Column(String(20))
    # varchar
    ping_status = Column(String(20))
    # varchar
    post_name = Column(String(20))
    # datetime
    post_modified = Column(DateTime(20))
    # datetime
    post_modified_gmt = Column(DateTime(20))
    # bigint
    post_parent = Column(BIGINT)
    # varchar
    guid = Column(String(20))
    # int
    menu_order = Column(BIGINT)
    # varchar
    post_type = Column(String(20))
    # bigint
    comment_count = Column(BIGINT)
    post_mime_type=Column(String(20))
    def __init__(self,ID,post_author,post_date,post_date_gmt,post_content,post_title,post_status,comment_status,ping_status,post_name,post_modified,post_modified_gmt
                 ,post_parent,guid,menu_order,post_type,comment_count,post_mime_type):
        self.ID=ID
        self.post_author=post_author
        self.post_date=post_date
        self.post_date_gmt=post_date_gmt
        self.post_content=post_content
        self.post_title=post_title
        self.post_status=post_status
        self.comment_status=comment_status
        self.ping_status=ping_status
        self.post_name=post_name
        self.post_modified=post_modified
        self.post_modified_gmt=post_modified_gmt
        self.post_parent=post_parent
        self.guid=guid
        self.menu_order=menu_order
        self.post_type=post_type
        self.comment_count=comment_count
        self.post_mime_type=post_mime_type

    # 初始化数据库连接,:
    engine = create_engine('mysql+mysqlconnector://htmlmuban_zhiyi:RArApcsdwAEanFAH@www.zhiyigo.cn:3306/htmlmuban_zhiyi')
    DBSession=sessionmaker(bind=engine)

class wp_posts_meta(Base):
    __tablename__='wp_postmeta'
    meta_id=Column(BIGINT,primary_key=True)
    post_id=Column(BIGINT)
    meta_key=Column(String(255))
    meta_value=Column(TEXT)

    def __init__(self,meta_id,post_id,meta_key,meta_value):
        self.meta_id=meta_id
        self.post_id=post_id
        self.meta_key=meta_key
        self.meta_value=meta_value

    engine = create_engine(
        'mysql+mysqlconnector://htmlmuban_zhiyi:RArApcsdwAEanFAH@www.zhiyigo.cn:3306/htmlmuban_zhiyi')
    DBSession = sessionmaker(bind=engine)
