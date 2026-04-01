import pandas as pd

# CSV 읽기
df = pd.read_csv("data.csv")

print("원본 데이터")
print(df)

# 중복 제거
df = df.drop_duplicates()

# 지역별 평균 가격
region_avg = df.groupby("region")["price"].mean()

print("\n지역별 평균 가격")
print(region_avg)

region_avg.to_excel("result.xlsx")