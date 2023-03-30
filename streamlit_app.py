import streamlit 
import pandas

streamlit.title('My parents new healthy Dinner')

streamlit.header('Breakfeast Menu')

streamlit.text('🥣 Omega 3 and blueberry Oatmeal ')

streamlit.text('🥗 Kale, spinach and Rocket smoothies')

streamlit.text('🐔 HArd-boiled Free-Range Egg')

streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
