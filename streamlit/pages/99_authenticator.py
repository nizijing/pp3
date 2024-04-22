#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   99_authenticator.py
@Time    :   2024/02/02 10:44:57
@Author  :   zijing
@Version :   1.0
@Site    :   
@Desc    :   None
'''

import streamlit as st
from common.auth import devops_auth, load_config, save_config, get_authenticator_from_config


def intro():
    st.write("# Welcome to 用户管理界面 ! 👋")


def change_passwd():
    st.write("Change password")
    config = load_config()
    authenticator = get_authenticator_from_config(config)
    try:
        if authenticator.reset_password(st.session_state["username"]):
            save_config(config)
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)


def forgot_passwd():
    st.write("Forgot password")
    config = load_config()
    authenticator = get_authenticator_from_config(config)
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
        if username_of_forgotten_password:
            save_config(config)
            st.success(new_random_password)
        else:
            st.error('Username not found')
    except Exception as e:
        st.error(e)


def create_users():
    st.write("Create users")
    config = load_config()
    authenticator = get_authenticator_from_config(config)
    try:
        if authenticator.register_user(preauthorization=False):
            save_config(config)
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)


def delete_users():
    st.write("Delete users")
    st.write("没有删除用户的功能，可以修改他的密码")
    forgot_passwd()


def modify_users():
    st.write("Modify users")
    config = load_config()
    authenticator = get_authenticator_from_config(config)
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            save_config(config)
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)


def user_is_admin(username):
    return username in ["devops", "lihongliang", "luohui", "nizijing"]


def main():
    page_names_to_funcs = {
        "—": intro,
        "新增用户": create_users,
        "修改用户": modify_users,
        "删除用户": delete_users,
        "修改密码": change_passwd,
        "忘记密码": forgot_passwd,
    }

    demo_name = st.sidebar.selectbox("用户管理", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()


if st.session_state.get("authentication_status", False):
    if user_is_admin(st.session_state["username"]):
        st.write('welcome *%s*' % (st.session_state["name"]))
        main()
else:
    name, authentication_status, username = devops_auth()
    if user_is_admin(username) and authentication_status:
        st.write('welcome *%s*' % (name))
        main()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')


