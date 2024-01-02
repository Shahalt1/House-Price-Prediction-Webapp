**House Price Prediction Webapp:**

The House Price Prediction Webapp is a simple yet powerful tool that allows users to estimate the price of a house based on input parameters such as square footage, the number of bedrooms, and the number of bathrooms. The web application is built using Flask, a web framework for Python, and incorporates machine learning to provide predictions.

**Key Components:**

1. **Flask Web Application:**
   - The backend of the web application is powered by Flask, a lightweight and versatile web framework for Python.
   - Flask handles the routing, requests, and responses, providing a seamless user experience.

2. **Machine Learning Model:**
   - The heart of the House Price Prediction Webapp is a machine learning model trained to predict house prices.
   - The model is loaded into the Flask application using the `pickle` library, allowing it to make predictions based on user input.

3. **User Interface (HTML and CSS):**
   - The user interface is designed using HTML for structuring and CSS for styling.
   - The HTML templates are extended from a base template (`base.html`) to maintain a consistent layout across pages.
   - The input form allows users to enter details such as square footage, the number of bedrooms, and the number of bathrooms.
   - The submit button triggers a prediction, and the results are displayed below the form.

4. **Responsive Design:**
   - The web application is designed with responsiveness in mind, ensuring a user-friendly experience on devices of various screen sizes.
   - The CSS includes media queries to adjust styles for better visibility and usability on smaller screens.

**Code Overview:**

- The Python code (`app.py`) contains the Flask application, which loads the machine learning model and handles user input to make predictions.
- HTML templates (`index.html` and `base.html`) structure the web pages, and they are styled using the CSS file (`index.css`).
- The CSS file provides a visually appealing and responsive design, ensuring a consistent and user-friendly experience across devices.

**How to Use:**

1. Users input details such as square footage, the number of bedrooms, and the number of bathrooms into the provided form.
2. Upon submitting the form, the web application utilizes the loaded machine learning model to predict the house price.
3. The predicted house price, along with the input details, is displayed on the page, providing users with valuable insights.

By combining Flask, machine learning, and a well-designed user interface, the House Price Prediction Webapp offers a practical solution for individuals seeking quick and accurate estimates of house prices based on key features.

![web1](https://github.com/Shahalt1/House-Price-Prediction-Webapp/assets/148101954/5d8d53b3-7de6-4a38-99cf-5b7b4f7a0531)
![web2](https://github.com/Shahalt1/House-Price-Prediction-Webapp/assets/148101954/416f9edb-b40e-464a-a280-f1324de50f47)
