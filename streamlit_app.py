import pandas as pd
import streamlit as st

st.title("Data Analysis with Python")
st.write("This dashboard will showcase information about the OpenFlights Organisation: depicting the busiest airpots,time zones, distribution of airpots globaly,most visited airpots , and more interesting facts")

st.write("Interesting fact about the Airlines dataframe")

# visualizing the dataframe
df = pd.read_csv('airlines1.csv', sep=",")
df.columns = ['Airline ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country', 'Active']

df2 = df[df['Active'] == 'Y'].groupby('Country')['Name'].count().reset_index()
st.write('Number of active airlines per country')
st.bar_chart(df2.set_index('Country'))


##looking at the airpots data
airpots = pd.read_csv('airports1.csv', sep=",", encoding='utf-8')
airpots.columns = ['Airport ID','Name','City','Country','IATA','ICAO','Latitude','Longitude','Altitude','Timezone','DST','Tz database time zone',
'Type','Source']
airpotsDist = airpots[['Latitude','Longitude']].rename(columns={'Latitude': 'latitude','Longitude':'longitude'})
st.write('Distribution of the airports across the globe')
st.map(data=airpotsDist)
###Showing the number of airpots per country
st.write('Number of airpots per country')
NameofCountry =airpots.groupby('Country')
CountofAirpotperCountry = NameofCountry.size().reset_index(name='Count of Airports')
st.bar_chart(CountofAirpotperCountry,x='Country')

#st.table(CountofAirpotperCountry)
##grouping the airpots looking at the altitude

st.write('Bar graph of the Altitude of all the airpots across the globe,Altitude(in feet)')
st.line_chart(data=airpots, x='Name', y='Altitude')

##Checking the timezones with the most airpots
st.write('Time Zones with their respective number of airpots')
TimeZone=airpots.groupby('Tz database time zone')
CountofAirpotsperTimeZone=TimeZone.size().reset_index(name='Count of Airpots per TimeZone')
st.bar_chart(CountofAirpotsperTimeZone,x='Tz database time zone')

##Analyzing the routes dataframe
routes = pd.read_csv('routes1.csv',sep=",")
routes.columns = ['Airline','Airline ID','Source airpot','Source airport ID','Destination airpot','Destination airpot ID','Codeshare' ,'Stops','Equipment']

##checking mos visited airpot
st.write('The most visited airports with a count of visits greater than or equal to 100')
MostVisitedAirport = routes.groupby('Destination airpot')
MVAirport = MostVisitedAirport.size().reset_index(name='Count of visits per airport')
MVAirport_filtered = MVAirport[MVAirport['Count of visits per airport'] >= 100]
st.table(MVAirport_filtered)



##Routes joined with airpots
# Merge the two datasets
merged_data = pd.merge(routes, airpots, left_on='Source airport ID', right_on='Airport ID', how='left')

merged_data = pd.merge(merged_data, airpots, left_on='Destination airport ID', right_on='Airport ID', how='left', suffixes=('_source', '_destination'))

# Display the merged data in Streamlit
st.write(merged_data)


