#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   devops.py
@Time    :   2024/01/30 17:32:11
@Author  :   zijing
@Version :   1.0
@Site    :   
@Desc    :   None
'''

import streamlit as st
import os
from common.auth import get_authenticator


def main():
    env_vars = ["ALIBABA_CLOUD_ACCESS_KEY_ID", "ALIBABA_CLOUD_ACCESS_KEY_SECRET", "ORGANIZATIONID"]

    st.write("环境变量检测")
    for env_var in env_vars:
        if env_var in os.environ:
            st.markdown("- {} ok.".format(env_var))
        else:
            st.error("{} is not set.".format(env_var))


if __name__ == "__main__":
    authenticator = get_authenticator()
    name, authentication_status, username = authenticator.login()
    if authentication_status:
        with st.container():
            cols1,cols2 = st.columns(2)
            cols1.write('welcome *%s*' % (name))
            with cols2.container():
                authenticator.logout('Logout', 'main')
        main()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

