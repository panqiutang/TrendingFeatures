Overview:

Review Miner: Trending Feature Analyzer is a tool that helps users identify the most trendy features of a product in each of the recent years. This Trending Feature Analyzer includes five categories of products’ trendy features in past ten years. Users can simply selected desired category and view the results summarized in a table. This analyzer also support user customized data input by taking command line arguments. To use this software with customized category, a JSON file containing reviews and time information will be required.




Usage:

1. Regular usage:

1. Run ui.py

2. Choose a category of products from the drop down menu, a table with trending features of the selected category of products over time will be displayed.

2. Extended usage:

If users would like to use ReviewMiner with customized categories of products, dataset with time and reviews in JSON format will be needed.

1. Run read.py with command : ./read.py [-category] [--path to JSON file]

(Note path is an optional arg, if the JSON file is already in default folder, i.e. AmazonReviews, path is not necessary)

2. Run processes.py with command: ./processes.py [-category]

3. Run features.py with command: ./features.py [-category]

4. Run ui.py with command: ./ui.py [-category]




Implementation:

1. We collect Amazon reviews of six categories of products in JSON format. We only use five of them to perform training while leave one category as a test case for extended usage mentioned above. The five categories are tablet, camera, TV mobilephone, and video surveillance. The category laptop will be used as a test case for extended usage.

2. For each category, we parse the JSON and separate the reviews by year. This step corresponds to the code in read.py. This step also supports reading and parsing file from user-customized file path and category.

3. By taking user specified category as an input, processes.py performs LDA on each year’s review data of the selected category. We use Gensim library in this step.

4. In features.py, we defined our filter_words list, which is used to filter out frequent words with no meaningful information in reviews. This list serves the similar purpose as stop words list, but stop words removing is done before performing LDA. This list is created after examining our dataset. For general dataset and analysis, words that expressing personal opinion may be important and not removed when perform top modelling. However, for the purpose of analyzing the trending features products from reviews, words such as “love, like, great, good, bad” may not indicate any feature of the product despite showing strong personal preference of the users.   

5. After filtering the result features, features.py write the output to a csv file for GUI to use.

6. In ui.py, we implement a basic GUI for users to choose the category they want to analyze from a drop-down menu. Once a category is selected, a table including the trendy features of the selected category of products with corresponding time will show up.

7. If user choose to use the extended mode by providing a path to JSON and a new category, our GUI handles that by adding a new category to the bottom of the option menu, so user can access the newly included result after running read.py, processes.py, and features.py.  



Group member contribution:

panqiut2: read.py, processes.py, features.py, video presentation

mengdig2: processes.py, ui.py, video presentation, documentation
