import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# create containers for each section of the web app
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()
interactive = st.beta_container()

with header:
	st.title('Welcome to my CS 021 Final:') 
	st.title('Bike Lanes!')
	st.header("In this project, I will look into the city of Baltimore's BikeBaltimore project.")
	st.text("BikeBaltimore is the Department of Transportation's bike program including anything")
	st.text("bike related, including 'incorporating cycling in many transportation projects,")
	st.text("installing bike racks and coordinating cycling events.'")

with dataset:
	st.header('Bike Lanes Data')
	st.text('This dataset is from the City of Baltimore and was obtained via data.world')
	st.text("Below is a table of the first 10 entries. This dataset includes mainly string")
	st.text("data, with the fields 'subtype', 'name', 'block', 'type', 'project' and 'route.'")
	st.text("The data contains three numeric data types, with 'numLanes' and 'dateInstalled'")
	st.text("as integers and 'length' as float.")
	st.text("Personally, I wish 'dateInstalled' was a string for easier analysis, as Plotly")
	st.text("often wanted to summarize this category via summation or other mathematical")
	st.text("operators that are not appropriate for years.")


	Bike_Lanes = pd.read_csv('DATA/Bike_Lanes.csv')
	st.write(Bike_Lanes.head(10))

	st.header('Definitions')
	st.text('As we are not all Department of Transportation specialists, I believe it')
	st.text('is vital to add a definitions section as to what the types of infrastructure')
	st.text('mean in a practical sense.')
	st.markdown("* **Bike Lane: ** an area for bike travel only, 5' wide lane with a bike symbol indicating that only bikes should use that lane")
	st.markdown("* **Sharrow: ** a roadway which is shared by bikes and automobiles, cars should treat bikes as vehicles in the lane and pass only when it is safe to do so")
	st.markdown("* **Signed Route: ** a roadway with no pavement markings, used on low-traffic volume streets where cyclists can 'take the lane'")
	st.markdown("* **Floating Bike Lane: ** used along off-peak temporary parking, adjust to presence of parked cars")
	st.markdown("* **Share The Road: ** when space does not exist for bike lanes, 'SHARE THE ROAD' signs are installed to remind motorists of presence of cyclists")
	st.markdown("* **Shared Bus & Bike Lanes: ** (only on Pratt St), these lanes are only available to buses, bicycles and right turning vehicles")


with interactive:
	st.title("Now, let's take a closer look at the data...")
	st.header('Table')

	st.subheader('Table of Infrastructure, including Name and Length')

	fig = go.Figure(data=go.Table(
		header=dict(values=(Bike_Lanes[['name', 'type', 'length']].columns), 
		fill_color='#FD8E72',
		align='center'),
	cells=dict(values=[Bike_Lanes.name, Bike_Lanes.type, Bike_Lanes.length], 
		fill_color = '#E5ECF6',
		align = 'left')))

	fig.update_layout(margin = dict(l=5,r=5, b=10, t=10))

	st.write(fig)

	st.text("Above is a table of each infrastructure addition including its length as well as its named")
	st.text("attribute, typially its location, such as 'Bank St' or 'E Clement St.")
	st.text("length is of the data type 'float', with its average value being nearly 270.") 
	st.text("The length attribute has a range of 3,749.323 as the minimum length is 0") 
	st.text("and the maximum is 3,749.323.")

	st.header('Graphs')

	st.subheader('Bar Chart of Type of Infrastructure Distribution')
	type_distribution = pd.DataFrame(Bike_Lanes['type'].value_counts())
	st.bar_chart(type_distribution)
	st.text('Above is the distribution of types of infrastructure, including bike lanes, sharrows,')
	st.text('and signed routes. As we can see, bike lanes are the most common solution the')
	st.text('BikeBaltimore program has implemented, followed by sharrows and signed routes.')

	st.subheader('Line Chart of Length')

	chart_data = pd.DataFrame(Bike_Lanes, columns = ['length'])
	st.line_chart(chart_data)
	st.text("Seen above is a line chart of the length of the different types of infrastructure")
	st.text("implemented through the BikeBaltimore program. As previously stated, the maximum")
	st.text("length is 3,749.323 and is a Signed Route.")

	st.subheader("Graph of Project by Length, including Type")

	df = pd.DataFrame(Bike_Lanes)
	fig = px.histogram(df, x="length", y="project", color="type")
	st.write(fig)

	st.text("Above is a graph of the project type summarized by length, inlcuding the type of")
	st.text("infrastructure as the color coding of the graph. Operation Orange Cone and Collegetown")
	st.text("are the largest projects as they cover the greatest summed lengths.")
	st.text("Operation Orange Cone is majority bie lanes, whereas Collegetown appears to be")
	st.text("evenly distributed amongst signed routes, bike lanes and sharrows.")

	st.subheader('Bar Chart of Project Distribution')

	proj_distribution = pd.DataFrame(Bike_Lanes['project'].value_counts())
	st.bar_chart(proj_distribution)
	st.text("The bar chart above shows the distribution of the city's projects.")
	st.text("These projects were headed by the city's Department of Transportation as a part")
	st.text("of their BikeBaltimore initiative. There are 12 distinct projects,")
	st.text("with Operation Orange Cone and Collegetown being the biggest.")


	st.subheader('Scatter Plot of Type by Project')
	df = pd.DataFrame(Bike_Lanes)
	fig = px.scatter(df, x="project", y="type")
	st.write(fig)

	st.text("The scatter plot above shows the types of infrastructure created") 
	st.text("through each city of Baltimore project. Mostly every project includes")
	st.text("more than one type of infrastructure except for the Guilford Ave Bike")
	st.text("Blvd, which only included a Bike Boulevard.")

	st.subheader('Sunburst Chart of Type by Project')

	fig = px.sunburst(df, path=['project', 'type'], values='length',
                  color='project', hover_data=['project'])
	st.write(fig)

	st.text("Sunburst plots visualize hierarchical data spanning outwards. This sunburst")
	st.text("shows the project in the middle, followed by the type of infrastructure.")
	st.text("It is color coded by project and the values are determined by the length attribute.")
	st.text("Click on one of the project types to see further summary!")

	

	
	
	
