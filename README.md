# final-project





## Model notes
### Model overview:
Our model is trained on data from users and if they bought particular book titles (11 books including *Bridget Jones's Diary*) . The model uses the data about which of the other 10 books the user has bought/not bought and predicts whether or not the user will buy *Bridget Jones's Diary*. We are using the k-nearest neighbor model to determine this.

**Basic premise:** Based on your buying history and the buying history of other users like you, we are predicting whether or not you will buy *Bridget Jones's Diary*.

### Putting together the model:
We're starting out with a data set on books people have bought with their reviews (if they did review): https://www.kaggle.com/ruchi798/bookcrossing-dataset
	
This dataset has a million rows and almost 300K users and ~300K books. In an effort to (1) whittle down the dataset I was working with and (2) through trial and error I couldn't run the model with all of the books [even running in Google Colab] and (3) we wanted our app survey to be as short as possible and 10 is a nice number, I slimmed down the dataset to rows where the user had read at least one of the 11 most read books. This gives us ~7,000 of the original 300K users in our dataset.
	
I manipulated our data into a matrix where the columns are the book titles, the rows are the users, and the value is 0 or 1 based on if the user did not buy, or did buy the book (respectively). Then I grouped on user and summed up the values, so I could get one row per user with all of their buy/not buy data instead of one row per user/book combination.
	
The model uses 10 of the book columns to predict an 11th book column. Based on your buying history of 10 books, would you buy the 11th book?


