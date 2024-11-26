import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv("df.csv")  # Path to your CSV file
    return df

df = load_data()

# Sidebar for user input
st.sidebar.title('Mobile Sales Analysis')

# Display the dataset
st.header("Mobile Sales Dataset")
st.write(df.head())

# 1. Which brand has the highest overall sales?
st.header("1. Which brand has the highest overall sales?")
brand_sales = df.groupby('Brand')['Selling Price'].sum().reset_index().sort_values('Selling Price', ascending=False)
top_brand = brand_sales.iloc[0]
st.write(f"The brand with the highest overall sales is {top_brand['Brand']} with total sales of {top_brand['Selling Price']:.2f}")

# Visualization for highest sales by brand
st.subheader("Sales by Brand")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Selling Price', y='Brand', data=brand_sales, palette='viridis', ax=ax)
st.pyplot(fig)

# 2. What memory and storage option are most popular among customers?
st.header("2. What memory and storage option are most popular among customers?")
memory_storage = df.groupby(['Memory', 'Storage']).size().reset_index(name='Count').sort_values('Count', ascending=False)
top_memory_storage = memory_storage.iloc[0]
st.write(f"The most popular memory and storage option is {top_memory_storage['Memory']} with {top_memory_storage['Storage']} storage.")

# Visualization for memory and storage popularity
st.subheader("Memory and Storage Popularity")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='Memory', hue='Storage', data=df, palette='muted', ax=ax)
st.pyplot(fig)

# 3. What is the average discount percentage across brands?
st.header("3. What is the average discount percentage across brands?")
avg_discount_per_brand = df.groupby('Brand')['discount percentage'].mean().reset_index()
overall_avg_discount = avg_discount_per_brand['discount percentage'].mean()

# Plot average discount percentage by brand
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Brand', y='discount percentage', data=avg_discount_per_brand, palette='coolwarm', ax=ax)
ax.axhline(overall_avg_discount, color='red', linestyle='--', label=f'Overall Avg: {overall_avg_discount:.2f}%')
ax.legend()
st.pyplot(fig)

st.write(f"Overall Average Discount Percentage: {overall_avg_discount:.2f}%")

# 4. What are the top three models in terms of revenue?
st.header("4. What are the top three models in terms of revenue?")
model_revenue = df.groupby('Models')['Selling Price'].sum().reset_index().sort_values('Selling Price', ascending=False).head(3)
st.write("Top 3 models by revenue:")
st.write(model_revenue)

# Visualization for top models by revenue
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='Selling Price', y='Models', data=model_revenue, palette='magma', ax=ax)
st.pyplot(fig)

# Footer
st.markdown("### Developed by Hemendra Suman")
st.markdown("### Data analysis and visualization done with Streamlit and Python!")