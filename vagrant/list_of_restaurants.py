from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

#importing the CRUD operations from database_setup.py
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#creating session and connecting to the database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            #Objective 3(2): Create new restaurant page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body>"
                message += "<h1>Add a New Restaurant</h1>"
                message += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new' >"
                message += "<input name='NewRestaurantName type='text' placeholder='New Restaurant Name' >"
                message += "<input type='submit' value='Create' >"
                message += "</body></html>"
                self.wfile.write(bytes(message,"utf8"))
                return

            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                message = ""
                # Objective 3(1): Create a Link to create a new menu item
                message += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body>"
                # Objective 1: Listing out the restaurant names
                for restaurant in restaurants:
                    message += restaurant.name
                    message += "</br>"
                    #Objective 2: Adding Edit and Delete links
                    message += "<a href ='#' >Edit </a> "
                    message += "</br>"
                    message += "<a href ='#' >Delete </a> "
                    message += "</br>"
                    message += "</br></br></br>"
      
                message += "</body></html>"
                self.wfile.write(bytes(message,"utf8"))
                print (message)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    #Objective 3(3): POST method to add the restaurant
    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
            if ctype == 'multipart/form-data':
                pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')[0].decode('utf-8')




def main():
    try:
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web server running...open localhost:8000/restaurants in your browser")
        server.serve_forever()
    except KeyboardInterrupt:
        print ("^C received, shutting down server....")
        server.socket.close()

if __name__ == '__main__':
    main()