from MovieToPicture import MovieToPicture
import sys

def main():
    result_path = sys.argv[1]
    movie_path = sys.argv[2]
    picture_name = sys.argv[3]
    movie = MovieToPicture(result_path, movie_path, picture_name)
    movie.change()

if __name__ == '__main__':
    main()