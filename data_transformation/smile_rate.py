import pandas as pd

df = pd.read_csv('data.csv')

# calculate the smile_rate
smile_rate = df['smile'] / (df['smile'] + df['fine'] + df['cry'])
smile_rate = smile_rate.round(4)
df['smile_rate'] = smile_rate

df.to_csv('data.csv', index=False)

# calculate the cry_rate
smile_rate = df['cry'] / (df['smile'] + df['fine'] + df['cry'])
smile_rate = smile_rate.round(4)
df['cry_rate'] = smile_rate

df.to_csv('data.csv', index=False)

# broad category
df['category_origin'] = df['category']
df.replace({'category': {'Cantonese Cuisine(Guangdong)': 'Hong Kong Style', 'Taiwan Cuisine': 'Chinese Cuisine', 'Sichuan Cuisine': 'Chinese Cuisine','Dianella(Yunnan)': 'Chinese Cuisine','Shanghai Cuisine': 'Chinese Cuisine','Beijing, Sichuan and Shanghai': 'Chinese Cuisine','Hunan Cuisine': 'Chinese Cuisine','Beijing Cuisine(Official Cuisine)': 'Chinese Cuisine','Fujian Cuisine': 'Chinese Cuisine','Shunde Cuisine': 'Chinese Cuisine','Irish Cuisine': 'British Cuisine','Teochew Cuisine': 'Chinese Cuisine','Thai Cuisine': 'Southeast Asian Cuisine','Vietnamese Cuisine': 'Southeast Asian Cuisine','Singaporean Cuisine': 'Southeast Asian Cuisine','Malaysian Cuisine': 'Southeast Asian Cuisine','Indonesian cuisine': 'Southeast Asian Cuisine','Hakka cuisine': 'Chinese Cuisine'}}, inplace=True)
df.replace({'category': {'Italian Cuisine': 'European cuisine','French Cuisine': 'European cuisine','Spanish Cuisine': 'European cuisine','British Cuisine': 'European cuisine','German Cuisine': 'European cuisine','Belgian Cuisine': 'European cuisine','Portuguese Cuisine': 'European cuisine','Eastern European cuisine': 'European cuisine'}}, inplace=True)
df.to_csv('data.csv', index=False)

# print(df1["district"].value_counts().index)
df['district_map_origin'] = df['district_map']
df.replace({'district_map': {'Sai Wan': 'Central and Western District',
                             'Central': 'Central and Western District',
                             'Tsim Sha Tsui': 'Yau Tsim Mong District',
                             'Tseung Kwan O': 'Sai Kung District',
                             'Tsuen Wan': 'Tsuen Wan District',
                             'North Point': 'Eastern District',
                             'Mong Kok': 'Yau Tsim Mong District',
                             'Causeway Bay': 'Wan Chai District',
                             'Kwun Tong': 'Kwun Tong District',
                             'Wan Chai': 'Wan Chai District',
                             'Tseung Kwan': 'Sai Kung District',
                             'Prince Edward': 'Kowloon City District',
                             'Lai Chi Kok': 'Kwai Tsing District',
                             'Kowloon City': 'Kowloon City District',
                             'Sha Tin': 'Sha Tin District',
                             'Tai Po': 'Tai Po District',
                             'Sheung Wan': 'Wan Chai District',
                             'San Po Kong': 'Kowloon City District',
                             'Sai Kung': 'Sai Kung District',
                             'Yuen Long': 'Yuen Long District',
                             'Kwai Chung': 'Kwai Tsing District',
                             'Kwai Fong': 'Kwai Tsing District',
                             'Kowloon Bay': 'Kwun Tong District',
                             'To Kwa Wan': 'Kowloon City District',
                             'Hung Hom': 'Kowloon City District',
                             'Tin Shui Wai': 'Yuen Long District',
                             'Jordan': 'Yau Tsim Mong District',
                             'Yau Ma Tei': 'Yau Tsim Mong District',
                             'Tai Kok Tsui': 'Yau Tsim Mong District',
                             'Quarry Bay': 'Eastern District',
                             'Sham Shui Po': 'Sham Shui Po District',
                             'Cheung Sha Wan': 'Sham Shui Po District',
                             'Tuen Mun': 'Tuen Mun District',
                             'Tai Wai': 'Sha Tin District',
                             'Tsing Yi': 'Kwai Tsing District',
                             'Ma On Shan': 'Sha Tin District',
                             'Fanling': 'North District',
                             'Chai Wan': 'Eastern District',
                             'Aberdeen': 'Southern District',
                             'Sheung Shui': 'North District',
                             'Tung Chung': 'Islands District',
                             'Shau Kei Wan': 'Eastern District',
                             'Wong Tai Sin': 'Wong Tai Sin District',
                             'Taikoo': 'Eastern District',
                             'Cheung Chau': 'Islands District',
                             'Tin Hau': 'Wan Chai District',
                             'Admiralty': 'Wan Chai District',
                             'Sai Wan Ho': 'Eastern District',
                             'Ngau Tau Kok': 'Kwun Tong District',
                             'Lam Tin': 'Kwun Tong District',
                             'Fo Tan': 'Sha Tin District',
                             'Ap Lei Chau': 'Islands District',
                             'Wong Chuk Hang': 'Southern District',
                             'Chek Lap Kok': 'Islands District',
                             'Happy Valley': 'Wan Chai District',
                             'Kowloon Tong': 'Kowloon City District',
                             'Yau Tong': 'Kwun Tong District',
                             'Lantau Island': 'Islands District',
                             'Tai Hang': 'Wan Chai District',
                             'Ho Man Tin': 'Kowloon City District',
                             'Pok Fu Lam': 'Southern District',
                             'Diamond Hill': 'Wong Tai Sin District',
                             'Shek Kip Mei': 'Sham Shui Po District',
                             'Meifoo': 'Kwai Tsing District',
                             'Tsz Wan Shan': 'Wong Tai Sin District',
                             'Lok Fu': 'Kwun Tong District',
                             'Rainbow': 'Kwun Tong District',
                             'Lamma Island': 'Islands District',
                             'The Peak': 'Central and Western District',
                             'Tai O': 'Islands District',
                             'Tai Wo': 'Tai Po District',
                             'Stanley': 'Southern District',
                             'Sham Tseng': 'Tsuen Wan District',
                             'Discovery Bay': 'Islands District',
                             'Lei Yue Mun': 'Kwun Tong District',
                             'Mid-Levels': 'Central and Western District',
                             'Ma Wan': 'Tsuen Wan District',
                             'Peng Chau': 'Islands District',
                             'Heng Fa Chuen': 'Central and Western District',
                             'Lau Fau Shan': 'Yuen Long District',
                             'Repulse Bay': 'Southern District',
                             'Shek O': 'Southern District',
                             'Deep Water Bay': 'Southern District',
                             'Po Toi Island': 'Southern District',
                             'Lok Ma Chau': 'Yuen Long District',
                             'Lo Wu': 'North District'}}, inplace=True)
df.to_csv('data.csv', index=False)
