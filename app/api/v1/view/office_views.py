from flask import Flask,request
from flask_restful import Resource,reqparse
from app.api.v1.model.models import Model

Officedb = []


parser = reqparse.RequestParser()
parser.add_argument(
    "name",type = str,required = True,help = "Name field is required"
)
parser.add_argument(
    "age",type = int, required =True,help = "age field required"
)
parser.add_argument(
    "office_type",type = str, required =True,help = "type field required"
)
parser.add_argument(
    "education",type = str,required =True,help = "education field required"
)


class Officebase(Model):
    #Initiates class for storing offices
    def __init__(self):
    #Initialises the class 'Model' that contains references for offfice
        super().__init__(Officedb)


class Offices(Resource):
#This class and methods creates endpoints that work on several offices
    def __init__(self):
        self.dt = Officebase()

   
    def post(self):
        data = parser.parse_args()

        office = {
            'name': data['name'],
            'age':data['age'],
            'office_type':data['office_type'],
            'education':data['education'],
                }

        response = {
            'Message':'Input is required',
            'status':417
                } 
        if self.dt.valid(data['name']) == False: 
            return response
        if self.dt.valid(data['office_type']) == False:
            return response
        if self.dt.valid(data['education']) == False: 
            return response

        self.dt.save(office)
        return{
                'Message': 'Successfully saved',
                'status':201,
                'Data': office
                }


    def get(self):
        if self.dt.all() == []:    
            return {
                    'Message':'Offices not found',
                    'status':400
                }
        else:
            return {    
                'Message':'Returned successfully',
                'status':200,
                'data':self.dt.all()
                }


class Office(Resource):
    #class and its methods creates endpoints that act on a single office
    def __init__(self):
        self.dt = Officebase()


    def get(self, office_id):
        office = self.dt.find(office_id)
        if not office:
            return {
                'Message':'Office not found',
                'status':404,
            }
        return{
            'Message':'The office has been returned successfully',
            'status':200,
            'data':office
            }

    def delete(self, office_id):
        office = self.dt.find(office_id)
        if office:
            self.dt.remove(office_id)
            return {
                'Message':'Office successfully deleted',
                'status':204
            }
        return{
            'Message':'The office not found',
            'status':404
        }



    
