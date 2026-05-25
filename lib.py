import pandas as pd
data={"name":["pooja","anjali","john"],
      "age":[20,30,40],
      "qualified":[True,False,False],
      "address":["Nagpur","Pune","Mumbai"],
      "mob no":[50,60,70]}
df=pd.DataFrame(data)
newdf = df.drop(["name","address"],axis=1)
print(newdf)
