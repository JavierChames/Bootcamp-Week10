from module1 import get_letters as a
from module4 import get_letters as get_letters4
from module import get_letters5
from last.w_z import get_last_letters
from last.t_v import get_letters as get_t_v
from last.medium.q_s import get_letters
from middle.m_p.get_m_p import m_p

def get_alphabet():
    return a() + get_letters4() + get_letters5() +m_p() + get_letters() + get_t_v() + get_last_letters()


print(get_alphabet())