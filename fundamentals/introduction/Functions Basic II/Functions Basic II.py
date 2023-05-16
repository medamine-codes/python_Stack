# #Countdown
# # def Countdown(x):
# #     arr=[]
# #     for i in range(x,0,-1):
# #         arr.append(i)
# #     return arr 
# # print(Countdown(5))

# # # Print and Return
# # def pand(x):
# #     print(x[0])
# #     return x[1]
# # a=pand([1,2])
# # print(a)

# # #First Plus Length
# # def FplusL(a):
# #     return a[0]+len(a)
# # b=FplusL([1,2,3,4,5])
# # print(b)

# #Values Greater than Second
# def VgreatS(x):
#     temp=[]
#     for i in range (0,len(x)-1,2):
#         if x[i]>x[i+1]:
#             temp.append(x[i])
#         elif x[i]<x[i+1]:
#             temp.append(x[i+1])
#         elif len(x)<2 :
#             return False
#     return temp
# temp=VgreatS([5,7,4,2,1,9])    
# print(temp)

# This Length, That Value 
def LV(size,value):
    arr=[]
    for i in range (0,size):
        arr.append(value)
    return arr
arr=LV(4,7)
print(arr)

