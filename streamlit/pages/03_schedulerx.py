#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   02_schedulerx.py
@Time    :   2024/01/30 18:11:51
@Author  :   zijing
@Version :   1.0
@Site    :   
@Desc    :   None
'''


import streamlit as st
from common.auth import devops_auth


def intro():
    st.write("# Welcome to 分布式调度器X! 👋")
    

def get_task_list():
    from aliapi.SchedulerXApi import SchedulerXApi
    client = SchedulerXApi.get_client()

    with st.container():
        cols1,cols2 = st.columns(2)
        with cols1.container():
            region_id = st.radio("区域id", ("cn-hangzhou",))
        with cols2.container():
            nameSpace_dict = SchedulerXApi.get_ListNamespacesRequest(client, region_id)
            namespace_select = st.radio("namespace:", nameSpace_dict.keys())
            namespace_uid = nameSpace_dict[namespace_select]
            
    
    st.divider()
    search_str = st.text_input("检索字段")

    group_dict = SchedulerXApi.get_ListGroups(client, namespace_uid, region_id)
    group_id = st.radio("应用:", group_dict.keys())
    status_map = {0: "禁用", 1:"启用"}

    if st.button("开始搜索"):
        if not search_str:
            st.warning("请输入检索的字段")
            return
        job_List = SchedulerXApi.get_ListJobs(client, namespace_uid, region_id, group_id)

        for job in job_List:
            if job["Content"].find(search_str) != -1:
                st.write(job["Name"], status_map[job["Status"]], job["TimeConfig"]["TimeExpression"])


def main():
    page_names_to_funcs = {
        "—": intro,
        "搜索任务": get_task_list,
    }

    demo_name = st.sidebar.selectbox("分布式调度器X", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()


if st.session_state.get("authentication_status", False):
    st.write(f'Welcome *{st.session_state["name"]}*')
    main()
else:
    name, authentication_status, username = devops_auth()
    if authentication_status:
        st.write('welcome *%s*' % (name))
        main()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

