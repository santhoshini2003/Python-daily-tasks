import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv(r"C:\Users\ELCOT\Downloads\DataNetflixRevenue2020_V2.csv")
df2=pd.read_csv(r"C:\Users\ELCOT\Downloads\DataNetflixSubscriber2020_V2.csv")
df3=pd.read_csv(r"C:\Users\ELCOT\Downloads\NetflixSubscribersbyCountryfrom2018toQ2_2020.csv")

def dataset():
    datasetlist={1:"Revenue Data",
                 2:"Subscribers Data",
                 3:"Subscribers of country"}
    for i in datasetlist:
        print(i,".",datasetlist[i])
    option = int(input("Enter the option (1/2/3):"))
    if option==1:
        print(df1)
        print("\nNetflixRevenueData2020_V2")
        df1.columns = df1.columns.str.strip()
        print(df1.head())
        print(df1.columns)
        print(df1.info())
        print(df1.isnull().sum())
        plt.bar(df1['Years'],df1['Revenue'],color='red')
        plt.title("Netflix Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()
        print("-----------------------------------------------------------------------------")
    elif option == 2:
        print(df2)
        print("\nNetflixSubscriberData2020_V2")
        df2.columns = df2.columns.str.strip()
        print(df2.head())
        print(df2.columns)
        print(df2.info())
        print(df2.isnull().sum())
        plt.bar(df2['Years'],df2['Subscribers'],color='black')
        plt.title("Netflix Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()
        print("-----------------------------------------------------------------------------")
    elif option == 3:
        print(df3)
        print("\nNetflixSubscribersbyCountryfrom2018toQ2_2020")
        df3.columns = df3.columns.str.strip()
        print(df3.head())
        print(df3.columns)
        print(df3.info())
        print(df3.isnull().sum())
        plt.scatter(df3['Area'],df3['Q1 - 2018'],color='orange')
        plt.title("Netflix Subscribers by Country")
        plt.xlabel('Area')
        plt.ylabel('Q1 - 2018')
        plt.show()
        print("-----------------------------------------------------------------------------")
    else:
        print("invalided")
dataset()        





    
        










