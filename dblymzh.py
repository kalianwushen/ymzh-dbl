import streamlit as st
st.image("https://www.gxvnu.edu.cn/images/QQtupian20240701090920_fuben.png")
tab1, tab2, tab3 ,tab4= st.tabs(["个人简历生成器", "南宁美食数据", "视频播放器","数字档案"])
with tab1:
    import streamlit as st# 导入库

    st.title("🎨个人简历生成器")
    st.text("使用Streamlit创建您的个性化简历")
    
    c1,c2=st.columns([1,2])
    with c1:
        st.subheader("个人信息表单")
        st.markdown('<hr style="border: none; border-top: 2px solid #007bff; margin: 0;">', unsafe_allow_html=True)

         # 表单组件
        name = st.text_input("姓名", "")
        position = st.text_input("职位", "")
        phone = st.text_input("电话", "")
        email = st.text_input("邮箱", "")
        birth_date = st.date_input("出生日期", value=None)
        gender = st.radio("性别", ["男", "女", "其他"],horizontal=True)
        education = st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"])
        # 语言能力（可多选） - 下拉选择框
        language_ability = st.multiselect(
            "语言能力",
            options=["汉语", "英语", "日语", "俄语",'法语','德语','西班牙语'],
            default=[]  # 默认选中项
        )

        language_text = "、".join(language_ability)
    
        # 技能（可多选）- 下拉多选框
        skills = st.multiselect(
            "技能 (可多选)",
            options=["Python", "Java", "JaveScript","HTML/CSS","SQL","数据分析", "机器学习", "深度学习","项目管理","UI/UX设计"],
            default=[]  # 默认选中项
        )

        # 工作经验（年）- 滑块
        work_experience = st.slider(
            "工作经验（年）",
            min_value=0,
            max_value=30,
            value=0,  # 默认值
            step=1  # 步长
        )

        # 期望薪资范围（元）- 双滑块
        salary_min, salary_max = st.slider(
            "期望薪资范围（元）",
            min_value=5000,
            max_value=50000,
            value=(10000, 20000),  # 默认的区间值
            step=1  # 步长
        )
        # 显示当前选择的薪资区间
        st.write(f"当前选择：{salary_min} - {salary_max} 元")
  
        # 个人简介 - 文本框
        personal_intro = st.text_area(
            label="个人简介",
            height=150,  
            placeholder="请简要介绍您的专业背景、职业目标和个人特点..."
        )

        # 每日最佳联系时间段 - 下拉选择框
        time_options = []
        for hour in range(0, 24):  # 小时范围 0~1
            for minute in [0, 15, 30, 45]:
                time_str = f"{hour:02d}:{minute:02d}"
                time_options.append(time_str)
        best_contact_time = st.selectbox(
            "每日最佳联系时间段",
            options=time_options,
            index=32 # 默认的时间段
        )   

        # 上传个人照片 - 文件上传组件
        uploaded_file = st.file_uploader(
            "上传个人照片",
            type=["jpg", "jpeg", "png"],  # 允许上传的文件类型
            accept_multiple_files=False  # 是否允许上传多个文件
        )
        # 如果有文件上传，简单显示文件名（预览图片，可结合 st.image 实现）
        if uploaded_file:
            st.write(f"已上传照片：{uploaded_file.name}")
        with c2:
            st.subheader("简历实时预览")
            st.markdown('<hr style="border: none; border-top: 2px solid #007bff; margin: 0;">', unsafe_allow_html=True)
    
            c1,c2=st.columns([1,2])
        with c1:
            st.write(f"{name}")
            if uploaded_file:
                st.image(uploaded_file)
            st.write(f"**职位**：{position}")
            st.write(f"**电话**：{phone}")
            st.write(f"**邮箱**：{email}")
            if birth_date:
                st.write(f"**出生日期**：{birth_date.strftime('%Y/%m/%d')}")
        with c2:
             st.write(f"**性别**：{gender}")
             st.write(f"**学历**：{education}")
             st.write(f"**工作经验**：{work_experience}年")
             st.write(f"**期望薪资**：{salary_min} - {salary_max} 元")
             st.write(f"**最佳联系时间**：{best_contact_time}")
             if language_text:
                 st.write(f"**语言能力**：{language_text}")

        st.markdown("---")
        st.write(f"### 个人简介")
        if personal_intro:
           st.write(personal_intro)
        else:
            st.text("这个人很神秘，没有留下任何介绍……")
        if skills:
            if skills:
                st.write(f"### 专业技能")
                st.write('\n'.join([f"* **{skill}**" for skill in skills]))

