# Movie-Recommendation-API

- It is a API made in Flask to get the movies having similar genres to the movie entered by the user.
- It uses the OMDB API to get the genres of the movie entered by the user and processes it using a Word2Vec Model 
  to generate a vector using the genres. 
- Then this vector is compared with the vectors of around 60k+ movies in the database and the vectors having high Cosine
  similarity are picked. 
- Then the movies related to this vector are given as output to the User.
- Also, If the movie is new to our database then it is added to database for enhanced future experience. 


- Link for the database (Extract the files from this zip file and store it with these files) - https://drive.google.com/file/d/1mjV3UJdqrREOmujnA5oxn4hW8WohKh74/view?usp=sharing
