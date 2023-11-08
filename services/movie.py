from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    # Function to get all the movies in our database
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    # Function to get a movie by ID
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()  # Get the movie from the database using filter from SQLAlchemy and show the first result
        return result
    
    # Function to get a movie by category
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()    # Get the movies from the database using filter from SQLAlchemy and show all results
        return result
    
    # Function to create a movie
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())        # Create a movie object
        self.db.add(new_movie)                              # Add the movie to the database
        self.db.commit()                                    # Save changes
        return
    
    # Function to update a movie
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()                                    # Save changes
        return
    
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()  # Delete movie
        self.db.commit()                                                # Save changes
        return