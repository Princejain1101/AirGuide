from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
import streamlit as st
from agno.models.openai import OpenAIChat
from parameters import set_png_as_page_bg, airlines_list, set_bg_hack_url

# set_png_as_page_bg('airline_background.png')
# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
#     }
#    .sidebar .sidebar-content {
#         background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# with st.echo():
# st.markdown("[![Click me](airline_background2.jpeg)](https://streamlit.io)")
#
# # with st.echo():
# st.markdown(
#     '<img src="airline_background2.jpeg" height="333" style="border: 5px solid orange">',
#     unsafe_allow_html=True,
# )# Set up the Streamlit app
set_bg_hack_url()
st.title("AI Air Guide ✈️")
st.subheader("Enjoy smooth and well prepared travel!")

# Get OpenAI API key from user
openai_api_key = st.secrets["openai_api_key"]
#st.text_input("Enter OpenAI API Key to access GPT-4o", type="password")

# Get SerpAPI key from the user
serp_api_key = st.secrets["serp_api_key"]
#st.text_input("Enter Serp API Key for Search functionality", type="password")

if openai_api_key and serp_api_key:
    airlineguide = Agent(
        name="Airlineguide",
        role="Searches for airline general information",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        description=dedent(
            """\
        You are a world-class Airline guide. Given an airline and domestic/international and the information user is looking for,
        find the airline website and also the blogposts to find relevant travel details about the airline.
        Then in all these websites, search for requested information, analyze and summarize the results.
        Generate and return in 10 to 20 lines of text.
        """
        ),
        instructions=[
            "Given an airline and domestic/international user wants to travel for, find airline website and other related partner websites.",
            "On each of these websites, search for the information user is looking for and analyze the results.",
            "From these results, summarize the results across all websites and provide results in 10-20 lines.",
            "Remember, the quality of the results in important.",
            "Make sure to include links of the source."
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )

    baggage, transit, terminal = st.tabs(["Baggage", "Transit", "Terminal"])
    with baggage:
        airline = st.selectbox("Which airline do you wish to travel?", airlines_list, index=None)
        domestic = st.radio("Are you traveling domestic or international?", ["Domestic", "International"])
        if st.button("Get Baggage information"):
            with st.spinner("Getting Baggage information..."):
                response = airlineguide.run(f"with {airline} travelling {domestic} and getting baggage information for checked bad, carry-on bag with weight and count limit", stream=False)
                st.write(response.content)

