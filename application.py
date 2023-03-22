from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
import csv 

logging.basicConfig(filename='scrapper.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filemode='w')

application = Flask(__name__)
app = application


@app.route("/")
@cross_origin()
def index():
    logging.info('Rendering index.html')
    return render_template('index.html')


@app.route ('/review', methods=['GET', 'POST'])
@cross_origin()
def review():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            logging.info(f'Search query: {searchString}')
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString

            logging.info(f'Scraping search page: {flipkart_url}')
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()

            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})

            del bigboxes[0:3]
            box = bigboxes[0]

            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            logging.info(f'Scraping product page: {productLink}')
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'

            prod_html = bs(prodRes.text, "html.parser")
            logging.info(f'Parsed HTML of product page')

            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            filename = searchString + ".csv"
            with open(filename, "w", newline='', encoding='utf-8') as fw:
                writer = csv.writer(fw)
                writer.writerow(["Product", "Customer Name", "Rating", "Heading", "Comment"])

                reviews = []

                for commentbox in commentboxes:
                    try:
                        # name.encode(encoding='utf-8')
                        name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                        logging.info('Successfully got name of the reviewer!')
                    except Exception as e:
                        logging.error(f'Unable to retrieve the name due to {e}')
                        name = 'No Name'

                    try:
                        # rating.encode(encoding='utf-8')
                        logging.info('Successfully got rating of the reviewer!')
                        rating = commentbox.div.div.div.div.text
                    except Exception as e:
                        logging.error(f'Unable to retrieve the rating due to {e}')
                        rating = 'No Rating'

                    try:
                        # commentHead.encode(encoding='utf-8')
                        logging.info('Successfully got comment head of the reviewer!')
                        commentHead = commentbox.div.div.div.p.text
                    except Exception as e:
                        logging.error(f'Unable to retrieve the rating due to {e}')
                        commentHead = 'No Comment Heading'

                    try:
                        comtag = commentbox.div.div.find_all('div', {'class': ''})
                        # custComment.encode(encoding='utf-8')
                        custComment = comtag[0].div.text
                        logging.info('Successfully got comment/review of the reviewer!')
                    except Exception as e:
                        logging.error(f'Unable to retrieve the comment due to {e}')
                        custComment = 'No Comment'

                    writer.writerow([searchString, name, rating, commentHead, custComment])
                    mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                            "Comment": custComment}

                    reviews.append(mydict)

            logging.info(f'Returning reviews for search query: {searchString}')
            return render_template('results.html', reviews=reviews[:(len(reviews)-1)])
        except Exception as e:
            logging.error(f'The Exception message is: {e}')
            return 'Something is Wrong!'
    # return render_template('results.html')
    else:
        logging.info('Rendering index.html')
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
