from administer import db

class Funcionario(db.Model):
    """docstring for Funcionario"""
    
    __tablename__ = "funcionarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    setor = db.Column(db.String(120), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('administradores.id'))

    def __init__(self, form):

        self.nome = form.nome.data
        self.idade = form.idade.data
        self.email = form.idade.data
        self.setor = form.idade.data