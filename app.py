import streamlit as st

#Welcome
st.title("Welcome to Portfolio Flash!")
st.heading("Here, you can build custom portfolios in a flash.")
st.write(" ")
st.markdown("*Please format all information the way you would on your actual resume, and leave a space behind each punctuation.")
st.write(" ")

#Contact info
st.markdown("This section includes all of your necessary contact information")
firstName = st.text_input("What is your first name?")
lastName = st.text_input("What is your last name?")
email = st.text_input("What is your email?")
city = st.text_input("Which city do you live in?")
state = st.text_input("Which state do you live in?")

#Career summary
st.heading("Career Summary")
st.markdown("This section includes a short, 2-4 sentence career summary.")
relevantWorkExperience = st.text_input("What are 1-2 examples of your relevant work experience?")
skillSummary = st.text_input("What are some of your relevant skills?")
profAccompSummary = st.text_input("What are some of your professional accomplishments?")

#Mission statement
st.heading("Career Summary")
st.markdown("This section includes a mission statement of a few sentences.")
whatDoYouDo = st.text_input("What do you do?")
professionImportance = st.text_input("Why is your profession important?")
thriveSkills = st.text_input("Which skills help you thrive in your work?")
differenceFromOthers = st.text_input("What makes you different from other individuals in similar industries?")

#Brief biography
st.heading("Brief Biography")
st.markdown("This section is a biography that tells others about yourself, showcasing more of your own personality to connect on a more personal level with the employers.")
st.markdown("Be sure to consider your audience and the goal, to personalize it for each specific employer.")
st.markdown("Also include storytelling elements of how you overcame challenges, linked examples of your work, and possibly humor to give an impression of your humorous side.")
biography = st.text_input("What is your biography?")

#Resume
st.heading("Resume")
st.markdown("This section is a resume that provides easy access to your work experience and skills.")
objective = st.text_input("What are your career goals and objectives?")
workExperience = st.text_input("What are your relevant work experiences from the past 10 years? What are your daily responsibilities and tasks of each position? (Bulleted list)")
skills = st.text_input("What are your skills related to your position?")
education = st.text_input("What education have you completed? Include the institution name, month and year of graduation, and type of degree received.")

#Marketable skills
st.heading("Marketable Skills")
st.markdown("This section is a list of specific marketable skills and abilities that make you qualified.")
hardSkills = st.text_input("What are your hard skills?")
softSkills = st.text_input("What are your soft skills?")

#Professional accomplishments
st.heading("Professional accomplishments")
st.markdown("This section includes a list of your professional accomplishments which allow you to prove your value to an employer.")
accomp = st.text_input("What are your professional accomplishments, starting from your most recent ones?")

#Work samples
st.heading("Work Samples")
st.markdown("This section includes showcasing work samples that highlight your abilities and display a broad range of your talents. You may include positive feedback received about those samples as well.")
samples = st.text_input("What are some samples of your work?")

#Awards
st.heading("Awards")
st.markdown("This section displays your past awards to  employers, signalling that they can expect a high level of work performance if they hire you. This includes scholarships, certificates, job-related awards, and school leadership positions.")
st.markdown("Include your most relevant awards, along with it's title, date received, and the positive impact it had on your career.")
awards = st.text_input("What awards have you received?")

#Transcripts, Degrees, Licenses, and Certifications
st.heading("Transcripts, Degrees, Licenses, and Certifications")
st.markdown("This section includes transcripts, degrees, licenses, and certifications that prove your competence in your area of expertise to employers.")
transcripts = st.text_input("What are your transcripts, degree, licenses, and certifications? Include links to PDFs when applicable.")

#Professional development
st.heading("Professional Development")
st.markdown("This section includes professional development such as career training or continued education, which proves your dedication and enthusiasm about your career.")
profDev = st.text_input("What are some of your professional developments?")

#Volunteer experience
st.heading("Volunteer Experience")
st.markdown("This section includes all the volunteer activites you have participated in, demonstrating your compassion for helping others.")
volunteer = st.text_input("What is your volunteer experience?")

#Professional testimonials and references
st.heading("Professional References and Testimonials")
st.markdown("This section includes 3-5 professional references and testimonials that allow employers to see positive comments about you from professionals.")
references = st.text_input("What are some testimonials or references, and their contacts?")