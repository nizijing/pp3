import streamlit as st
from jinja2 import Environment, FileSystemLoader
from appDataClass import App

# __app = {
#     'name': 'test',
#     'replicas': 1,
#     'namespace': 'test'
# }

namespaceMap = {
    '生产环境': 'production',
    '预发布环境': 'pre',
    '开发环境': 'dev',
    '测试环境': 'test'
}

def generate_k8s_yaml(app_name):
    __app = App(app_name)

    namespace = st.selectbox("部署环境", namespaceMap.keys())
    __app.namespace = namespaceMap[namespace]
    __app.update_replicas()

    __app.first_image_tag = st.text_input("镜像tag", "")
    st.write(__app)

    if st.button("生成k8s.yaml"):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('k8s_deployment.j2')

        body = template.render(app = __app)
        st.code(body, language='yaml')


app_name = st.text_input("app name", "")
if app_name == '':
    st.error('you must set app name first')
else:
    generate_k8s_yaml(app_name)