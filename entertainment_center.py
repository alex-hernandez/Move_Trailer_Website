import fresh_tomatoes
import media

# This is the Toy Story instance:

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://www.dvdsreleasedates.com/posters/800/T/Toy-Story-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# This is the Avatar instance:

avatar = media.Movie("Avatar", "A marine on an alient planet",
                     "http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&feature=youtu.be")

# This is the Home Alone instance:

home_alone = media.Movie("Home Alone", "An 8 year old trouble maker is left at home by accident and he must protect his home from burglars",
                         "https://s-media-cache-ak0.pinimg.com/originals/14/de/51/14de51206eca408919374362065553be.jpg",
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

# This is the Ratatouille instance:

ratatouille = media.Movie("Ratatouille", "A mouse discovers he is a chef",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratslovakia.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# This is the Bench Warmers instance:

bench_warmers = media.Movie("Benchwarmers", "A trio of guys start a baseball team and compete against other kids",
                            "http://www.impawards.com/2006/posters/benchwarmers_xlg.jpg",
                            "https://www.youtube.com/watch?v=bhZxNtEnWU8")

# This is the Paranormal Activity instance:

paranormal_activity = media.Movie("Paranormal Activity", "A couple move into a cursed home",
                                  "http://www.imncreative.com/wp-content/uploads/2016/03/paranormal-activity-dvd-cover.jpg",
                                  "https://www.youtube.com/watch?v=F_UxLEqd074")

# This is the Striped Pajamas instance:

striped_pajamas = media.Movie("Boy in the Striped Pajamas", "During WWII, a story of a German 8 year old boy who befriends a Jewish boy",
                                  "http://static.rogerebert.com/uploads/movie/movie_poster/the-boy-in-the-striped-pajamas-2008/large_7ZS28nuK3VPKUVXKpStoefMjFb9.jpg",
                                  "https://www.youtube.com/watch?v=9ypMp0s5Hiw")

# This is the Lone Survivor instance:

lone_survivor = media.Movie("Lone Survivor", "A mission to capture or kill notorious Taliban leader Ahmad Shah",
                                  "http://www.impawards.com/2013/posters/lone_survivor_xlg.jpg",
                                  "https://www.youtube.com/watch?v=0cPJ1ifjBDs")

# This is the Wolf of Wall Street instance:

wolf_street = media.Movie("Wolf of Wall Street", "The story of wealthy stock-broker, Jordan Belfort.",
                                  "http://www.impawards.com/2013/posters/wolf_of_wall_street_ver3_xlg.jpg",
                                  "https://www.youtube.com/watch?v=iszwuX1AK6A")

movies = [toy_story, avatar, home_alone, ratatouille, bench_warmers, paranormal_activity,
          striped_pajamas, lone_survivor, wolf_street]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
