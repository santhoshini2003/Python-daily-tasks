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
        revenue()
    elif option == 2:
        subscribers()
    elif option == 3:
        subscribersbycountry()
    else:
        print("invalided")
        dataset()
def revenue():
    print("Netflix Revenue Data")
    data={1:"df1",
          2:"United States and Canada",
          3:"Europe,  Middle East and Africa",
          4:"Latin America",
          5:"Asia-Pacific"}
    for i in data:
        print(i,'.',data[i])
    foption=int(input("Enter the option(1,2,3,4,5):"))
    if foption==1:
        print("-----------------------------------------------------")
        print("\nNetflixRevenueData2020_V2")
        df1.columns = df1.columns.str.strip()
        print(df1)
        print(df1.head())
        print(df1.columns)
        print(df1.info())
        print(df1.isnull().sum())
        plt.bar(df1['Years'],df1['Revenue'],color='red')
        plt.title("Netflix Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()

    elif foption==2:
        print("------------------------------------------------------")
        print("\nNetflixRevenueData2020_V2")
        usa_data1 = df1[df1['Area'].str.contains('United States', case=False)]
        print(usa_data1)
        print(usa_data1.head())
        print(usa_data1.columns)
        print(usa_data1.info())
        print(usa_data1.isnull().sum())
        plt.bar(usa_data1['Years'], usa_data1['Revenue'], color='red')
        plt.title("United States and Canada Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()
    elif foption==3:
        print("-------------------------------------------------------")
        print("\nNetflixRevenueData2020_V2")
        usa_data2 = df1[df1['Area'].str.contains('Europe', case=False)]
        print(usa_data2)
        print(usa_data2.head())
        print(usa_data2.columns)
        print(usa_data2.info())
        print(usa_data2.isnull().sum())
        plt.bar(usa_data2['Years'],usa_data2['Revenue'],color='red')
        plt.title("Europe Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()
    elif foption==4:
        print("--------------------------------------------------------")
        print("\nNetflixRevenueData2020_V2")
        usa_data3 = df1[df1['Area'].str.contains('Latin America', case=False)]
        print(usa_data3.head())
        print(usa_data3.columns)
        print(usa_data3.info())
        print(usa_data3.isnull().sum())
        plt.bar(usa_data3['Years'],usa_data3['Revenue'],color='red')
        plt.title("Latin America Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()
        
    elif foption==5:
        print("----------------------------------------------------------")
        print("\nNetflixRevenueData2020_V2")
        usa_data4 = df1[df1['Area'].str.contains('Asia-Pacific', case=False)]
        print(usa_data4.head())
        print(usa_data4.columns)
        print(usa_data4.info())
        print(usa_data4.isnull().sum())
        plt.bar(usa_data4['Years'],usa_data4['Revenue'],color='red')
        plt.title("Asia-Pacific Revenue Growth")
        plt.xlabel('Years')
        plt.ylabel('Revenue')
        plt.show()
    else:
        print("data invalided")

def subscribers():
    print("Netflix Subscribers Data")
    data={1:"df2",
          2:"United States and Canada",
          3:"Europe,  Middle East and Africa",
          4:"Latin America",
          5:"Asia-Pacific"}
    for i in data:
        print(i,'.',data[i])
    foption=int(input("Enter the option(1,2,3,4,5):"))
    if foption==1:
        print("-----------------------------------------------------")
        print("\nNetflixSubscribersData2020_V2")
        df2.columns = df2.columns.str.strip()
        print(df2)
        print(df2.head())
        print(df2.columns)
        print(df2.info())
        print(df2.isnull().sum())
        plt.bar(df2['Years'],df2['Subscribers'],color='black')
        plt.title("Netflix Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()

    elif foption==2:
        print("------------------------------------------------------")
        print("\nNetflixSubscribersData2020_V2")
        usa_data1 = df2[df2['Area'].str.contains('United States', case=False)]
        print(usa_data1)
        print(usa_data1.head())
        print(usa_data1.columns)
        print(usa_data1.info())
        print(usa_data1.isnull().sum())
        plt.bar(usa_data1['Years'], usa_data1['Subscribers'], color='black')
        plt.title("United States and Canada Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()

    elif foption==3:
        print("-------------------------------------------------------")
        print("\nNetflixSubscribersData2020_V2")
        usa_data2 = df2[df2['Area'].str.contains('Europe', case=False)]
        print(usa_data2)
        print(usa_data2.head())
        print(usa_data2.columns)
        print(usa_data2.info())
        print(usa_data2.isnull().sum())
        plt.bar(usa_data2['Years'],usa_data2['Subscribers'],color='black')
        plt.title("Europe Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()
    elif foption==4:
        print("--------------------------------------------------------")
        print("\nNetflixSubscribersData2020_V2")
        usa_data3 = df2[df2['Area'].str.contains('Latin America', case=False)]
        print(usa_data3.head())
        print(usa_data3.columns)
        print(usa_data3.info())
        print(usa_data3.isnull().sum())
        plt.bar(usa_data3['Years'],usa_data3['Subscribers'],color='black')
        plt.title("Latin America Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()
        
    elif foption==5:
        print("----------------------------------------------------------")
        print("\nNetflixSubscribersData2020_V2")
        usa_data4 = df2[df2['Area'].str.contains('Asia-Pacific', case=False)]
        print(usa_data4.head())
        print(usa_data4.columns)
        print(usa_data4.info())
        print(usa_data4.isnull().sum())
        plt.bar(usa_data4['Years'],usa_data4['Subscribers'],color='black')
        plt.title("Asia-Pacific Subscribers Growth")
        plt.xlabel('Years')
        plt.ylabel('Subscribers')
        plt.show()
    else:
        print("data invalided")

def subscribersbycountry():
        print("Netflix SubscribersbyCountry Data")
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
while True:
    dataset()  






    
        










