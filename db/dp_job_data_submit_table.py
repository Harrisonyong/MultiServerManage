from enum import unique
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class JobDataSubmit(Base):
    """表示作业数据投递的实体，与作业数据投递表映射"""
    __tablename__ = 'dp_job_data_submit_table'

    primary_id = Column(Integer, primary_key=True)
    '用户名'
    user_name = Column(String)
    '整体作业投递批号'
    job_total_id = Column(Integer)
    '作业名称'
    job_name=Column(String)
    '待处理数据目录'
    data_dir=Column(String)
    '执行文件目录'
    execute_file_path=Column(String)
    '单条执行耗费资源，使用json'
    single_item_allocation=Column(String)
    '记录创建时间'
    create_time=Column(String)


    '是否已经转化, 转化指的是把批处理的所有作业条目存储数据库中'
    transfer_flag=Column(String)
    '转化状态'
    transfer_state=Column(String)
    '转化开始时间'
    transfer_begin_time=Column(String)
    '转化结束时间'
    transfer_end_time=Column(String)

