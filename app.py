import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import joblib
import json
import base64

# Set page width
st.set_page_config(layout="wide")

# # Custom CSS styles
# st.markdown("""
#     <style>
#         .stApp {
#             background-color: #B4B4B8;
#         }
#         .stApp * {
#             color: white;
#         }
#         .sidebar .sidebar-content {
#             background-color: #378CE7;
#             color: #ffffff;
#         }
#         .sidebar .sidebar-content .block-container {
#             margin-top: 20px;
#         }
#         .stButton>button {
#             background-color: #2ecc71;
#             color: #ffffff;
#             border-radius: 5px;
#             padding: 10px 20px;
#             font-size: 16px;
#         }
#         .stButton>button:hover {
#             background-color: #27ae60;
#         }
#         .stTextInput>div>div>input {
#             border-radius: 5px;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)



# Setting custom css
css = f"""
<style>

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""
st.markdown(css, unsafe_allow_html=True)


#impliment background formating
def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-repeat: no-repeat;
             background-position: right 50% bottom 50% ;
             background-size: cover;
             background-attachment: scroll;
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )

set_bg_hack("G:\\Loan Data Analysis\\images\\black-wallpaper-to-set-as-background-17-640x360.jpg")



# # Custom CSS styles
# st.markdown("""
#     <style>
#         .stApp {
#             background-color: #B4B4B8;
#         }
#         .sidebar .sidebar-content {
#             background-color: #378CE7;
#             color: #ffffff;
#         }
#         .sidebar .sidebar-content .block-container {
#             margin-top: 20px;
#         }
#         .stButton>button {
#             background-color: #2ecc71;
#             color: #ffffff;
#             border-radius: 5px;
#             padding: 10px 20px;
#             font-size: 16px;
#         }
#         .stButton>button:hover {
#             background-color: #27ae60;
#         }
#         .stTextInput>div>div>input {
#             border-radius: 5px;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)

## Side Tab:
l=["Giới thiệu","Dự đoán Điểm tín dụng của bạn"]
st.sidebar.subheader("Sau đây là những gì bạn có thể làm:")
option=st.sidebar.selectbox("Chọn những gì bạn muốn làm:",l)

