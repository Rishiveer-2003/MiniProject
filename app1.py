from flask import Flask, request, jsonify
from scraper import flipkartScraper

app = Flask(__name__)
scraper_instance = flipkartScraper()


@app.route('/run_scraper', methods=['POST'])
def run_scraper():
    data = request.get_json()
    product_link = data.get('productLink')

    if product_link:
        # Here, you should call the Python function to run the scraper with the provided product_link
        # Example:
        # result = my_class_instance.iterate_over_pages(product_link)
        result =

        # For now, we'll return a success message
        result = "Scraper executed successfully."

        if result:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
    else:
        return jsonify({'error': 'productLink not provided'})

if __name__ == '__main__':
    app.run()
