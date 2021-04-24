# Product Sentiment Classifier
## COMP 3610 Project
This project is part of the COMP 3610 Big Data Analytics course at the University of the West Indies, St. Augustine Campus. It involves the training of a sentiment classifier on product reviews, and the deployment of a user interface. The UI will allow users to interact with the classifier by uploading a CSV of product reviews and view the sentiments and a wordcloud for the reviews of the top 10 and worse 10 products. This user interface uses Streamlit and this repository serves as the source code for the Streamlit application, among other things. The models were trained in a Google Colab notebook, which can be accessed [here](https://colab.research.google.com/drive/1iFk46h7z8-3COwoVezEQnaxQp1qXIvbX?usp=sharing).
You can run the the app yourself if you have Apache Spark installed, as well as the following Python packages:
- streamlit
- streamlit-wordclouds
- pyspark
- findspark

You do this by running the app.py script using Streamlit by running the following command from the repository root folder:
`streamlit run app.py`
You must also have a Spark instance running before doing this.
