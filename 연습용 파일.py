import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gender = ["남자","여자"]
gender_list = []
height_list = []
weight_list = []

#무작위로 데이터 만들기
for i in range(100) :
    idx = np.random.randint(2)
    gender_list.append(gender[idx])
    if idx == 0 :
        height_list.append(np.random.randint(170,190))
        weight_list.append(np.random.randint(70,80))
    else :
        height_list.append(np.random.randint(150,165))
        weight_list.append(np.random.randint(40,60))

data2 = {"gender" : gender_list,"height" : height_list,"weight" : weight_list}

ex_df2 = pd.DataFrame(data2)

plt.rc("font",family = "Malgun Gothic")
sns.scatterplot(data = ex_df2,x = "weight",y = "height",hue = "gender")
plt.show()
