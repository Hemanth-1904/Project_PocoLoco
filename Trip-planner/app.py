import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
from main import TripCrew
import sys
from AgentProcess_Streamlit import StreamToExpander
import textwrap

# Current date and next year/month/day calculation
today = datetime.datetime.now().date()
next_daterange = today + relativedelta(months=1, years=1)

def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[((n//10 % 10 != 1)*(n % 10 < 4)*n % 10)::4])

def to_markdown(text):
    text = textwrap.dedent(text)
    text = text.replace("•", " ")
    text = text.replace("*", " ")
    return text

st.set_page_config(page_title="Trip Planner Agent", page_icon="🏖️", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("✈️ 🎫 Trip Planner Agent 🏝️ 🗺️")
st.write("Let AI agents plan your next vacation! 🏖️")

with st.sidebar:
    st.header("Enter your trip details 👇")
    with st.form("my_form"):
        origin = st.text_input("📍 From where will you be traveling from?", placeholder="Kolkata, West Bengal, India")
        destination = st.text_input("🏝️ Which location you are interested in visiting?", placeholder="Bali, Indonesia")
        date_range = st.date_input(
            "📅 Date range you are interested in traveling?",
            min_value=today,
            value=(today, today + datetime.timedelta(days=6)),
            format="MM/DD/YYYY",
        )
        interests = st.text_area("🍹🛍️ High level interests and hobbies or extra details about your trip?",
                                 placeholder="2 adults who love swimming, dancing, hiking, and eating")
        person = st.number_input("👩‍👩‍👧‍👦 No of person traveling?", min_value=1, step=1, format="%d")
        
        submitted = st.form_submit_button("💫 Submit")
    
    st.divider()
    
    st.sidebar.markdown(
        """
        🚀 Created by : [**Team PocoLoco**]
        """,
        unsafe_allow_html=True
    )
    

if submitted:
    if origin and destination and date_range and interests and person > 0:
        start_date, end_date = date_range
        formatted_start_date = f"{ordinal(start_date.day)} {start_date.strftime('%B, %Y')}"
        formatted_end_date = f"{ordinal(end_date.day)} {end_date.strftime('%B, %Y')}"
        og_date_range = f"{formatted_start_date} - {formatted_end_date}"
        
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            with st.container(height=500, border=False):
                sys.stdout = StreamToExpander(st)
                trip_crew = TripCrew(origin, destination, og_date_range, interests, person)
                result = trip_crew.run()
                
            status.update(label="✅ Trip Plan Ready!", state="complete", expanded=False)
        
        st.subheader("Here is your Trip Plan")
        st.markdown(result)
        
        output_str = str(result)
        output_bytes = output_str.encode('utf-8')
        st.download_button(
            label="Download the Trip Plan",
            data=output_bytes,
            file_name="Trip Plan.txt",
            mime="text/plain",
        )
    else:
        st.warning("Please fill out all fields before submitting.")
