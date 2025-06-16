import streamlit as st
from datetime import datetime, time

st.set_page_config(layout="wide")
st.title("🎨 个人简历生成器")
st.text("使用Streamlit创建您的个性化简历")


c1,c2=st.columns([1,2])
with c1:
    st.subheader("个人信息表单")
    st.markdown("---")
    xm=st.text_input('姓名', '')
    zw=st.text_input('职位', '')
    dh=st.text_input('电话', '')
    yx=st.text_input('邮箱', '')
    cs= st.date_input("出生日期", value=datetime.today())  
    # 转成字符串后按 "-" 分割
    year, month, day = str(cs).split("-")  
    # 拼接成 "YYYY/MM/DD" 格式
    cs = f"{year}/{month}/{day}"  
    
    
    # 设置水平排列
    xb=st.radio("性别",['男', '女', '其他'],horizontal=True,)
    xl=st.selectbox('学历', ['高中', '专科', '本科','硕士','博士'])
    yy= st.multiselect('语言能力(可多选)',['中文', '英文', '日语', '法语', '德语',"西班牙语"])
    jn=st.multiselect('技能（可多选）',['Python', 'Java', 'JavaScript','HTML/CSS','SQL','数据分析','机器学习','深度学习','项目管理','UI/UX设计'])
    jy=st.slider('工作经验（年）',0,30,0)
    xz=st.slider('期望薪资范围（元）',5000, 50000, (10000, 20000))
    jj=st.text_area(label='个人简历', placeholder='请简要介绍您的专业背景,职业目标和个人特点...')
    sj=st.time_input("每日最佳联系时段", datetime(2025, 7, 6, 21, 15))
    sj= sj.strftime("%H:%M")
    st.subheader("上传个人照片")
    uploaded_file = st.file_uploader("Drag and drop file here  Limit 200MB per file · JPG, JPEG, PNG", 
                                     type=["jpg", "jpeg", "png"], 
                                     accept_multiple_files=False)

    
with c2:
    st.subheader("简历实时预览")
    st.markdown("---")
    c1,c2=st.columns([1,2])
    with c1:
        st.write(xm)
        # 输出上传的照片
        if uploaded_file:
            st.image(uploaded_file)
        st.write("职位:",zw)
        st.write("电话:",dh)
        st.write("邮箱:",yx)
        st.write("出生日期:",cs)

    with c2:
        st.write("性别:",xb)
        st.write("学历:",xl)
        st.write("工作经验:", f"{jy} 年")
        xz= f"{xz[0]} - {xz[1]} 元" 
        st.write("期望薪资:",xz)
        st.write("最佳练习时间:",sj)
        yy= ", ".join(yy)
        st.write("语言能力:",yy)
    with st.container():
        st.markdown('***')
        st.subheader("个人简介")
        # 判断个人简历内容是否为空，为空显示提示文本，不为空显示用户输入内容
        if not jj:  
            st.write("这个人很神秘，没有留下任何介绍...")
        else:
            st.write(jj)
        if jn:  
            st.subheader("专业技能")
            # 遍历技能列表，逐个输出
            for jn in jn:
                st.write(jn)
