import pandas as pd

'''
**** note ****
bicycle_information.csv = 2021년 1월까지의 따릉이 대여소 데이터
gu_count_df <= 구별 따릉이 정류소 보유개수 dataframe
'''

bi_df = pd.read_csv("data/bicycle_information.csv")

gu_count_df = bi_df[["소재지(위치)"]]
gu_count_df = gu_count_df.value_counts().reset_index(name = "count")