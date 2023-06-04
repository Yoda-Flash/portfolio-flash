import streamlit as st
import urllib
# import pdf.py as doc


#Welcome
# st.image("PortfolioFlashLogo.png")
st.title("Welcome to Portfolio Flash!")
st.header("Here, you can build custom portfolios in a flash.")
st.write(" ")
st.markdown("*Please format all information the way you would on any portfolio, and leave a space behind each punctuation.")
st.write(" ")

#Contact info
st.markdown("This section includes all of your necessary contact information")
firstName = st.text_input("What is your first name?")
def getFirstName():
    return firstName

lastName = st.text_input("What is your last name?")
def getLastName():
    return lastName
email = st.text_input("What is your email?")
def getEmail():
    return email
city = st.text_input("Which city do you live in?")
def getCity():
    return city
state = st.text_input("Which state do you live in?")
def getState():
    return state

#Career summary
st.header("Career Summary")
st.markdown("This section includes a short, 2-4 sentence career summary.")
relevantWorkExperience = st.text_input("What are 1-2 examples of your relevant work experience?")
def getRelevantWorkExperience():
    return relevantWorkExperience
skillSummary = st.text_input("What are some of your relevant skills?")
def getSkillSummary():
    return skillSummary
profAccompSummary = st.text_input("What are some of your professional accomplishments?")
def getProfAccompSummary():
    return profAccompSummary

#Mission statement
st.header("Career Summary")
st.markdown("This section includes a mission statement of a few sentences.")
whatDoYouDo = st.text_input("What do you do?")
def getWhatDoYouDo():
    return whatDoYouDo
professionImportance = st.text_input("Why is your profession important?")
def getProfessionImportance():
    return professionImportance
thriveSkills = st.text_input("Which skills help you thrive in your work?")
def getThriveSkills():
    return thriveSkills
differenceFromOthers = st.text_input("What makes you different from other individuals in similar industries?")
def getDifferenceFromOthers():
    return differenceFromOthers

#Brief biography
st.header("Brief Biography")
st.markdown("This section is a biography that tells others about yourself, showcasing more of your own personality to connect on a more personal level with the employers.")
st.markdown("Be sure to consider your audience and the goal, to personalize it for each specific employer.")
st.markdown("Also include storytelling elements of how you overcame challenges, linked examples of your work, and possibly humor to give an impression of your humorous side.")
biography = st.text_input("What is your biography?")
def getBiography():
    return biography

#Resume
st.header("Resume")
st.markdown("This section is a resume that provides easy access to your work experience and skills.")
objective = st.text_input("What are your career goals and objectives?")
def getObjective():
    return objective
workExperience = st.text_input("What are your relevant work experiences from the past 10 years? What are your daily responsibilities and tasks of each position? (Bulleted list)")
def getWorkExperience():
    return workExperience
skills = st.text_input("What are your skills related to your position?")
def getSkills():   
    return skills
education = st.text_input("What education have you completed? Include the institution name, month and year of graduation, and type of degree received.")
def getEducation():
    return education

#Marketable skills
st.header("Marketable Skills")
st.markdown("This section is a list of specific marketable skills and abilities that make you qualified.")
hardSkills = st.text_input("What are your hard skills?")
def getHardSkills():
    return hardSkills
softSkills = st.text_input("What are your soft skills?")
def getSoftSkills():
    return softSkills

#Professional accomplishments
st.header("Professional accomplishments")
st.markdown("This section includes a list of your professional accomplishments which allow you to prove your value to an employer.")
accomp = st.text_input("What are your professional accomplishments, starting from your most recent ones?")
def getAccomp():
    return accomp

#Work samples
st.header("Work Samples")
st.markdown("This section includes showcasing work samples that highlight your abilities and display a broad range of your talents. You may include positive feedback received about those samples as well.")
samples = st.text_input("What are some samples of your work?")
def getSamples():
    return samples

#Awards
st.header("Awards")
st.markdown("This section displays your past awards to  employers, signalling that they can expect a high level of work performance if they hire you. This includes scholarships, certificates, job-related awards, and school leadership positions.")
st.markdown("Include your most relevant awards, along with it's title, date received, and the positive impact it had on your career.")
awards = st.text_input("What awards have you received?")
def getAwards():
    return awards

#Transcripts, Degrees, Licenses, and Certifications
st.header("Transcripts, Degrees, Licenses, and Certifications")
st.markdown("This section includes transcripts, degrees, licenses, and certifications that prove your competence in your area of expertise to employers.")
transcripts = st.text_input("What are your transcripts, degree, licenses, and certifications? Include links to PDFs when applicable.")
def getTranscripts():
    return transcripts

#Professional development
st.header("Professional Development")
st.markdown("This section includes professional development such as career training or continued education, which proves your dedication and enthusiasm about your career.")
profDev = st.text_input("What are some of your professional developments?")
def getProfDev():
    return profDev

#Volunteer experience
st.header("Volunteer Experience")
st.markdown("This section includes all the volunteer activites you have participated in, demonstrating your compassion for helping others.")
volunteer = st.text_input("What is your volunteer experience?")
def getVolunteer():
    return volunteer

#Professional testimonials and references
st.header("Professional References and Testimonials")
st.markdown("This section includes 3-5 professional references and testimonials that allow employers to see positive comments about you from professionals.")
references = st.text_input("What are some testimonials or references, and their contacts?")
def getReferences():
    return references

#Customize your portfolio
st.header("Customize your portfolio!")
st.markdown("You are nearly finished! Just customize your portfolio by choosing from a few different font and color options, and then your portfolio will be ready!")
font = st.selectbox("What font would you like to use?", ("Courier", "Helvetica", "Arial", "Times", "Symbol"))
def getFont():
    return font
bgcolor = st.selectbox("What background color would you like to use?", ("Black", "White", "Dark blue", "Light blue", "Dark green", "Light green", "Dark purple", "Light purple"))
def getBGColor():
    return bgcolor

# #Button to pdf
# def goToPDF():
#     return urllib.urlopen("MyPortfolio.pdf")
# if st.button('Generate PDF Portfolio!'):
#     goToPDF()