with tab2:
        # 导入库
    import streamlit as st
    import pandas as pd
    import numpy as np
    import random

    

    st.title("🍔 南宁美食探索")
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
    # 餐厅数据
    restaurants = pd.DataFrame({
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "价格": [15, 20, 25, 35, 50],
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    })
    st.subheader("💎南宁美食地图")
    st.map(restaurants)
    st.subheader("⭐餐厅评分")

    # 创建条形图
    st.bar_chart(restaurants, x='餐厅',y='评分')
  
    # 创建折线图
    st.subheader("💰不同类型餐厅价格")
    st.line_chart(restaurants, x='类型',y='价格')

    st.subheader("⏱用餐高峰时段")
    # 构造模拟的用餐高峰时段数据，这里假设按时间点（11.0 - 19.0 间隔 0.5 ）统计各餐厅用餐量
    time_points = np.arange(11.0, 19.5, 0.5)
    peak_data = {
        "时间": time_points,
        "星艺会尝不忘": np.random.randint(30, 100, size=len(time_points)),
        "高峰柠檬鸭": np.random.randint(30, 100, size=len(time_points)),
        "复记老友粉": np.random.randint(30, 100, size=len(time_points))
    }
    peak_df = pd.DataFrame(peak_data)
    peak_df = peak_df.set_index("时间")  # 设置时间为索引，方便绘图

    # 使用st.area_chart绘制面积图
    st.area_chart(peak_df)

    import streamlit as st

    restaurant_data = {
        "星艺会尝不忘": {
            "rating": "4.2/5.0",
            "average_cost": "15元",
            "recommended_dishes": ["桂林米粉", "瘦肉粉", "干拌粉"],
            "crowd_density":84
        },
        "高峰柠檬鸭": {
            "rating": "4.5/5.0",
            "average_cost": "20元",
            "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
            "crowd_density":90
        },
        "复记老友粉": {
            "rating": "4.0/5.0",
            "average_cost": "25元",
            "recommended_dishes": ["老友牛肉", "老友猪肉","炒粉"],
            "crowd_density":80
        },
        "好有缘": {
            "rating": "4.7/5.0",
            "average_cost": "35元",
            "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
            "crowd_density":94
        },
        "白妈螺蛳粉": {
            "rating": "4.3/5.0",
            "average_cost": "50元",
            "recommended_dishes": ["特色套餐", "地方小吃","时令蔬菜"],
            "crowd_density":86
        }
    }

    st.subheader("餐厅详情")
    selected_restaurant = st.selectbox("选择餐厅查看详情", list(restaurant_data.keys()))

    if selected_restaurant:
        data = restaurant_data[selected_restaurant]
      
        # 使用容器组织内容
        with st.container():
            st.markdown(f"### {selected_restaurant}")
          
            # 基本信息区域
            st.write(f"评分：{data['rating']}")
            st.write(f"人均消费：{data['average_cost']}")
        
            # 添加分隔线
            st.divider()
        
            # 推荐菜品区域
            st.subheader("推荐菜品")
            for dish in data["recommended_dishes"]:
                st.write(f"- {dish}")

        st.subheader("当前拥挤程度")
        crowd_percent = data['crowd_density']
        st.write(f"{crowd_percent}% 拥挤")
        progress_bar = st.progress(crowd_percent)
    
    st.subheader("5个餐厅12个月价格走势折线图")
    # 定义数据
    data = {
        '月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
        '星艺会尝不忘':[200, 150, 180,150,140,163,148,145,126,168,149,153],
        '高峰柠檬鸭':[120, 160, 123,145,125,148,169,142,125,145,165,154],
        '复记老友粉':[130, 120, 160,145,123,156,148,156,142,123,147,154],
        '好有缘':[150, 170, 160,141,145,141,156,124,157,184,142,152],
        '白妈螺蛳粉':[140, 160, 140,145,165,148,169,185,126,142,175,158],
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)

    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5], name='序号')

    # 通过x指定月份所在这一列为折线图的x轴
    st.line_chart(df, x='月份')

    st.subheader("🎲今日午餐推荐")

    # 餐厅数据
    restaurants = [
        {"名称": "复记老友粉", "类型": "快餐"},
        {"名称": "星艺会尝不忘", "类型": "中餐"},
        {"名称": "高峰柠檬鸭", "类型": "中餐"},
        {"名称": "西冷牛排店", "类型": "西餐"}
    ]

    # 按钮
    if st.button("帮我选午餐"):
        selected_restaurant = random.choice(restaurants)
        st.success(f"今日推荐: {selected_restaurant['名称']}({selected_restaurant['类型']})")
        st.text('🍛🍙🥟🍧🍦🍹🥛美味午餐等着你！')


