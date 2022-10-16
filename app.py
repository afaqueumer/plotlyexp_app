import streamlit as st
import plotly.express as px

st.title(" Plotly Express 🚀")



add_selectbox = st.sidebar.selectbox("Select the type of Charts 📈", ("Basic", "1D Distributions", "2D Distributions"))
with st.sidebar:
    if add_selectbox == "Basic":
        add_radio = st.radio("Type",("Scatter", "Line", "Area", "Bar"), label_visibility="hidden" )

    elif add_selectbox == "1D Distributions":
        add_radio = st.radio("Type",("Histogram", "Box", "Violin"), label_visibility="hidden" )

    elif add_selectbox == "2D Distributions":
        add_radio = st.radio("Type",("Heatmap", "Density"), label_visibility="hidden" )


if add_selectbox=="Basic":
    if add_radio == "Scatter":
        st.header("Scatter Plot")
        st.text('''A scatter plot uses dots to represent values for two different numeric variables.\nThe position of each dot on the horizontal and vertical axis indicates values for an individual data point.\nScatter Plots are typically employed to find the relationship between two variables, often quantities.''')

        col1, col2 = st.columns(2)
        col1.markdown("**When to use ✅**")
        col1.markdown('''
                        `To show correlation and clustering in big datasets.` \n
                        `If your dataset contains points that have a pair of values.`\n
                        `If the order of points in the dataset is not essential.` \n
                    ''')
        col2.markdown("**When not to ❌**")
        col2.markdown('''
                        `If you have a small dataset.` \n
                        `If the values in your dataset are not correlated.`\n
                    ''')

        with st.container():
            st.subheader("Building a Scatter Plot with Iris Dataset 👇")
            tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data", "🚀 Code"])

            df = px.data.iris()
            fig = px.scatter(df,  x=df.sepal_length, y=df.sepal_width, color=df.species)
            tab1.plotly_chart(fig, use_container_width=True)
            tab2.write(df)
            code = '''df = px.data.iris()\nfig = px.scatter(df, x = df.sepal_length, y = df.sepal_width, color = df.species)
                    '''
            tab3.code(code, language='python')

     

        


