from fpdf import FPDF
import app.py as app

pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
if app.getBGColor() == "Black":
    r = 0
    g = 0
    b = 0
    theme = "dark"
elif app.getBGColor() == "White":
    r = 255
    g = 255
    b = 255
    theme = "light"
elif app.getBGColor()== "Dark blue":
    r = 2
    g = 8
    b = 74
    theme = "dark"
elif app.getBGColor() == "Light blue":
    r = 136
    g = 198
    b = 252
    theme = "light"
elif app.getBGColor() == "Dark green":
    r = 1
    g = 54
    b = 2
    theme = "dark"
elif app.getBGColor() == "Light green":
    r = 203
    g = 247
    b = 204
    theme = "light"
elif app.getBGColor() == "Dark purple":
    r = 26
    g = 1
    b = 69
    theme = "dark"
elif app.getBGColor() == "Light purple":
    r = 212
    g = 190
    b = 250
    theme = "light"

pdf.set_fill_color(r, g, b)
pdf.set_font(app.getFont(), "B")
if theme == "dark":
    pdf.set_text_color(255, 255, 255)
else:
    pdf.set_text_color(0, 0, 0)

#Contact info
pdf.write(5, app.getFirstName() + app.getLastName())
pdf.write(5, app.getEmail())
pdf.write(5, app.getCity() + " ," + app.getState())

#Career summary
pdf.write(5, app.getRelevantWorkExperience())
pdf.write(5, app.getSkillSummary())
pdf.write(5,app.getProfAccompSummary())

#Mission statement
pdf.write(5, app.getWhatYouDo())
pdf.write(5, app.getProfessionImportance())
pdf.write(5, app.getThriveSkills())
pdf.write(5, app.getDifferenceFromOthers())

#Biography
pdf.write(5, app.getBiography())

#Resume
pdf.write(5, app.getObjective())
pdf.write(5, app.getWorkExperience())
pdf.write(5, app.getSkills())
pdf.write(5, app.getEducation())

#Marketable skills
pdf.write(5, app.getHardSkills())
pdf.write(5, app.getSoftSkills())

#Professional accomplishments
pdf.write(5, app.getAccomp())

#Work samples
pdf.write(5, app.getSamples())

#Awards
pdf.write(5, app.getAwards())

#Transcripts...
pdf.write(5, app.getTranscripts())

#Professional development
pdf.write(5, app.getProfDev())

#Volunteer experience
pdf.write(5, app.getVolunteer())

#Professional testimonials and references
pdf.write(5, app.getReferences())

pdf.output('My Portfolio.pdf', "file:///C:/Users/admin/OneDrive/Downloads")