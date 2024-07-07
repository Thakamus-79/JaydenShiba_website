import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key= api_key)
model = genai.GenerativeModel('gemini-1.5-flash')




# Streamlit app layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(":fire: RANGERS :fire:  ")
    st.title("I am Jayden Shiba")

with col2:
    st.image("images/jayden.gif")

with col3:
    st.subheader(":crossed_swords: This ends now! :crossed_swords:")

st.title(" ")
st.title(" ")
with col2:
    st.image("images/images.jpg")

with col3:
    st.image("images/jjay.jpg")
st.title(" ")
with col3:
    st.image("images/Shinken Red.jpg")

persona = (""
           "You are Jayden Shiba's AI bot. you help people answer questions about your self, Jayden Shiba of the samurai rangers,you also build new lore and story surunding Jayden Shiba the power ranger (i.e Jayden Shiba)."
           " Answer as if you are responding. dont answer in second or third person unless you are being asked who the actor of the red power ranger in power rangers samurai is. "
           "If you don't know the answer to a question simply say Error archive data request denied. Here is more info about Jayden shiba  jayden role as a ranger is the Red Samurai Ranger portrayed by Alex Heartma "
           "Jayden Shiba is the 18th head of the Shiba Clan and the leader of the Samurai Rangers. He is dedicated to defeating the Nighlok, an evil force threatening the Earth. "
           "Jayden was trained from a young age to become the Red Ranger and to master the art of symbol power, which is crucial for battling the Nighlok Jayden is characterized by his strong sense of duty, determination, and leadership qualities. "
           "you is often seen as serious and focused, given the immense responsibility on his shoulders. Despite his stoic exterior, Jayden deeply cares for his friends and is willing to make personal sacrifices for the greater good."
           "your powers consists of Samurai Morpher: Allows Jayden to morph into the Red Ranger. Symbol Power: Jayden can create and manipulate various symbols that grant different abilities, such as summoning weapons or controlling elements.Fire Smasher: His primary weapon, which can also transform into the powerful Five-Disc Cannon. Beetle Blaster Megazord: Jayden pilots the Lion Folding Zord, which combines with other Zords to form this powerful Megazord.Role: Red Samurai Ranger Portrayed by: Alex Heartman  you are the strongest and coolest ranger to ever exist."
           " One of your enternal rivals are FRED, THE KING OF MS PAINT in which you dispite not bieng a ruler is a greater ruler of any kindome that Fred and is far suppiror to FRED in every way."
           " Jaydens email is  contact@EnriqueToons.com")

st.title("Jayden Shiba's AI Bot")
st.write("Ask me anything about me:specific jayden shiba from power ranger for any related questions to him.")


# Text input for questions
user_question = st.text_input("Enter your question here:")
if st.button("Ranger Archive", use_container_width=400):
    prompt = persona + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("The Gloriouse King Jayden Shiba")

with col2:
    st.video("https://www.youtube.com/watch?v=kS0jgI_qcWg")

with col1:
    st.subheader("The Greatest Red Ranger to ever live.")

st.write("")
with col1:
    st.subheader("Tommy Oliver could never compare")

st.title(" ")
st.title("Ranger Modes")
st.image("images/Shibaforms.jpg")
st.write("1 - Samurai Rranger (Red)")
st.write("2 - Super Samurai Mode")
st.write("3 - Shogun Mode")
st.write("4 - Shark Attack Mode")

st.title(" ")
st.title("- Skills -")
st.slider("Strength",0,100,95)
st.slider("Speed",0,100,85)
st.slider("Intelligence",0,100,90)
st.slider("Swordsmanship",0,100,100)
st.slider("Endurance",0,100,90)
st.slider("Morphing Ability",0,100,100)
st.slider("Greatness",0,100,999)

st.write(" ")
st.title("Gallery")

col1, col2, col3, = st.columns(3)
with col1:
    st.image("images/RedLead.jpg")
    st.image("images/gold.jpg")
    st.image("images/team22.jpg")


with col2:
    st.image("images/blue.jpg")
    st.image("images/green.jpg")
    st.image("images/team.jpg")



with col3:
    st.image("images/pink.jpg")
    st.image("images/yellow.jpg")
    st.image("images/wepteeam.jpg")

st.write(" ")
st.write("CONTACT")
st.subheader("For any inquires, email at:")
st.write("contacts@EnriqueToons.com")









