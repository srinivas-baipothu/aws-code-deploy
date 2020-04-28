from flask import Blueprint


pprod_compilation = Blueprint('pprod_compilation', __name__)


@pprod_compilation.route('/')
def home():
    return 'PPROD - Compilation Home'