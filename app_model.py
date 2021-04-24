#Using pickle to load the model file (.pkl)
import pickle

file_name = "book_model.pkl"
with open(file_name, 'rb') as file:
    Pickled_book_model = pickle.load(file)
    
#We want to have a list similar to the one below output from the answers our users give to the questions
new_book_data = [[0,0,0,0,0,0,0,0,0,1]]
predicted_class = Pickled_book_model.predict(new_book_data)

if predicted_class == 0:
    print("Shoot! The user will not buy Bridget Jones's Diary")
elif predicted_class == 1:
    print("The user will buy Bridget Jones's Diary. Yay!")
else:
     "Something went horribly wrong" 