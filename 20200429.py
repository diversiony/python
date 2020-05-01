# 計算で使うかもしれないNumPy
import numpy as np
# データフレームを使うためにPandas
import pandas as pd
 
# 可視化ライブラリ
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# データセット
from sklearn import datasets
# ランダムフォレスト回帰のクラスをRFRというあだ名を付けてimport
from sklearn.ensemble import RandomForestRegressor  as RFR
 
# 教師データとテストデータに分割してくれる
from sklearn.model_selection import train_test_split
 
# 平均二乗誤差を計算する関数
from sklearn.metrics import mean_squared_error
 
# もしパラメータ探索がしたい場合は以下もimport
from sklearn.model_selection import GridSearchCV
 
# もしデータの標準化がしたい場合は以下もimport
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', 100)

# ボストンデータの読み込み
boston = datasets.load_boston() 

print( boston.keys() )

# 教師データとテストデータに分割
train_data, test_data, train_target, test_target = train_test_split(boston.data, boston.target, test_size=0.2)

# データフレーム化 
train_df = pd.DataFrame(train_data, columns=boston.feature_names)
 
# 上から10行を表示
print( train_df.head(5) )

# 予測したい値
train_df["MEDV"] = train_target
 
print( train_df.head(5) )

#print( train_df.info() )

# 統計量の表示
print( train_df.describe() )

#PairGrid pg = sns.pariplot( train_df )

#pg = sns.pairplot( train_df )
#pg.savefig('C:\\Users\\diver\\boston.png')

rg = RFR(n_jobs=-1, random_state=2525) # n_jobs=-1でコアすべてを使って並列に学習できる
 
rg.fit(train_data, train_target) # 訓練

predicted_train_target = rg.predict(train_data)
print( "mean_squared_error(training) " + str(mean_squared_error(train_target, predicted_train_target)) )

predicted_test_target = rg.predict(test_data)
print( "mean_squared_error(test) " + str(mean_squared_error(test_target, predicted_test_target)) )

print( rg.score(test_data, test_target) )

# データフレーム化 
test_df = pd.DataFrame(test_data, columns=boston.feature_names)

# 予測したい値
test_df["MEDV"] = test_target
 
print( test_df.head(5) )