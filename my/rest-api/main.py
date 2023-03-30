from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_restful import Api, Resource
from sqlalchemy.dialects.postgresql import ARRAY

from inspect import getmembers


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_ws:admin_ws@localhost:5433/worldskills'

db = SQLAlchemy(app) 
ma = Marshmallow(app)
api = Api(app)


# --------------- Models
class Subdivision(db.Model):
    __tablename__ = 'subdivisions'
    subdivision_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    def __repr__(self):
        return '<Subdivision %s>' % self.title


class Visitor(db.Model):
    __tablename__ = 'visitors'
    visitor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(50))
    s_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    phone_num = db.Column(db.String(11))
    email = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    notes = db.Column(db.Text)
    birthday = db.Column(db.Date)
    passport_data = db.Column(db.String(11))
    visitor_photo = db.Column(db.LargeBinary)
    group_id = db.Column(db.Integer)
    appointment = db.Column(db.String(50))

    def __repr__(self):
        return '<Visitor %s>' % self.visitor_id


class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(50))
    s_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    subdivision_id = db.Column(db.Integer)
    department = db.Column(db.String(50))

    def __repr__(self):
        return '<Employee %s>' % self.employee_id


class Request(db.Model):
    __tablename__ = 'requests'
    req_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    req_type= db.Column(db.String(50))
    subdivision_id = db.Column(db.Integer)
    req_date = db.Column(db.Date)
    req_time = db.Column(db.Time)
    req_status = db.Column(db.String(20))
    req_status_description = db.Column(db.Text)
    user_id = db.Column(db.String(50))


    def __repr__(self):
        return '<Request %s>' % self.req_id


class Pass(db.Model):
    __tablename__ = 'pass'
    pass_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visit_purpose = db.Column(db.String(50))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    employee_id = db.Column(db.Integer)
    visitor_id = db.Column(db.Integer)
    subdivision_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Pass %s>' % self.pass_id


class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String(50))
    list_requests_id = db.Column(ARRAY(db.Integer))


    def __repr__(self):
        return '<User %s>' % self.email



# --------------- Shemas
class SubdivisionSchema(ma.Schema):
    class Meta:
        fields = ("subdivision_id", "title")
        model = Subdivision

subdivision_schema = SubdivisionSchema()
subdivisions_schema = SubdivisionSchema(many=True)


class VisitorSchema(ma.Schema):
    class Meta:
        fields = (
                    "visitor_id", "f_name", "s_name",
                    "surname", "phone_num", "email",
                    "organization", "notes", "birthday",
                    "passport_data", "visitor_photo", "group_id",
                    "appointment"
                )
        model = Visitor

visitor_schema = VisitorSchema()
visitors_schema = VisitorSchema(many=True)


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = (
                    "employee_id", "f_name", "s_name",
                    "surname", "subdivision_id", "department"
                )
        model = Employee

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class RequestSchema(ma.Schema):
    class Meta:
        fields = (
                    "req_id", "req_type", "subdivision_id",
                    "req_date", "req_time", "req_status",
                    "req_status_description", "user_id"
                )
        model = Request

request_schema = RequestSchema()
requests_schema= RequestSchema(many=True)
    

class PassSchema(ma.Schema):
    class Meta:
        fields = (
                    "pass_id", "visit_purpose", "date_start",
                    "date_end", "employee_id", "visitor_id"
                )
        model = Pass