def page_1():
    ## Intro Tab::


    ## Headers:
    # st.set_page_config(page_title="Giới thiệu")
    st.title("MÔ HÌNH DỰ ĐOÁN KHẢ NĂNG VỠ NỢ TỪ DỮ LIỆU TÍN DỤNG 🏦")
    st.header("Giới thiệu 📝")
    st.write("""
        #### Cho vay là hoạt động kinh doanh cơ bản của các ngân hàng, với nguồn lợi nhuận chính là lãi suất tích lũy từ các khoản vay. Trước khi cấp khoản vay, các tổ chức tài chính tiến hành một quá trình xác minh và xác nhận kỹ lưỡng. Mặc dù vậy, vẫn còn sự không chắc chắn về việc liệu người nộp đơn có khả năng trả nợ mà không gặp khó khăn hay không. Trong bài viết này, tôi xây dựng một mô hình dự đoán nhằm xác định xem người nộp đơn có khả năng trả nợ cho công ty cho vay hay không.
        """)
    st.markdown("---") 
    
    
    st.header("Problem 🤔")
    st.write("""#### Hiện tại, quy trình thẩm định khoản vay của các công ty này dựa trên nhiều yếu tố như tuổi tác, quyền sở hữu nhà, kinh nghiệm làm việc, mục đích vay, thu nhập, số tiền vay và lịch sử tín dụng. Tuy nhiên, quá trình này vẫn còn mang tính thủ công và tốn thời gian, dẫn đến hiệu quả chưa cao và khả năng xảy ra sai sót. Hơn nữa, với sự gia tăng nhanh chóng của số lượng đơn xin vay, các công ty cho vay cần một giải pháp tự động và chính xác hơn để đánh giá rủi ro tín dụng và đưa ra quyết định cho vay. Vấn đề đặt ra là làm thế nào để xây dựng một mô hình dự đoán hiệu quả, có khả năng tự động hóa quá trình đánh giá điều kiện vay và xác định chính xác các phân khúc khách hàng đủ điều kiện cho các khoản vay. Mô hình này cần phải có khả năng xử lý lượng lớn dữ liệu, tích hợp nhiều yếu tố đánh giá, và đưa ra dự đoán chính xác về khả năng trả nợ của người vay.

                """)
    st.markdown("---") 

    st.header("Tổng quan nhanh về tập dữ liệu 🗃️")
    df = pd.read_csv("G:\\Loan Data Analysis\\data\\credit_risk_dataset2.csv")
    st.dataframe(df.head())

    st.markdown("---")

    st.header("Top Insights 🧐")
    st.write("""
           - **Age Distribution**: Phần lớn người vay có độ tuổi từ 20-35, cho thấy những người nộp đơn vay trẻ tuổi.
           - **Housing Status**: Một nửa tập dữ liệu của chúng tôi nằm trong nhà cho thuê, trong khi 40% có nhà thế chấp.
           - **Loan Preference**: Các khoản vay giáo dục phổ biến nhất, tiếp theo là các khoản vay y tế. Các khoản vay cá nhân và đầu tư cho thấy nhu cầu tương tự.
           - **Default Rates**: Trong khi hầu hết người vay có hồ sơ sạch, một bộ phận nhỏ vỡ nợ 3-5 lần.
           - **Loan Grades**: Các lớp A và B chiếm ưu thế, phản ánh rủi ro thấp hơn. Các lớp C-G biểu thị rủi ro cao hơn, với ít trường hợp hơn.
           - **Loan Amounts**: Các khoản vay từ 5000 đến 10000 đô la là phổ biến nhất, tiếp theo là các khoản vay từ 300 đến 5000 đô la. Một nhóm đáng kể vay hơn 15000 đô la.

             """)
    
    st.markdown("---") 

    st.header("Công nghệ sử dụng🤖")
    st.write("""
            - Pandas: Thư viện Python để xử lý và phân tích dữ liệu.
            - Numpy: Thư viện Python xử lý data.
            - Streamlit: Thư viện Python để xây dựng ứng dụng web.
            - Joblib: Thư viện Python để lưu và tải các mô hình học máy.
            - Scikit-learn: Thư viện python trong machine learning.
            - Plotly: Thư viện Python để trực quan hóa dữ liệu tương tác.
            - Machine learning algorithms: XG Boost, Random Forest, Logistic Regression, and Support Vector Machine.
            - SMOTE: Thư viện Python để lấy mẫu quá mức dữ liệu.
            """)
    st.markdown("---") 

    st.header("About the developer 👨🏻‍💻")
    st.markdown("""
                This app is developed by me

        [![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/Khavanw)
               
             """)
    


