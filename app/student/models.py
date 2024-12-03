from app import db

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key = True)
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"), nullable = False)
    name = db.Column(db.String(50), nullable = False, unique = True)
    code = db.Column(db.String(10), nullable = False, unique = True)

    program = db.relationship("Program", backref = "student")

    def __repr__(self):
        return f"<Student>{self.name}"