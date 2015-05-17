from splinter import Browser

browser = Browser()

def login(username, password):
	browser.visit("http://selenium.wpcp.org/m/")
	browser.fill("username", username)
	browser.fill("password", password)
	browser.find_by_name("Submit").click()

def getEnrichments():
	links = []
	for link in browser.find_link_by_partial_href("enrichment"):
		links.append(link["href"])
	return links

def changeEnrichment(link, possibleEnrichments):
	browser.visit(link)
	for enrichment in possibleEnrichments:
		if(browser.find_option_by_text(enrichment)):
			browser.find_option_by_text(enrichment).first.click()
			break
	browser.find_by_name("Submit").first.click()

if __name__ == "__main__":
	login(username, password)
	links = getEnrichments()
	for link in links:
		changeEnrichment(link, ["food", "Journalism Club: Radio and Newspaper Service Project", "Radio Production", "Young Life Club", "Astronomy / Anatomy & Physiology Tutoring", "H2O"])
	browser.quit()
