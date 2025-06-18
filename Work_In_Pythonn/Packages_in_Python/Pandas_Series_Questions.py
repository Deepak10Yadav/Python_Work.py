import pandas as pd
import numpy as np
# sr = pd.Series([1,2,3,4,5,6])
# print(sr)
# # df = pd.DataFrame({
# #     "A" : [1,2,3,4],
# #     "B" : [11,12,13,14]
# # });
# # print(df)
# ls = list(sr)
# print(ls)
# print(type(ls))

# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

# ds1 = pd.Series([2, 4, 6, 8, 10])
# ds2 = pd.Series([1, 3, 5, 7, 9])

# print(f"Addition := {ds1+ds2}")
# print(f"Subtraction := {ds1-ds2}")
# print(f"Multiplication := {ds1*ds2}")
# print(f"Division := {ds1/ds2}")


# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

# my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# ds = pd.Series(my_dict)
# print(ds)

# arr1 = np.array([1,2,3,4,5])
# ds = pd.Series(arr1)
# print(type(arr1))
# print(type(ds))

# s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
# change = pd.to_numeric(s1,errors='coerce')
# print(change)

# d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
# df = pd.DataFrame(d)
# # print(df)
# # s1 = df.iloc[:,0]
# # or
# s1 = df['col1']
# print(s1)

# s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
# s2 = np.array(s1)
# print(s2)
# print(type(s2))

# s = pd.Series([
#     ['Red', 'Green', 'White'],
#     ['Red', 'Black'],
#     ['Yellow']])

# s1 = s.apply(pd.Series).stack().reset_index(drop = True)
# print(s1)

# s = pd.Series([
#     ['Red', 'Green', 'White'],
#     ['Red', 'Black'],
#     ['Yellow']])
# s1 = s.apply(pd.Series).stack().reset_index(drop = True)
# print(s1)


# s = pd.Series(['100', '200', 'python', '300.12', '400'])
# s1 = pd.Series(s).sort_values()
# print(s)


# s = pd.Series(['100', '200', 'python', '300.12', '400'])
# new = pd.concat([s,pd.Series([500,'php'])],ignore_index=True)
# print(new)


# s = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
# # n = 6
# # s1 = s[s<n]
# # print(s1)
# # n =  5
# s1 = s[s<5]
# print(s1)


# s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
# s1 = s.reindex(index=['B','C','D','A','E'])
# print(s1)


# s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
# print(s)
# print(s.mean())
# print(s.std()) # STD = Standard Deviation


# sr1 = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series([2, 4, 6, 8, 10])
# result = sr1[~sr1.isin(sr2)]
# print(result)


# sr1 = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series([2, 4, 6, 8, 10])
# sr11 = pd.Series(np.union1d(sr1,sr2))
# sr22 = pd.Series(np.intersect1d(sr1, sr2))
# result = sr11[~sr11.isin(sr22)]
# print(sr11)
# print(sr22)
# print(result)


num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))
result = np.percentile(num_series, q =[0,25,50,75,100])
print(result)

num  = np.random.RandomState(100)