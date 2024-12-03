from app import db

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key = True)
    program_id = db.Column(db.Integer, db.ForeignKey("program.id"), nullable = False)
    level_id = db.Column(db.Integer, db.ForeignKey("level.id"), nullable = False)
    name = db.Column(db.String(50), nullable = False, unique = True)
    code = db.Column(db.String(10), nullable = False, unique = True)

    program = db.relationship("Program", backref = "course")
    level = db.relationship("Level", backref = "course")

    def __repr__(self):
        return f"<Course>{self.name}"