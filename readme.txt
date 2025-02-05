Documentation for Text Analysis Project
This documentation provides a comprehensive overview of the project, ensuring that developers and users can easily understand its functionality and usage.


1. Introduction
    Purpose: This project provides a web-based tool for analyzing text for toxicity and gibberish content. It uses machine learning models to classify text and displays results in real-time.
    Core Features:
        Detects the toxicity level of input text.
        Identifies whether the input text is gibberish.
        Maintains a history of analyzed texts with scores and timestamps.

2. Project Structure
    This project consists of the following key files:
        index.html - Frontend interface for user interaction with style.css as the css file.
        history.html - Template for displaying analysis history with style1.css as the css file.
        app.py - Backend Flask application managing routes and database operations.
        cal_toxic.py - Toxicity detection module using a pre-trained RoBERTa model.
        cal_gibberish.py - Gibberish detection module using a pre-trained transformer model.

3. Detailed File Descriptions
    index.html
           Provides the user interface for:
           Inputting text for analysis.
           Viewing results (toxicity and gibberish scores).
           Accessing analysis history via a button.
           Includes JavaScript to handle form submission asynchronously and update results dynamically.
    history.html
        Displays a table of past analyses with columns for ID, input string, toxicity score, gibberish score, and timestamp.
        Includes pagination controls for navigating through records.
    app.py
        Implements the backend logic:
            Routes:
                /: Renders the main page (index.html).
                /process: Handles POST requests to process input text and return analysis results in JSON format.
                /history: Displays a paginated history of analyzed texts using history.html.
            Database:
                Stores input text, toxicity score, gibberish score, and timestamp in an SQLite database.
    cal_toxic.py
        Contains the detect_toxic function to classify text as "Neutral" or "Toxic" using a pre-trained RoBERTa model.
            Outputs:
                label: Classification result (e.g., "Toxic").
                score: Confidence score of the classification.
    cal_gibberish.py
        Contains the detect_gibberish function to detect gibberish content using a transformer-based model.
                Outputs:
                    label: Classification result (e.g., "gibberish").
                    score: Confidence score for gibberish classification.
4. API Endpoints
    POST /process
        Description: Processes input text and returns toxicity and gibberish analysis results.
        Request Body:
                json
                    {
                        "text-input": "Your text here"
                    }
        Response:
                json
                    {
                      "toxicity": { "score": 0.85 },
                      "gibberish": { "score": 0.12 }
                     }
    GET /history
        Description: Displays a paginated history of previous analyses.
5. Glossary
    Toxicity: Refers to offensive or harmful language in the text.
    Gibberish: Refers to nonsensical or meaningless text.
6. Database Structure
    The project uses an SQLite database (output.db) to store the results of text analysis. It contains a single table named Output with the following structure:

    Column Name     	        Data Type	                   Description
    id	                        Integer (Primary Key)	       A unique identifier for each record.
    text	                    String (500 characters max)	   The input text submitted by the user for analysis.
    toxicity_score	            Float	                       The toxicity score of the input text (confidence level).
    gibberish_score	            Float	                       The gibberish score of the input text (confidence level).
    timestamp	                DateTime	                   The timestamp when the text was analyzed.

7. Future Enhancements
    Database Improvements:
        Transition from the current single-table structure to a more robust Entity-Relationship (ER) model.
    Frontend Enhancements:
        Using modern frontend frameworks like React.js or Vue.js for dynamic rendering.
    Additional Features:
        Implement user authentication and authorization to allow users to log in and view their analysis history securely.






