# Loan Risk Prediction

## Giới thiệu
Dự án này nhằm xây dựng một mô hình dự đoán rủi ro cho vay sử dụng các thuật toán machine learning. Mục tiêu là dự đoán khả năng một khoản vay có thể bị vỡ nợ dựa trên các đặc điểm của người vay và khoản vay.

## Yêu cầu
- Python 3.7+
- pandas
- numpy
- scikit-learn
- xgboost

Bạn có thể cài đặt các thư viện cần thiết bằng lệnh:

pip install pandas numpy scikit-learn xgboost

## Cấu trúc dự án

loan-risk-prediction/
- best_model/
  - best_pipeline.joblib
  - best_pipeline.pkl
  - random_forest_model.joblib
- data/
  - credit_risk_dataset1.csv
  - credit_risk_dataset2.csv
  - loan_data.csv
- images/
- scripts/
  - Credit_Prediction.ipynb
  - Loan_Prediction.ipynb
  - pipeline.ipynb
- app.py
- requirements.txt
- README.md



## Quy trình thực hiện

1. **Thu thập và tiền xử lý dữ liệu**
   - Làm sạch dữ liệu
   - Xử lý giá trị thiếu
   - Mã hóa biến phân loại

2. **Khám phá và phân tích dữ liệu (EDA)**
   - Visualize phân phối các biến
   - Phân tích tương quan

3. **Feature Engineering**
   - Tạo các đặc trưng mới
   - Chuẩn hóa đặc trưng

4. **Xây dựng và huấn luyện mô hình**
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - XGBoost với hyperparameter tuning

5. **Đánh giá mô hình**
   - Sử dụng các metric như accuracy, precision, recall, F1-score, và AUC-ROC

## Hướng dẫn sử dụng

1. Clone repository:

## Kết quả
(Thêm bảng so sánh hiệu suất của các mô hình sau khi có kết quả)

## Tối ưu hóa hyperparameter
Đối với XGBoost, chúng tôi sử dụng GridSearchCV để tìm các hyperparameter tối ưu. Các tham số được điều chỉnh bao gồm:
- learning_rate
- max_depth
- n_estimators
- subsample


## Giấy phép
[MIT](https://choosealicense.com/licenses/mit/)
