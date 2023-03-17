import pandas as pd
import streamlit as st
import plotly.express as px

# Display title and text
st.title("AirBnb data and visualization")
st.markdown("Here we can see the dataframe created during AirBnb project.")

# Read the dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_amsterdam_listings_proj_2.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitiude",
        "Longitude",
        "Meters from chosen location",
        "Location",],    
    )

# We have a limited budget, therefore we would like to exclude
# listings with a price above 100 pounds per night
dataframe = dataframe[dataframe["Price"] <= 100]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe['Airbnb Listing ID'].astype(int)

# Round to values
dataframe["Price"] = "£ " + dataframe["Price"].round(2).astype(str)

# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
    )

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all Airbnb listings with a red dot and the location we've chosen with a blue dot")

# Create a plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"colors": "Locations"},
    )

fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
