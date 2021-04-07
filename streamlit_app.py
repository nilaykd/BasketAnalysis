import streamlit as st
import pandas as pd
import os
from apriori import runApriori, dataFromFile, to_str_results

st.markdown("# Market Basket Analysis")

# st.sidebar.markdown(
#     """The code attempts to implement the following paper:

# > *Agrawal, Rakesh, and Ramakrishnan Srikant. "Fast algorithms for mining association rules." Proc. 20th int. conf. very large data bases, VLDB. Vol. 1215. 1994.*
# """
# )

uploaded_file = st.file_uploader("Choose a file", type=['csv'])
if uploaded_file is not None:

    # if default_csv == 'INTEGRATED-DATASET.csv':
    #     st.markdown('''The dataset is a copy of the “Online directory of certified businesses with a detailed profile” file from the 
    #     Small Business Services (SBS) dataset in the NYC Open Data Sets http://nycopendata.socrata.com/''')
    # elif default_csv == 'tesco.csv':
    #     st.markdown('The dataset is a toy dataset contain frequently purchased grocery items')

    st.markdown('Here are some sample rows from the dataset')
    csv_file = pd.read_csv(uploaded_file, encoding = "UTF-8", header=0, sep=",")
    st.write(csv_file.head())

    st.markdown('---')
    st.markdown("## Inputs")

    st.markdown('''
                **Support** shows transactions with items purchased together in a single transaction.
                
                **Confidence** shows transactions where the items are purchased one after the other.''')

    #st.markdown('Support and Confidence for Itemsets A and B can be represented by formulas')

    support_helper = ''' > Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions') '''
    confidence_helper = ''' > Confidence(A->B) = Support(AUB)/Support(A)') '''
    st.markdown('---')

    support = st.slider("Enter the Minimum Support Value", min_value=0.01,
                        max_value=1.0, value=0.6,
                        help=support_helper)

    confidence = st.slider("Enter the Minimum Confidence Value", min_value=0.01,
                        max_value=1.0, value=0.2, help=confidence_helper)

    inFile = dataFromFile(csv_file)

    items, rules = runApriori(inFile, support, confidence)

    i, r = to_str_results(items, rules)

    st.markdown("## Results")

    st.markdown("### Frequent Itemsets")
    st.write(i)

    st.markdown("### Frequent Rules")
    st.write(r)
