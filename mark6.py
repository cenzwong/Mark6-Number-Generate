# -*- coding: utf-8 -*-
"""Mark6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uWxrZ-mxprjeERfoLaBBOW6iMuGe8gnx
"""

import pandas as pd

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vR4c2uYSSSFd_MQ_aifSUH4d3gPLVGoSnmVTzMHbHe0YOjUJJHkKtvM4SzI3HEb2R-dKI07lvjhh4AC/pub?gid=0&single=true&output=csv")
df_six_history = df.dropna(axis=1, how="any")
df_six_history

"""

```
# 
獎	派彩 / 獎金分配
頭　獎	獎金基金減去四獎至七獎的總獎金及金多寶扣數後的 45%
每期頭獎獎金定為不少於港幣8,000,000元
二　獎	獎金基金減去四獎至七獎的總獎金及金多寶扣數後的 15%
三　獎	獎金基金減去四獎至七獎的總獎金及金多寶扣數後的 40%
四　獎	固定派彩為每注港幣9,600元
五　獎	固定派彩為每注港幣640元
六　獎	固定派彩為每注港幣320元
七　獎	固定派彩為每注港幣40元
```


"""

MarkSixPrice = {"3.0":40, "3.5":320, "4.0":640, "4.5":9600,  "5.0":100000, "5.5":1000000,  "6.0":1000000}

def getBingoNum(_iloc,df_history):
    sixNum = df_history.iloc[_iloc]["_1":"_6"]
    specialNum = {df_history.iloc[_iloc]["_6_5"]}
    return sixNum,specialNum

def getHistoryBingo(ary_yourNum,df_history):
  result = []
  id = []
  dollar = []
  for i in range(len(df_history)):
    sixNum,specialNum = getBingoNum(i, df_history)
    bingo = len(set(ary_yourNum) & set(sixNum))
    bingo = bingo + len(set(ary_yourNum) & set(specialNum))/2
    if bingo >= 3:
      result.append(bingo)
      dollar.append(MarkSixPrice[str(bingo)])
      id.append(df_history.iloc[i]["id"])

  myResult = {'ID':id,'Price':result,'Dollar':dollar}
  df_myPrice = pd.DataFrame(myResult)
  return df_myPrice

mySix = [4,	8,	15,	18,	30,	45]

getHistoryBingo(mySix,df_six_history)

"""# Random generate number and return best number"""

import random

def getRandSix():
  randSix = []
  while len(randSix) !=6:
    RandNum = random.randint(1,49)
    duplicate = len(set(randSix) & set({RandNum}))
    if duplicate == 0:
      randSix.append(RandNum)
  randSix.sort()
  return randSix

myRand = getRandSix()

myRand

"""# Feed in random mark six and find the most repeated combination to earn point"""

myRand = getRandSix()
df_result = getHistoryBingo(myRand,df_six_history)
print(myRand)
print(df_result)

df_result.Dollar.sum()

len_result = 23
result = []
for i in range(10000000):
  myRand = getRandSix()
  df_result = getHistoryBingo(myRand,df_six_history)
  if len(df_result) >= len_result:
    # len_result = len(df_result)
    print(myRand)
    print(df_result)
    print("You earn:", df_result.Dollar.sum())
    print("========================================")

"""# buy the last bingo number and find how many time can bingo

This shows that, this is not work!!!!
"""

result = []
id = []
for i in range(len(df_six_history)-1):
  sixNum,specialNum = getBingoNum(i, df_six_history)
  buy_sixNum, _ = getBingoNum(i+1, df_six_history)
  bingo = len(set(buy_sixNum) & set(sixNum))
  bingo = bingo + len(set(buy_sixNum) & set(specialNum))/2
  # print(bingo)
  if bingo >= 3.5:
    result.append(bingo)
    id.append(df_six_history.iloc[i]["id"])

myResult = {'ID':id,'Price':result}
df_myPrice = pd.DataFrame(myResult)
df_myPrice