with tab3:
    import streamlit as st# 导入库

    
    st.title("🎬Streamlit视频播放器")
    st.text("点击下方视频封面选择要播放的视频")
    st.subheader("视频播放")
   
    # 初始化会话状态，用于跟踪当前选中的视频
    if 'selected_video' not in st.session_state:
        st.session_state.selected_video = None

    # 定义视频数据
    videos = {
        "自然风光": {
            "title": "自然风光",
            "description": "美丽的自然景观，山川湖海",
            "duration": "0:27",
            "category": "自然",
            "url": "https://cdn.pixabay.com/video/2025/04/10/271161_large.mp4"
        },
        "城市夜景": {
            "title": "城市夜景",
            "description": "高楼大厦，灯光明亮",
            "duration": "0:30",
            "category": "城市",
            "url": "https://cdn.pixabay.com/video/2022/08/31/129716-745174979_large.mp4"
        },  
        "野生动物": {
            "title": "野生动物",
            "description": "活泼可爱",
            "duration": "0:49",
            "category": "动物",
            "url": "https://cdn.pixabay.com/video/2023/09/19/181314-866094614_large.mp4"
        }
    }

    # 在顶部显示选中的视频
    if st.session_state.selected_video:
        video = videos[st.session_state.selected_video]
        st.subheader(f"正在播放: {video['title']}")
        st.text(f"描述：{video['description']}")
        st.text(f"时长{video['duration']}：|分类：{video['category']}")
        st.video(video["url"])
        st.write("---")  # 添加分隔线

    # 创建分类选择下拉菜单
    st.subheader("视频库")
    st.text("点击图片选择视频")
    st.text("按分类筛选")
    selected_category = st.selectbox(
        '全部',
        ['全部', '自然风光', '城市夜景', '野生动物'],
        label_visibility='collapsed'
    )

    # 根据选择的分类显示视频
    if selected_category == "全部":
        # 显示所有分类的视频
        for category, video in videos.items():
        # 创建一个按钮，点击时更新选中的视频
            col1, col2 = st.columns([1, 11])  # 创建两列布局
            with col1:
                if st.button(f"▶️", key=f"play_{category}"):
                    st.session_state.selected_video = category
                
            with col2:
                st.subheader(video["title"])
                st.text(f"描述：{video['description']}")
                st.text(f"时长{video['duration']}：|分类：{video['category']}")
                st.video(video["url"])
    else:
        # 只显示所选分类的视频
        video = videos.get(selected_category)
        if video:
        # 创建一个按钮，点击时更新选中的视频
            col1, col2 = st.columns([1, 11])  # 创建两列布局
            with col1:
                if st.button(f"▶️", key=f"play_{selected_category}"):
                   st.session_state.selected_video = selected_category
                
            with col2:
                st.subheader(video["title"])
                st.text(f"描述：{video['description']}")
                st.text(f"时长{video['duration']}：|分类：{video['category']}")
                st.video(video["url"])

with tab4:
        import streamlit as st  # 导入streamlit并用st代替
        import pandas as pd   # 导入Pandas并用pd代替

        st.title("🕶️学生 KQ-数字档案") # 创建一个标题
        st.header("🔑基础信息") # 创建一个章节
        st.text("学生ID：23051170127") # 创建一个文本
        st.markdown("注册时间："':green[2023-09-09 10:30:24]'" |精神状态：✅正常")# 绿色文本
        st.markdown("当前教室："':green[6号实验实训楼301室]'" |安全等级："':green[绝密]')

        st.header("📊学习情况") # 创建一个章节
        c1, c2, c3 = st.columns(3) # 定义列布局，分成3列
        c1.metric(label="数据挖掘与数据分析",help='有一点小退步', value="78%",delta="-10%")
        c2.metric(label="深度学习技术", value="88%",delta="1%")
        c3.metric(label="云计算与大数据",help='接近瓶颈', value="98%",delta="2%")

        st.subheader("Streamlit课程进度")  # 显示进度条
        st.progress(value=33,text="Streamlit课程进度")

        st.header("📝任务日志") # 创建一个章节
        # 定义数据,以便创建数据框
        data = {
            '日期':['2025-05-28','2025-05-31','2025-06-03'],
            '任务':['学生数字档案','课程管理系统','数据图表展示'],
            '状态':['✔️完成','🕒进行中','❌未完成'],
            '难度':['⭐⭐⛤⛤⛤','⭐⛤⛤⛤⛤','⭐⭐⭐⛤⛤']
         }
        # 定义数据框所用的索引
        index = pd.Series([0,1,2])
        # 根据上面创建的data和index，创建数据框
        df = pd.DataFrame(data, index=index)
        st.table(df)

        st.subheader("🔐最新代码成果") # 创建一个子章节
        # 创建要显示的Java代码块的内容
        python_code = '''def klws():
            while True：
                if detect_vulnerability():
                    exploit()
                    return "ACCESS GRANTED"
                else:
                stealth_evade()
        '''
        st.code(python_code,line_numbers=True)  # 设置line_numbers为True，即该代码块有行号

        st.markdown('***')  # 分割线
        st.markdown(':green[>>SYSTEM MESSAGE:] ''下一个任务目标已解锁…') # 绿色文本
        st.markdown(':green[>>TARGERT:] ''课程管理系统')
        st.markdown(':green[>>COUNTDOWN:] ''2025-06-02 13:14:52')
        st.markdown('系统状态：在线   连续状态：已加密')
    
    
