import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies_title = movies['title'].values

def fetch_posters(movie_id):
    response=requests.get(url='https://api.themoviedb.org/3/movie/{}?api_key=d0dafc4b86d078ed79f7377df1982d34'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    #recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster through api
        #recommended_movies_posters.append(fetch_posters(movie_id))

    return recommended_movies#,recommended_movies_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Search movie',
    (movies_title)
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
   # for i in recommendations:
   #   st.write(i)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(names[0])
       # st.image(posters[0])
    with col2:
        st.header(names[1])
      #  st.image(posters[1])
    with col3:
        st.header(names[2])
       # st.image(posters[2])
    with col4:
        st.header(names[3])
       # st.image(posters[3])
    with col5:
        st.header(names[4])
       # st.image(posters[4])
    