pass_schema = PassSchema()
passes_schema = PassSchema(many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = (
                    "email", "password", "list_requests_id"
                )
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# --------------- ListResource
class SubdivisionsListResource(Resource):
    def get(self):
        subds = Subdivision.query.all()
        return subdivisions_schema.dump(subds)

    def post(self):
        new_subd = Subdivision(
            title=request.json['title'],
        )
        db.session.add(new_subd)
        db.session.commit()
        return subdivision_schema.dump(new_subd)

    def delete(self):
        subds = Subdivision.query.all()
        for subd in subds:
            db.session.delete(subd)
        db.session.commit()
        return '', 204

api.add_resource(SubdivisionsListResource, '/api/v1/resources/subdivisions')


class VisitorsListResource(Resource):
    def get(self):
        visitors = Visitor.query.all()
        return visitors_schema.dump(visitors)

    def post(self):
        new_visitor= Visitor(
            f_name=request.json['f_name'],
            s_name=request.json['s_name'],
            surname=request.json['surname'],
            phone_num=request.json['phone_num'],
            email=request.json['email'],
            organization=request.json['organization'],
            notes=request.json['notes'],
            birthday=request.json['birthday'],
            passport_data=request.json['passport_data'],
            # visitor_photo=request.json['visitor_photo'],
            group_id=request.json['group_id'],
            appointment=request.json['appointment']
        )
        db.session.add(new_visitor)
        db.session.commit()
        return visitor_schema.dump(new_visitor)

    def delete(self):
        visitors = Visitor.query.all()
        for visitor in visitors:
            db.session.delete(visitor)
        db.session.commit()
        return '', 204

api.add_resource(VisitorsListResource, '/api/v1/resources/visitors')


class EmployeesListResource(Resource):
    def get(self):
        employees = Employee.query.all()
        return employees_schema.dump(employees)

    def post(self):
        new_employee=Employee(
            f_name=request.json['f_name'],
            s_name=request.json['s_name'],
            surname=request.json['surname'],
            subdivision_id=request.json['subdivision_id'],
            department=request.json['department']
        )
        db.session.add(new_employee)
        db.session.commit()
        return employee_schema.dump(new_employee)

    def delete(self):
        employees = Employee.query.all()
        for employee in employees:
            db.session.delete(employee)
        db.session.commit()
        return '', 204

api.add_resource(EmployeesListResource, '/api/v1/resources/employees')


class RequestsListResource(Resource):
    def get(self):
        requests = Request.query.all()
        return requests_schema.dump(requests)

    def post(self):
        new_request = Request(
            req_type=request.json['req_type'],
            req_date=request.json['req_date'],
            subdivision_id=request.json['subdivision_id'],
            req_time=request.json['req_time'],
            req_status=request.json['req_status'],
            req_status_description=request.json['req_status_description'],
            user_id=request.json['user_id']
        )
        db.session.add(new_request)
        db.session.commit()
        return pass_schema.dump(new_request)

    def delete(self):
        requests = Request.query.all()
        for req in requests:
            db.session.delete(req)
        db.session.commit()
        return '', 204

api.add_resource(RequestsListResource, '/api/v1/resources/requests')


class RequestQueryList(Resource):
    def get(self, user_id):
        # print(type(user_id), user_id)
        requests_list = Request.query.filter_by(user_id=user_id)
        return requests_schema.dump(requests_list)

api.add_resource(RequestQueryList, '/api/v1/resources/requests/list/<string:user_id>')


class PassListResource(Resource):
    def get(self):
        passes = Pass.query.all()
        return passes_schema.dump(passes)

    def post(self):
        new_pass = Pass(
            visit_purpose=request.json['visit_purpose'],
            date_start=request.json['date_start'],
            date_end=request.json['date_end'],
            employee_id=request.json['employee_id'],
            visitor_id=request.json['visitor_id'],
            subdivision_id=request.json['subdivision_id']
        )
        db.session.add(new_pass)
        db.session.commit()
        return pass_schema.dump(new_pass)

    def delete(self):
        passes = Pass.query.all()
        for pass_inst in passes:
            db.session.delete(pass_inst)
        db.session.commit()
        return '', 204

api.add_resource(PassListResource, '/api/v1/resources/passes')


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(
            # email=request.json['email'],
            # password=request.json['password'],
            # list_requests_id=request.json['list_requests_id']
        )
        for field in UserSchema.Meta.fields:
            if field in request.json:
                exec(f"new_user.{field} = request.json['{field}']")

        db.session.add(new_user)
        db.session.commit()
        print('create user commit')
        return user_schema.dump(new_user)

    def delete(self):
        user = User.query.all()
        for user in users:
            db.session.delete(user)
        db.session.commit()
        return '', 204

api.add_resource(UserListResource, '/api/v1/resources/users')


# --------------- Resources
class SubdivisionResource(Resource):
    def get(self, subd_id):
        subd = Subdivision.query.get_or_404(subd_id)
        return subdivision_schema.dump(subd)

    def patch(self, subd_id):
        subd = Subdivision.query.get_or_404(subd_id)
        for field in SubdivisionSchema.Meta.fields:
            if field in request.json:
                exec(f"subd.{field} = request.json['{field}']")
        db.session.commit()
        return subdivision_schema.dump(subd)

    def delete(self, subd_id):
        subd = Subdivision.query.get_or_404(subd_id)
        db.session.delete(subd)
        db.session.commit()
        return '', 204

api.add_resource(SubdivisionResource, '/api/v1/resources/subdivisions/<int:subd_id>')


class VisitorResource(Resource):
    def get(self, visitor_id):
        visitor = Visitor.query.get_or_404(visitor_id)
        return visitor_schema.dump(visitor)

    def patch(self, visitor_id):
        visitor = Visitor.query.get_or_404(visitor_id)
        for field in VisitorSchema.Meta.fields:
            if field in request.json:
                exec(f"visitor.{field}= request.json['{field}']")
        db.session.commit()
        return visitor_schema.dump(visitor)

    def delete(self, visitor_id):
        visitor = Visitor.query.get_or_404(visitor_id)
        db.session.delete(visitor)
        db.session.commit()
        return '', 204

api.add_resource(VisitorResource, '/api/v1/resources/visitors/<int:visitor_id>')


class EmployeeResource(Resource):
    def get(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        return employee_schema.dump(employee)

    def patch(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        for field in EmployeeSchema.Meta.fields:
            if field in request.json:
                exec(f"employee.{field}= request.json['{field}']")
        db.session.commit()
        return employee_schema.dump(employee)

    def delete(self, employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return '', 204

api.add_resource(EmployeeResource, '/api/v1/resources/employees/<int:employee_id>')


class RequestsResource(Resource):
    def get(self, req_id):
        request = Request.query.get_or_404(req_id)
        return request_schema.dump(request)

    def patch(self, req_id):
        request = Request.query.get_or_404(req_id)
        for field in Request.Meta.fields:
            if field in request.json:
                exec(f"request.{field}= request.json['{field}']")
        db.session.commit()
        return request_schema.dump(request)

    def delete(self, req_id):
        request = Request.query.get_or_404(req_id)
        db.session.delete(request)
        db.session.commit()
        return '', 204

api.add_resource(RequestsResource, '/api/v1/resources/requests/<int:req_id>')


class PassResource(Resource):
    def get(self, pass_id):
        pass_instance = Pass.query.get_or_404(pass_id)
        return pass_schema.dump(pass_instance)

    def patch(self, pass_id):
        pass_inst = Pass.query.get_or_404(pass_id)
        for field in PassSchema.Meta.fields:
            if field in request.json:
                exec(f"pass_inst.{field}= request.json['{field}']")
        db.session.commit()
        return pass_schema.dump(pass_inst)

    def delete(self, pass_id):
        pass_instance = Pass.query.get_or_404(pass_id)
        db.session.delete(pass_instance)
        db.session.commit()
        return '', 204

api.add_resource(PassResource, '/api/v1/resources/passes/<int:pass_id>')


class UserResource(Resource):
    def get(self, email):
        user = User.query.get_or_404(email)
        return user_schema.dump(user)

    def patch(self, email):
        user = User.query.get_or_404(email)
        for field in UserSchema.Meta.fields:
            if field in request.json:
                exec(f"user.{field}= request.json['{field}']")
        db.session.commit()
        return user_schema.dump(user)

    def delete(self, email):
        user = User.query.get_or_404(email)
        db.session.delete(user)
        db.session.commit()
        return '', 204

api.add_resource(UserResource, '/api/v1/resources/users/<string:email>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)


