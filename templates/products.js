async function fetchJsonFile() {
    try {
        const response = await fetch('products.json');
        const jsonData = await response.json();

        processJsonData(jsonData);
    } catch (error) {
        console.error('Error loading JSON file:', error);
    }
}

function processJsonData(jsonData) {
    console.log(jsonData);
    const container = document.getElementById('product-container');

    jsonData.slice(0, 24).forEach((product, index) => {
        console.log(product);
        const box = document.createElement('div');
        box.className = 'box';

        const image = document.createElement('img');
        image.className = 'product-image';
        image.src = product['Image Link'];
        image.alt = 'Product ' + (index + 1);

        const name = document.createElement('p');
        name.className = 'product-name';
        name.textContent = product['Product Name'];

        box.appendChild(image);
        box.appendChild(name);

        container.appendChild(box);
    });
}

fetchJsonFile();
