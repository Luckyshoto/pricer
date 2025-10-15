import streamlit as st

st.title("Pricer App")

# Gets the product
product = st.text_input("Enter the product:")
quantity = st.number_input("Enter the quantity of product:", min_value=0.0)
price = st.number_input("Enter the price per unit:", min_value=0.0)
discount = st.number_input("Enter the discount (%):", min_value=0.0)
tax = st.number_input("Enter the tax (%):", min_value=0.0)

# Button to calculate
if st.button("Calculate Total"):
    total = price * quantity
    discounted_amount = total * (discount / 100)
    total_after_discount = total - discounted_amount
    final_price = total_after_discount + tax

    st.write("Total cost: ", total)
    st.write("Discounted amount: ", discounted_amount)
    st.write("Total after the discount: ", total_after_discount)
    st.write("Final price with tax: ",  final_price)