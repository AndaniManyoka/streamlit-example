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

st.write('Number of airports per country')
NameofCountry = airpots.groupby('Country')
CountofAirpotperCountry = NameofCountry.size().reset_index(name='Count of Airports')
min_airports = CountofAirpotperCountry['Count of Airports'].min()
max_airports = CountofAirpotperCountry['Count of Airports'].max()
min_country = CountofAirpotperCountry.loc[CountofAirpotperCountry['Count of Airports'] == min_airports, 'Country'].iloc[0]
max_country = CountofAirpotperCountry.loc[CountofAirpotperCountry['Count of Airports'] == max_airports, 'Country'].iloc[0]
st.write(f"Minimum number of airports: {min_airports}")
st.write(f"Maximum number of airports: {max_airports}")
st.bar_chart(CountofAirpotperCountry, x='Country')

##grouping the airpots looking at the altitude

st.write('Bar graph of the Altitude of all the airpots across the globe,Altitude(in feet)')
airports_filtered = airpots[airpots['Altitude'] > 0]
# Find the airport with the highest altitude
max_altitude_airport = airpots.loc[airpots["Altitude"].idxmax()]
st.line_chart(data=airports_filtered, x='Name', y='Altitude')
# Display the name of the airport with the highest altitude
st.write("The airport with the highest altitude is", max_altitude_airport["Name"], "with an altitude of", max_altitude_airport["Altitude"], "feet.")


##Checking the timezones with the most airports
st.write('Time Zones with their respective number of airports')
airpots_cleaned = airpots.dropna(subset=['Tz database time zone'])
TimeZone = airpots_cleaned.groupby('Tz database time zone')
CountofAirportsperTimeZone = TimeZone.size().reset_index(name='Count of Airports per TimeZone')
CountofAirportsperTimeZone = CountofAirportsperTimeZone.sort_values(by='Count of Airports per TimeZone', ascending=False)
most_airports_tz = CountofAirportsperTimeZone.iloc[0]['Tz database time zone']
st.write(f"The timezone with the highest number of airports is {most_airports_tz}")
st.bar_chart(CountofAirportsperTimeZone, x='Tz database time zone')



##Analyzing the routes dataframe
routes = pd.read_csv('routes1.csv',sep=",")
routes.columns = ['Airline','Airline ID','Source airpot','Source airport ID','Destination airpot','Destination airpot ID','Codeshare' ,'Stops','Equipment']

##checking mos visited airpot
st.write('The most visited airports with a count of visits greater than or equal to 100')
MostVisitedAirport = routes.groupby('Destination airpot')
MVAirport = MostVisitedAirport.size().reset_index(name='Count of visits per airport')
MVAirport_filtered = MVAirport[MVAirport['Count of visits per airport'] >= 100]
MVAirport_filtered = MVAirport_filtered.sort_values(by='Count of visits per airport', ascending=False)
st.table(MVAirport_filtered)


# Merge airlines with routes dataframe
merged_df = pd.merge(df, routes, on='Airline ID')
st.table(merged_df)



