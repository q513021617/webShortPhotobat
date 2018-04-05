
class wp_posts():
    # 结构
    ID = Column(BIGINT, primary_key=True)
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
    post_mime_type = Column(String(20))