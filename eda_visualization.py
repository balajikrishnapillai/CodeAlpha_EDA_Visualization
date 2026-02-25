import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("books_data.csv")
print(df.head())
print(df.info())
print(df.describe(include="all"))
df["Price"] = df["Price"].str.replace("Â£", "", regex=False).astype(float)
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)
print(df.head())
print("Average Price:", df["Price"].mean())
print(df["Rating"].value_counts())
plt.figure()
plt.hist(df["Price"])
plt.title("Price Distribution of Books")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()
plt.figure()
sns.countplot(x="Rating", data=df)
plt.title("Book Ratings Count")
plt.show()
plt.figure()
sns.boxplot(x="Rating", y="Price", data=df)
plt.title("Price vs Rating")
plt.show()

print("EDA and Visualization Completed Successfully")