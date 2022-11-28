import pandas as pd  # importing 
from matplotlib import pyplot as plt # importing 


dat=pd.read_csv('Cars93.csv') # reading csv file to a local data frame 
#########################scatter plot to determine wether the car with heigher horse power have less mileage #######

#MPG.city
# Horsepower  are the two colomn  required
mc=dat.loc[:,'MPG.city'].values # storing the values in varible
hs=dat.loc[:,'Horsepower'].values# storing the values in varible

#hs= x axis  , mc= yaxis
plt.title('horse power and mileage scatter') # title of our plot
plt.scatter(hs,mc,marker='*',color="blue") # ploting the scatter plot with two varibles 

plt.xlabel("horse power")# x axis label
plt.ylabel("mileage in city ")# Yaxis label
plt.show() # showing the plot



###########################################line chart engine size vs horse power

egsize=dat.loc[:,'EngineSize'].values# storing the colomn values 
hpower=dat.loc[:,'Horsepower'].values# storing the colomn values 
ser=pd.DataFrame(egsize,hpower)# creating a new data frame with thhese varibles 
ser.reset_index(inplace=True)# adding a new index for dataframe
ser.sort_values('index',inplace=True)# sorting them to get a linear line chart other wise line chart will not look like aline chart you can try removing this line of code to see
hp=ser.iloc[:,0].values # now reading the sorted serialwise horse power 
eg=ser.iloc[:,1].values# engine size

plt.title('engine size vs horse power line chart')# title
plt.plot(hp,eg)# ploting line chart
plt.xlabel("horse power")# labels
plt.ylabel("engine size ")
plt.show()# showing the plot

###############################histogram to mark down heigest frequency
plt.title('histogram of mileage in city')
mc=dat.loc[:,'MPG.city'].values# reading colomn values and storing in varible
plt.hist(mc)# histogram requires only one parameter it shows repetance of value 
plt.show()# shoing the plot 


############################box plot

plt.title("box plot of types of cars and their price range ")
temp=dat.groupby(['Type'])['Price'].apply(list)# making a simple view of types of car and their values and converting them into python list
print(temp) # just for confirmation of cars available compair them with graph
plt.xlabel("types of cars ")
plt.ylabel("price of cars ")
plt.boxplot(temp)# ploting the graph plot
plt.show() # showing the plot 

'''to understand more about box plot refer this video ; https://www.youtube.com/watch?v=tpToLyZibKM 
github-contacts;  https://github.com/sayeed-cyber 
'''