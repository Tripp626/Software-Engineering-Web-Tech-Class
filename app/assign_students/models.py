from app import db

class Assign_Students(db.Model):
    __tablename__ = "assign_students"
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable = False)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable = False)

    student = db.relationship("Student", backref = "assign_student")
    group = db.relationship("Group", backref = "assign_student")

    def __repr__(self):
        return f"<Assign_Students>{self.name}"