def page_2():
    data = {}
    
    # Divide the page into three columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Details Tab:
    with col2:
        st.header("Hãy cho tôi thông tin chi tiết của bạn!")

    # Full Name:
    with col2:
        first = st.text_input("Nhập Tên của bạn:")
        last = st.text_input("Nhập Họ của bạn:")
        data["First Name"] = first
        data["Last Name"] = last

    name = first + " " + last
    data["Full Name"] = name

    # Age:
    with col2:
        age = st.slider("Nhập tuổi của bạn:", 20, 85)
        data["Age"] = age

    # Annual Income:
    with col2:
        ai = st.number_input("Nhập Thu nhập hàng năm của bạn:", 1, 1000000)
        data["Annual Income"] = ai

    # Home Ownership:
    with col2:
        ho = st.selectbox("Loại hình sở hữu nhà là gì:", ["RENT", "OWN", "MORTGAGE", "OTHER"])
        data["Home Ownership"] = ho

    # Employment Length:
    with col2:
        el = st.number_input("Nhập Kinh nghiệm làm việc của bạn theo năm:", 2, 50)
        data["Employment Length"] = el

    # Loan Intent:
    with col2:
        li = st.selectbox("Tại sao bạn muốn vay tiền?", ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'])
        data["Loan Intent"] = li

    # Loan Grade:
    with col2:
        lg = st.selectbox("Mức độ cho vay mong đợi?", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        data["Loan Grade"] = lg

    # Loan Amount:
    with col2:
        la = st.number_input("Nhập số tiền vay của bạn:", 100, 10000000000)
        data["Loan Amount"] = la

    # Loan Amount:
    with col2:
        lit = st.number_input("Lãi suất vay:", 1, 100)
        data["Loan Interest"] = lit

    # loan_percent_income:
    with col2:
        lpi = st.number_input("Nhập % Thu nhập của bạn để sử dụng cho việc trả nợ:", 0, 100)
        data["Loan Percent Income"] = lpi

    # cb_person_default_on_file:
    with col2:
        def_his = st.selectbox("Bạn đã bao giờ vỡ nợ chưa?", ["Y", "N"])
        data["Previous Defaults"] = def_his

        if def_his == "Y":
            # cb_person_cred_hist_length:
            n_def = st.slider("Tổng số lần vỡ nợ:", 0, 10)
            data["Number of Defaults"] = n_def
        else:
            data["Number of Defaults"] = 0
            n_def = 0

    # Make a submit button:
    with col2:
        # Display the input data as a json:
        if st.button("Hiển thị dữ liệu", key=8):
            data_display = json.dumps(data)
            temp = pd.DataFrame(data, index=[0])  # making a record
            st.write("Dữ liệu ở định dạng JSON:")
            st.write(data_display)
            st.write("\nDữ liệu ở định dạng bảng:")
            st.write(temp)

        # Display the prediction:
        if st.button("Kiểm tra tính đủ điều kiện", key=9):
            # Order of passing the data into the pipeline:
            cols = ['person_age', 'person_income', 'person_emp_length', 'loan_amnt', "loan_int_rate",
                    'loan_percent_income', 'cb_person_cred_hist_length',
                    'person_home_ownership', 'loan_intent', 'loan_grade',
                    'cb_person_default_on_file']  # List of columns of the original dataframe

            input_data = [[data["Age"], data["Annual Income"], data["Employment Length"], data["Loan Amount"],
                        data["Loan Interest"],
                        round(data["Loan Percent Income"] / 100, 2), data["Number of Defaults"],
                        data["Home Ownership"], data["Loan Intent"], data["Loan Grade"], data["Previous Defaults"]]]

            pipe = joblib.load('G:\\Loan Data Analysis\\scripts\\best_pipeline_1.pkl')  # Loading the pipeline

            input_data = pd.DataFrame(input_data, columns=cols)  # Converting input into a dataframe with respective columns

            res = pipe.predict(input_data)[0]  # Predicting the class
            prob = pipe.predict_proba(input_data)[0][res]  # Predicting the probability of the class
            out = {1: "Khách hàng có khả năng VỠ NỢ. Do đó, việc cho vay là RỦI RO!",
                0: "Khách hàng CÓ KHẢ NĂNG TRẢ NỢ. Do đó, CÓ THỂ cung cấp khoản vay!"}
            st.write(f"Dự đoán cuối cùng thu được từ mô hình đã cho là: {out[res]}, với xác suất là {round(prob * 100, 2)}%")

            if res == 1:
                image_n = Image.open('G:\\Loan Data Analysis\\images\\not_approve.png')
                st.image(image_n)
            else:
                image_a = Image.open('G:\\Loan Data Analysis\\images\\approve.png')
                st.image(image_a, width=400)




if option==l[0]:
    page_1()

if option==l[1]:
    page_2()